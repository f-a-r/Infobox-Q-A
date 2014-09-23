#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_header(name, entity_types_matched):
    print_hline()
    entities = ', '.join(entity_types_matched).upper()
    title = '%s(%s)'%(name, entities)
    print ' '*4 + '|' + title.center(98) + '|'
    return 

def cut_str(s, n):
    if len(s) > n:
        if n > 4:
            s = s[0:n-4] + ' ...'
    return s


def print_person(attrs):
    attrs_paragraph = ['Name', 'Birthday', 'Place_of_Birth', 'Death', 'Description']
    attrs_lines = ['Spouses', 'Siblings', 'Books', 'Books_About', 'Influenced','Influenced_By', 'Founded']
    attrs_table = ['Films', 'Board_Member', 'Leadership']

    attrs_keys = attrs.keys()
    for a in attrs_paragraph:
        if a in attrs_keys:
            print_paragraph(a, attrs[a])
    for a in attrs_lines:
        if a in attrs_keys:
            print_lines(a, attrs[a])
    for a in attrs_table:
        if a in attrs_keys:
            print_table(a, attrs[a])

def print_team(attrs):
    attrs_paragraph = ['Name', 'Sport', 'Arena', 'Founded', 'Leagues', 'Locations', 'Description']
    attrs_lines = ['Championships']
    attrs_table = ['Coaches', 'Players_Roster']

    attrs_keys = attrs.keys()
    for a in attrs_paragraph:
        if a in attrs_keys:
            print_paragraph(a, attrs[a])
    for a in attrs_lines:
        if a in attrs_keys:
            print_lines(a, attrs[a])
    for a in attrs_table:
        if a in attrs_keys:
            print_table(a, attrs[a])


def print_league(attrs):
    attrs_paragraph = ['Name', 'Championship', 'Sport', 'Slogan', 'Official_Website', 'Description']
    attrs_lines = ['Teams']

    attrs_keys = attrs.keys()
    for a in attrs_paragraph:
        if a in attrs_keys:
            print_paragraph(a, attrs[a])
    for a in attrs_lines:
        if a in attrs_keys:
            print_lines(a, attrs[a])


def print_paragraph(key, output_str):
    output_str = output_str.replace('\n', ' ')
    key = key.replace('_', ' ')
    key = ' '+key+':'
    key = key.ljust(17)
    str_len = len(output_str)
    para_width = 81

    if str_len < para_width:
        if str_len > 0:
            print_hline()
            print ' '*4 + '|' + key + output_str.ljust(para_width) + '|'
    else:
        print_hline()
        print ' '*4 + '|' + key + output_str[0:para_width] + '|'
        counter = para_width
        while (counter < str_len):
            print ' '*4 + '|' + ' '*17 + output_str[counter:counter+para_width].ljust(para_width) + '|'
            counter = min(str_len, counter+para_width)
    #print output_str

def print_hline():
    print ' '*5 + '-'*98
    return

def print_lines(key, output_list):
    if len(output_list) > 0:
        para_width = 81
        print_hline()
        key = key.replace('_', ' ')
        key = ' '+key+':'
        key = key.ljust(17)
        s = cut_str(output_list[0], para_width)
        print ' '*4 + '|' + key + s.ljust(para_width) + '|'
        for s in output_list[1:]:
            s = cut_str(s, para_width)
            print ' '*4 + '|' + ' '*17 + s.ljust(para_width) + '|'

def print_table(key, output_list):
    if len(output_list):
        para_width = 82
        N = len(output_list[0])
        L = para_width/N
        R = para_width-L*N
        column_widthes = [L+1]*R
        column_widthes.extend([L]*(N-R))
        
        print_hline()

        key = key.replace('_', ' ')
        key = ' '+key+':'
        key = key.ljust(15)
        headers = sorted(output_list[0].keys())
        print ' '*4 + '|' + key,

        row_strs = {}
        row_format = ''
        
        for i, h in enumerate(headers):
            h = h.replace('_', ' ')
            row_strs[i] = '| ' + h
            row_format += '{0[%d]:%d}'%(i,column_widthes[i])
        row_format += '|'
        row_format = unicode(row_format)
        print row_format.format(row_strs)
        #print row_strs
        #print row_format
        

        print ' '*4 + '|' + ' '*16 + '-'*82
        for obj in output_list:
            row_strs = {}
            row_format = ' '*4 + '|' + ' '*16
            for i , k in enumerate(headers):
                s = obj[k]
                s = cut_str(s, column_widthes[i]-2)
                obj[k] = s
                row_format += '| {0[%s]:%d}'%(k,column_widthes[i]-2)
            row_format += '|'
            row_format = unicode(row_format)
            print row_format.format(obj)
            #print row_format
            #print obj

 



