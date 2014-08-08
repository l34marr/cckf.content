from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from cckf.content import MessageFactory as _


class Region(object):
    """Region Vocabulary
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='Australia', title=_(u'Australia')),
            SimpleTerm(value='Austria', title=_(u'Austria')),
            SimpleTerm(value='Bangladesh', title=_(u'Bangladesh')),
            SimpleTerm(value='Belgium', title=_(u'Belgium')),
            SimpleTerm(value='Bulgaria', title=_(u'Bulgaria')),
            SimpleTerm(value='Canada', title=_(u'Canada')),
            SimpleTerm(value='Chile', title=_(u'Chile')),
            SimpleTerm(value='China', title=_(u'China')),
            SimpleTerm(value='Costa Rica', title=_(u'Costa Rica')),
            SimpleTerm(value='Croatia', title=_(u'Croatia')),
            SimpleTerm(value='Czech Republic', title=_(u'Czech Republic')),
            SimpleTerm(value='Denmark', title=_(u'Denmark')),
            SimpleTerm(value='Estonia', title=_(u'Estonia')),
            SimpleTerm(value='Finland', title=_(u'Finland')),
            SimpleTerm(value='France', title=_(u'France')),
            SimpleTerm(value='Germany', title=_(u'Germany')),
            SimpleTerm(value='Greece', title=_(u'Greece')),
            SimpleTerm(value='Hong Kong', title=_(u'Hong Kong')),
            SimpleTerm(value='Hungary', title=_(u'Hungary')),
            SimpleTerm(value='Iceland', title=_(u'Iceland')),
            SimpleTerm(value='India', title=_(u'India')),
            SimpleTerm(value='Indonesia', title=_(u'Indonesia')),
            SimpleTerm(value='Ireland', title=_(u'Ireland')),
            SimpleTerm(value='Israel', title=_(u'Israel')),
            SimpleTerm(value='Italy', title=_(u'Italy')),
            SimpleTerm(value='Japan', title=_(u'Japan')),
            SimpleTerm(value='Jordan', title=_(u'Jordan')),
            SimpleTerm(value='Kazakhstan', title=_(u'Kazakhstan')),
            SimpleTerm(value='Korea', title=_(u'Korea')),
            SimpleTerm(value='Latvia', title=_(u'Latvia')),
            SimpleTerm(value='Lithuania', title=_(u'Lithuania')),
            SimpleTerm(value='Macau', title=_(u'Macau')),
            SimpleTerm(value='Malaysia', title=_(u'Malaysia')),
            SimpleTerm(value='Mexico', title=_(u'Mexico')),
            SimpleTerm(value='Mongolia', title=_(u'Mongolia')),
            SimpleTerm(value='New Zealand', title=_(u'New Zealand')),
            SimpleTerm(value='Norway', title=_(u'Norway')),
            SimpleTerm(value='Panama', title=_(u'Panama')),
            SimpleTerm(value='Philippines', title=_(u'Philippines')),
            SimpleTerm(value='Poland', title=_(u'Poland')),
            SimpleTerm(value='Portugal', title=_(u'Portugal')),
            SimpleTerm(value='Republic of China', title=_(u'Republic of China')),
            SimpleTerm(value='Romania', title=_(u'Romania')),
            SimpleTerm(value='Russia', title=_(u'Russia')),
            SimpleTerm(value='Serbia', title=_(u'Serbia')),
            SimpleTerm(value='Singapore', title=_(u'Singapore')),
            SimpleTerm(value='Slovakia', title=_(u'Slovakia')),
            SimpleTerm(value='Slovenia', title=_(u'Slovenia')),
            SimpleTerm(value='South Africa', title=_(u'South Africa')),
            SimpleTerm(value='Spain', title=_(u'Spain')),
            SimpleTerm(value='Sweden', title=_(u'Sweden')),
            SimpleTerm(value='Switzerland', title=_(u'Switzerland')),
            SimpleTerm(value='Thailand', title=_(u'Thailand')),
            SimpleTerm(value='The Netherlands', title=_(u'The Netherlands')),
            SimpleTerm(value='Turkey', title=_(u'Turkey')),
            SimpleTerm(value='Uganda', title=_(u'Uganda')),
            SimpleTerm(value='UK', title=_(u'UK')),
            SimpleTerm(value='Ukraine', title=_(u'Ukraine')),
            SimpleTerm(value='USA', title=_(u'USA')),
            SimpleTerm(value='USSR', title=_(u'USSR')),
            SimpleTerm(value='Uzbekistan', title=_(u'Uzbekistan')),
            SimpleTerm(value='Vietnam', title=_(u'Vietnam')),
            SimpleTerm(value='Yugoslavia', title=_(u'Yugoslavia'))
        )
        return SimpleVocabulary(items)
RegionFactory = Region()

class Category(object):
    """Category Vocabulary
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='CS', title=_(u'Conference and Seminar Grants')),
            SimpleTerm(value='RG', title=_(u'Research Grants')),
            SimpleTerm(value='SP', title=_(u'Publication Subsidies')),
            SimpleTerm(value='DB', title=_(u'Database Grants')),
            SimpleTerm(value='DL', title=_(u'Distinguished Lectureships')),
            SimpleTerm(value='IE', title=_(u'Institutional Enhancement Grants')),
            SimpleTerm(value='SS', title=_(u'Senior Scholar Grants')),
            SimpleTerm(value='LA', title=_(u'Library Acquisition Grants')),
            SimpleTerm(value='VS', title=_(u'Visiting Fellowships')),
            SimpleTerm(value='XP', title=_(u'Special Project Grants')),
            SimpleTerm(value='TG', title=_(u'Travel Grants')),
            SimpleTerm(value='GP', title=_(u'Professor Grants')),
            SimpleTerm(value='BO', title=_(u'Bilateral Cooperation Grants')),
            SimpleTerm(value='CO', title=_(u'Consortium Operations')),
            SimpleTerm(value='LS', title=_(u'Lecture Series Grants')),
            SimpleTerm(value='DS', title=_(u'Distinguished Scholar Grants')),
            SimpleTerm(value='GS', title=_(u'Scholar Grants')),
            SimpleTerm(value='JS', title=_(u'Junior Scholar Grants')),
            SimpleTerm(value='CG', title=_(u'Cooperative Guidance')),
            SimpleTerm(value='WJ', title=_(u'Walter Judd Research Fellowship')),
            SimpleTerm(value='DD', title=_(u'Doctoral Fellowships')),
            SimpleTerm(value='PD', title=_(u'Postdoctoral Research Fellowships')),
            SimpleTerm(value='DF', title=_(u'Dissertation Fellowships for ROC Students Abroad')),
            SimpleTerm(value='CASA-PD', title=_(u'Canadian Asian Studies Association/Post')),
            SimpleTerm(value='CASA-DD', title=_(u'Canadian Asian Studies Association/Pre')),
            SimpleTerm(value='MG', title=_(u'Graduate Student and Faculty Mobility Grants')),
            SimpleTerm(value='SW', title=_(u'Graduate Student Workshops'))
        )
        return SimpleVocabulary(items)
CategoryFactory = Category()

class Classify(object):
    """Classify Vocabulary
    """
    implements(IVocabularyFactory)
    def __call__(self, context=None):
        items = (
            SimpleTerm(value='01', title=_(u'Selected')),
            SimpleTerm(value='02', title=_(u'Directory')),
            SimpleTerm(value='03', title=_(u'Library')),
            SimpleTerm(value='04', title=_(u'Literature')),
            SimpleTerm(value='05', title=_(u'Religion')),
            SimpleTerm(value='06', title=_(u'Family Tree')),
            SimpleTerm(value='07', title=_(u'Biography')),
            SimpleTerm(value='08', title=_(u'Journal')),
            SimpleTerm(value='09', title=_(u'Essay')),
            SimpleTerm(value='10', title=_(u'Newspapper')),
            SimpleTerm(value='11', title=_(u'Archive'))
        )
        return SimpleVocabulary(items)
ClassifyFactory = Classify()

