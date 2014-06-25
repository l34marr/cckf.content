from zope.interface import implements
from plone.dexterity.content import Item

from cckf.content.interfaces import ISinology


class Sinology(Item):
    implements(ISinology)

