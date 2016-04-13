# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from DateTime import DateTime


class Noticias(BrowserView):
    def getDate(self, date):
        data = DateTime(date).strftime('%d/%m/%Y')
        return data


class Colecao(BrowserView):
    def getDate(self, date):
        data = DateTime(date).strftime('%d/%m/%Y')
        return data

    def Filtro(self):
        try:
            filtro = self.request.form['SearchableText']
            return filtro
        except:
            return False

    def getFilteredContent(self, items):
        try:
            filtro = self.request.form['SearchableText']
        except:
            filtro = None

        filtered = []

        for i in items:
            terms = i.getObject().pergunta.raw + i.getObject().resposta.raw
            if filtro in terms:
                filtered.append(i.getObject())

        return filtered

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

    def getLegislacao(self, items):
        try:
            filtro = self.request.form['filtrarLegislacao']
        except:
            filtro = None

        items = [x for x in items if x.getObject().tipo == filtro]

        return items

    def isSAT(self, obj):
        parentId = obj.aq_parent
        if parentId == 'sat-iss':
            return 'sat-iss'
        else:
            return False
