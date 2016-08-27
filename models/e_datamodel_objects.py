#coding: utf-8

# definir tabelas de objetos do sistema

# Category
# id, name, description
db.define_table("category",
	Field("name", length=128, requires=IS_NOT_EMPTY(), unique=True ),
	Field("description", "text" ),
	Field("picture", "upload"),
	auth.signature
	# format='%(nome)s'
	)

# Product
# id, name, category, description, qtd, origin, unit_price
# total_price, tax_price, picture, thumbnail, barcode (signature)
db.define_table("product",
	Field("name", requires=IS_NOT_EMPTY()),
	Field("category", "reference category"),
	Field("qtd", "integer", requires=IS_NOT_EMPTY()),
	Field("origin", "string"),
	Field("unit_price","double"),
	Field("total_price","double"), # computed fields
	# campo virtual tax_price
	Field("picture","upload"),
	Field("thumbnail","upload"),
	Field("barcode", "string"),
	Field("featured","boolean", default=False),
	auth.signature
	)
origin = {"BR": 1.0, "JP": 1.2, "EUA": 1.8, "UK": 1.5}

# Order
# id, client, total_items, total_price, payment, (signature)

# OrderItems
# id, order_id, product_id, unit_price, qtd, total_price (signature)
 