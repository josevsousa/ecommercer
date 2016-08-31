# -*- coding: utf-8 -*-

def show():
	# pegar produto no bando de dados
	# buscar pelo slug //qualquer campo != id
	# acessar api do twitte
	#slice //pega registro por outro campo da tabela
	db.product.tax_price = Field.Virtual(lambda row: row.product.unit_price * origins.get(row.product.origin, 1))

	try: #se for passado o id
		pid = int(request.args(0))
		product = db.product[pid]
	except Exception: # se for pegar outro campo
		try:
			pid = int(request.args(0)[:5])
			product = db.product[pid]
		except Exception:
			redirect(URL('home','index'))

	# poderia esta no db
	colors = ["amarelo","azul", "vermelho"]

	fields = [
		Field("qtd", "integer", label=T("Quantity"), requires=IS_NOT_EMPTY(error_message=T("You have to information quantity"))),
		Field("pid", default="%s"% product.id ),
		Field("colors", label=T("Colors"), requires=IS_IN_SET(colors))
	]

	form = SQLFORM.factory(*fields, 
		submit_button=T("Add to cart"),
		_method="POST" #nao vai pela url. o valor é pego pelo nome dos fields la no metodo add
		)

	if form.process().accepted:
		session.cart = session.cart or [] #se session.cart não existir ele cria ela vazia
		item = {
			"id" :  product.id,
			"qtd" :  form.vars.qtd,
			"name" :  product.name,
			"thumbnail" :  product.thumbnail,
			"price" :  product.unit_price,
			"total" :  float(form.vars.qtd) * float(product.unit_price)
		}
		session.cart.append(item)
		redirect(URL('cart','show'))

	# alterando os elementos desse form
	btn = form.elements('input[type=submit]')
	btn[0]["_class"] = "jose"


	return dict(product=product, form=form)

def search():
	# receber parametros e efetuar busca
	pass

def list():
	hide_fields("product",["id","featured","description","picture","thumbnail","total_price"]) #esconder campos
	
	if request.args(0):
		tipo = request.args(0)
		id_tipo = request.args(2)
		if tipo == "view":
			redirect(URL("product/%s"%"dados_product",id_tipo))
		elif tipo == "edit":
			redirect(URL("product/%s"%tipo,id_tipo))	

	query = db.product.id>2
	# rows = db(query).select()
	tax_price = lambda row: row.unit_price * origins.get(row.origin, 1)
	img = lambda row: get_miniatura(row)

	links = [
			dict(header='Produto', body=img),
			dict(header='Tax', body=tax_price)
			]

	table = SQLFORM.grid(query, 
		user_signature=False,
		paginate=2,
		# fields = [db.product.name],
		links=links,
		csv=False,
		# deletable=False,
		# editable=False,
		# details=False,
		selectable=False,
		links_placement = 'left')
	return dict(table=table)

def list_2():
    # hide_fields("product",["total_price"]) #esconder campos
	
	# campos virtuais pra tabela
	db.product.tax_price = Field.Virtual(lambda row: row.product.unit_price * origins.get(row.product.origin, 1))
	db.product.edit = Field.Virtual(lambda row: A("Edit", _href=URL("edit", args=row.product.id)))
	db.product.img = Field.Virtual(lambda row: get_miniatura_sqlformgrid(row))	

	# query da busca no db
	query = db.product.id > 2
	
	# nome dos headers e dos campos do db referente a cada header
	headers =["Produto", "Name","Unit Price","Tax","Edit"]
	fields = ["img","name","unit_price","tax_price","edit"]

	# tabela vazia 
	table = TABLE()

	# thead vazio sendo populado pelo for
	thead = THEAD(TR())
	for header in headers:
		thead[0].append(TD(B(header)))
	table.append(thead)
	
	# montando todos os rows da tabela product
	rows = db(query).select()

	# navegando em todos os rows e populando os tr com o retorno 
	for row in rows:
		tr = TR()
		for field in fields:
			tr.append(row[field])
		table.append(tr)
	
	# add class a tabela
	table["_class"] = "table table-striped table-bordered table=condensed list"

	
	return dict(table=table)

@auth.requires_login()
@auth.requires_membership("admin")
def edit(): 
	# pegar produto pelo id ou slug
	# criar formulario de edicao
	# apenas para admin
	p_id = request.args(0) or redirect(URL("home","index"))
	form = SQLFORM(db.product, int(p_id))
	form.process()
	return dict(form=form)



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


def dados_product():
	pid = request.args(0)
	query = db(db.product.id == int(pid))
	return dict(products=query.select())