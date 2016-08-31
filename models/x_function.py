# -*- coding: utf-8 -*-

#esconde campos da tabela passada por parametro
def hide_fields(tablename, fields):
	for field in fields:
		db[tablename][field].writable = \
			db[tablename][field].readable = False

#trata o id passado por parametro add zero a esquerda
def slugfy(product):
	template = "%(id_formatado)s-%(name)s"
	id_formatado = str(product.id).zfill(5)
	return template % dict(id_formatado=id_formatado, name=product.name)


# esconder campos da tabela
def hide_fields(tablename, fields):
     for field in fields:
          db[tablename][field].writable = \
               db[tablename][field].readable = False

# formato de moeda
def format_price(value):
	valor = "R$ %.2f"% float(value)
	return valor.replace('.',',')