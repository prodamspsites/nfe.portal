# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api


class Duvidas(ViewletBase):
    def getDuvidas(self):
        portal = api.portal.get()
        try:
            secao = self.context.secaoID
            folder = portal[secao]
            duvidas = folder['duvidas-contato']
            perguntas = duvidas.listFolderContents(contentFilter={"portal_type": "pergunta"})

            return perguntas
        except:
            return False

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

        items = [x.getObject() for x in items]

        if searchPergunta and searchResposta:
            lista1 = [x.getObject() for x in searchPergunta]
            lista2 = [x.getObject() for x in searchResposta if x.getObject().aq_parent not in lista1]

            items = lista1 + lista2

        return items
