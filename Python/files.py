

def files_1():
    with open("test.txt", "r") as f:
        f_name = f.name
        print(f_name)

        for line in f:
            print(line, end='')


def files_2():
    with open("test.txt", "r") as f:
        print(f.read(30)) # Die Zahl spezifiziert die Anzahl an Zeichen, die gelesen werden.
        print(f.read(30)) # Mehrfache Aufrufe lesen die nächsten X Zeichen.

def files_3():
    with open("test.txt", "r") as f:
        print(f.read(30)) 
        f.seek(0) # Mit .seek() kann an die Position des übergebenen Wertes in der Datei gesprungen werden.
        print(f.read(30)) # Der nächste .read()-Befehl liest dann ab der veränderten Position.

def copy_file_to_file():
    """
    Kopiert die Inhalte einer Datei in eine neue Datei.
    """
    with open("test.txt", "r") as rf:
        with open("test_copy.txt", "w") as wf:
            for line in rf:
                wf.write(line)




if __name__ == "__main__":
    copy_file_to_file()
