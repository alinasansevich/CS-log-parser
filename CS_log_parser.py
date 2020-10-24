#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:35:10 2020

@author: alina

"""

import re
import sqlite3

filename = 'hlds6_hb.log'

nameParser = re.compile(r'"(?:(.+?)<\d+?><(.+?)><(.+?)>)"')



with open(filename) as f:
    log = f.readlines()

line = 'L 10/18/2020 - 20:26:02: "1KNJ<1><XXX><TERRORIST>" killed "CHooSe<14><STEAM_0:0:540992438><CT>" with "sg552"'
line2 = 'L 10/18/2020 - 20:26:02: '

killed_lines = []
with open(filename) as f:
    for line in f:
        if 'killed' in line:
            killed_lines.append(line)

total_kills = len(killed_lines)

name_regex = re.compile(r'"(?:(.+?)<\d+?><(.+?)><(.+?)>)"')

all_m_o = []
for i in range(len(killed_lines)):
    m_o = name_regex.split(killed_lines[i])
    all_m_o.append(m_o)

con = sqlite3.connect('CS_results.db')
cur = con.cursor()

cur.execute("""
            CREATE TABLE CSResults (
            FirstPlayer TEXT NOT NULL,
            SecondPlayer TEXT NOT NULL,
            Weapon TEXT NOT NULL)
            """)



game_info = tuple()
cur.execute("""
            INSERT INTO CSResults
            VALUES (?, ?, ?)""",
            (game_info[0], game_info[1], game_info[2])




















# mo = name_regex.search(killed_lines[0]) # este no
# m_o = name_regex.split(killed_lines[0])
# mo_l = name_regex.findall(killed_lines[0]) # puede ser



























