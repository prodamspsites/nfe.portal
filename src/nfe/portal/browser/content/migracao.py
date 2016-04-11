# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from plone.app.textfield.value import RichTextValue

class Migracao(BrowserView):

    def migracao(self):
        catalog = self.context.portal_catalog
        pergunta = catalog(portal_type='pergunta')
        for i in pergunta:
            path = '/'.join(i.getObject().getPhysicalPath())
            parent = i.getObject().aq_parent
            resposta = catalog(path=path, portal_type='resposta')
            if resposta:
                resposta = resposta[0].getObject()
                p_texto = i.getObject().pergunta.raw
                r_texto = resposta.resposta.raw
                portal.invokeFactory('pergunta', 'pergunta', pergunta=RichTextValue(p_texto, 'text/html', 'text/x-html-safe', encoding='utf-8'), resposta=RichTextValue(r_texto, 'text/html', 'text/x-html-safe', encoding='utf-8'))
            parent.manage_delObjects([i.id])