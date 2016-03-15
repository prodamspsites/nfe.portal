# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone import api
from DateTime import DateTime


class Noticias(BrowserView):
    def getDate(self, date):
        data = DateTime(date).strftime('%d/%m/%Y')
        hora = DateTime(date).strftime('%H:%M')
        return data + ' às ' + hora


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

        items = [x.getObject() for x in items]

        if searchPergunta and searchResposta:
            lista1 = [x.getObject() for x in searchPergunta]
            lista2 = [x.getObject() for x in searchResposta if x.getObject().aq_parent not in lista1]

            items = lista1 + lista2

        return items

    def FiltroLegislacao(self):
        try:
            filtro = self.request.form['filtrarLegislacao']
            return filtro
        except:
            return False

    def FiltroDuvida(self):
        try:
            filtro = self.request.form['SearchableText']
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

        items = [x for x in search if x.getObject().tipo == filtro]

        return items

    def isSAT(self, obj):
        isSat = 'sat-iss' in obj.getPhysicalPath()
        contextPath = 'sat-iss' in self.context.getPhysicalPath()
        if isSat and not contextPath:
            return 'sat-iss'
        else:
            return False
