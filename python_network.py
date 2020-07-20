#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:01:49 2020

@author: ahmedomar
"""

from geopy.geocoders import Nominatim


address = '207 N. Defiance St, Archbold, OH'
user_agent= 'Foundations of Python Network Programming example '
location = Nominatim(user_agent=user_agent).geocode(address)
print(location.latitude, location.longitude)


import requests

def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Foundations of Python Network Programming example search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    print(reply[0]['lat'], reply[0]['lon'])
    
    geocode('207 N. Defiance St, Archbold, OH')


import socket

hostname = 'www.python.org'
addr = socket.gethostbyname(hostname)
print('The IP address of {} is {}'.format(hostname, addr))

socket.getservbyname('bgp')

