from duckduckgo import duckduckgo

search_results = duckduckgo.search('coca cola cnpj')

for r in search_results: 
	print(r.name, r.description)