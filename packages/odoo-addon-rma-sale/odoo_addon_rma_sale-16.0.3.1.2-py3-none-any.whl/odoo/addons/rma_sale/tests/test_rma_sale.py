# Copyright 2020 Tecnativa - Ernesto Tejeda
# Copyright 2022 Tecnativa - Víctor Martínez
# Copyright 2023 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import Form, tagged
from odoo.tests.common import users

from odoo.addons.base.tests.common import BaseCommon


class TestRmaSaleBase(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        if not cls.env.company.chart_template_id:
            # Load a CoA if there's none in current company
            coa = cls.env.ref("l10n_generic_coa.configurable_chart_template", False)
            if not coa:
                # Load the first available CoA
                coa = cls.env["account.chart.template"].search(
                    [("visible", "=", True)], limit=1
                )
            coa.try_loading(company=cls.env.company, install_demo=False)
        cls.res_partner = cls.env["res.partner"]
        cls.product_product = cls.env["product.product"]
        cls.so_model = cls.env["sale.order"]

        cls.product_1 = cls.product_product.create(
            {"name": "Product test 1", "type": "product"}
        )
        cls.product_2 = cls.product_product.create(
            {"name": "Product test 2", "type": "product"}
        )
        cls.partner = cls.res_partner.create(
            {"name": "Partner test", "email": "partner@rma"}
        )
        cls.report_model = cls.env["ir.actions.report"]
        cls.rma_operation_model = cls.env["rma.operation"]
        cls.operation = cls.env.ref("rma.rma_operation_replace")
        cls._partner_portal_wizard(cls, cls.partner)

    def _create_sale_order(self, products):
        order_form = Form(self.so_model)
        order_form.partner_id = self.partner
        for product_info in products:
            with order_form.order_line.new() as line_form:
                line_form.product_id = product_info[0]
                line_form.product_uom_qty = product_info[1]
        return order_form.save()

    def _partner_portal_wizard(self, partner):
        wizard_all = (
            self.env["portal.wizard"]
            .with_context(**{"active_ids": [partner.id]})
            .create({})
        )
        wizard_all.user_ids.action_grant_access()

    def _rma_sale_wizard(self, order):
        wizard_id = order.action_create_rma()["res_id"]
        wizard = self.env["sale.order.rma.wizard"].browse(wizard_id)
        wizard.operation_id = self.operation
        return wizard


@tagged("-at_install", "post_install")
class TestRmaSale(TestRmaSaleBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.sale_order = cls._create_sale_order(cls, [[cls.product_1, 5]])
        cls.sale_order.action_confirm()
        # Maybe other modules create additional lines in the create
        # method in sale.order model, so let's find the correct line.
        cls.order_line = cls.sale_order.order_line.filtered(
            lambda r: r.product_id == cls.product_1
        )
        cls.order_out_picking = cls.sale_order.picking_ids
        cls.order_out_picking.move_ids.quantity_done = 5
        cls.order_out_picking.button_validate()

    def test_rma_sale_computes_onchange(self):
        rma = self.env["rma"].new()
        # No m2m values when everything is selectable
        self.assertFalse(rma.allowed_picking_ids)
        self.assertFalse(rma.allowed_move_ids)
        self.assertFalse(rma.allowed_product_ids)
        # Partner selected
        rma.order_id = self.sale_order
        rma.partner_id = self.partner
        self.assertFalse(rma.order_id)
        self.assertEqual(rma.allowed_picking_ids._origin, self.order_out_picking)
        # Order selected
        rma.order_id = self.sale_order
        self.assertEqual(rma.allowed_picking_ids._origin, self.order_out_picking)
        rma.picking_id = self.order_out_picking
        self.assertEqual(rma.allowed_move_ids._origin, self.order_out_picking.move_ids)
        self.assertEqual(rma.allowed_product_ids._origin, self.product_1)
        # Onchanges
        rma.product_id = self.product_1
        rma._onchange_order_id()
        self.assertFalse(rma.product_id)
        self.assertFalse(rma.picking_id)

    def test_create_rma_with_so(self):
        rma_vals = {
            "partner_id": self.partner.id,
            "order_id": self.sale_order.id,
            "product_id": self.product_1.id,
            "product_uom_qty": 5,
            "location_id": self.sale_order.warehouse_id.rma_loc_id.id,
            "operation_id": self.operation.id,
        }
        rma = self.env["rma"].create(rma_vals)
        rma.action_confirm()
        self.assertTrue(rma.reception_move_id)
        self.assertFalse(rma.reception_move_id.origin_returned_move_id)

    def test_create_rma_from_so(self):
        order = self.sale_order
        wizard = self._rma_sale_wizard(order)
        rma = self.env["rma"].browse(wizard.create_and_open_rma()["res_id"])
        self.assertEqual(rma.partner_id, order.partner_id)
        self.assertEqual(rma.order_id, order)
        self.assertEqual(rma.picking_id, self.order_out_picking)
        self.assertEqual(rma.move_id, self.order_out_picking.move_ids)
        self.assertEqual(rma.product_id, self.product_1)
        self.assertEqual(rma.product_uom_qty, self.order_line.product_uom_qty)
        self.assertEqual(rma.product_uom, self.order_line.product_uom)
        self.assertEqual(rma.state, "confirmed")
        self.assertEqual(
            rma.reception_move_id.origin_returned_move_id,
            self.order_out_picking.move_ids,
        )
        self.assertEqual(
            rma.reception_move_id.picking_id + self.order_out_picking,
            order.picking_ids,
        )
        user = self.env["res.users"].create(
            {"login": "test_refund_with_so", "name": "Test"}
        )
        order.user_id = user.id
        # Receive the RMA
        rma.action_confirm()
        rma.reception_move_id.quantity_done = rma.product_uom_qty
        rma.reception_move_id.picking_id._action_done()
        # Refund the RMA
        rma.action_refund()
        self.assertEqual(self.order_line.qty_delivered, 0)
        self.assertEqual(self.order_line.qty_invoiced, -5)
        self.assertEqual(rma.refund_id.user_id, user)
        self.assertEqual(rma.refund_id.invoice_line_ids.sale_line_ids, self.order_line)
        # Cancel the refund
        rma.refund_id.button_cancel()
        self.assertEqual(self.order_line.qty_delivered, 5)
        self.assertEqual(self.order_line.qty_invoiced, 0)
        # And put it to draft again
        rma.refund_id.button_draft()
        self.assertEqual(self.order_line.qty_delivered, 0)
        self.assertEqual(self.order_line.qty_invoiced, -5)

    @users("partner@rma")
    def test_create_rma_from_so_portal_user(self):
        order = self.sale_order
        wizard_obj = (
            self.env["sale.order.rma.wizard"].sudo().with_context(active_id=order.id)
        )
        operation = self.rma_operation_model.sudo().search([], limit=1)
        line_vals = [
            (
                0,
                0,
                {
                    "product_id": order.order_line.product_id.id,
                    "sale_line_id": order.order_line.id,
                    "quantity": order.order_line.product_uom_qty,
                    "uom_id": order.order_line.product_uom.id,
                    "picking_id": order.picking_ids[0].id,
                    "operation_id": operation.id,
                },
            )
        ]
        wizard = wizard_obj.create(
            {
                "line_ids": line_vals,
                "location_id": order.warehouse_id.rma_loc_id.id,
            }
        )
        rma = wizard.sudo().create_rma(from_portal=True)
        self.assertEqual(rma.order_id, order)
        self.assertIn(order.partner_id, rma.message_partner_ids)
        self.assertEqual(order.rma_count, 1)

    def test_create_recurrent_rma(self):
        """An RMA of a product that had an RMA in the past should be possible"""
        wizard = self._rma_sale_wizard(self.sale_order)
        rma = self.env["rma"].browse(wizard.create_and_open_rma()["res_id"])
        rma.reception_move_id.quantity_done = rma.product_uom_qty
        rma.reception_move_id.picking_id._action_done()
        wizard = self._rma_sale_wizard(self.sale_order)
        self.assertEqual(
            wizard.line_ids.quantity,
            0,
            "There shouldn't be any allowed quantities for RMAs",
        )
        delivery_form = Form(
            self.env["rma.delivery.wizard"].with_context(
                active_ids=rma.ids,
                rma_delivery_type="return",
            )
        )
        delivery_form.product_uom_qty = rma.product_uom_qty
        delivery_wizard = delivery_form.save()
        delivery_wizard.action_deliver()
        picking = rma.delivery_move_ids.picking_id
        picking.move_ids.quantity_done = rma.product_uom_qty
        picking._action_done()
        # The product is returned to the customer, so we should be able to make
        # another RMA in the future
        wizard = self._rma_sale_wizard(self.sale_order)
        self.assertEqual(
            wizard.line_ids.quantity,
            rma.product_uom_qty,
            "We should be allowed to return the product again",
        )

    def test_report_rma(self):
        wizard = self._rma_sale_wizard(self.sale_order)
        rma = self.env["rma"].browse(wizard.create_and_open_rma()["res_id"])
        operation = self.rma_operation_model.sudo().search([], limit=1)
        rma.operation_id = operation.id
        res = self.env["ir.actions.report"]._render_qweb_html("rma.report_rma", rma.ids)
        res = str(res[0])
        self.assertRegex(res, self.sale_order.name)
        self.assertRegex(res, operation.name)
