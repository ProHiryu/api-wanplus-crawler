# blockexplorer

module All functions support an optional parameter called api_code. It won't be listed with every function description.

#### get_competitions

Get all the competitions. Returns a Competitions object.

Usage:

```python
from wanplusapi import wanplusapi
competitions = wanplusapi.get_competitions()
```

#### get_team_competition_info

Get all the teams in the specific Competition. Returns a CompetitionTeams object.

Params:

```
eid : the id of competition , you can get it from get_competitions
```

Usage:

```python
from wanplusapi import wanplusapi
competitions_teams = wanplusapi.get_team_competition_info()
```

#### get_team_performance

Get the specified team's data in the specific Competition. Returns a TeamPerformance object.

Params:

```
eid : the id of competition , you can get it from get_competitions and get_team_competition_info
teamid : the id of team , you can get it from get_team_competition_info
```

Usage:

```python
from wanplusapi import wanplusapi
team_performance = wanplusapi.get_team_performance()
```

#### get_player_competition_info

Get all the players in the specific Competition. Returns a CompetitionPlayers object.

Params:

```
eid : the id of competition , you can get it from get_competitions
```

Usage:

```python
from wanplusapi import wanplusapi
competitions_teams = wanplusapi.get_player_competition_info()
```

#### get_player_competition_info

Get the specified player's data in the specific Competition. Returns a PlayerPerformance object.

Params:

```
eid : the id of competition , you can get it from get_competitions and get_player_competition_info
playerid : the id of player , you can get it from get_player_competition_info
```

Usage:

```python
from wanplusapi import wanplusapi
team_performance = wanplusapi.get_player_performance()
```

### Object field definitions

#### Competition

```python
order : str
eid : str
name : str
eventtype : str
```

#### TeamInfo

```python
teamid : str
teamname : str
area : str
```

#### TeamPerformance

```python
eid : str
teamid : str
area : str
appearedTimes : str
kda : str
fstbloodpercentage : str
proAppearedTimes : str
goldsPermin : str
lasthitPermin : str
damagetoheroPermin : str
wardsplacedpermin : str
wardskilledpermin : str
killsPergame : str
deathsPergame : str
assistsPergame : str
lasthitpermatch : str
highestgoldpermin : str
baronkillsPergame : str
dragonkillsPergame : str
towertakensPergame : str
towerdeathsPergame : str
dragonkillspercentage : str
baronkillspercentage : str
wardskilledrate : str
avgDuration : str
```

#### CompetitionTeams

```python
eid : str
teams : a list of TeamInfo objects
```

#### PlayerInfo

```python
teamid : str
playerid : str
meta : str
playername : str
```

#### PlayerPerformance

```python
eid : str
playername : str
teamname : str
appearedTimes : str
kda : str
meta : str
damagetakenPermin : str
goldsPermin : str
lasthitPermin : str
damagetoheroPermin : str
wardsplacedpermin : str
wardskilledpermin : str
killsPergame : str
deathsPergame : str
assistsPergame : str
wardsplacedPergame : str
wardskilledPergame : str
goldsPercent : str
damagetakenPercent : str
damagetoheroPercent : str
attendrate : str
```

#### CompetitionTeams

```python
eid : str
teams : a list of PlayerInfo objects
```
