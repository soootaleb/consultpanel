from django.shortcuts import redirect
from formtools.wizard.views import SessionWizardView
from admin_panel.forms.registration_forms import RegistrationForm
from admin_panel.forms.forms import ProfileForm


class RegistrationWizard(SessionWizardView):

    def get_template_names(self):
        return ['registration/admin_registration_steps.html']

    def done(self, form_list, **kwargs):
        """
        Do something with form_list like saving them or other
        :param form_list:
        :param kwargs:
        :return:
        """
        return redirect('admin_index')
