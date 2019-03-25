#!/usr/bin/env python3
"""
Module Docstring
"""

from bs4 import BeautifulSoup
from requests import get
import pandas as pd


def main():
    """ Main entry point of the app """
    url = "http://www.curlingzone.com/statistics.php"
    resp = get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    # for tag in soup.find_all(re.compile("td")):
    #    print(tag)

    rows_list = []

    for tr in soup.find_all("tr"):
        team = ""
        rank = ""
        for td in tr.find_all("td"):
            if td.get("data-th") == "Rank":
                rank = td.text.strip()[:-1]
            if td.get("data-th") == "Team":
                team = td.text.strip()
            if td.get("data-th") == "Location":
                location = td.text.strip()
            if td.get("data-th") == "W":
                wins = td.text.strip()
            if td.get("data-th") == "L":
                loses = td.text.strip()
            if td.get("data-th") == "T":
                ties = td.text.strip()
            if td.get("data-th") == "PCT":
                pct = td.text.strip()
            if td.get("data-th") == "HMR":
                hmr = td.text.strip()
            if td.get("data-th") == "STL":
                stl = td.text.strip()
            if td.get("data-th") == "1PT":
                onept = td.text.strip()
            if td.get("data-th") == "EEH":
                eeh = td.text.strip()
            if td.get("data-th") == "EES":
                ees = td.text.strip()
        if team != "":
            row = {
                "Rank": rank,
                "Team": team,
                "Location": location,
                "W": wins,
                "L": loses,
                "T": ties,
                "PCT": pct,
                "HMR": hmr,
                "STL": stl,
                "1PT": onept,
                "EEH": eeh,
                "EES": ees,
            }
            rows_list.append(row)

    df = pd.DataFrame(rows_list)
    print(df)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
