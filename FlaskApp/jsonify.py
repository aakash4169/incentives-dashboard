import pandas as pd
import numpy as np
import re

def _multivalued_comma_delim(programs, field):

    unique_multivalued = set()

    for index, row in programs.iterrows():
        values = row[field]
        if values is np.NaN: continue
        if (values.find(', ') == -1):
            unique_multivalued.add(values)
        else:
            while (values.find(', ') != -1):
                unique_multivalued.add(values[:values.find(', ')])
                values = values[values.find(', ')+2:]
            unique_multivalued.add(values)
    toRemove = []
    for i in unique_multivalued:
        if i[len(i)-1] == ',':
            toRemove.append(i)

    for i in toRemove:
        unique_multivalued.remove(i)

    return unique_multivalued

def prepValue(value):
    if value is np.NaN: return 'null'
    for i in range(0, len(value)):
        if value[i] == '\"' or value[i] == '\\':
            if value[i-1] != '\\':
                value = value[:i]+'\\'+value[i:]
    if value[len(value)-1] == '\"':
            if value[len(value)-2] != '\\':
                value = value[:len(value)-1]+'\\'+value[len(value)-1:]
    return str('\"'+value+'\"')

def buildJSONRecord(row, ubn, ugf, upc, upt, upi):
    record = '{'
    record += '\"program_name\":' + prepValue(row['program_name']) + ','
    record += '\"program_description\":' + prepValue(row['program_description']) + ','
    record += '\"program_objectives\":' + prepValue(row['program_objectives']) + ','
    record += '\"contact_email\":' + prepValue(row['contact_email']) + ','
    record += '\"contact_info\":' + prepValue(row['contact_info']) + ','
    record += '\"department\":' + prepValue(row['department']) + ','
    record += '\"program_administration_type\":' + prepValue(row['program_administration_type']) + ','
    record += '\"program_cap\":' + prepValue(row['program_cap']) + ','
    record += '\"program_finish\":' + prepValue(row['program_finish']) + ','
    record += '\"program_start\":' + prepValue(row['program_start']) + ','
    record += '\"program_specifics\":' + prepValue(row['program_specifics']) + ','
    record += '\"state\":' + prepValue(row['state']) + ','
    record += '\"website\":' + prepValue(row['website']) + ','
    
    record += '\"business_needs\":['
    for need in ubn:
        if need in str(row['business_needs']):
            record += '\"' + need + '\",'
    if record[len(record)-1] == ',':
        record = record[:len(record)-1]
    record += '],'
    
    record += '\"geographic_focus\":['
    for focus in ugf:
        if focus in str(row['geographic_focus']):
            record += '\"' + focus + '\",'
    if record[len(record)-1] == ',':
        record = record[:len(record)-1]
    record += '],'
        
    record += '\"program_category\":['
    for cat in upc:
        if cat in str(row['program_category']):
            record += '\"' + cat + '\",'
    if record[len(record)-1] == ',':
        record = record[:len(record)-1]
    record += '],'
    
    record += '\"program_industries\":['
    for ind in upi:
        if ind in str(row['program_industries']):
            record += '\"' + ind + '\",'
    if record[len(record)-1] == ',':
        record = record[:len(record)-1]
    record += '],'
            
    record += '\"program_type\":['
    for ty in upt:
        if ty in str(row['program_type']):
            record += '\"' + ty + '\",'
    if record[len(record)-1] == ',':
        record = record[:len(record)-1]
    record += ']'
            
    record += '}'

    return record

def jsonifyPrograms():
	programs = pd.read_csv('programdata.csv')

	programs = programs.drop(columns=['additional_website', 'application_information', 'contact_address', 'eligibility_requirements', 'legal_citation'])
	rowsToDrop = []
	for index, row in programs.iterrows():
	    if row['program_administration_type'] not in ['Statutory', 'Discretionary', np.NaN]:
	        rowsToDrop.append(index)
	programs = programs.drop(rowsToDrop)

	ubn = _multivalued_comma_delim(programs, 'business_needs')
	ugf = _multivalued_comma_delim(programs, 'geographic_focus')
	upc = _multivalued_comma_delim(programs, 'program_category')
	upt = _multivalued_comma_delim(programs, 'program_type')

	upi = set()

	for index, row in programs.iterrows():
	    industries = row['program_industries']
	    if industries is np.NaN: continue
	    if re.search(', \d', industries) == None:
	        cleaned = industries[industries.find('- ')+2:]
	        upi.add(cleaned)
	    else:
	        while re.search(', \d', industries) != None:
	            toAdd = industries[:re.search(', \d', industries).start()]
	            cleaned = toAdd[toAdd.find('- ')+2:]
	            upi.add(cleaned)
	            industries = industries[re.search(', \d', industries).start()+2:]
	        cleaned = industries[industries.find('- ')+2:]
	        upi.add(cleaned)
	        
	toRemove = []
	for i in upi:
	    if i[len(i)-1] == ',':
	        toRemove.append(i)

	for i in toRemove:
	    upi.remove(i)

	program_json = ''

	for index, row in programs.iterrows():
	    program_json += buildJSONRecord(row, ubn, ugf, upc, upt, upi) + '\n'

	f = open('programs_formatted.json', 'w')
	f.write(program_json)
	f.close()

	program_json_without_header = ''
