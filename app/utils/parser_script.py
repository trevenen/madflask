import json
from json_paser import Parser
import sys
import os

args = sys.argv[1:]
file = args[0]
key_data = args[1:]
if len(key_data)>0:
    result = []
    for i in range(0,len(key_data)):
        key = key_data[i]
        print(key)
        try:
            if os.path.exists(file):
                f = open(file,'r')
                json_obj = json.load(f)
                res = Parser.parse_data(json_obj, key)
                result.append(res)
                print(res)
                f.close()
            else:
                print('files does not exist')
        except IOError:
            print ('parameters error')
    return result