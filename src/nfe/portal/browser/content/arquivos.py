# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from DateTime import DateTime


class ArquivosView(BrowserView):
    def getDate(self, date):
        data = DateTime(date).strftime('%d/%m/%Y')
        return data
