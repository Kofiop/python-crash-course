mobiles = []
mobiles.append('samsung')
mobiles.append('iphone')
mobiles.append('motorola')
mobiles.append('lg')
mobiles.append('oneplus')
print(mobiles)

# To delete an element from a list #
print("\nThis program deletes and element from a list using 'del': ")
# deleting item by its position #
del mobiles[-2]
print(mobiles)


# To remove an elements from a list #
print("\nThis program removes and element from a list using 'remove': ")
# removing an item by its  value #
mobiles.remove('motorola')
print(mobiles)
