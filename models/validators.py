# -*- coding: utf-8 -*-
from costumvalidators import IS_VALID_BARCODE
from smarthumb import SMARTHUMB
from plugin_ckeditor import CKEditor
ckeditor = CKEditor(db)

db.product.description.widget = ckeditor.widget

# validadores para tabelas
db.product.name.requires=IS_NOT_EMPTY(error_message='nome obrigatório')

db.product.origin.requires = IS_IN_SET(origins.keys())
db.product.origin.widget = SQLFORM.widgets.radio.widget
db.product.barcode.requires = [
	IS_NOT_EMPTY(error_message="Insira um Barcode"),
	IS_VALID_BARCODE("987","BARCODE INVALIDO")
]

##########################################################################################

# computations total
db.product.total_price.compute = \
	lambda row: float(row.unit_price) * float(row.qtd)

# computations thumbnail
box = (200, 200)
db.product.thumbnail.compute = lambda row: SMARTHUMB(row.picture, box)

def get_miniatura(row):
     if row.thumbnail: #se usar virtual field tem que ser "row.product.thumbnail"
          return IMG(_width=50, _heigth=50, _src=URL('home', 'download', args=[row.thumbnail]))
     else:
          return IMG(_src="http://placehold.it/50x50")

def get_miniatura_sqlformgrid(row):
     if row.product.thumbnail: #se usar virtual field tem que ser "row.product.thumbnail"
          return IMG(_width=50, _heigth=50, _src=URL('home', 'download', args=[row.product.thumbnail]))
     else:
          return IMG(_src="http://placehold.it/50x50")


# form widgets
# visibility
# campos virtuais
# funcoes de validators
# validadores customizados


