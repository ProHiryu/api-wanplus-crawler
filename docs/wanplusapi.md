##blockexplorer

module All functions support an optional parameter called api_code. It won't be listed with every function description.

#### get_competitions

Get all the competitions. Returns a Competitions object.

Usage:

```
from wanplusapi import wanplusapi
competitions = wanplusapi.get_competitions()

for cs in c:
    print(cs.name)

```
