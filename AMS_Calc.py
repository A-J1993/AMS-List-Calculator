# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:46:08 2018

@author: ali-j
"""

'''
Python 3.6
This is a program that calculates apportionment of seats based on the D'Hondt \
method of Proportional Representation within an Additional Member System \
framework.
'''

import numpy as np
from matplotlib import pyplot as plt

candidates = []
votes = []
const_seats = []
list_seats = []

seats_to_fill = int(input("How many seats to fill: "))
seats_filled = 0

party_lists = int(input("How many party lists are there in this count: "))
print()
print("For the purposes of this calculator please input any Independent candidates \
or lists with only one person either as \'Independent\' or \'Ind\'")

def add_vote(integer):
    votes = float(input("How many votes did the " + str(candidate_i) + " list recieve: "))
    return votes

def add_const_seat():
    const_seat = int(input("How many constituency seats did the party/group win: "))
    return const_seat

def total_seats_count(np_const_seats, np_list_seats):
    total_seats = np_const_seats + np_list_seats
    return total_seats

for i in range(party_lists):
    candidate_i = input("Input list " + str(i + 1) +  " : ")
    try:
        votes_i = add_vote(i)
    except ValueError:
        print("That is not a number. Please Try again:")
        votes_i = add_vote(i)
    candidates.append(candidate_i)
    try:
        votes.append(votes_i)
    except ValueError:
        print("That is not a number. Please Try again:")
        votes.append(votes_i)
    try:
        const_seat_i = add_const_seat()
    except:
        print("That is not a number. Please Try again:")
        const_seat_i = add_const_seat()
    const_seats.append(const_seat_i)
    list_seats.append(0)

question = input("Have there been any candidates or groups who won constituency\
 seats but did not stand in the lists? Please click \"Y\" if so: ")
if (question == "Y" or question == "y"):
    other_seats = add_const_seat()
else:
    other_seats = 0    
    
np_candidates = np.array(candidates)
np_votes = np.array(votes)
np_list_seats = np.array(list_seats)
np_const_seats = np.array(const_seats)

print(np_const_seats)
print()

print("I, the Acting Returning Officer, hereby give notice that the total \
number of seats and list votes given for each candidate at the election was as follows: \n")
for i in range(len(np_candidates)):
    print(str(np_candidates[i]) + ": " + str(np_const_seats[i]) + " constituenc\
y seats and "  + str(np_votes[i]) + " list votes")
    if ((i == len(np_candidates)-1) & other_seats != 0):
        print("Other candidates who did not contest on the list: " + str(other_seats))
print()

if (other_seats != 0):
    np_votes = np.append(np_votes, [0])
    np_list_seats= np.append(np_list_seats, [0])
    np_const_seats = np.append(np_const_seats, other_seats)
    np_candidates = np.append(np_candidates, ["Constituency Only Seats"])

while(seats_filled < seats_to_fill):
    criterion = np.array(np_votes)
    for i in range(len(np_candidates)):
        if((np_candidates[i].upper() == 'IND' or np_candidates[i].upper() == "INDEPENDENT") and (np_list_seats[i] == 1)):
            criterion[i] = 0
    criterion = criterion / (1 + np_list_seats + np_const_seats)
    max_index = np.argmax(criterion)
    np_list_seats[max_index] += 1
    seats_filled += 1


print("And that the following seats have been duly granted to each list in \
this region: \n")
for i in range(len(np_candidates)):
    if (np_candidates[i] != "Constituency Only Seats"):
        if(np_list_seats[i] != 0 ):
            print(str(np_candidates[i]) + ": " + str(np_list_seats[i]))

print()
total_seats = np_list_seats + np_const_seats

print("Hence the total seats granted in this election is a follows")
for i in range(len(np_candidates)):
            print(str(np_candidates[i]) + ": " + str(total_seats[i]))


ask_pie = input("Do you want to see a chart of the results? If so push \"Y\" If not hit any other key: ")
if (ask_pie == "Y" or ask_pie == "y"):
    plt.pie(np_votes)
    plt.legend(np_candidates)
    plt.title("Share of the votes")
    plt.show()
    plt.clf()
    
    plt.pie(np_const_seats)
    plt.legend(np_candidates)
    plt.title("Share of the Constituency Seats")
    plt.show()
    plt.clf()
    
    plt.pie(np_list_seats)
    plt.legend(np_candidates)
    plt.title("Share of the List Seats")
    plt.show()
    plt.clf()
    
    plt.pie(total_seats)
    plt.legend(np_candidates)
    plt.title("Share of the Total Seats")
    plt.show()
"""
    plt.pie(np_seats)
    plt.legend(np_candidates)
    plt.title("Share of the Seats")
    plt.show()
    plt.clf()
    plt.pie(np_votes)
    plt.legend(np_candidates)
    plt.title("Share of the votes")
    plt.show()
    """