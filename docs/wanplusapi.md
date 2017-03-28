# blockexplorer

module All functions support an optional parameter called api_code. It won't be listed with every function description.

## get_competitions

Get all the competitions. Returns a Competitions object.

Usage:

```
from wanplusapi import wanplusapi
competitions = wanplusapi.get_competitions()
```

## get_team_competition_info

Get all the teams in the specific Competition. Returns a CompetitionTeams object.

Params:

```
eid : the id of competition , you can get it from get_competitions
```

Usage:

```
from wanplusapi import wanplusapi
competitions_teams = wanplusapi.get_team_competition_info()
```

## get_team_performance

Get the specified teams' data in the specific Competition. Returns a TeamPerformance object.

Params:

```
eid : the id of competition , you can get it from get_competitions and get_team_competition_info
teamid : the id of team , you can get it from get_team_competition_info
```

Usage:

```
from wanplusapi import wanplusapi
team_performance = wanplusapi.get_team_performance()
```
