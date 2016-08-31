# -*- coding: utf-8 -*-

def list():
	# grid de categorias
	# apenas admin
	pass

def new():
	form = SQLFORM(db.category)
	return dict(form=form)