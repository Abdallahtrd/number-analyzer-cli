numbers = [] #This main list stores input.

def calculate_average(numbers): #This function calculates the average.
    total_sum = sum(numbers)
    total_avg = len(numbers)
    average = total_sum / total_avg
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
            print(numbers)
            calculate_average(numbers)
            calculate_sum(numbers)
            calculate_range(numbers)
            number_count(numbers)
    elif choice == 's':
        print("Byee .")
        break
    else:
        print("Please input a valid choice.")
        continue


