# -*- coding: utf-8 -*-

from Products.Five import BrowserView


class SectionView(BrowserView):

    def getSecao(self):
        context = self.context
        secao = context.Title()
        secaoID = context.id

        if not context.hasProperty('secao'):
            context.manage_addProperty(id='secao', type='string', value=secao)
            context.manage_addProperty(id='secaoID', type='string', value=secaoID)
        else:
            pass

        return secao
