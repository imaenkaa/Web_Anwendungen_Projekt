---
layout: default
title: Technical Documentation
permalink: /Web_Anwendungen_Projekt/technical-documentation/
---
# Technical Documentation

Hier bieten wir eine detaillierte technische Dokumentation unserer Habit Tracker App, um die Architektur, die zugrunde liegenden Technologien und die wichtigsten Funktionen umfassend zu erläutern. 

## Architecture

### Overview
Unsere Habit Tracker-Anwendung hilft Nutzern dabei, gesunde Gewohnheiten zu bilden und aufrechtzuerhalten, indem sie ihnen ermöglicht, ihre täglichen Routinen zu erstellen, zu verfolgen und zu visualisieren. Die Hauptfunktionen umfassen das Setzen von Zielgewohnheiten, das tägliche Protokollieren von Aktivitäten, das Erwerben von Abzeichen für konsequente Leistung und das Einfrieren von Gewohnheiten ohne Verlust der Streaks. Die App bietet eine personalisierte Erfahrung durch sichere Benutzerauthentifizierung und ein intuitives Dashboard zur Fortschrittsverfolgung.

Hauptfunktionen:

- Benutzerauthentifizierung: Sichere Registrierung und Anmeldung mittels Flask-Login.
- Gewohnheitsverwaltung: Benutzer können Gewohnheiten erstellen, aktualisieren und löschen.
- Tägliches Protokollieren: Benutzer protokollieren tägliche Aktivitäten mit optionalen Notizen.
- Zielsetzung: Benutzer setzen Ziele mit spezifischen Start- und Zieldaten.
- Abzeichensystem: Benutzer erhalten Abzeichen für das Erreichen von Gewohnheitsstreaks.
- Einfrieren von Gewohnheiten: Benutzer können das Verfolgen bestimmter Gewohnheiten pausieren, ohne die Streaks zu unterbrechen.
- Dashboard: Benutzer können ihren Gewohnheitsfortschritt, Streaks und Zielerreichungen visualisieren.

### Codemap

- app.py: Der Haupteinstiegspunkt der Anwendung, initialisiert die App und ihre Komponenten.
- config.py: Konfigurationseinstellungen für die Anwendung (nicht gezeigt, umfasst in der Regel DB-Einstellungen, geheime Schlüssel usw.).
- models.py: SQLAlchemy-Modelle, die das Datenbankschema darstellen, einschließlich Benutzer, Gewohnheiten, Logs, Ziele, Abzeichen,           Benutzerabzeichen und Einfrieren.
- templates/: HTML-Templates zur Darstellung von Ansichten.
   - auth/: Authentifizierungsbezogene Ansichten (Login, Registrierung).
   - habit/: Gewohnheitsverwaltungsansichten (Gewohnheit erstellen, Gewohnheit anzeigen, Log hinzufügen, Ziel hinzufügen, Gewohnheit             einfrieren, Dashboard).
   - badges/: Ansichten zum Anzeigen erworbener Abzeichen.
   - index.html: Haupt-Homepage-Template.
- static/: Statische Dateien (CSS, JS, Bilder).
- blueprints/: Blueprint-Definitionen für verschiedene Anwendungsmodule.
   - auth.routes: Behandelt auth-bezogene Routen.
   - habits.routes: Verwaltet gewohnheitsbezogene Routen.
   - badges.routes: Verwaltet abzeichenbezogene Routen.
   - main.routes: Behandelt Haupt-Homepage-Routen.

### Cross-cutting concerns

Authentifizierung:
- Implementiert mit Flask-Login.
- Benutzersitzungen gewährleisten personalisiertes Gewohnheitstracking.
- login_user, logout_user und login_required Dekoratoren sichern Routen.

Datenbankverwaltung:
- SQLAlchemy wird als ORM für Datenbankinteraktionen verwendet.
- Modelle definieren Beziehungen und Einschränkungen.
- Beispielmodelle umfassen Benutzer, Gewohnheiten, LogHabits, Ziele, Abzeichen, Benutzerabzeichen und Einfrieren.

Gewohnheitsprotokollierung:
- Benutzer protokollieren tägliche Gewohnheitsaktivitäten.
- Logs umfassen den Erledigungsstatus und optionale Notizen.
- Validierung verhindert das Protokollieren für zukünftige Daten.

Zielverfolgung:
- Benutzer setzen Ziele mit Start- und Zieldaten.
- Der Fortschritt wird basierend auf täglichen Logs verfolgt.
- Ziele können als erreicht oder fehlgeschlagen markiert werden, basierend auf der Log-Erfüllung.

Abzeichensystem:
- Abzeichen werden für das Erreichen spezifischer Streaks vergeben.
- Die Abzeicheninitialisierung wird durch einen benutzerdefinierten CLI-Befehl gehandhabt.
- Das UserBadge-Modell verknüpft Benutzer mit ihren erworbenen Abzeichen.

Einfrieren von Gewohnheiten:
- Benutzer können Gewohnheiten für bestimmte Daten einfrieren.
- Eingefrorene Daten werden in Streak- und Zielberechnungen berücksichtigt.

Fehlerbehandlung:
- Flash-Nachrichten bieten Benutzerrückmeldungen.
- Durch ordnungsgemäße Validierung und Fehlerbehandlung wird eine reibungslose Benutzererfahrung gewährleistet.

Templates und statische Dateien:
- Jinja2-Templates für dynamisches HTML-Rendering.
- CSS- und JavaScript-Dateien im Verzeichnis static.

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

7. Freeze

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
