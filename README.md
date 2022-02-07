# marcidev-map-reduce-nhl
Using python to analyze NHL Stanley Cup Finals interviews conducted between 1997 and 2019.

## Data Format:
Expected data for this program is a list of NHL interviews preformed during the Stanely Cup Finals. The file is expected to be a CSV of the following format:
| RowID | team1 | team2 | date | name | job | quote |
|---|---|---|---|---|---|---|
| Unique Identifier | Team that played in game | Other team that played in game | date of interview | interviewee | interviewee's job (player/coach/other) | text of interview |

## Questions:
I had two major questions I wanted to answer with this data, represented by JQ1 and JQ2 reducers.
JQ1 answers the question of "how many times were 'getting pucks in deep' or similar sentiments mentioned?" This is a very common phrase to hear in a regular season interview and generally is regarded as filler of no real substance. I was curious as to how many times this filler was used in interviews regarding the finals matchups.

The second question I wanted answered with JQ2 was "how many times was the word 'boy (or boys)' said?" Hockey is known as a team sport above all else and I was curious as to how often mention of teammates as good friends (i.e. "the boys") was said.
### Answers:
Question one: There were 19 mentions by a coach and 73 mentions by players.
Question two: There were 40 mentions by a coach, 33 by players, and one by a front office person.

## How to Run:
```powershell
cat .\interview_data.csv | python .\JQmap.py | sort | python .\JQ1reduce.py # Answers Question One
cat .\interview_data.csv | python .\JQmap.py | sort | python .\JQ2reduce.py # Answers Question Two
```