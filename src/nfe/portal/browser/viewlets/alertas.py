# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase


class Alertas(ViewletBase):
    def getAlertas(self):
        catalog = self.context.portal_catalog
        alertas = catalog(portal_type='alerta', review_state='published', sort_on='effective', sort_order='reverse')
        return alertas
