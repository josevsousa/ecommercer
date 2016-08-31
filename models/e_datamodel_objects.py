# -*- coding: utf-8 -*-

# definir tabelas de objetos do sistema

# Category
# id, name, description
db.define_table("category",
	Field("name", length=128, notnull=True, unique=True ),
	Field("description", "text" ),
	Field("picture", "upload"),
	auth.signature,
	format='%(name)s'
	)

# Product
# id, name, category, description, qtd, origin, unit_price
# total_price, tax_price, picture, thumbnail, barcode (signature)
db.define_table("product",
	Field("name"),
	Field("category", "reference category"),
	Field("description"),
	Field("qtd", "integer", notnull=True),
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
origins = {"BR": 1.0, "JP": 1.2, "EUA": 1.8, "UK": 1.5}

# Order
# id, client, total_items, total_price, payment, (signature)

# OrderItems
# id, order_id, product_id, unit_price, qtd, total_price (signature)
 

UFS = {
	"AC":{"capital": u"Rio Branco", "cep_ini": "69900", "cep_fin": "69920"},
	"AL":{"capital": u"Maceió", "cep_ini": "57000", "cep_fin": "57099"},
	"AM":{"capital": u"Manaus", "cep_ini": "69000", "cep_fin": "69099"},
	"AP":{"capital": u"Macapá", "cep_ini": "68900", "cep_fin": "68914"},
	"BA":{"capital": u"Salvador", "cep_ini": "40000", "cep_fin": "41999"},
	"CE":{"capital": u"Fortaleza", "cep_ini": "60000", "cep_fin": "60999"},
	"DF":{"capital": u"Brasília", "cep_ini": "70700", "cep_fin": "70999"},
	"ES":{"capital": u"Vitória", "cep_ini": "29000", "cep_fin": "29099"},
	"GO":{"capital": u"Goiânia", "cep_ini": "74000", "cep_fin": "74894"},
	"MA":{"capital": u"São Luís", "cep_ini": "65000", "cep_fin": "65099"},
	"MG":{"capital": u"Belo Horizonte", "cep_ini": "30000", "cep_fin": "31999"},
	"MS":{"capital": u"Campo Grande", "cep_ini": "79000", "cep_fin": "79129"},
	"MT":{"capital": u"Cuiabá", "cep_ini": "78000", "cep_fin": "78109"},
	"PA":{"capital": u"Belém", "cep_ini": "66000", "cep_fin": "66999"},
	"PB":{"capital": u"João Pessoa", "cep_ini": "58000", "cep_fin": "58099"},
	"PE":{"capital": u"Recife", "cep_ini": "50000", "cep_fin": "52999"},
	"PI":{"capital": u"Teresina", "cep_ini": "64000", "cep_fin": "64099"},
	"PR":{"capital": u"Curitiba", "cep_ini": "80000", "cep_fin": "82999"},
	"RJ":{"capital": u"Rio de Janeiro", "cep_ini": "20000", "cep_fin": "23799"},
	"RN":{"capital": u"Natal", "cep_ini": "59000", "cep_fin": "59099"},
	"RO":{"capital": u"Porto Velho", "cep_ini": "78900", "cep_fin": "78930"},
	"RR":{"capital": u"Boa Vista", "cep_ini": "69300", "cep_fin": "69339"},
	"RS":{"capital": u"Porto Alegre", "cep_ini": "90000", "cep_fin": "91999"},
	"SC":{"capital": u"Florianópolis", "cep_ini": "88000", "cep_fin": "82999"},
	"SE":{"capital": u"Aracaju", "cep_ini": "49000", "cep_fin": "49099"},
	"SP":{"capital": u"São Paulo", "cep_ini": "01000", "cep_fin": "05999"},
	"TO":{"capital": u"Palmas", "cep_ini": "77000", "cep_fin": "77270"}
	}