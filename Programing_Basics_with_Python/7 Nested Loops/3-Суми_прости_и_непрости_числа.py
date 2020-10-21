import math

prime_sum = 0
not_prime_sum = 0
is_prime = True

while True:
    number = input()
    if number == "stop":
        break
    intiger_num = int(number)
    if intiger_num < 0:
        print(f"Number is negative.")
        continue
    else:
        end_i = math.sqrt(intiger_num)
        for num in range(2, int(end_i) + 1):
            if intiger_num / num == intiger_num // num:
                is_prime = False
            else:
                is_prime = True
        if is_prime:
            prime_sum += intiger_num
        else:
            not_prime_sum += intiger_num
    # if int(number) > 1:
    #
    #     for i in range(2, int(number)//2):
    #         if int(number) % i == 0:
    #             not_prime_sum += int(number)
    #         else:
    #             prime_sum += int(number)
    #
    # elif int(number) < 0:
    #     print(f"Number is negative.")
    #     continue
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {not_prime_sum}")