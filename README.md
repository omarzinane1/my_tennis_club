
# My Tennis Club

My Tennis Club is a web application developed with Python and Django.

The project is based on the management of members of a tennis club. It was created to learn and practice the main concepts of Django.

## Technologies

* Python
* Django
* HTML
* CSS
* SQLite

## Features

* Manage club members
* Display members
* Django Admin interface
* Add, update and delete members
* Custom 404 error page
* Static files management

## Project Structure

```text
my_tennis_club/
│
├── members/
├── my_tennis_club/
├── templates/
├── manage.py
├── db.sqlite3
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/omarzinane1/my_tennis_club.git
```

Go to the project folder:

```bash
cd my_tennis_club
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install Django:

```bash
python -m pip install django
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application:

```text
http://127.0.0.1:8000/
```

## Author

Omar Zinane

Portfolio: https://omar-zinane.vercel.app
