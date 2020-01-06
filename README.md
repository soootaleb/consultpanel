# Consult Panel

## Overview

You can have an overview of the product at http://consultpanel.fr.s3-website.eu-west-3.amazonaws.com/

Please note that only the landing page is online, don't hesitate to ask for a backend & full application deployment.

## Install

* `yarn install` (not `npm`)
* Create a virtualenv with python 3.4 and `pip install -r requirements.txt`

## Commands

* Run Django server `python manage.py runserver`
* Run gulp in watch mode: `yarn start`
* Build statics for production: `yarn build`
* Create or update the actions formation (cf. /data): `./manage.py create_or_update_actions_formation`
