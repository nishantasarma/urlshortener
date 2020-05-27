import random
import sys
import json

def gen_random_num():
    rand_int = random.randint(1000, 9999)

    return rand_int

def get_url():
    url = sys.argv[1]
    return url


fptr = open('urlmap.json')
u_map = json.load(fptr) #u_map is object in file urlmap.json
print(u_map)
url = get_url()
short_url = gen_random_num()

u_map[url] = short_url

with open('urlmap.json', 'w') as outfile:
    json.dump(u_map, outfile)
