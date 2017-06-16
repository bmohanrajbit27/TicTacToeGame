'''
    Env : Python3
    
Algorithm

1. Import the necessary modules for this program - re,urlopen,time
2. Initialize the list value = [1,2,3,4,5,6,7,8,9,15,25,29,30,11,12,14,17,27,40]
3. Initialize a list - list_of_teams which in final will contain list of tuples where each tuple contain the total_hundred,team name and player count.
4. for each value in value
     Based on the value open the appropriate website.
     Decode the website data from byte to string(html page of the website).
     split the very long string of HTML page based on new_line('\n) which in turn will produce a list contains each line of the HTML page.
     call the function cal_100(lis_content)(step 5) with the generated list to retrieve the team name, player count, total hundreds scored by that particular team
     After retrieving the data append the result to the list list_of_teams.
     continue the loop untill no more value in the value list..
5  cal_100(file_lis)
     Initialize a local variable tot_hundred
     Initialize a local variable team_player which is a dictionary for saving team details..
     Initialize a local variable for counting the payers.
     for each_line in file_lis
       Using regular expression team name, player count and total hundred are retrieved and stored in the dictionary team_player
       Exit the loop after crawled each line of the website
     return the team name, player count and total hundred value
6. sort the list list_of_teams and print the output value..


'''

import re
from urllib.request import urlopen
import time
start_time = time.time()

# Every cricket playing team assigned a number in cricinfo cricket, for ex India number is 6
value = [1,2,3,4,5,6,7,8,9,15,25,29,30,11,12,14,17,27,40]
list_of_teams = list()

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


for each_value in value:
  # Fetches team page based on the team_number
  print('************'+'{:10}'.format('processing')+'************')
  url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;orderby=runs;qualmin1=1;qualval1=hundreds;size=200;team={};template=results;type=batting'.format(int(each_value))
  response = urlopen(url)
  str_content = response.read().decode('utf-8')
  lis_content = str_content.split('\n')
  team,hundred,player_count = cal_100(lis_content)
  list_of_teams.append((hundred,team,player_count))  # New code

list_of_teams.sort(reverse = True)
print('{0:40}{1:<30}{2:>10}'.format('Team','No of players','100s'))
for hundred,team,player_count in list_of_teams:
  print('{0:40}{1:<30}{2:>10}'.format(team,player_count,hundred)) 
print("--- %s seconds ---" % (time.time() - start_time))

