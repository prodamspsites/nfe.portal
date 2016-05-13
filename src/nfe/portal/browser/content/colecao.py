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
            filtro = self.request.form['textoBusca']
            return filtro
        except:
            return False

    def getFilteredContent(self, items):
        try:
            filtro = self.request.form['textoBusca']
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
            filtro = self.request.form['textoBusca']
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

    def getParents(self, items):
        parents = []
        for i in items:
            parent = i.getObject().aq_parent
            if parent not in parents:
                parents.append(parent)
        for i in parents:
            num = i.Title().split('.')[0]
            try:
                setattr(i, 'numOrder', int(num))
            except:
                setattr(i, 'numOrder', int(99999))
        parents = sorted(parents, key=lambda x: x.numOrder)
        return parents

    def isSAT(self, obj):
        parentId = obj.aq_parent.id
        if parentId == 'sat-iss':
            return 'sat-iss'
        else:
            return False
