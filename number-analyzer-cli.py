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

def list_sort(numbers):#This sorts the numbers list to pass into the median
    sorted_numbers = sorted(numbers)     
    return sorted_numbers
        
    
def calculate_median(numbers):#This calculates the median 
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2  - 1] + numbers[len(numbers) // 2]) / 2
        return median
    else:
        median = numbers[len(numbers) // 2]
        return median
    
def closest_to_average(average, numbers):#This function finds the number closest to the average number
    closest_number = 0
    closest_distance = float("inf")
    for number in numbers:
        distance = abs(number - average)
        if distance < closest_distance:
            closest_number = number
            closest_distance = distance
        elif distance == closest_distance:
            closest_number = number
            closest_distance = distance
        
    return closest_number

def frequency_counter(numbers):
    freq = {}
    for number in numbers:
        freq.setdefault(number, 0)
        freq[number] += 1
    return freq



def main():
    
    if not numbers:
            print("Your list is Empty!!")
    else: #Analyze and display statistics using all functions
            print("Your list is:",numbers)
            avg = calculate_average(numbers)
            print("Your average is:", avg)
            print("-----------------------------------")
            calc_sum = calculate_sum(numbers)
            print("The sum is:", calc_sum)
            print("-----------------------------------")
            calc_range = calculate_range(numbers)
            print("The range is:", calc_range)
            print("-----------------------------------")
            num_count = number_count(numbers)
            print("The amount of digits entered are:", num_count)
            print("-----------------------------------")
            eql_avg = equal_average(numbers, avg)
            if not eql_avg:
                print("There are no numbers equal to average")
            else:
                print("Number(s) equal to average:", eql_avg)
        
            print("-----------------------------------")
            
            abv = above_average(numbers, avg)
            if not abv:
                print("No Numbers above average")
            else:
                print("These numbers are above average:", abv)

            print("-----------------------------------")
            
            below = below_average(numbers, avg)
            if not below:
                print("No numbers below average")
            else:
                print("These numbers are below average:", below)

            print("-----------------------------------")
            sorted_list = list_sort(numbers)
            print("This is your sorted list:", sorted_list)
            

            print("-----------------------------------")

            median_calc = calculate_median(sorted_list)
            print("Your median is:", median_calc)

            print("-----------------------------------")

            nearest_average = closest_to_average(avg, numbers)
            print("The number closest to average is:", nearest_average)

            print("-----------------------------------")
            
            count_freq = frequency_counter(numbers)
            print("The Frequency of digits are:", count_freq)
    



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


