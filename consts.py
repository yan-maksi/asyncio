from random import random
from aiohttp import web

# MAIN file
my_ip1 = "http://127.0.0.1:8080"
my_ip2 = "http://127.0.0.1:8081"
delay_one_milliseconds = 0.001

# SERVER file
eighty_eighty = 8080
eighty_eighty_one = 8081
random_number_from_one_to_ten = web.Response(text=str(random.randint(0, 10)))