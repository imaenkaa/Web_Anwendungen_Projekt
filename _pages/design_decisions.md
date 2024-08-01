# Design Decisions

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
    Contra: Lernkurve für das ORM-Konzept und SQLAlchemy
    Referenzdokumentation
