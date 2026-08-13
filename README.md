# 🏟️ My Tennis Club — Django Tutorial

> Mini-projet Django créé pour apprendre Django étape par étape.
>
> **Django utilisé pendant ce projet : 5.2.16**
> **Python : 3.11.9**

---

## 📚 Objectif du projet

Ce projet sert de support pratique pour apprendre les bases de Django.

Nous allons progressivement comprendre :

- ✅ Installation de Django
- ✅ Création d'un projet Django
- ✅ Création d'une application
- ✅ `urls.py`
- ✅ `views.py`
- ✅ Templates HTML
- ✅ `settings.py`
- ✅ `INSTALLED_APPS`
- ✅ Models
- ✅ Base de données SQLite
- ✅ Migrations
- ✅ Django ORM
- ✅ Django Shell
- ✅ Git et GitHub

L'idée est de ne pas seulement copier les commandes, mais de comprendre **pourquoi** on les utilise.

---

# 1. 🐍 Prérequis

Avant de commencer, installe Python.

Vérifier Python :

```powershell
python --version
```

Exemple :

```text
Python 3.11.9
```

Vérifier Django :

```powershell
python -m django --version
```

Exemple :

```text
5.2.16
```

---

# 2. 📁 Créer le projet

Créer un dossier de travail :

```powershell
mkdir Django
cd Django
```

---

# 3. 🌱 Créer un environnement virtuel

Créer le virtual environment :

```powershell
python -m venv venv
```

### Pourquoi utiliser `venv` ?

Le `venv` permet d'avoir un environnement Python séparé pour le projet.

Cela évite de mélanger les dépendances de plusieurs projets.

---

# 4. ▶️ Activer le virtual environment

Sous Windows PowerShell :

```powershell
venv\Scripts\activate
```

Le terminal devient normalement :

```text
(venv) PS C:\Users\...\Django>
```

---

# 5. 📦 Installer Django

```powershell
python -m pip install django
```

Vérifier :

```powershell
python -m django --version
```

---

# 6. 🏗️ Créer un projet Django

Créer le projet :

```powershell
django-admin startproject my_tennis_club
```

Structure :

```text
my_tennis_club/
│
├── manage.py
│
└── my_tennis_club/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## 🧠 Qu'est-ce qu'un projet Django ?

Le **projet** représente l'ensemble du site/application.

---

# 7. 📂 Entrer dans le projet

Le fichier `manage.py` se trouve dans le dossier du projet.

```powershell
cd my_tennis_club
```

Vérifier :

```powershell
dir
```

Tu dois voir :

```text
manage.py
my_tennis_club
```

> ⚠️ Les commandes `python manage.py ...` doivent généralement être exécutées dans le dossier contenant `manage.py`.

---

# 8. 🚀 Lancer le serveur

```powershell
python manage.py runserver
```

Django affiche normalement :

```text
Starting development server at http://127.0.0.1:8000/
```

Ouvrir :

```text
http://127.0.0.1:8000/
```

Arrêter le serveur :

```text
Ctrl + C
```

---

# 9. 🧩 Créer une App Django

Un projet peut contenir plusieurs applications.

Exemple :

```text
Project
│
├── users
├── products
├── orders
└── blog
```

Chaque app possède une responsabilité.

Pour notre projet :

```powershell
python manage.py startapp members
```

Structure :

```text
members/
│
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

# 10. ⚙️ Ajouter l'App dans `INSTALLED_APPS`

Ouvrir :

```text
my_tennis_club/settings.py
```

Chercher :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Ajouter :

```python
'members',
```

Donc :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members',
]
```

### Pourquoi ?

Parce qu'on indique à Django :

> "L'application `members` fait partie de mon projet."

---

# 11. 👀 `views.py`

Le fichier :

```text
members/views.py
```

contient les **views**.

Une view reçoit une requête et renvoie une réponse.

Exemple :

```python
from django.http import HttpResponse

def members(request):
    return HttpResponse("Bienvenue dans Members")
```

Ici :

- `request` = requête du navigateur
- `HttpResponse(...)` = réponse envoyée au navigateur

---

# 12. 🌐 `urls.py`

`urls.py` sert à faire le lien entre une **URL** et une **view**.

Exemple :

```python
from django.urls import path
from . import views

urlpatterns = [
    path("members/", views.members, name="members"),
]
```

Cette ligne :

```python
path("members/", views.members, name="members")
```

signifie :

> Quand l'utilisateur visite `/members/`, appelle `views.members`.

---

# 13. 🏠 URL Root et `include()`

Dans le `urls.py` principal :

```text
my_tennis_club/urls.py
```

On peut écrire :

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("members.urls")),
]
```

### Pourquoi :

```python
path("", include("members.urls"))
```

`""` représente la racine :

```text
http://127.0.0.1:8000/
```

`include("members.urls")` signifie :

> "Va chercher les routes dans `members/urls.py`."

Cela permet de séparer les URLs par application.

---

# 14. 🏷️ Pourquoi `name="members"` ?

Exemple :

```python
path("members/", views.members, name="members")
```

`name="members"` donne un **nom** à la route.

Dans un template, on peut écrire :

```html
<a href="{% url 'members' %}">Members</a>
```

Au lieu de mettre directement :

```html
<a href="/members/">Members</a>
```

### Avantage

Si demain on change :

```python
path("members/", ...)
```

en :

```python
path("users/", ...)
```

on peut garder :

```python
name="members"
```

et Django retrouvera automatiquement la bonne URL avec `{% url 'members' %}`.

---

# 15. 🎨 Django Templates

Un template est généralement un fichier HTML.

Exemple :

```text
members/
└── templates/
    └── index.html
```

`index.html` :

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Tennis Club</title>
</head>
<body>

<h1>Bienvenue dans My Tennis Club</h1>

</body>
</html>
```

---

# 16. 🖥️ Afficher un Template avec `render()`

Dans `views.py` :

```python
from django.shortcuts import render

def members(request):
    return render(request, "index.html")
```

### `render()`

```python
render(request, "index.html")
```

signifie :

> Cherche le template `index.html` et rends-le au navigateur.

---

# 17. 📤 Envoyer des données au Template

Dans `views.py` :

```python
from django.shortcuts import render

def members(request):

    context = {
        "name": "Omar",
        "age": 20,
    }

    return render(request, "index.html", context)
```

Dans `index.html` :

```html
<h1>Bonjour {{ name }}</h1>
<p>Age : {{ age }}</p>
```

Résultat :

```text
Bonjour Omar
Age : 20
```

---

# 18. 🔀 Les variables Django Templates

Afficher une variable :

```django
{{ name }}
```

Condition :

```django
{% if age >= 18 %}
    <p>Majeur</p>
{% endif %}
```

Boucle :

```django
{% for member in members %}
    <p>{{ member.firstname }}</p>
{% endfor %}
```

---

# 19. 🗃️ Models

Un **Model** représente une table dans la base de données.

Ouvrir :

```text
members/models.py
```

Exemple :

```python
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.firstname
```

### Correspondance

| Django | Base de données |
|---|---|
| `class Member` | Table |
| `firstname` | Colonne |
| `lastname` | Colonne |
| `phone` | Colonne |
| Objet `Member` | Ligne / enregistrement |

---

# 20. 🆔 Le champ `id`

Même si on ne l'écrit pas :

```python
class Member(models.Model):
    ...
```

Django ajoute automatiquement une clé primaire (`id`) si aucun champ primaire n'est défini.

Exemple :

```text
id | firstname | lastname
---|-----------|---------
1  | Omar      | Zinane
2  | Ali       | Ahmed
```

---

# 21. 🧱 Migrations

Quand on modifie `models.py`, la base de données n'est pas modifiée automatiquement.

On utilise :

```powershell
python manage.py makemigrations
```

Cette commande crée un fichier de migration.

Exemple :

```text
members/migrations/0001_initial.py
```

Ensuite :

```powershell
python manage.py migrate
```

applique réellement les changements à la base de données.

---

# 22. 🔍 `sqlmigrate`

Commande :

```powershell
python manage.py sqlmigrate members 0001
```

Elle montre le SQL généré pour la migration.

⚠️ Elle **n'exécute pas** le SQL.

Elle affiche seulement ce qui sera exécuté.

Exemple :

```sql
CREATE TABLE "members_member" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "firstname" varchar(255) NOT NULL,
    "lastname" varchar(255) NOT NULL
);
```

---

# 23. 🔄 Différence entre les migrations

### `makemigrations`

```powershell
python manage.py makemigrations
```

➡️ Prépare la migration.

### `sqlmigrate`

```powershell
python manage.py sqlmigrate members 0001
```

➡️ Affiche le SQL de la migration.

### `migrate`

```powershell
python manage.py migrate
```

➡️ Applique la migration à la base.

---

# 24. ⚠️ Ajouter un champ obligatoire à un Model existant

Supposons que la table contient déjà des membres.

On ajoute :

```python
phone = models.CharField(max_length=15)
```

Django peut afficher :

```text
It is impossible to add a non-nullable field...
```

Pourquoi ?

Parce que les anciennes lignes n'ont pas encore de valeur pour `phone`.

Django demande donc une valeur par défaut.

On peut :

### Option A — fournir une valeur par défaut pendant la migration

Choisir :

```text
1
```

et donner par exemple :

```python
'0000000000'
```

### Option B — définir un `default` dans le Model

Exemple :

```python
phone = models.CharField(
    max_length=15,
    default="0000000000"
)
```

---

# 25. ✅ Exemple avec `joined_date`

Pour une date :

```python
from django.utils import timezone

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    joined_date = models.DateField(default=timezone.now)
```

Puis :

```powershell
python manage.py makemigrations
python manage.py migrate
```

---

# 26. 🗄️ Base de données SQLite

Django utilise souvent SQLite pour commencer.

Le fichier est :

```text
db.sqlite3
```

Structure :

```text
my_tennis_club/
├── manage.py
├── db.sqlite3
├── members/
└── my_tennis_club/
```

SQLite est pratique pour apprendre et pour les petits projets.

---

# 27. 🐚 Django Shell

On peut ouvrir le shell Django :

```powershell
python manage.py shell
```

Importer le modèle :

```python
from members.models import Member
```

Créer un membre :

```python
Member.objects.create(
    firstname="Omar",
    lastname="Zinane",
    phone="0600000000"
)
```

Créer avec `save()` :

```python
member = Member(
    firstname="Ali",
    lastname="Ahmed",
    phone="0611111111"
)

member.save()
```

---

# 28. 🔎 Lire les données avec l'ORM

Tous les membres :

```python
Member.objects.all()
```

Premier membre :

```python
Member.objects.all()[0]
```

Compter :

```python
Member.objects.count()
```

Premier élément sans provoquer d'`IndexError` si la table est vide :

```python
Member.objects.first()
```

Un filtre :

```python
Member.objects.filter(firstname="Omar")
```

---

# 29. ❗ Comprendre `IndexError`

Cette commande :

```python
Member.objects.all()[4]
```

demande le **5ᵉ objet** car Python commence à compter à `0`.

```text
0 → 1er
1 → 2ème
2 → 3ème
3 → 4ème
4 → 5ème
```

Si la table contient seulement 2 membres :

```python
Member.objects.all()[4]
```

donnera :

```text
IndexError: list index out of range
```

---

# 30. 🛠️ Erreur `no such column`

Exemple :

```text
OperationalError: no such column: members_member.phone
```

Cela signifie généralement :

> Le Model contient `phone`, mais la base de données n'a pas encore cette colonne.

Solution :

```powershell
python manage.py makemigrations
python manage.py migrate
```

Si Django demande un default pour un champ obligatoire, il faut fournir une valeur ou définir un `default` dans `models.py`.

---

# 31. 🧪 Voir l'état des migrations

```powershell
python manage.py showmigrations members
```

Exemple :

```text
members
 [X] 0001_initial
 [X] 0002_member_phone
```

`[X]` signifie que la migration est appliquée.

`[ ]` signifie qu'elle existe mais n'est pas encore appliquée.

---

# 32. 🧭 Architecture simple Django

```text
Browser
   │
   ▼
urls.py
   │
   ▼
views.py
   │
   ├── models.py ──► Database
   │
   ▼
templates/
   │
   ▼
Browser
```

### Rôle de chaque élément

- `urls.py` → Quelle route ?
- `views.py` → Que faire ?
- `models.py` → Quelles données ?
- `templates/` → Quoi afficher ?
- Database → Où stocker les données ?

---

# 33. 📦 Structure finale du projet

Exemple :

```text
my_tennis_club/
│
├── .gitignore
├── manage.py
├── db.sqlite3
│
├── members/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── my_tennis_club/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

# 34. 🔐 Git et GitHub

Initialiser Git :

```powershell
git init
```

Créer un `.gitignore` :

```gitignore
venv/
__pycache__/
*.pyc
db.sqlite3
.env
.vscode/
.idea/
```

Ajouter les fichiers :

```powershell
git add .
```

Créer le premier commit :

```powershell
git commit -m "Initial Django tennis club project"
```

Renommer la branche :

```powershell
git branch -M main
```

Ajouter le repository GitHub :

```powershell
git remote add origin https://github.com/USERNAME/my-tennis-club.git
```

Envoyer :

```powershell
git push -u origin main
```

---

# 35. 🔁 Workflow quotidien

Quand tu travailles sur le projet :

```powershell
cd my_tennis_club
venv\Scripts\activate
python manage.py runserver
```

Si tu modifies `models.py` :

```powershell
python manage.py makemigrations
python manage.py migrate
```

Puis Git :

```powershell
git add .
git commit -m "Update members model"
git push
```

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

---

# 37. 🧠 Résumé final

Pour comprendre Django, retiens surtout ce flux :

```text
URL
 ↓
urls.py
 ↓
views.py
 ↓
models.py
 ↓
Database
 ↓
views.py
 ↓
template HTML
 ↓
Browser
```

Et pour les changements de base de données :

```text
models.py
   ↓
makemigrations
   ↓
Migration
   ↓
migrate
   ↓
Database
```

---

# 🚀 Prochaines étapes

Après ce mini-cours, tu peux continuer avec :

1. Django Admin
2. CRUD (Create, Read, Update, Delete)
3. Formulaires Django
4. Relations entre Models (`ForeignKey`, `ManyToManyField`)
5. Authentication / Login / Logout
6. Static files (CSS, JavaScript, images)
7. Template inheritance
8. Pagination
9. Django REST Framework
10. Déploiement du projet

---

## ⭐ Commande de départ

Pour reprendre le projet :

```powershell
cd my_tennis_club
venv\Scripts\activate
python manage.py runserver
```

Puis ouvre :

```text
http://127.0.0.1:8000/
```

---

## 📌 Auteur

Projet personnel d'apprentissage Django.

**My Tennis Club — Django Learning Project**
