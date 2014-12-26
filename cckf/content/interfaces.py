from plone.directives import form


class INews(form.Schema):
    """News Type."""
    form.model('models/news.xml')

class IGrant(form.Schema):
    """Grant Type."""
    form.model('models/grant.xml')

class ISinology(form.Schema):
    """Sinology Type."""
    form.model('models/sinology.xml')

