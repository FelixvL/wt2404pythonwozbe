import pandas as pd

def bestand_inlezen():
    data = pd.read_csv("woz_bewerkt.csv", delimiter=';')
    sorted_data = data.sort_values(by='Koopwoningen', ascending=False)
    top_20 = sorted_data.head(20)[['Regionaam', 'Koopwoningen']]
    # print(type(top_20))
    # print(top_20)
    return "go"

def main():
    bestand_inlezen()

if __name__ == "__main__":
    main()


