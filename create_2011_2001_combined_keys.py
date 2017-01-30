import dataset
db = dataset.connect('sqlite:///./db/attributes.sqlite')
state_code = 'ga'
state_table_name = state_code+'_village_2011_2001_code_mapping'
state_table  = db[state_table_name]

for state in  state_table.all():	
	state_code_2001 = str(state['state_code_2001'])
	district_code_2001 = str(state['district_code_2001'])
	sub_district_code_2001 = str(state['sub_district_code_2001'])
	village_code_2001 = str(state['village_code_2001'])
	CEN_2001 = "{:>2s}{:>2s}{:>4s}{:>8s}".format(state_code_2001,district_code_2001,sub_district_code_2001,village_code_2001)
	CEN_2001 = CEN_2001.replace(' ','0')
	print str(CEN_2001)
	print len(str(CEN_2001))
	sql =	   " UPDATE "+state_table_name;
	sql = sql +" SET CEN_2001= '"+str(CEN_2001)+"'" 
	sql = sql +" WHERE "
	sql = sql +" state_code_2001 = '"+state_code_2001+"'"
	sql = sql +" AND district_code_2001 = '"+district_code_2001+"'"
	sql = sql +" AND sub_district_code_2001 = '"+sub_district_code_2001+"'"
	sql = sql +" AND village_code_2001 = '"+village_code_2001+"';"
	result = db.query(sql)

result = state_table.all()
dataset.freeze(result, format='csv', filename=state_code+'.csv')
