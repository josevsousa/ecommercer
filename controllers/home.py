# coding: utf-8

def index():
    categories = db(db.category).select()
    # products = db(db.product.featured == False).select()
    # featured = db(db.product.featured == True).select()
    products = db(db.product).select(limitby=(0,100))
    featured = products.exclude(lambda registro: registro.featured == True)
    
    return dict(products=products,featured=featured)

def user(): 
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """

    if request.args(0) == 'not_authorized':
        return dict(form="Voce não tem autorização mané!")

    if request.args(0) == 'login':
        redirect(URL('home','conta', vars=request.vars))


    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def conta():
    registro = auth.register()
    # registro.elements('input')[1].attributes['_class'] = "form-control" 
    return dict(registro=registro,login=auth.login())