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

    plot_stats(df, 5, "L")


def plot_stats(df, qty=5, category="W", sort="Rank"):
    if sort == "Rank":
        df.sort_values(by=[sort])[:qty].plot.bar(x="Team", y=category)
    else:
        df.sort_values(by=[sort], ascending=False)[:qty].plot.bar(x="Team", y=category)
    plt.show()


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
                if pct == "---":
                    pct = 0.00
                else:
                    pct = float(pct)
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
