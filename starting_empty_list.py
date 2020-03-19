#!/usr/bin/env python

print("This program starts with an empty list and add list with 'append': ")
teams = []
teams.append('Barcelona')
teams.append('Real Madrid')
teams.append('Liverpool')
teams.append('Arsenal')
print(teams)

# inserting element at a particular position #
print("\nThis program inserts element in a list at any position: ")
teams.insert(0, 'PSG')
teams.insert(3, 'Bayern Munich')
print(teams)
