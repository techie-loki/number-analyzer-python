def reverse(number):
    rev = 0

    while number > 0:

        last = number % 10
        rev = rev * 10 + last
        number = number // 10

    return rev

def palindrome(number):

    original = number
    rev = 0

    while number > 0:

        last = number % 10
        rev = rev * 10 + last
        number = number // 10

    if original == rev:
        return True
    else:
        return False

def sum_num(number):
    total = 0

    while number > 0:

        last = number % 10
        total += last
        number = number // 10

    return total

def count_num(number):
    count = 0

    while number > 0:

        count += 1
        number = number // 10

    return count

while True:

    print("1. Analyze")
    print("2. Reverse")
    print("3. Palindrome")
    print("4. Sum")
    print("5. Count")
    print("6. Exit")

    option = int(input("Enter option: "))

    if option == 6:
        break

    if option in [1,2,3,4,5]:
        number = int(input("Enter the number : "))

        if option == 1:
            print("--------Analyze result-------------")
            print(f"Reverse number : {reverse(number)}")

            if palindrome(number):
                print("Palindrome : Yes")
            else:
                print("Palindrome : No")

            print(f"Sum of number : {sum_num(number)}")
            print(f"Count number : {count_num(number)}")

        elif option == 2:

            result = reverse(number)
            print("Reverse number :" , result)

        elif option == 3:

            result = palindrome(number)
            if result:
                print("Palindrome")
            else:
                print("Not palindrome")

        elif option == 4:

            result = sum_num(number)
            print(result)

        elif option == 5:

            result = count_num(number)
            print(result)

        else:
            print("Invalid option")










