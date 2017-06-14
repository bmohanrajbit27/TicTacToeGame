'''
    Env : Python3
    
    Below program gives us the details of total hundreds scored by ODI teams with player count. Basically there are no website
    that gives this detail and only way is to calculate manually by visiting each team stats page and its tedious process which 
    might take more than 15 minutes and high chance of making mistakes in manual calculation.
    
    Basically this program visit each ODI team page and collect the number of players scored hundred for that team and calculate 
    total number of hundreds scored by all players of that team. After obtain the details of all the teams, data sorted out based on the 
    total hundreds and printed as output on the terminal..
    


'''

import re, requests
from urllib.request import urlopen
import time

start_time = time.time()

# Every cricket playing team assigned a number in cricinfo website, for ex India is assigned with number 6.
value = [1,2,3,4,5,6,7,8,9,15,25,29,30,11,12,14,17,27,40]

team_dict = dict()

#functions for finding the total centuries of the team.
def cal_100(file_lis):
  #Initializing tot_hundred
  tot_hundred = 0
  #Initializing a dictionary
  team_player = dict()
  #Initializing player count
  player_count = 0
  
  for each_line in file_lis:
    team_name = re.search('<b>Primary team</b>&nbsp;([\w\s]+)<',each_line)
    if team_name:
      team_player['team name'] = team_name.group(1)
    player_name = re.search('<[\w\s="/.-]+>([\w\s]+)</a></td>',each_line)
     if player_name:
       player_count += 1 
       hundred = re.search('<td>(\d+)</td>',file_lis[file_lis.index(each_line)+10])
       team_player[player_name.group(1)] = int(hundred.group(1))
       tot_hundred = tot_hundred + team_player[player_name.group(1)]
  
  if team_player:
    return team_player['team name'],tot_hundred,player_count
  else:
    return 'empty',0,0

liss = list()

for each_value in value:
  # Fetches team page based on the team_number
  print('************'+'{:10}'.format('processing')+'************')
  url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;orderby=runs;qualmin1=1;qualval1=hundreds;size=200;team={};template=results;type=batting'.format(int(each_value))
  response = urlopen(url)
  str_content = response.read().decode('utf-8')
  lis_content = str_content.split('\n')
  team,hundred,player_count = cal_100(lis_content)
  liss.append((hundred,team,player_count))  # New code

liss.sort(reverse = True)

print('{0:40}{1:<30}{2:>10}'.format('Team','No of players','100s'))

for hundred,team,player_count in liss:
  print('{0:40}{1:<30}{2:>10}'.format(team,player_count,hundred)) 

print("--- %s seconds ---" % (time.time() - start_time))

