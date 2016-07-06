from zope.interface import implementer
from plone.dexterity.content import Item

from cckf.content.interfaces import IActivity
from cckf.content.interfaces import IGrant
from cckf.content.interfaces import ISinology


@implementer(IActivity)
class Activity(Item):
    """Item Subclass for Activity
    """

@implementer(IGrant)
class Grant(Item):
    """Item Subclass for Grant
    """

@implementer(ISinology)
class Sinology(Item):
    """Item Subclass for Sinology
    """

