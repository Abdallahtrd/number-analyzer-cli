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

def frequency_counter(numbers): #This function handles the frequency on numbers in the list.   
    freq = {}
    for number in numbers:
        freq.setdefault(number, 0)
        freq[number] += 1
    return freq

def duplicate_numbers(numbers):
    duplicates = {}
    duplicate_list = []
    for number in numbers:
        duplicates.setdefault(number, 0)
        duplicates[number] += 1
    for key, value in duplicates.items():
        if value >= 2:
            duplicate_list.append(key)
    return duplicate_list


    



def main():
    
    if not numbers:
            print("Your list is Empty!!")
    else: #Analyze and display statistics using all functions
            print("Your list is:",numbers)
           
            avg = calculate_average(numbers) 
            
            calc_sum = calculate_sum(numbers)
            
            calc_range = calculate_range(numbers)
            
            num_count = number_count(numbers)

            dupli_num = duplicate_numbers(numbers)
            
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

           
            sorted_list = list_sort(numbers)
            
            median_calc = calculate_median(sorted_list)
            
            nearest_average = closest_to_average(avg, numbers)
            
            count_freq = frequency_counter(numbers)
            
            
            
            results ={
                'average': avg,
                'sum' : calc_sum,
                'range' : calc_range,
                'number count' : num_count,
                'equal to average' : eql_avg,
                'above average' : abv,
                'below average' : below,
                'median' : median_calc,
                'nearest to average' : nearest_average,
                'frequency' : count_freq,
                'duplicate numbers' : dupli_num,
                
            }

            for result ,value in results.items():
                print("Your", result ,"is:", value)
    



while True: #This loop makes he program run
    choice = input("Use Add number(a) or stop(s) or analyze(z) or clear list(c)").lower()
    if choice == 'a':#This is the option that adds numbers to the list
        try:
            numbers_input = (input("Please input your numbers, Add a comma (,) after each entry: "))
            temp = ""
            for number in numbers_input:
                if number != ",":
                    temp += number
                else:
                    numbers.append(int(temp))
                    temp = ""

            if temp != "":
                numbers.append(int(temp))


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


