# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api


class Alertas(ViewletBase):
    def getAlertas(self):
        catalog = self.context.portal_catalog
        portal = api.portal.get()
        try:
            secao = self.context.secaoID
            folder = portal[secao]
            path = '/'.join(folder.getPhysicalPath())
        except:
            path = '/'.join(portal.getPhysicalPath()) + '/cidadao'

        alertas = catalog(path=path, portal_type='alerta', review_state='published', sort_on='effective', sort_order='reverse')
        return alertas
