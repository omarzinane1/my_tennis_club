# 🏟️ My Tennis Club — Django Tutorial

> Mini-projet Django créé pour apprendre Django étape par étape.>> **Django utilisé pendant ce projet : 5.2.16**> **Python : 3.11.9**

---

## 📚 Objectif du projet

Ce projet sert de support pratique pour apprendre les bases de Django.

Nous allons progressivement comprendre :

- ✅ Installation de Django- ✅ Création d'un projet Django- ✅ Création d'une application- ✅ `urls.py`- ✅ `views.py`- ✅ Templates HTML- ✅ `settings.py`- ✅ `INSTALLED_APPS`- ✅ Models- ✅ Base de données SQLite- ✅ Migrations- ✅ Django ORM- ✅ Django Shell- ✅ Git et GitHub

L'idée est de ne pas seulement copier les commandes, mais de comprendre **pourquoi** on les utilise.

---

# 1. 🐍 Prérequis

Avant de commencer, installe Python.

Vérifier Python :

```powershellpython --version```

Exemple :

```textPython 3.11.9```

Vérifier Django :

```powershellpython -m django --version```

Exemple :

```text5.2.16```

---

# 2. 📁 Créer le projet

Créer un dossier de travail :

```powershellmkdir Djangocd Django```

---

# 3. 🌱 Créer un environnement virtuel

Créer le virtual environment :

```powershellpython -m venv venv```

### Pourquoi utiliser `venv` ?

Le `venv` permet d'avoir un environnement Python séparé pour le projet.

Cela évite de mélanger les dépendances de plusieurs projets.

---

# 4. ▶️ Activer le virtual environment

Sous Windows PowerShell :

```powershellvenv\Scripts\activate```

Le terminal devient normalement :

```text(venv) PS C:\Users\...\Django>```

---

# 5. 📦 Installer Django

```powershellpython -m pip install django```

Vérifier :

```powershellpython -m django --version```

---

# 6. 🏗️ Créer un projet Django

Créer le projet :

```powershelldjango-admin startproject my_tennis_club```

Structure :

```textmy_tennis_club/│├── manage.py│└── my_tennis_club/    ├── __init__.py    ├── settings.py    ├── urls.py    ├── asgi.py    └── wsgi.py```

## 🧠 Qu'est-ce qu'un projet Django ?

Le **projet** représente l'ensemble du site/application.

---

# 7. 📂 Entrer dans le projet

Le fichier `manage.py` se trouve dans le dossier du projet.

```powershellcd my_tennis_club```

Vérifier :

```powershelldir```

Tu dois voir :

```textmanage.pymy_tennis_club```

> ⚠️ Les commandes `python manage.py ...` doivent généralement être exécutées dans le dossier contenant `manage.py`.

---

# 8. 🚀 Lancer le serveur

```powershellpython manage.py runserver```

Django affiche normalement :

```textStarting development server at http://127.0.0.1:8000/```

Ouvrir :

```texthttp://127.0.0.1:8000/```

Arrêter le serveur :

```textCtrl + C```

---

# 9. 🧩 Créer une App Django

Un projet peut contenir plusieurs applications.

Exemple :

```textProject│├── users├── products├── orders└── blog```

Chaque app possède une responsabilité.

Pour notre projet :

```powershellpython manage.py startapp members```

Structure :

```textmembers/│├── migrations/├── __init__.py├── admin.py├── apps.py├── models.py├── tests.py└── views.py```

---

# 10. ⚙️ Ajouter l'App dans `INSTALLED_APPS`

Ouvrir :

```textmy_tennis_club/settings.py```

Chercher :

```pythonINSTALLED_APPS = [    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',]```

Ajouter :

```python'members',```

Donc :

```pythonINSTALLED_APPS = [    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',    'members',]```

### Pourquoi ?

Parce qu'on indique à Django :

> "L'application `members` fait partie de mon projet."

---

# 11. 👀 `views.py`

Le fichier :

```textmembers/views.py```

contient les **views**.

Une view reçoit une requête et renvoie une réponse.

Exemple :

```pythonfrom django.http import HttpResponse

def members(request):    return HttpResponse("Bienvenue dans Members")```

Ici :

- `request` = requête du navigateur- `HttpResponse(...)` = réponse envoyée au navigateur

---

# 12. 🌐 `urls.py`

`urls.py` sert à faire le lien entre une **URL** et une **view**.

Exemple :

```pythonfrom django.urls import pathfrom . import views

urlpatterns = [    path("members/", views.members, name="members"),]```

Cette ligne :

```pythonpath("members/", views.members, name="members")```

signifie :

> Quand l'utilisateur visite `/members/`, appelle `views.members`.

---

# 13. 🏠 URL Root et `include()`

Dans le `urls.py` principal :

```textmy_tennis_club/urls.py```

On peut écrire :

```pythonfrom django.contrib import adminfrom django.urls import include, path

urlpatterns = [    path("admin/", admin.site.urls),    path("", include("members.urls")),]```

### Pourquoi :

```pythonpath("", include("members.urls"))```

`""` représente la racine :

```texthttp://127.0.0.1:8000/```

`include("members.urls")` signifie :

> "Va chercher les routes dans `members/urls.py`."

Cela permet de séparer les URLs par application.

---

# 14. 🏷️ Pourquoi `name="members"` ?

Exemple :

```pythonpath("members/", views.members, name="members")```

`name="members"` donne un **nom** à la route.

Dans un template, on peut écrire :

```html<a href="{% url 'members' %}">Members</a>```

Au lieu de mettre directement :

```html<a href="/members/">Members</a>```

### Avantage

Si demain on change :

```pythonpath("members/", ...)```

en :

```pythonpath("users/", ...)```

on peut garder :

```pythonname="members"```

et Django retrouvera automatiquement la bonne URL avec `{% url 'members' %}`.

---

# 15. 🎨 Django Templates

Un template est généralement un fichier HTML.

Exemple :

```textmembers/└── templates/    └── index.html```

`index.html` :

```html<!DOCTYPE html><html><head>    <title>My Tennis Club</title></head><body>

<h1>Bienvenue dans My Tennis Club</h1>

</body></html>```

---

# 16. 🖥️ Afficher un Template avec `render()`

Dans `views.py` :

```pythonfrom django.shortcuts import render

def members(request):    return render(request, "index.html")```

### `render()`

```pythonrender(request, "index.html")```

signifie :

> Cherche le template `index.html` et rends-le au navigateur.

---

# 17. 📤 Envoyer des données au Template

Dans `views.py` :

```pythonfrom django.shortcuts import render

def members(request):

    context = {        "name": "Omar",        "age": 20,    }

    return render(request, "index.html", context)```

Dans `index.html` :

```html<h1>Bonjour {{ name }}</h1><p>Age : {{ age }}</p>```

Résultat :

```textBonjour OmarAge : 20```

---

# 18. 🔀 Les variables Django Templates

Afficher une variable :

```django{{ name }}```

Condition :

```django{% if age >= 18 %}    <p>Majeur</p>{% endif %}```

Boucle :

```django{% for member in members %}    <p>{{ member.firstname }}</p>{% endfor %}```

---

# 19. 🗃️ Models

Un **Model** représente une table dans la base de données.

Ouvrir :

```textmembers/models.py```

Exemple :

```pythonfrom django.db import models

class Member(models.Model):    firstname = models.CharField(max_length=255)    lastname = models.CharField(max_length=255)    phone = models.CharField(max_length=15)

    def __str__(self):        return self.firstname```

### Correspondance

| Django | Base de données ||---|---|| `class Member` | Table || `firstname` | Colonne || `lastname` | Colonne || `phone` | Colonne || Objet `Member` | Ligne / enregistrement |

---

# 20. 🆔 Le champ `id`

Même si on ne l'écrit pas :

```pythonclass Member(models.Model):    ...```

Django ajoute automatiquement une clé primaire (`id`) si aucun champ primaire n'est défini.

Exemple :

```textid | firstname | lastname---|-----------|---------1  | Omar      | Zinane2  | Ali       | Ahmed```

---

# 21. 🧱 Migrations

Quand on modifie `models.py`, la base de données n'est pas modifiée automatiquement.

On utilise :

```powershellpython manage.py makemigrations```

Cette commande crée un fichier de migration.

Exemple :

```textmembers/migrations/0001_initial.py```

Ensuite :

```powershellpython manage.py migrate```

applique réellement les changements à la base de données.

---

# 22. 🔍 `sqlmigrate`

Commande :

```powershellpython manage.py sqlmigrate members 0001```

Elle montre le SQL généré pour la migration.

⚠️ Elle **n'exécute pas** le SQL.

Elle affiche seulement ce qui sera exécuté.

Exemple :

```sqlCREATE TABLE "members_member" (    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,    "firstname" varchar(255) NOT NULL,    "lastname" varchar(255) NOT NULL);```

---

# 23. 🔄 Différence entre les migrations

### `makemigrations`

```powershellpython manage.py makemigrations```

➡️ Prépare la migration.

### `sqlmigrate`

```powershellpython manage.py sqlmigrate members 0001```

➡️ Affiche le SQL de la migration.

### `migrate`

```powershellpython manage.py migrate```

➡️ Applique la migration à la base.

---

# 24. ⚠️ Ajouter un champ obligatoire à un Model existant

Supposons que la table contient déjà des membres.

On ajoute :

```pythonphone = models.CharField(max_length=15)```

Django peut afficher :

```textIt is impossible to add a non-nullable field...```

Pourquoi ?

Parce que les anciennes lignes n'ont pas encore de valeur pour `phone`.

Django demande donc une valeur par défaut.

On peut :

### Option A — fournir une valeur par défaut pendant la migration

Choisir :

```text1```

et donner par exemple :

```python'0000000000'```

### Option B — définir un `default` dans le Model

Exemple :

```pythonphone = models.CharField(    max_length=15,    default="0000000000")```

---

# 25. ✅ Exemple avec `joined_date`

Pour une date :

```pythonfrom django.utils import timezone

class Member(models.Model):    firstname = models.CharField(max_length=255)    lastname = models.CharField(max_length=255)    phone = models.CharField(max_length=15)    joined_date = models.DateField(default=timezone.now)```

Puis :

```powershellpython manage.py makemigrationspython manage.py migrate```

---

# 26. 🗄️ Base de données SQLite

Django utilise souvent SQLite pour commencer.

Le fichier est :

```textdb.sqlite3```

Structure :

```textmy_tennis_club/├── manage.py├── members/└── my_tennis_club/```

SQLite est pratique pour apprendre et pour les petits projets.

---

# 27. 🐚 Django Shell

On peut ouvrir le shell Django :

```powershellpython manage.py shell```

Importer le modèle :

```pythonfrom members.models import Member```

Créer un membre :

```pythonMember.objects.create(    firstname="Omar",    lastname="Zinane",    phone="0600000000")```

Créer avec `save()` :

```pythonmember = Member(    firstname="Ali",    lastname="Ahmed",    phone="0611111111")

member.save()```

---

# 28. 🔎 Lire les données avec l'ORM

Tous les membres :

```pythonMember.objects.all()```

Premier membre :

```pythonMember.objects.all()[0]```

Compter :

```pythonMember.objects.count()```

Premier élément sans provoquer d'`IndexError` si la table est vide :

```pythonMember.objects.first()```

Un filtre :

```pythonMember.objects.filter(firstname="Omar")```

---

# 29. ❗ Comprendre `IndexError`

Cette commande :

```pythonMember.objects.all()[4]```

demande le **5ᵉ objet** car Python commence à compter à `0`.

```text0 → 1er1 → 2ème2 → 3ème3 → 4ème4 → 5ème```

Si la table contient seulement 2 membres :

```pythonMember.objects.all()[4]```

donnera :

```textIndexError: list index out of range```

---

# 30. 🛠️ Erreur `no such column`

Exemple :

```textOperationalError: no such column: members_member.phone```

Cela signifie généralement :

> Le Model contient `phone`, mais la base de données n'a pas encore cette colonne.

Solution :

```powershellpython manage.py makemigrationspython manage.py migrate```

Si Django demande un default pour un champ obligatoire, il faut fournir une valeur ou définir un `default` dans `models.py`.

---

# 31. 🧪 Voir l'état des migrations

```powershellpython manage.py showmigrations members```

Exemple :

```textmembers [X] 0001_initial [X] 0002_member_phone```

`[X]` signifie que la migration est appliquée.

`[ ]` signifie qu'elle existe mais n'est pas encore appliquée.

---

# 32. 🧭 Architecture simple Django

```textBrowser   │   ▼urls.py   │   ▼views.py   │   ├── models.py ──► Database   │   ▼templates/   │   ▼Browser```

### Rôle de chaque élément

- `urls.py` → Quelle route ?- `views.py` → Que faire ?- `models.py` → Quelles données ?- `templates/` → Quoi afficher ?- Database → Où stocker les données ?

---

# 33. 📦 Structure finale du projet

Exemple :

```textmy_tennis_club/│├── .gitignore├── manage.py├── db.sqlite3│├── members/│   ├── migrations/│   │   ├── __init__.py│   │   └── 0001_initial.py│   ││   ├── templates/│   │   └── index.html│   ││   ├── admin.py│   ├── apps.py│   ├── models.py│   ├── tests.py│   ├── urls.py│   └── views.py│└── my_tennis_club/    ├── __init__.py    ├── settings.py    ├── urls.py    ├── asgi.py    └── wsgi.py```

---

# 34. 🔐 Git et GitHub

Initialiser Git :

```powershellgit init```

Créer un `.gitignore` :

```gitignorevenv/__pycache__/*.pycdb.sqlite3.env.vscode/.idea/```

Ajouter les fichiers :

```powershellgit add .```

Créer le premier commit :

```powershellgit commit -m "Initial Django tennis club project"```

Renommer la branche :

```powershellgit branch -M main```

Ajouter le repository GitHub :

```powershellgit remote add origin https://github.com/USERNAME/my-tennis-club.git```

Envoyer :

```powershellgit push -u origin main```

---

# 35. 🔁 Workflow quotidien

Quand tu travailles sur le projet :

```powershellcd my_tennis_clubvenv\Scripts\activatepython manage.py runserver```

Si tu modifies `models.py` :

```powershellpython manage.py makemigrationspython manage.py migrate```

Puis Git :

```powershellgit add .git commit -m "Update members model"git push```---18. 🧩 Django Add Master Template

Quand une application Django possède plusieurs pages, on ne veut pas répéter le même code HTML dans chaque fichier.

Par exemple, plusieurs pages peuvent avoir le même :

<header>menu de navigation<footer>CSSstructure HTML

Pour éviter de répéter ce code, Django permet de créer un Master Template (template parent).

📁 Structure

On peut créer :

templates/│├── master.html│└── members/    ├── index.html    └── about.html

Le fichier master.html contient la structure commune de toutes les pages.

1. 🏗️ Créer master.html

Exemple :

<!DOCTYPE html><html><head>    <title>{% block title %}My Tennis Club{% endblock %}</title></head>

<body>

<nav>    <a href="{% url 'members' %}">Members</a></nav>

<hr>

{% block content %}{% endblock %}

<hr>

<footer>    <p>My Tennis Club</p></footer>

</body></html> 2. 🧱 Comprendre {% block %}

Dans :

{% block title %}{% endblock %}

on crée une zone que les templates enfants pourront remplacer.

Par exemple :

{% block content %}{% endblock %}

Cette zone contiendra le contenu spécifique de chaque page.

3. 👶 Créer un Template enfant

Exemple :

templates/members/index.html{% extends "master.html" %}

{% block title %}Members{% endblock %}

{% block content %}

<h1>Members</h1>

<p>Bienvenue dans la page des membres.</p>

{% endblock %}4. 🔗 {% extends %}

Cette ligne :

{% extends "master.html" %}

signifie :

Le fichier index.html hérite de la structure de master.html.

Le template enfant réutilise donc automatiquement :

le <html>le <head>le menule footerles autres éléments du template parent5. 🎯 Résultat

Le navigateur reçoit une page composée de :

master.html       +index.html       ↓Page HTML finale

Par exemple :

------------------------------------------------My Tennis Club

Members------------------------------------------------

Members

Bienvenue dans la page des membres.

------------------------------------------------My Tennis Club------------------------------------------------6. 🔄 Plusieurs pages peuvent utiliser le même Master Templateabout.html{% extends "master.html" %}

{% block title %}About{% endblock %}

{% block content %}

<h1>About</h1>

<p>Bienvenue dans la page About.</p>

{% endblock %}contact.html{% extends "master.html" %}

{% block title %}Contact{% endblock %}

{% block content %}

<h1>Contact</h1>

<p>Contactez-nous.</p>

{% endblock %}

Les trois pages utilisent le même template parent :

master.html    │    ├── index.html    ├── about.html    └── contact.html✅ Pourquoi utiliser un Master Template ?

Sans Master Template :

index.html    → header    → menu    → content    → footer

about.html    → header    → menu    → content    → footer

contact.html    → header    → menu    → content    → footer

❌ Beaucoup de code répété.

Avec un Master Template :

master.html    ├── index.html    ├── about.html    └── contact.html

✅ Moins de répétition✅ Code plus propre✅ Maintenance plus facile✅ Modifier le menu ou le footer à un seul endroit

20. 🚫 Django Custom 404 Page

Une erreur 404 (Page Not Found) apparaît lorsqu'un utilisateur demande une URL qui n'existe pas dans notre application Django.

Par exemple :

http://127.0.0.1:8000/test123/

Si aucune route test123/ n'existe dans urls.py, Django retourne une erreur 404.

20.1 🧠 Comment fonctionne une erreur 404 ?

Le navigateur envoie une requête :

Browser
   │
   ▼
/test123/
   │
   ▼
urls.py
   │
   ▼
❌ Aucune URL correspondante
   │
   ▼
404 Not Found

Django recherche l'URL demandée dans urlpatterns.

Si aucune route ne correspond, Django déclenche une réponse 404.

20.2 🏗️ Créer une page 404 personnalisée

Par défaut, Django affiche sa propre page 404.

Nous pouvons créer notre propre page HTML :

templates/
└── 404.html

20.3 🎨 Créer 404.html

Exemple :

<!DOCTYPE html>
<html>
<head>
    <title>404 - Page Not Found</title>
</head>

<body>

    <h1>404 - Page Not Found</h1>

    <p>Désolé, cette page n'existe pas.</p>

    <a href="/">Back to Home</a>

</body>
</html>

Cette page sera affichée lorsqu'une URL n'est pas trouvée.

20.4 ⚙️ Configurer le dossier templates

Django doit savoir où chercher le fichier 404.html.

Dans settings.py :

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        # ...
    },
]

DIRS indique à Django où se trouve le dossier global templates.

20.5 🔴 Désactiver DEBUG

Pour tester la page 404 personnalisée, mettre :

DEBUG = False

En développement local :

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

Pourquoi DEBUG = False ?

Lorsque :

DEBUG = True

Django affiche généralement sa page d'erreur détaillée.

Avec :

DEBUG = False

Django peut utiliser la page 404 personnalisée.

20.6 🧪 Tester la page 404

Lancer le serveur :

python manage.py runserver

Puis entrer une URL qui n'existe pas :

http://127.0.0.1:8000/test123/

Django ne trouvera aucune route correspondante et affichera :

404 - Page Not Found

Désolé, cette page n'existe pas.

20.7 🎯 Utiliser le Master Template

Si le projet possède déjà un master.html, nous pouvons réutiliser sa structure.

{% extends "master.html" %}

{% block title %}
404 - Page Not Found
{% endblock %}

{% block content %}

<h1>404 - Page Not Found</h1>

<p>Désolé, cette page n'existe pas.</p>

<a href="{% url 'members' %}">
    Back to Home
</a>

{% endblock %}

Grâce à {% extends %}, la page 404 utilise le même :

Header

Menu

Footer

Style général

que les autres pages.

20.8 ❌ Pas besoin de créer une URL /404/

Nous ne devons pas faire :

path("404/", ...)

La page 404 n'est pas une page que l'utilisateur doit visiter directement.

Django déclenche automatiquement la page 404 lorsqu'une URL demandée n'existe pas.

🔄 Flux complet

Utilisateur
     │
     ▼
http://127.0.0.1:8000/test123/
     │
     ▼
urls.py
     │
     ▼
Aucune route trouvée
     │
     ▼
404 Not Found
     │
     ▼
templates/404.html
     │
     ▼
Navigateur

✅ Résumé

Pour créer une page 404 personnalisée :

1. Créer templates/404.html
        ↓
2. Configurer DIRS dans settings.py
        ↓
3. Mettre DEBUG = False
        ↓
4. Définir ALLOWED_HOSTS
        ↓
5. Tester avec une URL inexistante

---

# 36. 🎯 Commandes Django à connaître

```powershell
python manage.py runserver
python manage.py startapp members
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate members 0001
python manage.py showmigrations
python manage.py shell
python manage.py createsuperuser
```
