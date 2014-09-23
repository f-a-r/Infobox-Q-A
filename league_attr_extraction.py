#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parsing(content):
    #print "********************* LEAGUE ATTRS ******************************"
    attrs = {}
    attrs_keys = {\
    'LeagueName': ['/type/object/name'],\
    'Championship': ['/sports/sports_league/championship'],\
    'Sport': ['/sports/sports_league/sport'],\
    'Slogan': ['/organization/organization/slogan'],
    'OfficialWebsite': ['/common/topic/official_website'],\
    'Teams': ['/sports/sports_league/teams'],\
    'Description': ['/common/topic/description']}
    content_keys = content.keys()

    #Name of league
    attrs['Name'] = ''
    if attrs_keys['LeagueName'][0] in content_keys:
        attrs['Name'] = content[attrs_keys['LeagueName'][0]]['values'][0]['text']

    #Sport of league
    attrs['Sport'] = ''
    if attrs_keys['Sport'][0] in content_keys:
        attrs['Sport'] = content[attrs_keys['Sport'][0]]['values'][0]['text']

    #Slogan
    attrs['Slogan'] = ''
    if attrs_keys['Slogan'][0] in content_keys:
        attrs['Slogan'] = content[attrs_keys['Slogan'][0]]['values'][0]['text']

    #Official Website
    attrs ['Official_Website'] = ''
    if attrs_keys['OfficialWebsite'][0] in content_keys:
        attrs['Official_Website'] = content[attrs_keys['OfficialWebsite'][0]]['values'][0]['text']

    #Championship
    attrs['Championship'] = ''
    if attrs_keys['Championship'][0] in content_keys:
        attrs['Championship'] = content[attrs_keys['Championship'][0]]['values'][0]['text']

    #Teams
    attrs ['Teams'] = []
    if attrs_keys['Teams'][0] in content_keys:
        for team in content [attrs_keys['Teams'][0]]['values']:
            team = team['property']['/sports/sports_league_participation/team']['values'][0]['text']      
            attrs['Teams'].append(team) 


    #Description
    attrs ['Description'] = ''
    if attrs_keys['Description'][0] in content_keys:
        attrs['Description'] = content[attrs_keys['Description'][0]]['values'][0]['value']

    return attrs 