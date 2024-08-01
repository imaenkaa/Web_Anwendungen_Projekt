# Design Decisions

Ein wichtiger Aspekt unserer Codebasis ist die Behandlung von Benutzergewohnheiten und deren Logs. Jede Gewohnheit und jeder Log wird durch ein Modell repräsentiert, das SQLAlchemy verwendet, um eine flexible und erweiterbare Datenbankstruktur zu gewährleisten. Zusätzlich wurden wichtige Designentscheidungen dokumentiert, um die zukünftige Entwicklung zu unterstützen und die Nachvollziehbarkeit zu gewährleisten.

## 01: Database

### Meta
Status: Entscheiden

Aktualisiert: 30-Jun-2024

### Problemstellung
Sollen Datenbank-CRUD-Operationen (Erstellen, Lesen, Aktualisieren, Löschen) durch Schreiben von        SQL oder durch die Verwendung von SQLAlchemy als objekt-relationalen Mapper durchgeführt werden?        Unsere Webanwendung ist in Python mit Flask geschrieben und verbindet sich mit einer SQLite-            Datenbank. Um das aktuelle Projekt abzuschließen, reicht dieses Setup aus. Wir beabsichtigen, die       Anwendung später zu skalieren und dabei auch das Datenbankschema mehrfach zu ändern sowie eventuell     auf ein leistungsfähigeres Datenbanksystem umzusteigen.

### Entscheidung
Wir verwenden SQLAlchemy. Diese Entscheidung wurde von den Entwicklern getroffen, da SQLAlchemy die     Wartbarkeit des Codes verbessert und die Flexibilität bietet, das Datenbanksystem bei Bedarf zu         wechseln.

### Betrachtete Optionen
Plain SQL
Pro: Vertrautheit mit SQL
Contra: Schwierigkeiten bei Schemaänderungen und Wechsel des Datenbanksystems
    
SQLAlchemy
Pro: Abstraktion des Datenbanksystems, Erleichterung bei Schemaänderungen
Contra: Lernkurve für das ORM-Konzept und SQLAlchemy Referenzdokumentation

---- 

## 02: Benutzerverwaltung

### Meta

Status: Entscheiden

Aktualisiert: 30-Jun-2024

### Problemstellung

Wie sollen Benutzer authentifiziert und autorisiert werden? Das System benötigt eine sichere Möglichkeit, um Benutzer anzumelden, zu registrieren und abzumelden.

### Entscheidung

Wir verwenden Flask-Login für die Benutzer-Authentifizierung und -Autorisierung. Dies bietet eine einfache Integration mit unserer bestehenden Flask-Anwendung und ermöglicht uns, Benutzer-Sessions zu verwalten und sicherzustellen, dass nur authentifizierte Benutzer Zugriff auf bestimmte Routen haben.

### Betrachtete Optionen

Flask-Login
Pro: Einfach zu implementieren, gut dokumentiert, unterstützt Benutzer-Sessions.
Contra: Abhängigkeit von einer Drittanbieter-Bibliothek.

Manuelle Implementierung
Pro: Vollständige Kontrolle über den Authentifizierungsprozess.
Contra: Erhöhter Entwicklungsaufwand, höhere Fehleranfälligkeit, Sicherheitsrisiken.

---- 

## 03: Badges und Ziele

### Meta

Status: Entscheiden

Aktualisiert: 30-Jun-2024

### Problemstellung

Wie sollen Nutzer für das Erreichen bestimmter Ziele oder Meilensteine in ihren Gewohnheiten belohnt werden?

### Entscheidung

Wir haben uns entschieden, ein Badges-System zu implementieren, das Benutzer für das Erreichen bestimmter Streaks (aufeinanderfolgende Tage, an denen eine Gewohnheit erfolgreich durchgeführt wurde) belohnt. Zusätzlich wird ein Zielsystem eingeführt, bei dem Benutzer spezifische Ziele für ihre Gewohnheiten festlegen können.

### Betrachtete Optionen

Badges und Ziele
Pro: Fördert die Benutzerbindung und Motivation, klare und messbare Ziele.
Contra: Erhöhter Implementierungsaufwand, Komplexität bei der Verwaltung von Zielen und Belohnungen.

Keine Belohnungssysteme
Pro: Einfachere Implementierung.
Contra: Weniger Anreiz für Benutzer, kontinuierlich ihre Gewohnheiten zu verfolgen.

---- 
## 04: Frontend-Design und Templates

### Meta

Status: Entscheiden

Aktualisiert: 30-Jun-2024

### Problemstellung

Wie soll das Frontend unserer Anwendung gestaltet werden, um eine benutzerfreundliche und ansprechende Benutzeroberfläche zu bieten?

### Entscheidung

Wir verwenden Flask-Templates mit Jinja2, um dynamische HTML-Seiten zu erstellen. Zusätzlich verwenden wir Bootstrap zur Gestaltung und Verbesserung des Designs, um sicherzustellen, dass die Anwendung responsiv und benutzerfreundlich ist.

### Betrachtete Optionen

Flask-Templates mit Jinja2 und Bootstrap
Pro: Einfache Integration, viele vorgefertigte Komponenten, responsives Design.
Contra: Abhängigkeit von externen Bibliotheken.

Reines HTML/CSS
Pro: Vollständige Kontrolle über das Design, keine externen Abhängigkeiten.
Contra: Erhöhter Entwicklungsaufwand, mangelnde Wiederverwendbarkeit von Komponenten.
