from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.supermodel import model
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile

from cckf.content import MessageFactory as _


class IHintImage(model.Schema):

    image = namedfile.NamedBlobImage(
        title=_(u"Hint Image"),
        description=_(u"Image Size: 800x530"),
        required=False,
    )

    image_caption = schema.TextLine(
        title=_(u"Hint Image Caption"),
        description=u"",
        required=False,
    )

alsoProvides(IHintImage, IFormFieldProvider)


class HintImage(object):
    implements(IHintImage)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context

