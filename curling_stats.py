#!/usr/bin/env python3
"""
Module Docstring
"""

from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """ Main entry point of the app """
    url = "http://www.curlingzone.com/statistics.php"
    resp = get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    df = get_stats(soup)
    print(df)

    plot_wins(df, 10)
    #plot_wins_v_loses(df)


def plot_wins(df, qty=5):
    df[:qty].plot.bar(x="Team", y="W")
    plt.show()


# def plot_wins_v_loses(df, qty=5):
#     for x in range(qty - 1):
#         df[x].plot.scatter(x="L", y="W")
#         plt.show()


def get_stats(soup):
    rows_list = []

    for tr in soup.find_all("tr"):
        team = ""
        rank = ""
        for td in tr.find_all("td"):
            if td.get("data-th") == "Rank":
                rank = int(td.text.strip()[:-1])
            if td.get("data-th") == "Team":
                team = td.text.strip()
            if td.get("data-th") == "Location":
                location = td.text.strip()
            if td.get("data-th") == "W":
                wins = int(td.text.strip())
            if td.get("data-th") == "L":
                loses = int(td.text.strip())
            if td.get("data-th") == "T":
                ties = int(td.text.strip())
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

    return pd.DataFrame(rows_list)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
