numbers = [] #This main list stores input.

def calculate_average(numbers): #This function calculates the average.
    total_sum = sum(numbers)
    num_count = len(numbers)
    average = total_sum / num_count
    return average

def calculate_sum(numbers):#This function calculates the sum of numbers.
    total_sum = 0
    for number in numbers:
        total_sum += number
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
    return difference

def number_count(numbers):#This function checks the amount of digits in the list.
    count = 0
    for number in numbers:
        count += 1
    return count

def above_average(numbers, average):#This function calculates and prints all numbers above average.
    abv_avg_list = []#This stores all the numbers above average.
    for number in numbers:
        if number > average:
            abv_avg_list.append(number)
    return abv_avg_list

def below_average(numbers, average):#This function calculates and prints all numbers below average.
    below_average_list = []
    for number in numbers:
        if number < average:
            below_average_list.append(number)
    return below_average_list

def equal_average(numbers, average):#This function checks for any number equal to average.
    equal_average_list = []
    for number in numbers:
        if number == average:
            equal_average_list.append(number)
    return equal_average_list

def main():
    
    if not numbers:
            print("Your list is Empty!!")
    else:
            print("Your list is:",numbers)
            avg = calculate_average(numbers)
            calc_sum = calculate_sum(numbers)
            print("The sum is:", calc_sum)
            calc_range = calculate_range(numbers)
            print("The range is:", calc_range)
            num_count = number_count(numbers)
            print("The amount of digits entered are:", num_count)
            eql_avg = equal_average(numbers, avg)
    
            if not eql_avg:
                print("There are no numbers equal to average")
            else:
                print("Number(s) equal to average:", eql_avg)
        
            
            abv = above_average(numbers, avg)
            if not abv:
                print("No Numbers above average")
            else:
                print("These numbers are above average:", abv)

            
            below = below_average(numbers, avg)
            if not below:
                print("No numbers below average")
            else:
                print("These numbers are below average:", below)



while True: #This loop makes he program run
    choice = input("Use Add number(a) or stop(s) or analyze(z) or clear list(c)").lower()
    if choice == 'a':#This is the option that adds numbers to the list
        try:
            number = int(input("Please add a number. "))
            numbers.append(number)
        except ValueError:
            print("This is not a number.")
    elif choice == 'z':#This is the option thay analyzes numbers in the list.
        main()
    
    elif choice == 'c':#This is the option that clears the list
        numbers.clear()
        print("Your history has been cleared!!")


    elif choice == 's':#This is the option that stops the program from running.
        print("Byee .")
        break
    else:
        print("Please input a valid choice.") 
        continue


