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




        

