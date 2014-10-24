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
from __future__ import unicode_literals
from pytz import common_timezones
from zope.interface import Interface
from zope.schema import Choice
from zope.schema.vocabulary import SimpleVocabulary
from . import GSMessageFactory as _


timezones = SimpleVocabulary.fromValues(common_timezones)


class IGSSiteTimezone(Interface):
    'The site timezone schema'
    tz = Choice(title=_('Timezone'),
                description=_('The timezone you wish to use'),
                vocabulary=timezones,
                required=True,
                default='UTC',)
