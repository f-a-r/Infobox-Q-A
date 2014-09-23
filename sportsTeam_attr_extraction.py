#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parsing(content):
    
    #print "********************* SportsTeam ATTRS ******************************"
    attrs = {}
    attrs_keys = {\
    'Name': ['/type/object/name'],\
    'Sport': ['/sports/sports_team/sport'],\
    'Arena': ['/sports/sports_team/arena_stadium'],\
    'Championships': ['/sports/sports_team/championships'],\
    'Founded': ['/sports/sports_team/founded'],\
    'Leagues': ['/sports/sports_team/league'],\
    'Locations': ['/sports/sports_team/location'],\
    'Coaches': ['/sports/sports_team/coaches'],\
    'Players_Roster': ['/sports/sports_team/roster'],\
    'Description': ['/common/topic/description']\
    }
    
    #a dictioray key-values for each coach
    coachDic = {\
        'Name' : ['/sports/sports_team_coach_tenure/coach'],\
        'Position': ['/sports/sports_team_coach_tenure/position'],\
        'From/To':['/sports/sports_team_coach_tenure/from','/sports/sports_team_coach_tenure/to']\
    }
    #a dictionary of key-value pairs for each roster
    rosterDic = {\
    'Name': ['/sports/sports_team_roster/player'],\
    'Position': ['/sports/sports_team_roster/position'],\
    'Number': ['/sports/sports_team_roster/number'],\
    'From/To': ['/sports/sports_team_roster/from','/sports/sports_team_roster/to']\
    }
    
    content_keys = content.keys()
    
    #name of Sport team
    attrs ['Name'] = ''
    if attrs_keys['Name'][0] in content_keys:
        attrs['Name'] = content[attrs_keys['Name'][0]]['values'][0]['text']
    
    #type of sport
    attrs['Sport'] = ''
    if attrs_keys['Sport'][0] in content_keys:
        attrs['Sport'] = content[attrs_keys['Sport'][0]]['values'][0]['text']
    
    # Venue they play at
    attrs['Arena'] = ''
    if attrs_keys['Arena'][0] in content_keys:
        attrs['Arena'] = content[attrs_keys['Arena'][0]]['values'][0]['text']
    #saving Championships as a list of championships
    attrs['Championships'] = []
    if attrs_keys['Championships'][0] in content_keys:
        for champ in content[attrs_keys['Championships'][0]]['values']:
            attrs['Championships'].append(champ ['text'])
    
    #Frounded
    attrs['Founded'] = ''
    if attrs_keys['Founded'][0] in content_keys:
        attrs['Founded'] = content[attrs_keys['Founded'][0]]['values'][0]['text']
    
    #League
    attrs['Leagues'] = ''
    if attrs_keys['Leagues'][0] in content_keys:
        attrs['Leagues'] = content[attrs_keys['Leagues'][0]]['values'][0]['property']['/sports/sports_league_participation/league']['values'][0]['text']
    
    #Location
    attrs ['Locations'] = ''
    if attrs_keys['Locations'][0] in content_keys:
        attrs['Locations'] = content[attrs_keys['Locations'][0]]['values'][0]['text']
    
    #Coaches in a list of coaches with each coach represented in a dictionary, with keys Name, Position, From/To
    attrs['Coaches'] = []
    if attrs_keys['Coaches'][0] in content_keys:
        for coach in content[attrs_keys['Coaches'][0]]['values']:
            coachKeys = coach['property'].keys()
            eachCoach = {}
            #Coach Name
            eachCoach['Name']=''
            if coachDic['Name'][0] in coachKeys:
                eachCoach['Name'] = coach['property'][coachDic['Name'][0]]['values'][0]['text']
            #Coach Postion
            eachCoach['Position'] = ''
            if coachDic['Position'][0] in coachKeys:
                eachCoach['Position'] = coach['property'][coachDic['Position'][0]]['values'][0]['text']
            #Coqch From/To
            eachCoach['From/To'] = ''
            if coachDic['From/To'][0] in coachKeys:
                coach_obj = (coach['property'][coachDic['From/To'][0]]).get('values', None)
                if (coach_obj != None and len(coach_obj) != 0):
                    eachCoach['From/To'] += coach['property'][coachDic['From/To'][0]]['values'][0]['text']
            if coachDic['From/To'][1] in coachKeys:
                eachCoach['From/To'] += ' / '
                coach_obj = (coach['property'][coachDic['From/To'][1]]).get('values', None)
                if ( len(coach_obj) != 0 and coach_obj != None):
                    eachCoach['From/To'] += coach['property'][coachDic['From/To'][1]]['values'][0]['text']
                elif eachCoach['From/To'] != '':
                    eachCoach['From/To'] += 'now'
            elif eachCoach['From/To'] != '':
                eachCoach['From/To'] += ' / now'
            
            attrs['Coaches'].append(eachCoach)

    
    
    #Players_Roster is a list, each player represented in a dictionary, position in each dictionary is a list of positions
    #everything else is just string
    attrs['Players_Roster'] = []
    if attrs_keys['Players_Roster'][0] in content_keys:
        for roster in content[attrs_keys['Players_Roster'][0]]['values']:
            rosterKeys = roster['property'].keys()
            eachRoster = {}
            
            #Roster Name
            eachRoster['Name'] = ''
            if rosterDic['Name'][0] in rosterKeys:
                eachRoster['Name'] = roster['property'][rosterDic['Name'][0]]['values'][0]['text']
            eachRoster['Position'] = ''
            
            #Roster Position
            eachRoster['Position'] = ''
            positions = []
            if rosterDic['Position'][0] in rosterKeys:
                for position in roster['property'][rosterDic['Position'][0]]['values']:
                    positions.append(position['text'])
                eachRoster['Position'] = ', '.join(positions)
            
            #Roster Number
            eachRoster['Number'] = ''
            if rosterDic['Number'][0] in rosterKeys:
                Number = roster['property'][rosterDic['Number'][0]].get('values',None)
                if len(Number) != 0 and Number != None:
                    eachRoster['Number'] = roster['property'][rosterDic['Number'][0]]['values'][0]['text']

            #Roster From/To
            eachRoster['From/To'] = ''
            if rosterDic['From/To'][0] in rosterKeys:
                From = roster['property'][rosterDic['From/To'][0]].get('values', None)
                if len(From) != 0 and From != None:
                    eachRoster['From/To'] += roster['property'][rosterDic['From/To'][0]]['values'][0]['text']
            if rosterDic['From/To'][1] in rosterKeys:
                To = roster['property'][rosterDic['From/To'][1]].get('values', None)
                if len(To) !=0 and To != None:
                    eachRoster['From/To'] += ' / '
                    eachRoster['From/To'] += roster['property'][rosterDic['From/To'][1]]['values'][0]['text']
                elif eachRoster['From/To'] != '':
                    eachRoster['From/To'] += 'now'
            elif eachRoster['From/To'] != '':
                eachRoster['From/To'] += ' / now'
            
            attrs['Players_Roster'].append(eachRoster)
    
    #Description
    attrs ['Description'] = ''
    if attrs_keys['Description'][0] in content_keys:
        attrs['Description'] = content[attrs_keys['Description'][0]]['values'][0]['value']
    
    return attrs