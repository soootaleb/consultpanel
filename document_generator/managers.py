from django.db.models import Count
from consult_panel.models import Client, Profile
from consult_panel.settings import MEDIA_ROOT
from .generators import DocumentGenerator


class DocumentManager(object):

    generator = None
    user = None

    def __init__(self, user, generator):
        self.user = user
        self.generator = generator


class AdminDocumentManager(DocumentManager):

    admin = None

    def __init__(self, user):
        super().__init__(user, DocumentGenerator(user))
        self.admin = Profile.objects.get(user=user)

    def get_conventions_by_client(self, session):
        clients = Client.objects \
            .filter(inscription__session=session) \
            .annotate(inscriptions=Count('inscription')) \
            .distinct()
        for client in clients:
            client.convention_url += 'convention_client_' + \
                str(client.id) + '_session_' + str(session.id) + '.pdf'
        return clients
