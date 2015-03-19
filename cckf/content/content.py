from zope.interface import implements
from plone.dexterity.content import Item

from cckf.content.interfaces import INews
from cckf.content.interfaces import IActivity
from cckf.content.interfaces import IGrant
from cckf.content.interfaces import ISinology


class News(Item):
    implements(INews)

class Activity(Item):
    implements(IActivity)

class Grant(Item):
    implements(IGrant)

class Sinology(Item):
    implements(ISinology)

