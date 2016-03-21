# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    records = SQLTABLE(db().select(db.recipe.name,db.recipe.description,db.recipe.image),
                      upload=URL('download'),_id='records')
    recipe = SQLFORM.grid(db.recipe,upload=URL('download'))
    return locals()

@cache.action()
def download():
    return response.download(request, db)

def user():
    return dict(form=auth())

def call():
    return service()


@auth.requires_login()
def newrecipe():
    recipe = SQLFORM.grid(db.recipe,upload=URL('download'))
    return locals()