import requests
import json
import pandas as pd


def downloadMatchData():
    url = "https://armwrestlingfornerds.com/backend/matches"

    try:

        response = requests.get(url)

        if response.status_code == 200:

            with open("matches.json", "w", encoding="utf-8") as file:
                file.write(response.text)
            print("Matches data successfully downloaded and saved as 'matches.json'.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


def loadData():
    file = open("matches.json", "r", encoding="utf-8")
    data = json.load(file)

    rows = []
    for match in data:
        rows.append(
            {
                "Match ID": match["_id"],
                "Event Name": match["event"]["eventName"],
                "Event Location": match["event"]["location"],
                "Event Date": match["event"]["eventDate"],
                "Armwrestler A Name": f"{match['awA']['armwrestler']['firstName']} {match['awA']['armwrestler']['lastName']}",
                "Armwrestler B Name": f"{match['awB']['armwrestler']['firstName']} {match['awB']['armwrestler']['lastName']}",
                "Armwrestler A Rounds Won": match["awA"]["scoreCard"]["roundsWon"],
                "Armwrestler B Rounds Won": match["awB"]["scoreCard"]["roundsWon"],
            }
        )

    matches = pd.DataFrame(rows)
    print(matches.head())


def main():
    loadData()


if __name__ == "__main__":
    main()
