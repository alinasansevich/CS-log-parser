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

player_1 = []
for item in all_m_o:
    player_1.append(item[1])

player_1 = list(set(player_1))

all_kills = {}
for player in player_1:
    kills = {}
    for item in all_m_o:
        if player == item[1]:
            if item[5] not in kills.keys():
                kills[item[5]] = 1
            else:
                kills[item[5]] += 1
    all_kills[player] = kills


for player, kills in all_kills.items():
    print(player, '\t', kills)
       





# players = {'ender': {'konejo': 34,
#                      'colo': 28,
#                      'coco': 65
#                      }
#            'colo': {'pepitin': 99,
#                     'ender': 22,
#                     'konejo': 74}
#            }



















con = sqlite3.connect('CS_results.db')
cur = con.cursor()

cur.execute("""
            CREATE TABLE CSResults (
            FirstPlayer TEXT NOT NULL,
            SecondPlayer TEXT NOT NULL,
            Weapon TEXT NOT NULL)
            """)

for item in all_m_o:    
    cur.execute("""
                INSERT INTO CSResults
                VALUES (?, ?, ?)""",
                (item[1], item[5], item[8][7:-2]))

cur.execute("""
            SELECT *
            FROM CSResults
            """)
cur.fetchall()

cur.execute("""
            SELECT FirstPlayer, SUM(SecondPlayer), SecondPlayer
            FROM CSResults
            GROUP BY FirstPlayer
            """)
cur.fetchall()

cur.execute("""
            SELECT COUNT(FirstPlayer)
            FROM CSResults
            GROUP BY FirstPlayer
            """)
cur.fetchall()


















# mo = name_regex.search(killed_lines[0]) # este no
# m_o = name_regex.split(killed_lines[0])
# mo_l = name_regex.findall(killed_lines[0]) # puede ser



























