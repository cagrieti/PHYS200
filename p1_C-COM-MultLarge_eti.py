print("Welcome To The Number Cruncher! Here, you can multiply numbers with a lot of digits!")

while True:
    number1 = input("Please type in your first number: ")
    number2 = input("Please type the second number that you'd like to multiply now: ")
    n1_list = list(number1) #turn the numbers into lists
    n2_list = list(number2)

    if int(n1_list[0]) == 0 or int(n2_list[0]) == 0:
        print("Numbers cannot start with zero.")
    else:
        break

#the project wants me to multiply two 30-digit numbers but i will write a programme
#so that it will multiply any number with any other number regardless of its digits

n1 = []
n2 = []
for i in n1_list:  #turning the string values into integers (creating two lists that stores digits as integers)
    n1.append(int(i))
for m in n2_list:
    n2.append(int(m))

n1.reverse() # I am reversing the lists so that I can use the for loop for increasing i and m values
n2.reverse() # very right digit of the number will be the first element of the list!

reverse_multlarge = [0] * (len(n1) + len(n2)) #maximum nunmber of digits that the product of a multiplication can have is equal to the addition
                                               #of the number of digits which multiplicand and multiplier have
                                                # hence, i created such a list with digits that are holding the value "0"

for x in range(len(n1)): 
    hold = 0
    for y in range(len(n2)):
        a = n1[x] * n2[y] #multiply each digit one by one (no multiplication bigger than 9x9)
        reverse_multlarge[y+x] = int(reverse_multlarge[y+x]) + a%10 + hold  # a%10 gives us the value which we need to update on our reverse_multlarge list
        hold = a//10 #the number that we will hold and add to the upper digit later (e.g. if the multiplication gave us 13, number 1 will be added to the next digit)

        if y == len(n2)-1: #before the x value increases by one, we add the last holded number to our list as well
             reverse_multlarge[y+x+1] = int(reverse_multlarge[y+x+1]) + hold 

        if int(reverse_multlarge[y+x])//10 > 0: #if one of the "digits" in our list is more than 9, we move the tens digit to the upper digit as well just like as if we were solving on paper
            reverse_multlarge[y+x+1] = int(reverse_multlarge[y+x+1]) + int(reverse_multlarge[y+x])//10 
            reverse_multlarge[y+x] = int(reverse_multlarge[y+x])%10

reverse_multlarge.reverse() #because our list is keeping track of the digits from left to right, we will reverse it in order to get our number
multlarge = []
multlarge = reverse_multlarge

multiplication = 0

for number in multlarge: #take all the values of our multlarge list and add them next to each other in order to turn it into a single final number
    multiplication = str(multiplication) + str(number)
print(int(multiplication))
