#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parsing(content):
    #print "********************* AUTHOR ATTRS ******************************"
    attrs = {}
    attr_keys = {\
    'Books':['/book/author/works_written'],\
    'Books_About':['/book/book_subject/works'],\
    'Influenced':['/influence/influence_node/influenced'],\
    'Influenced_By': ['/influence/influence_node/influenced_by']}
    content_keys = content.keys()

    # Books Written 
    attrs['Books'] = []
    if attr_keys['Books'][0] in content_keys:
        for book in content[attr_keys['Books'][0]]['values']:
            book = book ['text']
            attrs['Books'].append(book)

    # Books About
    attrs['Books_About'] = []
    if attr_keys['Books_About'][0] in content_keys:
        for bookAbout in content[attr_keys['Books_About'][0]]['values']:
            bookAbout = bookAbout ['text']
            attrs['Books_About'].append(bookAbout)  

    # Influenced
    attrs['Influenced'] = []
    if attr_keys['Influenced'][0] in content_keys:
        for influenced in content[attr_keys['Influenced'][0]]['values']:
            influenced = influenced ['text']
            attrs['Influenced'].append(influenced) 

    #Influenced By
    attrs['Influenced_By'] = []
    if attr_keys['Influenced_By'][0] in content_keys:
        for influenced in content[attr_keys['Influenced_By'][0]]['values']:
            influenced = influenced ['text']
            attrs['Influenced_By'].append(influenced)


    return attrs
    #TODO: INFLUENCED BY SHOULD BE FOUND!