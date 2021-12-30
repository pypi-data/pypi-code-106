# -*- coding: utf-8 -*-
"""Init and utils."""
from Products.CMFPlone.interfaces import ISiteSchema
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.i18nmessageid import MessageFactory
from zope.interface import implementer
from zope.viewlet.interfaces import IViewlet


_ = MessageFactory('ruddocom.policy')


# -*- coding: utf-8 -*-


@implementer(IViewlet)
class PdfIframerViewlet(BrowserView):

    render = ViewPageTemplateFile("view.pt")

    def __init__(self, context, request, view, manager):
        super(PdfIframerViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.view = view
        self.manager = manager

    @property
    def src(self):
        root = self.context.portal_url.getPortalObject().absolute_url()
        version = "1.1-4"
        return root + "/++resource++ruddocom-pdfiframer/iframehandling-compiled.js?version=%s" % version

    def update(self):
        """The viewlet manager _updateViewlets requires this method"""
        pass
