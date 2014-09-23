#!/usr/bin/env python
# -*- coding: utf-8 -*-

def book_author(results):
    answers = []
    for result in results:
        answer = {'name':'', 'books':[]}
        answer['name'] = result['name']
        answer['books'] = [ x['a:name'] for x in result['/book/author/works_written'] ]
        answers.append(answer)
    return answers

def organozation_businessman(results):
    answers = []
    for result in results:
        answer = {'name':'', 'companies':[]}
        answer['name'] = result['name']
        answer['companies'] = [ x['a:name'] for x in result['/organization/organization_founder/organizations_founded'] ]
        answers.append(answer)
    return answers

