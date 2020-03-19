users = []
users.append('kofi')
users.append('cassie')
users.append('ike')
users.append('kwame')
print(users)

# Sorting alist permanently #
print("\nThis program sorts list permanently using 'sort':")
users.sort()
print(users)

# Sorting a list permannetly in reverse order #
print("\nThis program sorts list permanently in 'reverse' order: ")
users.sort(reverse=True)
print(users)

# Sorting a list temporary #
print("\nThis program sorts list temporary using 'sorted': ") 
print(sorted(users))
print(sorted(users, reverse=True))

# Reversing the order of a list #
print("\nThis program reverse the order of a list: ")
users.reverse()
