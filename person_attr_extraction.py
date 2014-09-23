#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parsing(content):
    #print "********************* PERSON ATTRS ******************************"
    attrs = {}
    attr_keys = {\
    'Name': ['/type/object/name'],\
    'Birthday': ['/people/person/date_of_birth'], \
    'Place_of_Birth': ['/people/person/place_of_birth'],\
    'Death': ['/people/deceased_person/date_of_death','/people/deceased_person/place_of_death','/people/deceased_person/cause_of_death'],\
    'Siblings': ['/people/person/sibling_s'],\
    'Spouses': ['/people/person/spouse_s'],\
    'Description': ['/common/topic/description']}
    content_keys = content.keys()
    
    # Name 
    attrs['Name'] = ''
    if attr_keys['Name'][0] in content_keys:
        attrs['Name'] = content[attr_keys['Name'][0]]['values'][0]['text']
        

    # Birthday
    attrs['Birthday'] = ''
    if attr_keys['Birthday'][0] in content_keys:
        attrs['Birthday'] = content[attr_keys['Birthday'][0]]['values'][0]['text']
    
    
    # Place of Birth
    attrs['Place_of_Birth'] = ''
    if attr_keys['Place_of_Birth'][0] in content_keys:
        attrs['Place_of_Birth'] = content[attr_keys['Place_of_Birth'][0]]['values'][0]['text']
    

    # Death: 2009-06-25 at Holmby Hills, cause: (Cardiac arrest, Homicide) 
    # Death: <2009-06-25> <at Holmby Hills> <, cause: (Cardiac arrest, Homicide)> 
    # Date
    attrs['Death'] = ''
    if attr_keys['Death'][0] in content_keys:
        attrs['Death'] += content[attr_keys['Death'][0]]['values'][0]['text'] + ' '
    # Place
    if attr_keys['Death'][1] in content_keys:
        attrs['Death'] += 'at ' + content[attr_keys['Death'][1]]['values'][0]['text']
    # Cause
    if attr_keys['Death'][2] in content_keys:
        causes = [ x['text'] for x in content[attr_keys['Death'][2]]['values']]
        attrs['Death'] += ', cause: (' + ', '.join(causes) + ')'
        
    # Siblings
    attrs['Siblings'] = []
    if attr_keys['Siblings'][0] in content_keys:
        for sibling in content[attr_keys['Siblings'][0]]['values']:
            sibling = sibling['property']['/people/sibling_relationship/sibling']['values'][0]['text']      
            attrs['Siblings'].append(sibling) 

    # Description
    attrs['Description'] = ''
    if attr_keys['Description'][0] in content_keys:
        attrs['Description'] = content[attr_keys['Description'][0]]['values'][0]['value'] 

    #Spouses
    attrs['Spouses'] = []
    if attr_keys['Spouses'][0] in content_keys:
        for spouse in content[attr_keys['Spouses'][0]]['values']:
            spouse = spouse['property']['/people/marriage/spouse']['values'][0]['text']      
            attrs['Spouses'].append(spouse) 

    #print content['/people/person/spouse_s']
    return attrs

#def printing(attrs):

