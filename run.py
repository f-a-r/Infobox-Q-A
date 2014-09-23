#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
import urllib
import base64
import json
import sys
import string
import re
import math
from numpy  import *
#from prettytable import  *

import person_attr_extraction
import businessperson_attr_extraction
import author_attr_extraction
import actor_attr_extraction
import league_attr_extraction
import sportsTeam_attr_extraction
import questions
import output

def type_match(entity_dict, entity_types):
    entity_types_matched = []
    for type_name in entity_dict:
        for t in entity_dict[type_name]:
            if t in entity_types:
                entity_types_matched.append(type_name)
                break  
    return entity_types_matched 

def question(queries_input, API_KEY):

    if queries_input[0:12].lower() != 'who created ':
        print 'Wrong question!!!'
        exit()

    if queries_input[-1]  == '?':
        queries_input = queries_input[:-1]
    query = queries_input[12:]
    query = query.strip()

    #print 'Query type: question' 
    print 'Query string: '
    print queries_input
    print '='*104
    
    # Book
    query_dict_book = '[{ "/book/author/works_written": [{ "a:name": null, "name~=": "%s"}], "id": null, "name": null, "type": "/book/author" }]'%(query)
    query_dict_book = urllib.quote(query_dict_book)
    apiUrl_search = 'https://www.googleapis.com/freebase/v1/mqlread?query=' + query_dict_book + '&key=' + API_KEY
    #print 'apiURL: ' + apiUrl_search
    response = urllib.urlopen(apiUrl_search).read()
    #print response
    response = unicode(response,"utf-8",errors="ignore")
    #content contains the xml/json response from Freebase. 
    content = json.loads(response)
    results = content.get('result',None)
    if results == None:
        print 'No result returned'
        exit()
    answers_book = questions.book_author(results)

    # Organization
    query_dict_organization = '[{ "/organization/organization_founder/organizations_founded": [{ "a:name": null, "name~=": "%s"}], "id": null, "name": null, "type": "/organization/organization_founder" }]'%(query)
    apiUrl_search = 'https://www.googleapis.com/freebase/v1/mqlread?query=' + query_dict_organization + '&key=' + API_KEY
    #print 'apiURL: ' + apiUrl_search
    response = urllib.urlopen(apiUrl_search).read()
    #print response
    response = unicode(response,"utf-8",errors="ignore")
    #content contains the xml/json response from Freebase. 
    content = json.loads(response)
    results = content.get('result',None)
    if results == None:
        print 'No result returned'
        exit()
    answers_organization = questions.organozation_businessman(results)

    tuples_book = [(x['name'], '(as Author) created', x['books']) for x in answers_book]
    tuples_organization = [(x['name'], '(as Businessperson) created', x['companies']) for x in answers_organization]
    tuples_print = []
    tuples_print.extend(tuples_book)
    tuples_print.extend(tuples_organization)
    tuples_print = sorted(tuples_print)
    
    for i, item in enumerate(tuples_print):
        if len(item[2]) > 2:
            objs = '>, <'.join(item[2][0:-1])
            objs = '<' + objs + '>'
            objs += ', and <%s>'%(item[2][-1])
        elif len(item[2]) == 2:
            objs = '<%s> and <%s>'%(item[2][0], item[2][1])     
        elif len(item[2]) == 1:
            objs = item[2][0]
            objs = '<' + objs + '>'
        else:
            print 'Wrong result returned'
        line = u'%d. %s %s %s'%(i+1, item[0], item[1], objs)
        print line      

def infobox(queries_input, API_KEY):
    queries_input = string.split(queries_input)
    apiUrl_search = 'https://www.googleapis.com/freebase/v1/search?query='+'%20'.join(queries_input)+'&key='+API_KEY
    #print 'apiURL: ' + apiUrl_search
    #print 'Query type: infobox' 
    print 'Query string: '
    print queries_input
    print '='*104

    response = urllib.urlopen(apiUrl_search).read()
    #print response
    response = unicode(response,"utf-8",errors="ignore")
    #content contains the xml/json response from Freebase. 
    content = json.loads(response) #keys: [u'status', u'cursor', u'hits', u'cost', u'result']
    results = content.get('result',None)
    if results == None:
        print 'No result returned'
        exit()
    mids = [ x['mid'] for x in results]
    names = [ x['name'] for x in results]

    #print mids

    entity_dict = { \
    'Person': ['/people/person', '/people/deceased_person'], \
    'Author': ['/book/author'], \
    'Actor': ['/film/actor', '/tv/tv_actor'], \
    'BusinessPerson': ['/organization/organization_founder', '/business/board_member'], \
    'League': ['/sports/sports_league'], \
    'SportsTeam': ['/sports/sports_team', '/sports/professional_sports_team'] \
    }

    entity_types_matched = []

    for i, m in enumerate(mids):
        apiUrl_topic = 'https://www.googleapis.com/freebase/v1/topic' + m + '?key='+ API_KEY
        print 'topicURL: ' + apiUrl_topic
        response = urllib.urlopen(apiUrl_topic).read()
        response = unicode(response,"utf-8",errors="ignore")
        #content contains the xml/json response from Freebase. 
        content = json.loads(response) #keys: [u'property', u'id']
        content = content.get('property', None)
        if content == None:
            print 'No result returned'
            exit()
        entity_types = [ x['id'] for x in content['/type/object/type']['values']]
        entity_types_matched = type_match(entity_dict, entity_types) # find to what entity_dict our found entity_types match
        #print 'Matched Entity Types:'
        #print entity_types_matched
        #print '='*104
        if len(entity_types_matched) > 0:
            break

    attrs_Person = {}
    attrs_Author = {}
    attrs_Actor ={}
    attrs_BusinessPerson = {}
    attrs_League ={}
    attrs_SportsTeam ={}
    if len(entity_types_matched) == 0:
        print "Query was not among the accepted entity types"
        exit()
    if 'Person' in entity_types_matched:
        attrs_Person = person_attr_extraction.parsing(content)
    if 'Author' in entity_types_matched:
        attrs_Author = author_attr_extraction.parsing(content)
    if 'Actor' in entity_types_matched:
        attrs_Actor = actor_attr_extraction.parsing(content)
    if 'BusinessPerson' in entity_types_matched:
        attrs_BusinessPerson = businessperson_attr_extraction.parsing(content)
    if 'League' in entity_types_matched:
        attrs_League = league_attr_extraction.parsing(content)
    if 'SportsTeam' in entity_types_matched:
        attrs_SportsTeam = sportsTeam_attr_extraction.parsing(content)

    

    if len(attrs_League) > 0:
        output.print_header(attrs_League['Name'], entity_types_matched)
        output.print_league(attrs_League)
        output.print_hline()
    elif len(attrs_SportsTeam) > 0:
        output.print_header(attrs_SportsTeam['Name'], entity_types_matched)
        output.print_team(attrs_SportsTeam)
        output.print_hline()
    elif (len(attrs_Person) > 0) or (len(attrs_Author) > 0) or (len(attrs_Actor) > 0) or (len(attrs_BusinessPerson) > 0):
        if len(attrs_Person) == 0:
            name = names[i]
        else:
            name = attrs_Person['Name']
        output.print_header(name, entity_types_matched)
        attrs = {}
        for a in attrs_Person:
            attrs[a] = attrs_Person[a]
        for a in attrs_Author:
            attrs[a] = attrs_Author[a]
        for a in attrs_Actor:
            attrs[a] = attrs_Actor[a]
        for a in attrs_BusinessPerson:
            attrs[a] = attrs_BusinessPerson[a]
        output.print_person(attrs)
        output.print_hline()
    else:
        print('Nothing found.')

def main():

    if (sys.argv[1] != '-key') or (sys.argv[5] != '-t'):
        print 'Wrong input format1.'
        exit()

    if (not sys.argv[3] == '-f') and (not sys.argv[3] == '-q'):
        print 'Wrong input format2.'
        exit()

    if (not sys.argv[6] == 'infobox') and (not sys.argv[6] == 'question'):  
        print 'Wrong input format3.'
        exit()        

    API_KEY = sys.argv[2]
    queries_type = sys.argv[6]

    queries_inputs = []
    if sys.argv[3] == '-q':
        queries_inputs.append(sys.argv[4])
    else:
        filename = sys.argv[4]
        for line in open(filename):
            queries_inputs.append(string.strip(line))
    #print queries_inputs
    
    for queries_input in queries_inputs:
        #print 'queries_type: ' + queries_type
        #print 'queries_input'
        #print queries_input
        #print API_KEY

        #API_KEY = 'AIzaSyA5c1nxOEDPual-jfeLVt-i571ngRFost4'
        if queries_type == 'infobox':
            infobox(queries_input, API_KEY)
        elif queries_type == 'question':
            question(queries_input, API_KEY)
        else:
            print('Query type error.')
        
main()