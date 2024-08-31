# Credit Number: 371449635398431 American Express (INVALID)
# Credit Number: 5893804115457289


creditList = [] #STORES THE CREDIT NUMBER IN A LIST
numLength = 0 #STORES THE LENGTH OF THE CREDIT NUMBER
checkDigit = 0 #STORES THE CHECK DIGIT WHEN REMOVED FROM THE ARRAY.
evenNumList =[] #ADDS ALL EVEN NUMBERS INTO THIS LIST
oddNumList = [] #ADDS ALL ODD NUMBERS INTO THIS LIST
sumEven = 0 #SUM OF EVEN DIGITS
sumOdd = 0 #SUM OF ODD DIGITS
creditSum = 0  #SUM OF EVEN  / ODD / CHECK DIGIT

#Ask user for input
creditNum = input("What credit# do you wanna check: ")

#loop to put the numbers in an list and get the length of the list
for n in creditNum:
    creditList.append(int(n))
    numLength = len(creditList)

#Store Check Digit in a variable (checkDigit) and remove from the list. 
checkDigit = creditList.pop(numLength - 1) 

#Reverse the array of numbers:
creditList.reverse() 

#Loop through creditList and get all the even numbers, multiply by 2 and add to the Even Num List based on conditionals
for num in range(0, len(creditList), 2): #range(start index, end Index, jump interval)
    evenNum = 0
    x = creditList[num] * 2 #Multiply by 2, if greater >= 9 subtract 9
    if x >= 9:
        x -= 9
        evenNumList.append(x) #Then add to evenNumList
    elif x <= 9:
        evenNumList.append(x) #if Smaller than 9, add the EvenNum List

#Loop through creditList and get the odd numbers and put them in a new list oddNumList
for y in range(1, len(creditList), 2):
    z = creditList[y]
    oddNumList.append(z)
#Sum even / odd lists and add Check digit.     
sumEven = sum(evenNumList)
sumOdd = sum(oddNumList)
creditSum = sumEven + sumOdd + checkDigit

#Check if creditSum total is divisible by 10. If true, print Valid, if not, print invalid. 
if creditSum % 10 == 0: 
    print("VALID")
else:
    print("INVALID")