import logging
from Products.Five.browser import BrowserView
from zope.interface import alsoProvides
from plone.protect.interfaces import IDisableCSRFProtection
from plone import api
from plone.app.multilingual.interfaces import ITranslationManager
import csv
from Products.CMFPlone.utils import safe_unicode


logger = logging.getLogger("ImportCSV")

class ImportCSV(BrowserView):
    """ Import Content
    """

    def __call__(self):
        context = self.context
        request = self.request
        catalog = context.portal_catalog
        portal = api.portal.get()
        alsoProvides(request, IDisableCSRFProtection)

        root_zh = portal.get('zh')
        if not root_zh: return
        root_en = portal.get('en')
        if not root_en: return

        prog_zh = root_zh.get('programs')
        if not prog_zh: return
        prog_en = root_en.get('programs')
        if not prog_en: return

        container_zh = prog_zh.get('recipients')
        if not container_zh: return
        container_en = prog_en.get('recipients')
        if not container_en: return

        with open('grant-list.csv', "rb") as file:
            rows = csv.reader(file, delimiter='\t')

            next(rows, None)
            for row in rows:
                folder_zh = container_zh.get(str(row[1]))
                if not folder_zh:
                    fldr = api.content.create(
                        type='Folder',
                        container=container_zh,
                        id=row[1],
                        title=row[1]
                    )
                    fldr.reindexObject()

                if row[2] == '': row[2] = row[3]
                if row[4] == '': row[4] = row[5]
                if row[3] == '': row[3] = row[2]
                if row[5] == '': row[5] = row[4]

                ctnt = api.content.create(
                    type='Grant',
                    container=container_zh.get(str(row[1])),
                    id=row[0],
                    title=safe_unicode(row[2]),
                    year=row[1],
                    director=row[4],
                    description=row[6],
                    department=row[7],
                    region=row[8],
                    category=row[9],
                    budget=row[10],
                    currency=row[11],
                    status=row[12]
                )

                manager = ITranslationManager(ctnt)
                manager.add_translation('en')
                trns = manager.get_translation('en')
                trns.id = str(row[0])
                trns.title = row[3]
                trns.year = row[1]
                trns.director = row[5]
                trns.description = row[6]
                trns.department = row[7]
                trns.region = row[8]
                trns.category = row[9]
                trns.budget = row[10]
                trns.currency = row[11]
                trns.status = row[13]

                ctnt.reindexObject()
                trns.reindexObject()

