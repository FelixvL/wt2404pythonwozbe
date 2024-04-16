import pandas
from json import loads, dumps

def filter_huurwoningen(zoekterm, bedragrange):
    bestandsinhoud = pandas.read_csv("woz_bewerkt.csv", sep=";")
    print(bestandsinhoud)
    result = bestandsinhoud.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)  