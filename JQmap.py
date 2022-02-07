# Author: Marci Devuaughan
# Created: 04 February 2022
# Updated: 04 February 2022
# Map to Job and Quote

from sys import stdin

stdin.readline()
for line in stdin:
    rowData = line.strip().split(",")
    if len(rowData) == 7:
        rowID, team1, team2, date, name, job, quote = rowData
        print("{0},{1}".format(job, quote))