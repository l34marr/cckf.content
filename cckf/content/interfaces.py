from plone.directives import form


class IGrant(form.Schema):
    form.model('models/grant.xml')

class ISinology(form.Schema):
    """Sinology Type."""
    form.model('models/sinology.xml')

