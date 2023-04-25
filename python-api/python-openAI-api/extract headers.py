

#import the necessary libraries
import requests
from bs4 import BeautifulSoup
import googletrans

#specify the url
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

#send a request to the specified url
page = requests.get(url)

#parse the html content
soup = BeautifulSoup(page.content, 'html.parser')

#find all html headers
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

#create a list to store the translated headers
translated_headers = []

#translate each header to spanish using googletrans

translator = googletrans.Translator()
for header in headers:
    
    translator.translate(header.text, dest='es')
    translate_results = {
       "text": translator.translate(header.text, dest='es').text,
       "name": header.name
    }
    translated_headers.append(translate_results)
    

#open a new html file
f = open('translated_headers.html', 'w')

#write the html code to the file
f.write('<html><head><title>Translated Headers</title></head><body>')

#iterate through the translated headers list
for header in translated_headers:
    #write each header to the html file
    f.write(f'<{header["name"]}> {header["text"]}  </{header["name"]}>\n')

#close the html file
f.write('</body></html>')
f.close()