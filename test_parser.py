
# Python program to convert text
# file to JSON
  
  
import json
  
def text_to_json():  
    # the file to be converted to 
    # json format
    filename = 'test1.txt'
    
    # dictionary where the lines from
    # text will be stored
    dict1 = {}
    
    # creating dictionary
    with open(filename) as fh:
    
        for line in fh:
    
            # reads each line and trims of extra the spaces 
            # and gives only the valid words
            command, description = line.strip().split(None, 1)
    
            dict1[command] = description.strip()
    
    # creating json file
    # the JSON file is named as test1
    out_file = open("details.json", "w")
    json.dump(dict1, out_file, indent = 4, sort_keys = False)
    out_file.close()