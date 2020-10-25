#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:35:10 2020

@author: alina

"""

import re
import sqlite3

filename = 'hlds6_hb.log'

# with open(filename) as f:
#     log = f.readlines()

with open(filename) as f:
    counter = 0
    start_line = []
    end_line = []
    for line in f:
        counter += 1
        if 'Started map' in line:
            start_line.append(counter)
        if 'changelevel' in line:
            end_line.append(counter)

killed_lines = []
with open(filename) as f:
    counter = 0
    for line in f:
        counter += 1
        if 455 < counter < 1162:
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
            CREATE TABLE Kills (
            FirstPlayer TEXT NOT NULL,
            SecondPlayer TEXT NOT NULL,
            Weapon TEXT NOT NULL)
            """)

for item in all_m_o:    
    cur.execute("""
                INSERT INTO Kills
                VALUES (?, ?, ?)""",
                (item[1], item[5], item[8][7:-2]))
con.commit()

# View complete table
cur.execute("""
            SELECT *
            FROM Kills
            """)
cur.fetchall()

# how many kills a player had
cur.execute("""
            SELECT FirstPlayer, COUNT(FirstPlayer)
            FROM Kills
            GROUP BY FirstPlayer
            ORDER BY COUNT(FirstPlayer) DESC
            """)
cur.fetchall()

# how many times a player was killed
cur.execute("""
            SELECT SecondPlayer, COUNT(SecondPlayer)
            FROM Kills
            GROUP BY SecondPlayer
            ORDER BY COUNT(SecondPlayer) DESC
            """)
cur.fetchall()

# how many times a player killed every other player
cur.execute("""
            SELECT FirstPlayer, SecondPlayer, COUNT(*) as NumKills
            FROM Kills
            GROUP BY FirstPlayer, SecondPlayer
            ORDER BY FirstPlayer, NumKills DESC
            """)
cur.fetchall()
# thank you StackOverflow!!!!!!!!!!!!!!!!!!!!























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

player_totals = {}
for player, kills in all_kills.items():
    counter = 0
    for value in kills.values():
        counter += value
    player_totals[player] = counter
    #print(player, '\t', kills)

player_totals_sorted = {k: v for k, v in sorted(player_totals.items(),
                                                key=lambda item: item[1],
                                                reverse=True)}

player_totals_list = {}
for player in player_totals_sorted.keys():
    num_per_player = []
    for player in player_totals_sorted.items():
        all_kills[player]
    # ESTOY ACA

all_kills
Sut      {'Ghydium': 3, 'Marca': 3, 'Claudia Palópoli': 1, 'Dr. Kamper': 3, 'colo': 1, 'Ender': 1}
Ender    {'1KNJ': 22, 'Ghydium': 26, 'Claudia Palópoli': 7, 'Marca': 6, 'Evilpac': 29, 'Sut': 11, 'colo': 13, 'CHooSe': 6}
1KNJ     {'Ender': 14, 'colo': 11, 'Evilpac': 12, 'Sut': 4, 'Marca': 11, 'Claudia Palópoli': 26, 'Ghydium': 14, 'Dr. Kamper': 20, 'CHooSe': 56}
Ghydium  {'Evilpac': 13, 'Ender': 34, 'colo': 16, 'Sut': 6, '1KNJ': 11, 'Claudia Palópoli': 25, 'Marca': 8, 'Dr. Kamper': 28, 'CHooSe': 21}
Evilpac  {'1KNJ': 13, 'Ghydium': 6, 'Claudia Palópoli': 14, 'Marca': 10, 'colo': 15, 'Ender': 26, 'Sut': 3, 'Dr. Kamper': 14, 'CHooSe': 14}
Marca    {'colo': 11, 'Sut': 8, '1KNJ': 8, 'Claudia Palópoli': 3, 'Evilpac': 7, 'Ender': 1, 'Ghydium': 4}
Dr. Kamper{'Ghydium': 21, 'Evilpac': 16, '1KNJ': 17, 'Sut': 11, 'Claudia Palópoli': 4, 'colo': 11, 'Ender': 7, 'CHooSe': 2}
CHooSe   {'1KNJ': 22, 'Ender': 2, 'Evilpac': 10, 'Marca': 1, 'Ghydium': 7, 'Sut': 2, 'Claudia Palópoli': 5, 'colo': 5, 'Dr. Kamper': 2}
colo     {'Claudia Palópoli': 19, '1KNJ': 7, 'Evilpac': 4, 'Ghydium': 13, 'Marca': 2, 'Ender': 10, 'Sut': 7, 'Dr. Kamper': 4, 'CHooSe': 7}
Claudia Palópoli {'Evilpac': 12, 'Sut': 8, 'Ender': 9, '1KNJ': 21, 'colo': 12, 'Marca': 2, 'Ghydium': 14, 'CHooSe': 2, 'Dr. Kamper': 1}


player_totals_sorted
Out[13]: 
{'1KNJ': 168,
 'Ghydium': 162,
 'Ender': 120,
 'Evilpac': 115,
 'Dr. Kamper': 89,
 'Claudia Palópoli': 81,
 'colo': 73,
 'CHooSe': 56,
 'Marca': 42,
 'Sut': 12}














# ver con H:
len(start_line)
Out[70]: 15

len(end_line)
Out[71]: 22

cur.execute("""
            SELECT *
            FROM Kills
            """)
cur.fetchall()
Out[72]: 
[('Ender', 'Ghydium', 'glock18'),
 ('colo', 'Claudia Palópoli', 'glock18'),
 ('colo', 'Evilpac', 'glock18'),
 ('Claudia Palópoli', 'Sut', 'mp5navy'),
 ('colo', 'Ghydium', 'ak47'),
 ('1KNJ', 'Evilpac', 'galil'),
 ('colo', 'Claudia Palópoli', 'ak47'),
 ('Ender', 'Marca', 'ak47'),
 ('Ender', 'Evilpac', 'ak47'),
 ('colo', 'Ghydium', 'ak47'),
 ('Claudia Palópoli', 'Sut', 'mp5navy'),
 ('Claudia Palópoli', 'Ender', 'mp5navy'),
 ('Claudia Palópoli', '1KNJ', 'mp5navy'),
 ('Ghydium', 'Ender', 'famas'),
 ('colo', 'Ghydium', 'ak47'),
 ('Claudia Palópoli', 'colo', 'mp5navy'),
 ('1KNJ', 'Sut', 'galil'),
 ('Evilpac', '1KNJ', 'deagle'),
 ('Claudia Palópoli', 'Ender', 'ak47'),
 ('Claudia Palópoli', '1KNJ', 'ak47'),
 ('Ghydium', 'Sut', 'famas'),
 ('colo', 'Claudia Palópoli', 'ak47'),
 ('colo', 'Ghydium', 'ak47'),
 ('Evilpac', 'colo', 'galil'),
 ('Ghydium', 'colo', 'm4a1'),
 ('Ghydium', 'Sut', 'm4a1'),
 ('Ghydium', '1KNJ', 'm4a1'),
 ('Ender', 'Ghydium', 'm3'),
 ('Ender', 'Claudia Palópoli', 'm4a1'),
 ('Evilpac', 'Ender', 'galil'),
 ('Ender', 'Claudia Palópoli', 'ak47'),
 ('Ender', 'Evilpac', 'ak47'),
 ('colo', 'Ghydium', 'galil'),
 ('1KNJ', 'Marca', 'galil'),
 ('Ender', 'Ghydium', 'ak47'),
 ('colo', 'Claudia Palópoli', 'galil'),
 ('Evilpac', 'colo', 'm4a1'),
 ('1KNJ', 'Evilpac', 'galil'),
 ('1KNJ', 'Claudia Palópoli', 'galil'),
 ('Ghydium', 'Ender', 'usp'),
 ('1KNJ', 'Ghydium', 'galil'),
 ('Evilpac', '1KNJ', 'deagle'),
 ('Evilpac', 'colo', 'deagle'),
 ('Evilpac', 'Sut', 'ak47'),
 ('Evilpac', 'Ender', 'ak47'),
 ('1KNJ', 'Evilpac', 'galil'),
 ('colo', 'Claudia Palópoli', 'mp5navy'),
 ('Ghydium', 'colo', 'mp5navy'),
 ('1KNJ', 'Marca', 'galil'),
 ('Sut', 'Ghydium', 'ump45'),
 ('colo', 'Claudia Palópoli', 'ak47'),
 ('1KNJ', 'Evilpac', 'galil'),
 ('Marca', 'colo', 'deagle'),
 ('Sut', 'Marca', 'ump45'),
 ('Sut', 'Ghydium', 'ump45'),
 ('1KNJ', 'Marca', 'galil'),
 ('colo', 'Ghydium', 'ak47'),
 ('colo', 'Claudia Palópoli', 'glock18'),
 ('Evilpac', '1KNJ', 'm4a1'),
 ('Ender', 'Evilpac', 'ak47'),
 ('Evilpac', 'Ender', 'deagle'),
 ('colo', 'Marca', 'ak47'),
 ('Claudia Palópoli', 'Sut', 'm4a1'),
 ('Claudia Palópoli', 'colo', 'm4a1'),
 ('1KNJ', 'Claudia Palópoli', 'galil'),
 ('Ghydium', '1KNJ', 'ak47'),
 ('Claudia Palópoli', 'Ender', 'm4a1'),
 ('1KNJ', 'Ghydium', 'galil'),
 ('1KNJ', 'Claudia Palópoli', 'galil'),
 ('Evilpac', 'colo', 'm4a1'),
 ('1KNJ', 'Evilpac', 'galil'),
 ('Ghydium', 'Ender', 'glock18'),
 ('Evilpac', '1KNJ', 'glock18'),
 ('Evilpac', 'colo', 'glock18'),
 ('Claudia Palópoli', 'Marca', 'glock18'),
 ('Claudia Palópoli', 'Sut', 'deagle'),
 ('Evilpac', 'colo', 'glock18'),
 ('1KNJ', 'Claudia Palópoli', 'usp'),
 ('Ghydium', '1KNJ', 'glock18'),
 ('Ender', 'Evilpac', 'usp'),
 ('Ghydium', 'Ender', 'glock18'),
 ('Ender', 'Evilpac', 'deagle'),
 ('Ghydium', 'colo', 'p90'),
 ('Ender', 'Marca', 'ak47'),
 ('Ender', 'Ghydium', 'ak47'),
 ('colo', 'Evilpac', 'famas'),
 ('colo', 'Ghydium', 'famas'),
 ('Marca', 'Sut', 'mac10'),
 ('Marca', 'colo', 'ump45'),
 ('Ender', 'Marca', 'ak47'),
 ('colo', 'Marca', 'famas'),
 ('Claudia Palópoli', 'colo', 'ak47'),
 ('Ghydium', 'Ender', 'ump45'),
 ('Claudia Palópoli', '1KNJ', 'ak47'),
 ('Ghydium', 'Sut', 'ump45'),
 ('Claudia Palópoli', 'Ender', 'ak47'),
 ('Marca', 'Sut', 'ak47'),
 ('1KNJ', 'Evilpac', 'm4a1'),
 ('colo', 'Claudia Palópoli', 'usp'),
 ('Marca', 'colo', 'ak47'),
 ('1KNJ', 'Ghydium', 'm4a1'),
 ('1KNJ', 'Marca', 'm4a1'),
 ('Ender', 'Marca', 'awp'),
 ('colo', 'Claudia Palópoli', 'm4a1'),
 ('Ender', 'Ghydium', 'awp'),
 ('Evilpac', 'Sut', 'ak47'),
 ('Evilpac', '1KNJ', 'ak47'),
 ('Ender', 'Evilpac', 'awp'),
 ('Evilpac', 'Ender', 'ak47'),
 ('Marca', 'colo', 'deagle'),
 ('1KNJ', 'Ghydium', 'm4a1'),
 ('Marca', 'Sut', 'm4a1'),
 ('Marca', '1KNJ', 'm4a1'),
 ('Claudia Palópoli', 'colo', 'mp5navy'),
 ('Claudia Palópoli', 'Marca', 'mp5navy'),
 ('Ghydium', 'Ender', 'm4a1'),
 ('1KNJ', 'Ghydium', 'm4a1'),
 ('1KNJ', 'Claudia Palópoli', 'm4a1'),
 ('Evilpac', 'Sut', 'ak47'),
 ('1KNJ', 'Evilpac', 'm4a1'),
 ('Evilpac', 'colo', 'ak47'),
 ('Ender', 'Ghydium', 'm4a1'),
 ('Ender', 'Claudia Palópoli', 'm4a1'),
 ('Marca', 'Sut', 'ak47'),
 ('1KNJ', 'Marca', 'm4a1'),
 ('1KNJ', 'Evilpac', 'm4a1'),
 ('Ender', 'Evilpac', 'm4a1'),
 ('colo', 'Claudia Palópoli', 'famas'),
 ('Ghydium', 'colo', 'deagle'),
 ('Ghydium', 'Ender', 'ak47'),
 ('Ghydium', 'Sut', 'ak47'),
 ('Marca', '1KNJ', 'ak47'),
 ('Sut', 'Marca', 'grenade'),
 ('Ghydium', '1KNJ', 'ak47'),
 ('Marca', 'Sut', 'ak47'),
 ('Evilpac', 'Ender', 'ak47'),
 ('Evilpac', 'colo', 'ak47'),
 ('Claudia Palópoli', 'Sut', 'ak47'),
 ('Ender', 'Evilpac', 'm3'),
 ('1KNJ', 'Claudia Palópoli', 'm4a1'),
 ('Ghydium', 'Ender', 'ak47'),
 ('Marca', 'colo', 'ak47'),
 ('1KNJ', 'Ghydium', 'm4a1'),
 ('1KNJ', 'Evilpac', 'm4a1'),
 ('Claudia Palópoli', '1KNJ', 'ak47'),
 ('Ghydium', 'Ender', 'ak47'),
 ('Marca', 'colo', 'ak47'),
 ('Marca', 'Claudia Palópoli', 'ak47'),
 ('Ghydium', 'Sut', 'ak47'),
 ('colo', 'Evilpac', 'famas'),
 ('Claudia Palópoli', 'colo', 'ak47'),
 ('Ender', 'Claudia Palópoli', 'm3'),
 ('Ender', 'Ghydium', 'm3'),
 ('Marca', 'Sut', 'ak47'),
 ('1KNJ', 'Marca', 'm4a1'),
 ('1KNJ', 'Marca', 'm4a1'),
 ('Ghydium', 'colo', 'ak47'),
 ('Ender', 'Claudia Palópoli', 'ak47'),
 ('1KNJ', 'Evilpac', 'knife'),
 ('Ghydium', 'Ender', 'ak47'),
 ('Ghydium', '1KNJ', 'ak47'),
 ('Sut', 'Ghydium', 'ump45'),
 ('Marca', 'colo', 'ak47'),
 ('Ghydium', 'Sut', 'ak47'),
 ('Ghydium', 'Ender', 'ak47'),
 ('Evilpac', '1KNJ', 'ak47'),
 ('Ghydium', 'Ender', 'ak47'),
 ('Claudia Palópoli', 'colo', 'ak47'),
 ('1KNJ', 'Claudia Palópoli', 'deagle'),
 ('Marca', '1KNJ', 'ak47'),
 ('colo', '1KNJ', 'usp'),
 ('colo', 'Ender', 'usp')]

cur.execute("""
            SELECT FirstPlayer, COUNT(FirstPlayer)
            FROM Kills
            GROUP BY FirstPlayer
            ORDER BY COUNT(FirstPlayer) DESC
            """)
cur.fetchall()
Out[73]: 
[('1KNJ', 31),
 ('Ghydium', 28),
 ('colo', 24),
 ('Ender', 24),
 ('Evilpac', 22),
 ('Claudia Palópoli', 21),
 ('Marca', 17),
 ('Sut', 5)]

cur.execute("""
            SELECT SecondPlayer, COUNT(SecondPlayer)
            FROM Kills
            GROUP BY SecondPlayer
            ORDER BY COUNT(SecondPlayer) DESC
            """)
cur.fetchall()
Out[74]: 
[('colo', 26),
 ('Ghydium', 23),
 ('Claudia Palópoli', 23),
 ('Ender', 22),
 ('Sut', 21),
 ('Evilpac', 21),
 ('1KNJ', 19),
 ('Marca', 17)]

cur.execute("""
            SELECT FirstPlayer, SecondPlayer, COUNT(*) as NumKills
            FROM Kills
            GROUP BY FirstPlayer, SecondPlayer
            ORDER BY FirstPlayer, NumKills DESC
            """)
cur.fetchall()
Out[75]: 
[('1KNJ', 'Evilpac', 10),
 ('1KNJ', 'Marca', 7),
 ('1KNJ', 'Claudia Palópoli', 7),
 ('1KNJ', 'Ghydium', 6),
 ('1KNJ', 'Sut', 1),
 ('Claudia Palópoli', 'colo', 6),
 ('Claudia Palópoli', 'Sut', 5),
 ('Claudia Palópoli', 'Ender', 4),
 ('Claudia Palópoli', '1KNJ', 4),
 ('Claudia Palópoli', 'Marca', 2),
 ('Ender', 'Evilpac', 8),
 ('Ender', 'Ghydium', 7),
 ('Ender', 'Claudia Palópoli', 5),
 ('Ender', 'Marca', 4),
 ('Evilpac', 'colo', 8),
 ('Evilpac', '1KNJ', 6),
 ('Evilpac', 'Ender', 5),
 ('Evilpac', 'Sut', 3),
 ('Ghydium', 'Ender', 12),
 ('Ghydium', 'Sut', 6),
 ('Ghydium', 'colo', 5),
 ('Ghydium', '1KNJ', 5),
 ('Marca', 'colo', 7),
 ('Marca', 'Sut', 6),
 ('Marca', '1KNJ', 3),
 ('Marca', 'Claudia Palópoli', 1),
 ('Sut', 'Ghydium', 3),
 ('Sut', 'Marca', 2),
 ('colo', 'Claudia Palópoli', 10),
 ('colo', 'Ghydium', 7),
 ('colo', 'Evilpac', 3),
 ('colo', 'Marca', 2),
 ('colo', 'Ender', 1),
 ('colo', '1KNJ', 1)]



















# mo = name_regex.search(killed_lines[0]) # este no
# m_o = name_regex.split(killed_lines[0])
# mo_l = name_regex.findall(killed_lines[0]) # puede ser



























