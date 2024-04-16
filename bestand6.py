import csv

from json import loads, dumps

def amanienleon():
    return "Komt nog!"

def bestand_inlezen():
    import csv

    with open("woz_bewerkt.csv", 'r') as file:
        data = csv.reader(file)
        for row in data:
            print(row)

def main():
    bestand_inlezen()

if __name__ == "__main__":
    main()