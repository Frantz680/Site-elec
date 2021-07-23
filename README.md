# Site-elec

-----------------

**Le concept de l'application ?**

Cette application permettra à quiconque de comprendre et apprendre l'electriciter.

Il y'a diffrentes explications sur :
- La lumière
- Les prises
- Tableau électrique

L'admin pourra créer des catégories, sous-catégories et des articles directement sur le site internet.

Les utilisateurs pourront créer des comptes, changer de photo de profil mais aussi mettre des commentaires sur les différentes articles.

-----------------

**Le site te plaît ?**

Alors suit mes instructions en bas pour avoir le même site.
Autrement à ta libre imagination pour les modifications.

-----------------

**Avez vous déjà l'application Python ?**

Pour ouvrir cette application coder en Python, il vous faudra l'installer.
Rendez-vous sur le [site de Python](https://www.python.org/) pour l'installation.

**Comment lancer l'application ?**

Il vous faut tout d'abord créer un environnement virtuel.
Explication:

Il faut accéder à l'invite de commande:
Dans le champ de recherche du menu Démarrer taper la commande suivante:

-`cmd`
Ceci permet d'accéder a l'invite de commande.

-`pip install virtualenv`
Ceci est l'installation d'un environnement virtuel.

-`virtualenv -p python3 env`
Ceci va vous créer un dossier ''env''.

-`source env/bin/activate`
Ceci active un environnement virtuel.

-----------------

**Installation des différentes exigences**


Ensuite, il vous faudra installer les différentes exigences pour la bonne utilisation du jeu.
Explication :

-`python3 -m pip install -r requirements.txt`
Ceci installera les differentes exigences du jeu.

-----------------

**Base de données**

Pour créer la base de données avec les produits dedans.
Explication :

- `python manage.py makemigrations`
Qui est responsable de la création de nouvelle migrations.

- `python manage.py migrate`
Ceci lancera les migrations.

-----------------

**Lancement de l'application**

-`python manage.py runserver`
Ceci vous lancera automatiquement l'application.