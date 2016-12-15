# Search sys.path (a superset of PYTHONPATH) to find location of
# the module (.py or .pyc) that is specified as input parameter.

'''
This is a multiline comment
'''

def search_pythonpath(inn):
    import sys
    import os
    print ("--- sys.path ---")
    print sys.path

    for p in sys.path:
        search_string = p + "/" + inn
        found = os.path.isfile(search_string)
        if found:
            print ("found ---> " + search_string)
            break


def remove_all_routes():
    import sys
    import os
    import subprocess
    import json

    my_routes=[]

    # squirrel away URLs for the space, apps and services
    temp_p1 = json.loads(subprocess.check_output(["cf", "curl", "/v2/spaces"]))
    for num1, line1 in enumerate(temp_p1["resources"]):
        space_name = line1["entity"]["name"]
        routes_url  = line1["entity"]["routes_url"]
        temp_p2 = json.loads(subprocess.check_output(["cf", "curl", routes_url]))
        for num2,line2 in enumerate(temp_p2["resources"]):
              route_host_name = line2["entity"]["host"]
              route_url  = line2["metadata"]["url"]
              my_routes.append(route_url)
              #print space_name + " " + route_host_name + " " + route_url

    for r in my_routes:
        print "deleting route" + r
        subprocess.check_output(["cf", "curl",
                                 r + "?recursive=true?async=false",
                                "-X", "DELETE"])
    print "done"

    


        

