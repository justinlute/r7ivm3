import json

param_insert = """{
      "name": "view",
      "in": "query",
      "description": "The depth for the JSON response. Valid values are 'details' (default) and 'summary'",
      "required": false,
      "type": "string",
      "default": "details"
     }"""

def check_for_view_parameter(param_list):
    t_f = False
    for param in param_list:
        if param["name"] == "view":
            t_f = True
    return t_f

with open("../source/swag.json", 'r') as infile:
    swagger = json.load(infile)


for k1,v1 in swagger["paths"].items():
    for k2,v2 in v1.items():
        if k2 != "get":
            if 'application/json;charset=UTF-8' in v2["produces"]:
                view_parameter_already_exists = check_for_view_parameter(v2["parameters"])
                if view_parameter_already_exists == False:
                    print(k2, end="--- ")
                    print(swagger["paths"][k1][k2]["parameters"])
                    swagger["paths"][k1][k2]["parameters"].append(param_insert)

with open("swag.json", 'w') as outfile:
    outfile.write(json.dumps(swagger, indent=1))
