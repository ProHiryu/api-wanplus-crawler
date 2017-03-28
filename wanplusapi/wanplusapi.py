#-*- encoding: UTF-8 -*-

import call_api


def get_competitions():
    competitions = []
    data = call_api.send_post()
    temp = {'order': '', 'eid': '', 'name': '', 'eventtype': ''}
    for key in data['eventList'].keys():
        temp['order'] = key
        temp['eid'] = data['eventList'][key]['eid']
        temp['name'] = data['eventList'][key]['name']
        temp['eventtype'] = data['eventList'][key]['eventtype']
        competition_temp = competition(temp)
        competitions.append(competition_temp)
    return competitions

def get_teamperformance(eid=384,teamid=197):


class competition:

    def __init__(self, c):
        self.order = c['order']
        self.eid = c['eid']
        self.name = c['name']
        self.eventtype = c['eventtype']

class teaminfo:
    def __init__(self,t):
        self.teamid = t['teamid']
        self.area = t['area']
        self.teamname = t['teamname']

class teamperformance:

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
        self.totalGolds = t['totalGolds']
        self.damagetoheroPermin = t['damagetoheroPermin']
        self.goldsPermin = t['goldsPermin']
        self.wardsplacedpermin = t['wardsplacedpermin']
        self.wardskilledpermin = t['wardskilledpermin']
        self.baronkillsPergame = t['baronkillsPergame']
        self.dragonkillsPergame = t['dragonkillsPergame']
        self.towertakensPergame = t['towertakensPergame']
        self.towerdeathsPergame = t['towerdeathsPergame']
        self.highestgoldpermin = t['highestgoldpermin']
        self.dragonkillspercentage = t['dragonkillspercentage']
        self.baronkillspercentage = t['baronkillspercentage']
        self.wardskilledrate = t['wardskilledrate']
        self.avgDuration = ['avgDuration']

if __name__ == "__main__":
    competitions = get_competitions()
    for competition in competitions:
        print(competition.name)
