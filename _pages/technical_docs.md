# Technical Documentation

## Architecture

Unsere Anwendung ist eine Habit-Tracking-App, die es Benutzern ermöglicht, ihre täglichen Gewohnheiten zu erstellen, zu verfolgen und zu analysieren. Mit Funktionen zur Erfassung von täglichen Einträgen, Zielsetzung und Fortschrittsverfolgung unterstützt die App Nutzer dabei, ihre Gewohnheiten nachhaltig zu entwickeln. Dies wird durch eine Kombination aus Flask für das Web-Framework und SQLAlchemy für das Datenbankmanagement erreicht.

----

Der Code der Anwendung ist in verschiedene Module unterteilt, die jeweils spezifische Funktionen abdecken:

habits/routes.py: Hier werden die Routen und Logik für das Hinzufügen, Anzeigen und Verwalten von Gewohnheiten und deren Logs definiert.

models.py: Enthält die Definition der Datenbankmodelle, die von SQLAlchemy verwendet werden.
auth.py: Behandelt die Authentifizierung und Autorisierung von Benutzern, einschließlich Login, Registrierung und Logout.

main.py: Beinhaltet die Logik und Routen für die Startseite und die Anzeige der täglichen Gewohnheiten des Benutzers.

Cross-Cutting Concerns:
Ein wichtiger Aspekt unserer Codebasis ist die Behandlung von Benutzergewohnheiten und deren Logs. Jede Gewohnheit und jeder Log wird durch ein Modell repräsentiert, das SQLAlchemy verwendet, um eine flexible und erweiterbare Datenbankstruktur zu gewährleisten. Zusätzlich wurden wichtige Designentscheidungen dokumentiert, um die zukünftige Entwicklung zu unterstützen und die Nachvollziehbarkeit zu gewährleisten.

## Data Model

## Reference

