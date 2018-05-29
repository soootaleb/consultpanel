import os
import json
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from consult_panel.models import ActionFormation


class Command(BaseCommand):
    help = 'Create or update the actions formation (cf. /data).'

    def add_arguments(self, parser):
        default_actions_formation_path = \
            os.path.join(settings.BASE_DIR, 'data', 'actions_formation.json')

        parser.add_argument(
            '--file',
            dest='actions_formations',
            nargs='?',
            type=str,
            default=default_actions_formation_path,
            const=default_actions_formation_path,
            help=(
                'A json file of ActionFormation created '
                'with `./manage.py dumpdata` command.'
            )
        )

    def handle(self, *args, **options):
        actions_formation_path = options['actions_formations']

        if not os.path.isfile(actions_formation_path):
            raise CommandError('{}} not found.'.format(actions_formation_path))

        with open(actions_formation_path) as file:
            actions_formation = json.load(file)
            for action_formation in actions_formation:
                self.manage_action_formation(action_formation)

    def manage_action_formation(self, af_infos):
        try:
            act_form, created = ActionFormation.objects.update_or_create(
                pk=af_infos['pk'],
                defaults=af_infos['fields']
            )
        except Exception as err:
            raise CommandError(err)

        success_message = '{} successfully {}.'.format(
            act_form,
            'created' if created else 'updated'
        )
        self.stdout.write(success_message)
