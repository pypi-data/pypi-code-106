from django.utils.translation import ugettext_lazy as _

MENUS = {
    "NAV_MENU_CORE": [
        {
            "name": _("Orders"),
            "url": "#",
            "icon": "shopping_cart",
            "root": True,
            "validators": [
                ("aleksis.core.util.predicates.permission_validator", "order.show_menu",),
            ],
            "submenu": [
                {
                    "name": _("List"),
                    "url": "list_orders",
                    "icon": "receipt_long",
                    "validators": [
                        ("aleksis.core.util.predicates.permission_validator", "order.view_orders",),
                    ],
                },
            ],
        }
    ]
}
