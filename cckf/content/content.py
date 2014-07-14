from zope.interface import implements
from plone.dexterity.content import Item

from cckf.content.interfaces import IGrant
from cckf.content.interfaces import ISinology


class Grant(Item):
    implements(IGrant)

class Sinology(Item):
    implements(ISinology)

