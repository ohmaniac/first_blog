"""
Diese Klasse repräsentiert eine Notiz mit all ihren Attributen und Methoden.

"""
import datetime

class Note:
    
    text = ""
    created_date = None
    is_done = False

    # Attribute der Klasse definieren

    # Konstruktor durch überladen der __init__ Methode
    def __init__(self, text: str) -> Note:
        self.text = text

        now = datetime.datetime.now()
        self.created_date = now.strftime("%Y-%m-%d %H:%M:%S")

    # Methoden
    def print_note(self) -> None:
        """
        Gibt die Notiz inklusive Erstellungsdatum aus.
        """
        print("{}\n{}".format(self.text, self.created_date))

    def mark_as_done(self) -> None:
        """
        Marks a note as done.
        
        """
        pass






if __name__ == "__main__":
    pass
