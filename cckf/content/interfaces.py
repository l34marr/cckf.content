from plone.directives import form


class ISinology(form.Schema):
    """Sinology Type."""
    form.model('models/sinology.xml')

