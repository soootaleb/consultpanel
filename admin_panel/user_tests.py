def is_classique_client(user):
    return user.groups.filter(name="classique_client").exists()


def is_classique_formateur(user):
    return user.groups.filter(name="classique_formateur").exists()


def is_super_formateur(user):
    return user.groups.filter(name="super_formateur").exists()


def is_super_client(user):
    return user.groups.filter(name="super_client").exists()


def is_formateur(user):
    return is_classique_formateur(user) or is_super_formateur(user)


def is_client(user):
    return is_classique_client(user) or is_super_client(user)
