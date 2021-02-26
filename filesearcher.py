import os
import sys

count = 0
def search_file(path, to_search):
    global count
    try:
        fh = open(path, "r")
        for lines in fh.readlines():
            if lines.find(to_search) is not -1:
                print(to_search, "Found in",path)
                count += 1
    except:
        print("Error opening the file :",path)

root_path = os.walk(sys.argv[1])

try:
    search_string = sys.arv[2]
except:
    search_string = ""

for element in (root_path):
    path_start = element[0]
    if len(element[1]):
        subfiles = element[1]
    else:
        subfiles = element[2]
    for filee in subfiles:
        search_file(path_start + "/" + filee, search_string)

print("Found in {} number of files".format(count))
