"""
Docstring für notes_app.main
"""

# Ablaufsteuerung für die App
# - Abfrage zum Programmstart, was getan werden soll:
# -- Notiz erfassen
# -- Vorhandene Notizen anzeigen
# -- Vorhandene Notiz aktualisieren
# -- Vorhandene Notiz löschen
# -- Vorhandene Notiz als erledigt markieren
#
# Regelt auch das Lesen und Schreiben in die Datei zum Persistieren der Notizen
# Import json_utils.py
# Import note.py
#

from note import Note

new_note = Note("Das ist eine Testnotiz")

new_note.print_note()
# print(new_note.text)
# print(new_note.created_date)

