---
layout: default
title: Technical Documentation
permalink: /Web_Anwendungen_Projekt/technical-documentation/
---
# Technical Documentation

Hier bieten wir eine detaillierte technische Dokumentation unserer Habit Tracker App, um die Architektur, die zugrunde liegenden Technologien und die wichtigsten Funktionen umfassend zu erläutern. Diese Dokumentation soll Entwicklern und Interessierten einen klaren Einblick in die Struktur und die Funktionsweise der Anwendung geben.

## Architecture

Unsere Anwendung ist eine Habit-Tracking-App, die es Benutzern ermöglicht, ihre täglichen Gewohnheiten zu erstellen, zu verfolgen und zu analysieren. Mit Funktionen zur Erfassung von täglichen Einträgen, Zielsetzung und Fortschrittsverfolgung unterstützt die App Nutzer dabei, ihre Gewohnheiten nachhaltig zu entwickeln. Dies wird durch eine Kombination aus Flask für das Web-Framework und SQLAlchemy für das Datenbankmanagement erreicht.

Der Code der Anwendung ist in verschiedene Module unterteilt, die jeweils spezifische Funktionen abdecken:

habits/routes.py: Hier werden die Routen und Logik für das Hinzufügen, Anzeigen und Verwalten von Gewohnheiten und deren Logs definiert.

models.py: Enthält die Definition der Datenbankmodelle, die von SQLAlchemy verwendet werden.
auth.py: Behandelt die Authentifizierung und Autorisierung von Benutzern, einschließlich Login, Registrierung und Logout.

main.py: Beinhaltet die Logik und Routen für die Startseite und die Anzeige der täglichen Gewohnheiten des Benutzers.

## Data Model

1. User

   Attributes:
   - id: Primärschlüssel
   - username: Einzigartig, nicht null
   - password: Nicht null

   Relationships:
   - habits: Beziehung zu Habit

2. Habit

   Attributes:
   - id: Primärschlüssel
   - name: Nicht null
   - description
   - category: Nicht null
   - start_date: Nicht null, Standardwert ist das aktuelle Datum
   - highest_streak: Standardwert ist 0

   Relationships:
   - user_id: Fremdschlüssel zu User
   - logs: Beziehung zu LogHabit
   - goals: Beziehung zu Goal
   - user_badges: Beziehung zu UserBadge

3. LogHabit

   Attributes:
   - id: Primärschlüssel
   - date: Nicht null
   - completed: Nicht null, Standardwert ist False
   - notes

   Relationships:
   - habit_id: Fremdschlüssel zu Habit

4. Goal

   Attributes:
   - id: Primärschlüssel
   - target_date: Nicht null
   - achieved: Nicht null, Standardwert ist False
   - start_date: Nicht null
   - progress: Standardwert ist 0
   - Result

   Relationships:
   - habit_id: Fremdschlüssel zu Habit

5. Badge

   Attributes:
   - id: Primärschlüssel
   - name: Nicht null
   - description: Nicht null
   - streak_required: Nicht null

6. UserBadge

   Attributes:
   - id: Primärschlüssel
   - date_awarded: Nicht null, Standardwert ist das aktuelle Datum

   Relationships:
   - user_id: Fremdschlüssel zu User
   - badge_id: Fremdschlüssel zu Badge
   - habit_id: Fremdschlüssel zu Habit

11. Freeze

   Attributes:
   - id: Primärschlüssel
   - date: Nicht null

   Relationships:
   - habit_id: Fremdschlüssel zu Habit

Beziehungen
- User: Hat viele Habits.
- Habit: Gehört zu einem User und hat viele LogHabits, Goals, UserBadges, und Freezes.
- LogHabit: Gehört zu einem Habit.
- Goal: Gehört zu einem Habit.
- UserBadge: Gehört zu einem User, einem Badge und einem Habit.
- Freeze: Gehört zu einem Habit.

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
