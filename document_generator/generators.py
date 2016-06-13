from .models import Template
from django.template import Template as DjangoTemplate, Context
from consult_panel.models import Profile
import os


class DocumentGenerator():

    def __init__(self, user):
        self.profile = Profile.objects.get(user=user)
        self.context = {
            'profile': self.profile
        }

    def generate(self, document):
        self.file = os.path.join(self.profile.get_medias_directory(), document)
        self.template = DjangoTemplate(open(self.file, 'r').read())
        return self

    def with_context(self, context):
        self.context = {**self.context, **context}
        self.context['profile'] = self.profile
        return self

    def compile(self):
        self.html = self.template.render(Context(self.context))

    def as_html(self):
        self.compile()
        return self.html

    def as_pdf(self):
        self.compile()
        # Need to convert HTML to PDF
        return self.pdf


class ConventionGenerator(DocumentGenerator):
    pass
