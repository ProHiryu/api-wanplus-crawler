#-*- encoding: UTF-8 -*-
from . import call_api
# import call_api


def get_competitions():
    competitions = []
    data = call_api.send_post()
    temp = {'order': '', 'eid': '', 'name': '', 'eventtype': ''}
    for key in data['eventList'].keys():
        temp['order'] = key
        temp['eid'] = data['eventList'][key]['eid']
        temp['name'] = data['eventList'][key]['name']
        temp['eventtype'] = data['eventList'][key]['eventtype']
        competition_temp = Competition(temp)
        competitions.append(competition_temp)
    return competitions


def get_team_competition_info(eid=348):
    keys = ['teamid', 'area', 'teamname']

    data = call_api.send_post(eid=eid,
                              search_type='team')
    competition_teams = {'eid': str(eid), 'teams': []}
    team = {'teamid': '', 'area': '', 'teamname': ''}
    for block in data['data']:
        for key in keys:
            team[key] = block[key]
        single_team = TeamInfo(team)
        competition_teams['teams'].append(single_team)
    return_competition_teams = CompetitionTeams(competition_teams)

    return return_competition_teams


def get_player_competition_info(eid=348):
    keys = ['teamid', 'meta', 'playerid', 'playername']

    data = call_api.send_post(eid=eid,
                              search_type='player')
    # for i in range(len(data['data'])):
    #     print(data['data'][i]['playername'])
    competition_players = {'eid': str(eid), 'players': []}
    player = {'teamid': '', 'meta': '', 'playerid': '', 'playername': ''}
    for block in data['data']:
        for key in keys:
            if key == 'meta':
                if block[key] == '上单':
                    block[key] = 'Top'
                if block[key] == '中单':
                    block[key] = 'Mid'
                if block[key] == '辅助':
                    block[key] = 'Sup'
                if block[key] == '打野':
                    block[key] = 'Jug'

            player[key] = block[key]
        single_player = PlayerInfo(player)
        competition_players['players'].append(single_player)
    return_competition_players = CompetitionPlayers(competition_players)

    return return_competition_players


def get_team_performance(eid=348, teamid=271):
    keys = ["kda", "fstbloodpercentage", "eid", "teamid", "area", "appearedTimes",
            "proAppearedTimes", "goldsPermin", "lasthitPermin", "highestgoldpermin", "towertakensPergame", "towerdeathsPergame", "damagetoheroPermin", "wardsplacedpermin", "wardskilledpermin",
            "killsPergame", "deathsPergame", "assistsPergame", "lasthitpermatch"]

    data = call_api.send_post(eid=eid)
    temp = {"eid": "",
            "teamid": "",
            "area": "",
            "appearedTimes": "",
            "kda": "",
            "fstbloodpercentage": "",
            "proAppearedTimes": "",
            "goldsPermin": "",
            "lasthitPermin": "",
            "damagetoheroPermin": "",
            "wardsplacedpermin": "",
            "wardskilledpermin": "",
            "killsPergame": "",
            "deathsPergame": "",
            "assistsPergame": "",
            "lasthitpermatch": "",
            "highestgoldpermin": "",
            "baronkillsPergame": "",
            "dragonkillsPergame": "",
            "towertakensPergame": "",
            "towerdeathsPergame": "",
            "dragonkillspercentage": "",
            "baronkillspercentage": "",
            "wardskilledrate": "",
            "avgDuration": ""}

    for block in data['data']:
        if block['teamid'] == str(teamid):
            for key in keys:
                temp[key] = block[key]
    t = TeamPerformance(temp)
    return t


def get_player_performance(eid=348, playerid=2752):
    keys = ['eid', 'playername', 'teamname', 'meta', 'appearedTimes', 'killsPergame', 'deathsPergame', 'assistsPergame', 'goldsPermin', 'lasthitPermin', 'damagetakenPermin',
            'damagetoheroPermin', 'wardsplacedPergame', 'wardskilledPergame', 'goldsPercent', 'damagetakenPercent', 'damagetoheroPercent', 'kda', 'attendrate']
    data = call_api.send_post(eid=eid, search_type="player")
    temp = dict()
    for key in keys:
        temp[key] = ''
    for block in data['data']:
        if str(playerid) == block['playerid']:
            for key in keys:
                if key == 'meta':
                    if block[key] == '上单':
                        block[key] = 'Top'
                    if block[key] == '中单':
                        block[key] = 'Mid'
                    if block[key] == '辅助':
                        block[key] = 'Sup'
                    if block[key] == '打野':
                        block[key] = 'Jug'
                temp[key] = block[key]

    t = PlayerPerformance(temp)
    return t


class Competition:

    def __init__(self, c):
        self.order = c['order']
        self.eid = c['eid']
        self.name = c['name']
        self.eventtype = c['eventtype']


class TeamInfo:

    def __init__(self, t):
        self.teamid = t['teamid']
        self.area = t['area']
        self.teamname = t['teamname']


class PlayerInfo:

    def __init__(self, p):
        self.teamid = p['teamid']
        self.playerid = p['playerid']
        self.meta = p['meta']
        self.playername = p['playername']


class PlayerPerformance:

    def __init__(self, p):
        self.eid = p['eid']
        self.playername = p['playername']
        self.teamname = p['teamname']
        self.meta = p['meta']
        self.appearedTimes = p['appearedTimes']
        self.killsPergame = p['killsPergame']
        self.deathsPergame = p['deathsPergame']
        self.assistsPergame = p['assistsPergame']
        self.goldsPermin = p['goldsPermin']
        self.lasthitPermin = p['lasthitPermin']
        self.damagetakenPermin = p['damagetakenPermin']
        self.damagetoheroPermin = p['damagetoheroPermin']
        self.wardsplacedPergame = p['wardsplacedPergame']
        self.wardskilledPergame = p['wardskilledPergame']
        self.goldsPercent = p['goldsPercent']
        self.damagetakenPercent = p['damagetakenPercent']
        self.damagetoheroPercent = p['damagetoheroPercent']
        self.kda = p['kda']
        self.attendrate = p['attendrate']


class TeamPerformance:

    def __init__(self, t):
        self.eid = t['eid']
        self.teamid = t['teamid']
        self.area = t['area']
        self.appearedTimes = t['appearedTimes']
        self.kda = t['kda']
        self.fstbloodpercentage = t['fstbloodpercentage']
        self.proAppearedTimes = t['proAppearedTimes']
        self.killsPergame = t['killsPergame']
        self.deathsPergame = t['deathsPergame']
        self.assistsPergame = t['assistsPergame']
        self.lasthitPermin = t['lasthitPermin']
        self.lasthitpermatch = t['lasthitpermatch']
        self.damagetoheroPermin = t['damagetoheroPermin']
        self.goldsPermin = t['goldsPermin']
        self.wardsplacedpermin = t['wardsplacedpermin']
        self.wardskilledpermin = t['wardskilledpermin']
        self.baronkillsPergame = t['baronkillsPergame']
        self.dragonkillsPergame = t['dragonkillsPergame']
        self.baronkillsPergame = t['baronkillsPergame']
        self.towertakensPergame = t['towertakensPergame']
        self.towerdeathsPergame = t['towerdeathsPergame']
        self.highestgoldpermin = t['highestgoldpermin']
        self.dragonkillspercentage = t['dragonkillspercentage']
        self.baronkillspercentage = t['baronkillspercentage']
        self.wardskilledrate = t['wardskilledrate']
        self.avgDuration = ['avgDuration']


class CompetitionTeams:

    def __init__(self, c):
        self.eid = c['eid']
        self.teams = c['teams']


class CompetitionPlayers:

    def __init__(self, c):
        self.eid = c['eid']
        self.players = c['players']

if __name__ == "__main__":
    pass
