numbers = []
def calculate_average(numbers):
    total_sum = sum(numbers)
    total_avg = len(numbers)
    average = total_sum / total_avg
    print("Your average is ", average)
    return average

def calculate_sum():
    total_sum = sum(numbers)
    print("Your sum is ", total_sum)
    return total_sum




while True:
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
            calculate_average(numbers)
    elif choice == 's':
        print("Byee .")
        break
    else:
        print("Please input a valid choice.")
        continue


