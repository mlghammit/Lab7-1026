# # # Question 1

numbers = []
while len(numbers) < 10:
    new_number = int(input("Enter a number: "))
    if new_number not in numbers:
        numbers.append(new_number)

print(numbers)

# # # Question 2
def ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count

# # # Question 3
values = [1,2,3,4,5]
newValues = values.copy()
for i in range(len (values)): #Remove +1 clean spacing
    newValues[i] +=1 #change to newValues to add 1
    print ("Old Value at index {} is: {} ". format(i, values[i])) #prints newValues twice
    print ("New Value at index {} is: {} \n".format (i, newValues[i]))
