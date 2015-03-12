# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2012, 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.base import SiteForm, select_widget
from .interfaces import IGSSiteTimezone
from . import GSMessageFactory as _


class Change(SiteForm):
    label = _('change-timezone', 'Change the site timezone')
    pageTemplateFileName = 'browser/templates/change.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IGSSiteTimezone, render_context=False)

    def __init__(self, context, request):
        SiteForm.__init__(self, context, request)
        self.form_fields['tz'].custom_widget = select_widget

    @Lazy
    def divisionConfiguration(self):
        ctx = self.siteInfo.siteObj
        assert ctx
        retval = getattr(ctx, 'DivisionConfiguration')
        assert retval
        return retval

    def setUpWidgets(self, ignore_request=False):
        tz = getattr(self.divisionConfiguration, 'tz', 'UTC')
        data = {'tz': tz}
        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)

    @form.action(label=_('change-button', 'Change'), name='change',
                 failure='handle_change_action_failure')
    def handle_change(self, action, data):
        if not hasattr(self.divisionConfiguration, 'tz'):
            self.divisionConfiguration.manage_addProperty(
                'tz', data['tz'], 'string')
        else:
            self.divisionConfiguration.manage_changeProperties(
                tz=data['tz'])

        site = '<a href="/">{0}</a>'.format(self.siteInfo.name)
        tz = '<code>{0}</code>'.format(data['tz'])
        self.status = _(
            'status-success', 'The timezone on ${siteName} has been '
            'changed to ${tz}.', mapping={'siteName': site, 'tz': tz})

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            s = _('single-error', 'There is an error:')
        else:
            s = _('multiple-errors', 'There are errors:')
        self.status = '<p>{0}</p>'.format(s)
