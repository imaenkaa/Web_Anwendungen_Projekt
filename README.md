# Habit Tracker

Willkommen zur Dokumentation des Habit Tracker Projekts. Dieses Dokument führt Sie durch die Installation und Nutzung des Habit Trackers, um Ihre Gewohnheiten effizient zu verfolgen und zu verwalten.

## Installation

Um den Habit Tracker zu installieren, folgen Sie diesen Schritten:

1.	Öffnen Sie Ihr Terminal und klonen Sie das Repository auf Ihren lokalen Computer:

      git clone https://github.com/imaenkaa/Web_Anwendungen_Projekt.git

2.	Ins Projektverzeichnis wechseln:

      cd Web_Anwendungen_Projekt
  	
4.	Virtuelle Umgebung erstellen und aktivieren:

      python3 -m venv venv 
      source venv/bin/activate
  	
6.	Abhängigkeiten installieren:

  	  pip install -r requirements.txt

8.	Datenbank initialisieren:

      flask db init
      flask db migrate -m "Initial migration"
      flask db upgrade

9.	Anwendung starten:

      flask run

## Nutzung

1.	Registrierung und Anmeldung
    -	Gehen Sie zur Registrierungsseite, füllen Sie das Formular aus und klicken Sie          auf "Registrieren".
    - Gehen Sie zur Anmeldeseite, geben Sie Ihre Anmeldedaten ein und klicken Sie auf         "Anmelden".
2.	Dashboard
    -	Nach der Anmeldung werden Sie zum Dashboard weitergeleitet, wo Sie eine Übersicht       Ihrer Gewohnheiten sehen können.
3.	Neue Gewohnheit erstellen
    -	Gehen Sie zur Seite "Neue Gewohnheit erstellen“, füllen Sie das Formular aus und        klicken Sie auf "Erstellen".
4.	Ziele hinzufügen
    -	Gehen Sie zur Seite "Ziel hinzufügen", wählen Sie die Gewohnheit aus, setzen Sie        ein Ziel und speichern Sie es.
5.	Gewohnheiten verfolgen
    -	Tägliche Logs hinzufügen: Gehen Sie zur Seite "Log hinzufügen", wählen Sie die          Gewohnheit und das Datum aus und geben Sie Ihre Fortschritte ein.
    -	Gewohnheiten einfrieren: Gehen Sie zur Seite "Gewohnheit einfrieren", wählen Sie        die Gewohnheit und den Zeitraum aus und klicken Sie auf "Einfrieren".
6.	Berichte und Statistiken
    -	Klicken Sie auf eine spezifische Gewohnheit im Dashboard, um detaillierte               Berichte und Statistiken zu sehen.




