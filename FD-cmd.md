# Last : 09-01-2023

------------
## Mode d'emploi:

- manage.py
    - Ce qui permet de lancer les différents ligne de commande

### Premier répertoire racine

- __init__.py
    - Un fichier vide qui indique à Python que ce répertoire doit être considéré comme un paquet
- setting.py
    - Réglages et configuration de ce projet Django
- urls.py
    - Les déclarations des URL
- asgi.py
    - Un point d’entrée pour les serveurs Web compatibles aSGI pour déployer votre projet
- wsgi.py
    - Un point d’entrée pour les serveurs Web compatibles WSGI pour déployer votre projet

## Environnement virtuel

- Installation de l'environnement virtuel
    - pip install virtualenv
- Ceci va vous créer un dossier "env".
    - virtualenv -p python3 env
- Active un environnement virtuel
    - source env/bin/activate
    - env/Scripts/activate

## Commandes:

- Création d'un projet
    - django-admin startproject mysite
- Lancer le serveur local
    - python manage.py runserver
- Créer un superuser
    - python manage.py createsuperuser

- L'exécution et de l'annulation des migrations
    - python manage.py migrate
- Création de nouvelles migrations
    - python manage.py makemigrations