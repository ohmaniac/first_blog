# Passwort Generator
import random

def passwort_generator(laenge):
    zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    passwort = ''.join(random.choice(zeichen) for _ in range(laenge))
    return passwort

def copy_to_clipboard():
    copy = input("Passwort in die Zwischenablage kopieren? Y/N: ")
    if copy == "Y":
        ...
    elif copy == "N":
        pass

    

if __name__ == "__main__":
    laenge = int(input("Geben Sie die gewünschte Passwortlänge ein: "))
    print("Generiertes Passwort:", passwort_generator(laenge))  


