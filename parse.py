#!/usr/bin/env python3

import sys

from bs4 import BeautifulSoup

with open("fishy.html.orig") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    table = soup.find("tbody")
    if table is None:
        print("No table")
        sys.exit(1)

    # The first tr contains the field names.
    # headings = [th.get_text().strip() for th in table.find("tr").find_all("th")]
    # print(headings)

    datasets = []
    for row in table.find_all("tr")[1:]:
        # dataset = [td.get_text() for td in
        td = row.find("td")
        if td:
            text = td.get_text()
            if text:
                datasets.append(text)

    print("\n".join(datasets))
