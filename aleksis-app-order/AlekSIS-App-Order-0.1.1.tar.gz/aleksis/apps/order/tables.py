from django.template.loader import render_to_string

from django_tables2 import A, Column, LinkColumn, tables

from aleksis.apps.order.models import Order


class OrderTable(tables.Table):
    full_name = LinkColumn("show_order", args=[A("pk")])
    actions = Column(accessor="pk")

    def render_actions(self, value):
        return render_to_string("order/actions.html", {"pk": value}, self.request)

    class Meta:
        model = Order
        order_by = "-created"
        fields = (
            "form",
            "created",
            "full_name",
            "email",
            "notes",
            "confirmed",
            "paid",
            "sent",
            "processing_option",
            "processing_price",
            "items_count",
            "total",
        )
