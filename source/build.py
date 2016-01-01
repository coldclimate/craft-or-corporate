import json
import codecs

text_file = codecs.open("output.html", "w", "utf-8")

with open('data.json') as data_file:    
    data = json.load(data_file)
    data.sort(key=lambda tup: tup["name"])
    for item in data:
    	try:
    		text_file.write("<li class=\"%s\"><a href=\"%s\">%s</a> <a href=\"%s\">citation</a></li>" % (item["status"], item["link"], item["name"], item["citation"]))
    	except KeyError:
    		text_file.write("<li class=\"%s\"><a href=\"%s\">%s</a></li>" % (item["status"], item["link"], item["name"]))
text_file.close()
with open('../output/breweries.json', 'w') as outfile:
    json.dump(data, outfile)

