import json
import fnmatch
import os

def convert_json_to_txt(txt_name, want_to_search):
    wfile = open(txt_name+".txt", "w")
    for file in os.listdir('../raw_json/.'):
        if (want_to_search in file): 
            f = open(file,'r',encoding="utf8")
            data = json.load(f)
            wfile.write(json.dumps(data))
            wfile.write('\n')
            f.close()
    wfile.close()