import bs4
import re
import test_parser

html_to_text = ''
converted_string = ''

with open("sample.html", "r") as html_file:
    result = []
    text = html_file.read()
    soup = bs4.BeautifulSoup(text,'lxml')
    table = soup.find('table')
    headers = [heading.text for heading in table.find_all('tr')]
    #table_rows = [rows.text for rows in table.find('tr')]
    for each_content in headers:
        #print(each_content)
        result.append(each_content.replace('\n','').replace('\xa0','').replace('\u200b','').replace('\u00ae','').replace('\"',''))
    res = list(filter(None, result))
    final_result = list(set(res))
    for each_element in final_result:
        converted_string = converted_string + each_element + '\n'
    
def html_specific_funtion():
    name = str(re.findall(r"(?<=Name).*",converted_string)[1])
    emails = str(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", converted_string)[0])
    number = str(re.findall(r"r'\d{9,10}'",converted_string))
    datetime = str(re.findall(r"(?=April)\b.*",converted_string)[0])
    address = str(re.findall(r"(?<=I'm interested in).*?:",converted_string)[0])
    html_to_text = ('name ' + (name) + '\n' + 'email ' + (emails) + '\n' + 'number ' + (number)
    + '\n' + 'date ' + (datetime) + '\n' + 'address ' + (address) )
    print(html_to_text)
    with open("test1.txt", "w") as file1:
	    file1.writelines(html_to_text)

def Default_String_file_saving():
    with open("test1.txt", "w") as file1:
	    file1.writelines(converted_string)

def main():
    #UNomment the below Funtion to just get a default JSON File
    #Default_String_file_saving()
    #if you running the above funtion then please comment the below one 
    html_specific_funtion()
    test_parser.text_to_json()


