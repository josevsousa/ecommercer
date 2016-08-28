# -*- coding: utf-8 -*-
from costumvalidators import IS_VALID_BARCODE
# from smarthumb import THUMB
# from miniimage import MINI_IMG


# validadores para tabelas
db.product.name.requires=IS_NOT_EMPTY(error_message='nome obrigatório')
db.product.origin.requires = IS_IN_SET(origins.keys())
db.product.barcode.requires = [
	IS_NOT_EMPTY(error_message="Insira um Barcode"),
	IS_VALID_BARCODE("987","BARCODE INVALIDO")
]

# computations
db.product.total_price.compute = \
	lambda row: float(row.unit_price) * float(row.qtd)

# db.product.thumbnail.compute = \
# 	lambda row: MINI_IMG(row.picture)

from smarthumb import SMARTHUMB 
db.product.thumbnail.compute = lambda row: SMARTHUMB(row.picture, 200, 200)


# form widgets
# visibility
# campos virtuais
# funcoes de validators
# validadores customizados


# esconder campos da tabela
def hide_fields(tablename, fields):
     for field in fields:
          db[tablename][field].writable = \
               db[tablename][field].readable = False