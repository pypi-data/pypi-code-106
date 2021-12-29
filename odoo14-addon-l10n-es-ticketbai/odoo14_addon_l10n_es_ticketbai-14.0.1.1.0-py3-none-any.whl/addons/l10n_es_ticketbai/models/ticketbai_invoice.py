# Copyright 2021 Binovo IT Human Project SL
# Copyright 2021 Landoo Sistemas de Informacion SL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import _, exceptions, fields, models

from odoo.addons.l10n_es_ticketbai_api.models.ticketbai_invoice import (
    TicketBaiInvoiceState,
)
from odoo.addons.l10n_es_ticketbai_api.ticketbai.xml_schema import TicketBaiSchema


class TicketBAIInvoice(models.Model):
    _inherit = "tbai.invoice"

    invoice_id = fields.Many2one(comodel_name="account.move")
    cancelled_invoice_id = fields.Many2one(comodel_name="account.move")

    def get_ticketbai_api(self, **kwargs):
        self.ensure_one()
        cert = self.company_id.tbai_certificate_get_public_key()
        key = self.company_id.tbai_certificate_get_private_key()
        return super().get_ticketbai_api(cert=cert, key=key, **kwargs)

    def send(self, **kwargs):
        self.ensure_one()
        if TicketBaiSchema.TicketBai.value == self.schema and self.invoice_id:
            return super().send(invoice_id=self.invoice_id.id, **kwargs)
        elif (
            TicketBaiSchema.AnulaTicketBai.value == self.schema
            and self.cancelled_invoice_id
        ):
            return super().send(invoice_id=self.cancelled_invoice_id.id, **kwargs)
        else:
            return super().send(**kwargs)

    def cancel_and_recreate(self):
        if 0 < len(
            self.filtered(lambda x: x.state != TicketBaiInvoiceState.error.value)
        ):
            raise exceptions.ValidationError(
                _(
                    "TicketBAI: You cannot cancel and recreate an Invoice with a state "
                    "different than 'Error'."
                )
            )
        for record in self.sudo():
            record.cancel()
            if TicketBaiSchema.TicketBai.value == record.schema and record.invoice_id:
                record.invoice_id._tbai_build_invoice()
            elif (
                TicketBaiSchema.AnulaTicketBai.value == record.schema
                and record.cancelled_invoice_id
            ):
                record.cancelled_invoice_id._tbai_invoice_cancel()
