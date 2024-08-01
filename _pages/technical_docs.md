# Technical Documentation

## Architecture

Unsere Anwendung ist eine Habit-Tracking-App, die es Benutzern ermöglicht, ihre täglichen Gewohnheiten zu erstellen, zu verfolgen und zu analysieren. Mit Funktionen zur Erfassung von täglichen Einträgen, Zielsetzung und Fortschrittsverfolgung unterstützt die App Nutzer dabei, ihre Gewohnheiten nachhaltig zu entwickeln. Dies wird durch eine Kombination aus Flask für das Web-Framework und SQLAlchemy für das Datenbankmanagement erreicht.

Der Code der Anwendung ist in verschiedene Module unterteilt, die jeweils spezifische Funktionen abdecken:

habits/routes.py: Hier werden die Routen und Logik für das Hinzufügen, Anzeigen und Verwalten von Gewohnheiten und deren Logs definiert.

models.py: Enthält die Definition der Datenbankmodelle, die von SQLAlchemy verwendet werden.
auth.py: Behandelt die Authentifizierung und Autorisierung von Benutzern, einschließlich Login, Registrierung und Logout.

main.py: Beinhaltet die Logik und Routen für die Startseite und die Anzeige der täglichen Gewohnheiten des Benutzers.

## Data Model





## Reference

### add_habit()

    Route: /add_habit
    Methoden: GET, POST
    Zweck: Hinzufügen einer neuen Gewohnheit
    view_habit(habit_id)
    
    Route: /habit/<int:habit_id>
    Methoden: GET, POST
    Zweck: Anzeigen der Details und Logs einer spezifischen Gewohnheit
    add_log(habit_id, log_type)
    
    Route: /add_log/<int:habit_id>/<string:log_type>
    Methoden: GET, POST
    Zweck: Hinzufügen eines Logs für eine spezifische Gewohnheit
    add_goal(habit_id)
    
    Route: /add_goal/<int:habit_id>
    Methoden: GET, POST
    Zweck: Hinzufügen eines Ziels für eine spezifische Gewohnheit
    freeze_habit(habit_id)
    
    Route: /freeze_habit/<int:habit_id>
    Methoden: GET, POST
    Zweck: Einfrieren einer Gewohnheit für bestimmte Tage
    habit_dashboard(habit_id)
    
    Route: /habit/<int:habit_id>/dashboard
    Methoden: GET
    Zweck: Anzeigen des Dashboards für eine spezifische Gewohnheit
    Authentifizierung

### login()

    Route: /login
    Methoden: GET, POST
    Zweck: Benutzer-Login
    signup()
    
    Route: /signup
    Methoden: GET, POST
    Zweck: Benutzer-Registrierung
    logout()
    
    Route: /logout
    Methoden: GET
    Zweck: Benutzer-Logout
    Hauptseite

### home()

    Route: /
    Methoden: GET
    Zweck: Startseite, Anzeige der täglichen Gewohnheiten des Benutzers
