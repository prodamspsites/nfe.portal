# -*- coding: utf-8 -*-

from nfe.portal.interfaces import IPergunta
from plone.indexer.decorator import indexer


@indexer(IPergunta)
def PerguntaSearchableIndex(obj):
    return u' '.join([obj.pergunta.output])
