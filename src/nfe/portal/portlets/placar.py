# -*- coding: utf-8 -*-

from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base
from plone.memoize.compress import xhtml_compress
from plone.portlets.interfaces import IPortletDataProvider
from zope import schema
from zope.formlib import form
from zope.interface import implements


class iPlacar(IPortletDataProvider):

    hide = schema.Bool(
        title=_(u'Hide portlet'),
        description=_(u'Tick this box if you want to temporarily hide '
                      'the portlet without losing your information.'),
        required=True,
        default=False)


class Assignment(base.Assignment):

    implements(iPlacar)

    def __init__(self, hide=False):
        self.hide = hide

    @property
    def title(self):
        return 'Placar'


class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('templates/placar.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    def render(self):
        return xhtml_compress(self._template())

    @property
    def available(self):
        return not self.data.hide


class AddForm(base.AddForm):
    form_fields = form.Fields(iPlacar)
    label = _(u'Mostrar placar')
    description = _(u'Mostrar placar')

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(iPlacar)
    label = _(u'Mostrar placar')
    description = _(u'Mostrar placar')
