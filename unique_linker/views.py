from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from admin_panel.user_tests import is_formateur
from consult_panel.models import DebugValidateEmail
from unique_linker.models import Unique


# TODO Pages d'erreurs
def index(request, jeton):
    try:
        unique = Unique.objects.get(jeton=jeton)
    except Exception:
        return HttpResponse('<pre>Bad Token.</pre>')
    if unique.perime:
        return HttpResponse('<pre>Obsolete Token.</pre>')
    return unique.exec_methode()


@user_passes_test(is_formateur)  # L'auteur du lien doit être connecté
def debug_generate(request, mail):
    # Création d'un mail
    debug_validate_email = DebugValidateEmail(email=mail)
    # Sauvegarde
    debug_validate_email.save()

    # Création d'un dict contenant les paramètre à passer à la méthdoe
    params = {"id": debug_validate_email.id}

    # Création de la chaine d'inclusion de la méthode (module/object/method)
    methode = 'consult_panel.models/DebugValidateEmail/valid'

    # Création de l'objet unique
    unique = Unique(auteur=request.user, methode=methode, params=params)
    unique.save()

    # Récupération de l'URL unique
    url = unique.get_url()

    return HttpResponse('<pre>{}<a href="{}">Valider ce mail</a>. </pre>'
                        .format(unique, url))

