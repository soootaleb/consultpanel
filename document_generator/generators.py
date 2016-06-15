from .models import Template
from django.template import Template as DjangoTemplate, Context
from consult_panel.models import Profile
from consult_panel.settings import MEDIA_ROOT
import os
import pdfkit


class DocumentGenerator():

    def __init__(self, user):
        if user is None:
            raise Exception("You must give a user to the generator")
        self.profile = Profile.objects.get(user=user)
        self.do_save = False
        self.context = {
            'profile': self.profile
        }

    def generate(self, document):
        self.filename = document
        self.file = os.path.join(self.profile.get_medias_directory(), document)
        if not os.path.isfile(self.file):
            raise Exception("The file " + self.file +
                            " does not exists for user " + str(self.profile.user))
        self.template = DjangoTemplate(open(self.file, 'r').read())
        return self

    def with_context(self, context):
        self.context = {**self.context, **context}
        self.context['profile'] = self.profile
        return self

    def save(self):
        self.do_save = True
        return self

    def compile(self):
        self.html = self.template.render(Context(self.context))

    def as_html(self):
        self.compile()
        if self.do_save:
            open(self.file[:-5] + '_generated.html', 'w+').write(self.html)
        return self.html

    def as_pdf(self):
        self.compile()
        pdfkit.from_string(self.html, self.file[:-5] + '_new.pdf')
        return os.path.join('/medias/admin_documents', self.profile.get_medias_directory_simple(), self.filename[:-5] + '_new.pdf')


class ConventionGenerator(DocumentGenerator):
    pass