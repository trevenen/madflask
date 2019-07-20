class Parser():
    def parse_data(json_object, key_value):
        result = []
        def extract_json_value(json_object,result,key_value):
            #extraction result
            #verify if the loaded object is a json object
            if isinstance(json_object, dict):
                # extract all the pair (key, value) and check if it is a json object
                for k, v in json_object.items():
                    if isinstance(v, (dict, list)):
                        extract_json_value(v,result, key_value)
                    elif k == key_value: #verify if the pair (key, value) is equal to the passed argument
                        result.append(v)
                    #verify if the pair (key, value) is a list
            elif isinstance(json_object, list):
                for item in json_object:
                    extract_json_value(item,result, key_value)
            return result
        
        results = extract_json_value(json_object, result, key_value)
        return results
    

