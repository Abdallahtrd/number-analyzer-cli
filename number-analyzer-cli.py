numbers = [] #This main list stores input.

def calculate_average(numbers): #This function calculates the average.
    total_sum = sum(numbers)
    num_count = len(numbers)
    average = total_sum / num_count
    print("Your average is ", average)
    return average

def calculate_sum(numbers):#This function calculates the sum of numbers.
    total_sum = 0
    for number in numbers:
        total_sum += number
    print("Your sum is", total_sum)
    return total_sum 
    
def calculate_range(numbers):#This function calculates the difference (range).
    max_num = numbers[0]
    min_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
    difference = max_num - min_num
    print("Your range is", difference)
    return difference

def number_count(numbers):#This function checks the amount of digits in the list.
    count = 0
    for number in numbers:
        count += 1
    print("Total numbers entered", count)
    return count

def above_average(numbers, average):#This function calculates and prints all numbers above average.
    abv_avglist = []#This stores all the numbers above average.
    for number in numbers:
        if number > average:
            abv_avglist.append(number)
    return abv_avglist

def below_average(numbers, average):
    below_average = []
    for number in numbers:
        if number < average:
            below_average.append(number)
    return below_average


    


  
while True: #This loop makes he program run
    choice = input("Add number(a) or stop(s) or analyze(z)? ").lower()
    if choice == 'a':
        try:
            number = int(input("Please add a number. "))
            numbers.append(number)
        except ValueError:
            print("This is not a number.")
    elif choice == 'z':
        if not numbers:
            print("Your list is Empty!!")
        else:
            print("Your list is:",numbers)
            avg = calculate_average(numbers)
            calculate_sum(numbers)
            calculate_range(numbers)
            number_count(numbers)
            #
            abv = above_average(numbers, avg)
            print("These numbers are above average:", abv)
            #
            below = below_average(numbers, avg)
            print("These numbers are below average:", below)
    elif choice == 's':
        print("Byee .")
        break
    else:
        print("Please input a valid choice.")
        continue


