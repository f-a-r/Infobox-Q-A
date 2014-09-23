#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parsing(content):
    #print "********************* ACTOR ATTRS ******************************"
    attrs = {}
    attr_keys = {\
    'Films':['/film/performance/character','/film/performance/film']}
    content_keys = content.keys()

    # charcater and movie played with that character
    # each character and movie is a dictionary with keys character and movie and these dictionaries are saved in attrs list
    attrs['Films'] = []
    if '/film/actor/film' in content_keys:
        
        for x in content['/film/actor/film']['values']:
            #print x
            charfilm = {}
            charfilm['Character'] = ''
            if attr_keys['Films'][0] in x['property'].keys():
                charfilm['Character'] += x['property'][attr_keys['Films'][0]]['values'][0]['text']
            charfilm['Film_Name'] = ''
            if attr_keys['Films'][1] in x['property'].keys():
                charfilm['Film_Name']= x['property'][attr_keys['Films'][1]]['values'][0]['text']
            attrs['Films'].append(charfilm)

    return attrs