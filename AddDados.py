import csv 
import os

# open the file in the write mode

fileExist = os.path.isfile('dados.csv')
  
f = open('dados.csv', 'a', newline='') if fileExist else open('dados.csv', 'w', newline='')
# create the csv writer
writer = csv.writer(f)
  
if not fileExist:
    header = ['Team1', 'Team2', '1x', '2x', 'Result'] 
    # write the header
    writer.writerow(header)

awnser = input("Want to save a new row? 1 - add, 2 - exit:")

while (awnser == '1') :

    nameTeam1 = input("Name Team 1?")
    nameTeam2 = input("Name Team 2?")
    odd1x = input("1x odd?")
    odd2x = input("2x odd?")

    writer.writerow([nameTeam1, nameTeam2, odd1x, odd2x, ''])

    awnser = input("Want to save a new row? 1 - add, 2 - exit:")
  
# close the file
f.close()
