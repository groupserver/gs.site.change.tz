# coding=utf-8
import pytz
from zope.interface import Interface
from zope.schema import Choice
from zope.schema.vocabulary import SimpleVocabulary

timezones = SimpleVocabulary.fromValues(pytz.common_timezones)

class IGSSiteTimezone(Interface):
    
    tz = Choice(title=u'Timezone',
      description=u'The timezone you wish to use',
      required=True,
      default=u'UTC',
      vocabulary=timezones)

