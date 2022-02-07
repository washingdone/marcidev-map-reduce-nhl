# Author: Marci Devuaughan
# Created: 04 February 2022
# Updated: 04 February 2022
# Count references to mentions of boy(s)

from re import findall
from sys import stdin
fo = open("JQ2answer.csv", "w")

currentKey = ""
currentValue = 0

for line in stdin:
  rowData = line.strip().split(',')
  job, quote = rowData
  if job != currentKey: # check if current key is equal to key being scanned
    if currentKey: # check that key has been initialized

      # output the last key value pair result
      fo.write(currentKey + ',' + str(currentValue) + '\n')

    # start over when changing keys
    currentKey = job
    currentValue = 0

  # increase count for number of times wanted result is found
  currentValue += len(findall(r"(boy(s?)) ",quote))

# output the final entry when done
fo.write(currentKey + ',' + str(currentValue) + '\n')
fo.close()