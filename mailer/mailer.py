# -*- coding: utf-8 -*-
import os
import logging
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from datetime import datetime


logger = logging.getLogger(__name__)


class EmailTemplate(object):
    """Provide pattern to organize and send your common email messages.

    All Emails should be stored on these paths:
    templates/email/<template_name>/subject.txt
    templates/email/<template_name>/message.html
    templates/email/<template_name>/message.txt

    Examples:
    >>> email = EmailTemplate('<template_name>', {'date', datetime.now().date})
    >>> email.send(['foo@bar.com'], context={'name': 'Bill'})

    Only process your email templates:
    >>> user_data = {'name': 'Bill'}
    >>> subject = email.get_subject(user_data)
    >>> message = email.get_message_txt(user_data)
    >>> from django.core.mail import send_mail
    >>> send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                  ['bill@foo.bar'])


    Prevents method "send" to massive send.
    >>> email = EmailTemplate('<template_name>', {'date', datetime.now().date})
    >>> messages = []
    >>> messages.append(email.send(['bill@foo.bar'], context={'name': 'Bill'},
                                   commit=False))
    >>> messages.append(email.send(['jonh@foo.bar'], context={'name': 'Jonh'},
                                   commit=False))
    >>> from django.core import mail
    >>> connection = mail.get_connection()
    >>> connection.send_messages(messages)
    """

    template_base_dir = "email"
    template_subject = 'subject.txt'
    template_message_html = 'message.html'
    template_message_txt = 'message.txt'

    def __init__(self, name, default_context=None, **kwargs):
        self.name = name
        self.default_context = default_context or {}

    def __unicode__(self):
        return self.name

    @property
    def template_dir(self):
        return os.path.join(self.template_base_dir, self.name)

    @property
    def subject(self):
        """Template path of subject"""
        return os.path.join(self.template_dir, self.template_subject)

    @property
    def message_html(self):
        """Template path of html message"""
        return os.path.join(self.template_dir, self.template_message_html)

    @property
    def message_txt(self):
        """Template path of text message"""
        return os.path.join(self.template_dir, self.template_message_txt)

    def _get_template(self, template, context=None):
        try:
            return render_to_string(template, context)
        except TemplateDoesNotExist:
            logger.debug("Email template {} doesn't exists.".format(template))
            return None

    def get_subject(self, context=None):
        print("Subject : " + self.subject)
        return self._get_template(self.subject, context)

    def get_message_html(self, context=None):
        print("Message : " + self.message_html)
        return self._get_template(self.message_html, context)

    def get_message_txt(self, context=None):
        print("Message TXT : " + self.message_txt)
        return self._get_template(self.message_txt, context)

    def send(self, recipient_list, context=None, commit=True, **kwargs):
        """Send email message and return EmailMessage instance.

        Params:
            recipient_list -> List of emails to sent.
            context -> Contex data of template.
            commit -> If false, prevents to send message, only returning the
                      EmailMessage instance.
            kwargs -> Uses to pass other EmailMessage params like from_email,
                      bcc, cc and headers.
        """

        subject = self.get_subject(context)
        msg_html = self.get_message_html(context)
        msg_txt = self.get_message_txt(context)

        message = EmailMultiAlternatives(
            subject=subject,
            body=msg_txt,
            to=recipient_list,
            from_email=kwargs.get('from_email', settings.DEFAULT_FROM_EMAIL),
            bcc=kwargs.get('bcc'),
            cc=kwargs.get('cc'),
            headers=kwargs.get('headers'))

        if msg_html:
            message.attach_alternative(msg_html, 'text/html')

        if commit:
            message.send(fail_silently=kwargs.get('fail_silently', False))

        return message
