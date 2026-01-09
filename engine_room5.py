#DIctionary
#Basic 
company = {'name':'Google', 'location':'California', 'founder':'Larry Page', 'founded_year':1998}
print(company)
print(type(company))
print(company['name'])
print(company['location'])
print(len(company))

company['name']='Alphabet Inc.'
print(company)
company['location']='Mountain View, California'
print(company)

print(company.get('name'))
print(company.get('namee'))
print(company.keys())
print(company.values())
company['newkey']='newval'