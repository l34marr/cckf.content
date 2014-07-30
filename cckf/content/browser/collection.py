from Products.Five.browser import BrowserView
from Acquisition import aq_inner
from plone.app.contenttypes.behaviors.collection import ICollection
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


class AggregateView(BrowserView):

    def results(self, **kwargs):
        context = aq_inner(self.context)
        wrapped = ICollection(context)
        return wrapped.results(**kwargs)

    def getCategory(self):
        results = self.results(batch=False)
        _mapping = {}
        for item in results:
            obj = item.getObject()
            category = obj.category
            try:
                _mapping[category].append(item)
            except KeyError:
                _mapping[category] = []
                _mapping[category].append(item)
        return _mapping

    def t_title(self, vocab, value):
        try:
            factory = getUtility(IVocabularyFactory, vocab)
            vocabulary = factory(self.context)
            term = vocabulary.getTerm(value)
            return term.title
        except:
            return None

