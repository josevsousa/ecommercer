# -*- coding: utf-8 -*-

def show():
	# pegar produto no bando de dados
	# buscar pelo slug //qualquer campo != id
	# acessar api do twitter
	pass

def search():
	# receber parametros e efetuar busca
	pass

def list():
	#exibir todos os produtos
	# apenas para admin
	pass

def edit():
	# pegar produto pelo id ou slug
	# criar formulario de edicao
	# apenas para admin
	pass

@auth.requires_login()
@auth.requires_membership("admin")
def new():
	message = None
	#hide_fields("product",["total_price"]) #esconder campos
	form=SQLFORM(db.product)
	if form.process().accepted:
		message = T("Product registered")
	elif form.errors:
		message = T("Product erros")
	
	return dict(form=form, message=message)