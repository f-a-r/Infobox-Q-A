#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parsing(content):
    #print "********************* BUSINESS PERSON ATTRS ******************************"
    attrs = {}
    attr_keys = {\
    'Founded': ['/organization/organization_founder/organizations_founded'],\
    'Board_Member': ['/business/board_member/organization_board_memberships'], \
    'Leadership': ['/business/board_member/leader_of']\
    }
    content_keys = content.keys()
    
    # Founded
    attrs['Founded'] = []
    if attr_keys['Founded'][0] in content_keys:
        attrs['Founded'] = [x['text'] for x in content[attr_keys['Founded'][0]]['values']]

    attrs['Board_Member'] = []
    # Board Member
    if attr_keys['Board_Member'][0] in content_keys:
        for company in content[attr_keys['Board_Member'][0]]['values']:
            company_obj = {'Organization':'', 'Title':'', 'Role':'', 'From-To':''}
            company = company['property']
            
            # Organization
            company_obj['Organization'] = ''
            organization_obj = company.get('/organization/organization_board_membership/organization', None)
            if  organization_obj != None and len(organization_obj['values']) != 0:
                company_obj['Organization'] = organization_obj['values'][0]['text'] 
            
            # Title
            company_obj['Title'] = ''
            title_obj = company.get('/organization/organization_board_membership/title', None)
            if  title_obj != None and len(title_obj['values']) != 0:
                company_obj['Title'] = title_obj['values'][0]['text']
            
            # From
            company_obj['From-To'] = ''
            from_obj = company.get('/organization/organization_board_membership/from', None)
            if  from_obj != None and len(from_obj['values']) !=0 :
                company_obj['From-To'] = from_obj['values'][0]['text']
            # To
            to_obj = company.get('/organization/organization_board_membership/to', None)
            if  to_obj != None and len(to_obj['values']) != 0:
                if company_obj['From-To'] =='':
                    company_obj['From-To'] += ' N/A / ' 
                    company_obj['From-To'] += to_obj['values'][0]['text']
                else:
                    company_obj['From-To'] += ' / ' 
                    company_obj['From-To'] += to_obj['values'][0]['text']
            else:
                if company_obj['From-To'] != '':
                    company_obj['From-To'] += ' / now' 
            
            # role
            company_obj['Role'] = ''
            role_obj = company.get('/organization/organization_board_membership/role', None)
            if  role_obj != None and len(role_obj['values']):
                company_obj['Role'] = role_obj['values'][0]['text']
            
            attrs['Board_Member'].append(company_obj)
            #print company_obj

    #Leadership
    attrs['Leadership'] = []
    if attr_keys['Leadership'][0] in content_keys:
        for leader_of in content[attr_keys['Leadership'][0]]['values']:
            leadership_obj = {'Organization': '', 'Role': '', 'Title': '', 'From-To': ''}
            leader_of = leader_of['property']
            
            #Organization
            leadership_obj['Organization'] = ''
            organization_obj = leader_of.get('/organization/leadership/organization', None)
            if  organization_obj != None and len(organization_obj['values']) != 0:
                leadership_obj['Organization'] = organization_obj['values'][0]['text'] 

            #Title
            leadership_obj['Title'] = ''
            title_obj = leader_of.get('/organization/leadership/title', None)
            if  title_obj != None and len(title_obj['values']) != 0:
                leadership_obj['Title'] = title_obj['values'][0]['text']

            #Role
            leadership_obj['Role'] = ''
            role_obj = leader_of.get('/organization/leadership/role', None)
            if  role_obj != None and len(role_obj['values']) != 0:
                leadership_obj['Role'] = role_obj['values'][0]['text']

             #From
            leadership_obj['From-To'] = ''
            from_obj = leader_of.get('/organization/leadership/from', None)
            if  from_obj != None and len(from_obj['values']) != 0:
                leadership_obj['From-To'] = from_obj['values'][0]['text']

            #To
            to_obj = leader_of.get('/organization/leadership/to', None)
            if to_obj != None and len(to_obj['values']) != 0:
                if leadership_obj['From-To']=='':
                    leadership_obj['From-To'] += ' N/A / ' 
                    leadership_obj['From-To'] += to_obj['values'][0]['text']
                else:
                    leadership_obj['From-To'] += ' / ' 
                    leadership_obj['From-To'] += to_obj['values'][0]['text']
            else:
                leadership_obj['From-To'] += ' / now'  

            attrs['Leadership'].append(leadership_obj)

        
    return attrs