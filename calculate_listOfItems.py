# Record the list of items inside a list
list_of_items = [1, 2, 3, 4]

# Initial cost will be 0
totalCost = 0

# Loop through the list and increment the initial value by adding each item to it
for eachItem in list_of_items:
    totalCost += eachItem
print(totalCost)