# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api
import re


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
            filtro = self.request.form['textoBusca']
            return filtro
        except:
            return False

    def getFilteredContent(self):
        portal = api.portal.get()
        secao = self.context.secaoID
        print secao
        path = '/'.join(portal.getPhysicalPath()) + '/' + secao
        print path

        try:
            filtro = self.request.form['textoBusca']
            filtro = filtro.split(' ')
            print 'com filtro'
        except:
            filtro = None

        items = self.context.portal_catalog(path=path, portal_type="pergunta")
        results = []

        for i in items:
            print i
            term = i.getObject().pergunta.raw.lower() + ' ' + i.getObject().resposta.raw.lower()
            term = self.limpaCodigo(term).split(' ')
            if any(i in filtro for i in term):
                results.append(i)

        return results

    def limpaCodigo(self, text):
        p = re.compile(r'<.*?>')
        return p.sub('', text)
