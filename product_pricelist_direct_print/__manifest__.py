{
    "name": "Product Pricelist Direct Print",
    "summary": "Print price list from menu option, product templates, "
    "products variants or price lists",
    "description": "<p>Print price list from menu option, product templates, products variants or price lists</p>",
    "version": "19.0.1.0.0",
    "category": "Product",
    "website": "https://www.github.com/OCA/product-attribute",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/report_product_pricelist.xml",
        "data/mail_template_data.xml",
        "wizards/product_pricelist_print_view.xml",
    ],
    "installable": True,
    "auto_install": False,
}
