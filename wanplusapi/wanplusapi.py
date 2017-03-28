#-*- encoding: UTF-8 -*-
from . import call_api


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
    data = call_api.send_post(eid=eid)
    competition_team = {'eid': '', 'teamnames': [], 'teamids': [], 'areas': []}
    competition_team['eid'] = str(eid)
    for blcok in data['data']:
        competition_team['teamnames'].append(blcok['teamname'])
        competition_team['teamids'].append(blcok['teamid'])
        competition_team['areas'].append(blcok['area'])
    competition_team_return = CompetitionTeams(competition_team)
    return competition_team_return


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
        self.teamnames = c['teamnames']
        self.teamids = c['teamids']
        self.areas = c['areas']

if __name__ == "__main__":
    # c = get_team_competition_info()
    # print(c.teamnames, c.teamids, c.areas)

    t = get_team_performance()
    print(t.goldsPermin)

    # c = get_competitions()
    # for competition in c:
    #     print(competition.name)
