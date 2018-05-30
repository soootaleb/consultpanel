#!/usr/bin/env bash

echo "Seting up database..."
python manage.py localdb
sleep 3
echo "Apply migrations..."
python manage.py migrate
echo "Load data..."
python manage.py loaddata data/actions_formation.json
python manage.py loaddata data/entreprises.json
python manage.py loaddata data/formations.json
python manage.py loaddata data/catalogues.json
python manage.py loaddata data/clients.json
python manage.py loaddata data/centres_formation.json
python manage.py loaddata data/groups.json
python manage.py loaddata data/users.json
python manage.py loaddata data/profiles.json
echo "###########################"
echo " "
echo "ConsultPanel Demo Account: "
echo "Username: doe@consultpanel.fr"
echo "Password: azerty"
