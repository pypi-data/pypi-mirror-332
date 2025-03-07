# Copyright 2021 ACSONE SA/NV
# Copyright 2023 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Product Assortment",
    "summary": """
        Adds the ability to manage products assortment""",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "development_status": "Production/Stable",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/product-attribute",
    "depends": ["base", "product"],
    "data": [
        "data/ir_cron.xml",
        "security/product_assortment_security.xml",
        "views/product_assortment.xml",
        "views/res_partner_view.xml",
    ],
    "installable": True,
}
