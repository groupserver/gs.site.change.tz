# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form import SiteForm, select_widget
from interfaces import IGSSiteTimezone


class Change(SiteForm):
    label = u'Change the site timezone'
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

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        if not hasattr(self.divisionConfiguration, 'tz'):
            self.divisionConfiguration.manage_addProperty('tz',
                data['tz'], 'string')
        else:
            self.divisionConfiguration.manage_changeProperties(tz=data['tz'])

        self.status = u'<p>The timezone on <a href="/">%s</a> has been '\
            'changed to <code>%s</code>.</p>' % \
            (self.siteInfo.name, data['tz'])
        assert type(self.status) == unicode

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
        assert type(self.status) == unicode
