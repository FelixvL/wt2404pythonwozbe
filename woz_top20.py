import pandas as pd
from json import loads, dumps

def bestand_inlezen():
    data = pd.read_csv("woz_bewerkt.csv", delimiter=';')
    sorted_data = data.sort_values(by='Koopwoningen', ascending=False)
    top_20 = sorted_data.head(20)[['Regionaam', 'Koopwoningen']]
    # print(type(top_20))
    # print(top_20)
    result = top_20.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)


def main():
    bestand_inlezen()

if __name__ == "__main__":
    main()


