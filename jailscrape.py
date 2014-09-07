import requests
import csv
from BeautifulSoup import BeautifulSoup

url = "http://www.showmeboone.com/sheriff/jailresidents/jailresidents.asp"

############# Part 1 ###############

#Open the html file and turn it into a BeautifulSoup object for parsing. Response will bring back EVERYTHING on the webpage
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
#or you could do soup = BeautifulSoup(requests.get(url)) OR BeautifulSoup(response.content)

results_table = soup.find('table', attrs={'class': 'resultsTable'})

#print results_table

############### Part 2 ###############

output = []

for row in results_table.findAll('tr'):

    output_row = []
    
    for cell in row.findAll('td'):
        clean_data = cell.text.replace('&nbsp;','')
        output_row.append(clean_data)
    
    output.append(output_row)

#print output

#Need to change a list to csv file?...Copy this bit below.

csv_file = open('out-using-requests.csv', 'w')
writer = csv.writer(csv_file)
writer.writerows(output)

