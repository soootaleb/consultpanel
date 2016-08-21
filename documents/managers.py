from django.db.models import Count
from consult_panel.models import Client, Profile
from consult_panel.settings import MEDIA_ROOT
from .generators import ConventionGenerator
import os


class DocumentManager(object):

    generator = None
    user = None

    def __init__(self, user, generator):
        self.user = user
        self.generator = generator


class AdminDocumentManager(DocumentManager):

    admin = None

    def __init__(self, user):
        super().__init__(user, ConventionGenerator(user))
        self.admin = Profile.objects.get(user=user)

    def get_conventions(self, session):
        self.generator.session = session
        compiled = []
        clients = Client.objects \
            .filter(inscription__session=session) \
            .annotate(inscriptions=Count('inscription')) \
            .distinct() \

        for client in clients:
            self.generator.client = client
            document = self.generator \
                .generate(os.path.join(Profile.get_admin_medias_directory(), 'convention_base.html')) \
                .save() \
                .with_context({
                    'message': 'Hello World'
                }).as_pdf()
            compiled.append({
                'client': client,
                'doc': document
            })
        return compiled
