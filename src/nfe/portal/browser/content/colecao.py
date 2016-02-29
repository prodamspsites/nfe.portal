# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone import api


class Colecao(BrowserView):
    def Filtro(self):
        try:
            filtro = self.request.form['SearchableText']
            return filtro
        except:
            return False

    def getFilteredContent(self):
        portal = api.portal.get()
        secao = self.context.secaoID
        path = '/'.join(portal.getPhysicalPath()) + '/' + secao

        try:
            filtro = self.request.form['SearchableText']
        except:
            filtro = None

        searchPergunta = self.context.portal_catalog(path=path, portal_type="pergunta", SearchableText=filtro)
        searchResposta = self.context.portal_catalog(path=path, portal_type="resposta", SearchableText=filtro)

        items = searchPergunta + searchResposta

        return items

    def FiltroLegislacao(self):
        try:
            filtro = self.request.form['filtrarLegislacao']
            return filtro
        except:
            return False

    def getLegislacao(self):
        portal = api.portal.get()
        secao = self.context.secaoID
        path = '/'.join(portal.getPhysicalPath()) + '/' + secao

        try:
            filtro = self.request.form['filtrarLegislacao']
        except:
            filtro = None

        search = self.context.portal_catalog(path=path, portal_type="legislacao")

        items = [x for x in search if x.getObject().tipo==filtro]

        return items