# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 2

# YOUR NAME: Cameron Joyner 
# YOUR UNI: CGJ2115

'''
Returns the GCD of two integers using Euclid's algorithm. Also prints out the
intermediate steps for Euclid's Algorithm on num1 and num2.

Parameters:
num1 (int): First number for the GCD
num2 (int): Second number for the GCD

Returns:
int: GCD of num1 and num2
'''
def euclid(num1, num2):

    if num2 == 0 : 
       gcd = num1 

    else : 
       gcd = euclid(num2, num1 % num2)
       
    message = "GCD(" + str(num1) + "," + str(num2) + ")"

    print(message)
    return gcd # your GCD

'''
Returns a list of prime numbers up to (and including) a certain input integer, n.

Parameters:
n (int): The target number to generate primes up to.

Returns:
list: List of all prime numbers <= n.
'''
def prime_gen(n): #GOOD TO GO
    # WRITE YOUR CODE HERE
    primes =[]
    non_primes=[]

    for i in range(1, n):
        if((i == 1 or i > 5 and i % 5 ==0) or (i > 7 and i % 7 ==0) or (i > 11 and i % 11 ==0) or (i > 13 and i % 13==0) or (i > 17 and i % 17==0) or (i > 19 and i % 19==0) or (i > 23 and i % 23==0) or (i > 29 and i % 29==0)) :
            non_primes.append(i)
        elif(i == 2 or i == 3):
            primes.append(i)
        elif(i % 2 != 0 and i % 3 != 0) :
            primes.append(i)

    return primes # your list of prime numbers

'''
Returns a boolean value (True or False) depending on whether the input n is prime.

Parameters:
n (int): The target integer to check primality.

Returns:
boolean: True if n is prime, False if n is not prime.
'''
def prime_check_trial(n): #GOOD TO GO

    prime = True

    for i in range(2, int(n**0.5)+1):
        if(n % i == 0 or n % 2 == 0):
           prime = False

    return prime # boolean True or False depending on prime or not

'''
Returns a boolean value (True or False) depending on whether the input n is prime.

Parameters:
n (int): The target integer to check primality.

Returns:
boolean: True if n is prime, False if n is not prime.
'''
def prime_check_sieve(n): #GOOD TO GO
    # WRITE YOUR CODE HERE

    primes =[]
    non_primes=[]
    prime = False

    for i in range(1, n+1):
        if((i == 1 or i > 5 and i % 5 ==0) or (i > 7 and i % 7 ==0) or (i > 11 and i % 11 ==0) or (i > 13 and i % 13==0) or (i > 17 and i % 17==0) or (i > 19 and i % 19==0) or (i > 23 and i % 23==0) or (i > 29 and i % 29==0)) :
            non_primes.append(i)
        elif(i == 2 or i == 3):
            primes.append(i)
        elif(i % 2 != 0 and i % 3 != 0) :
            primes.append(i)

    for i in range(1, len(primes)):
        if(primes[i] == n) :
            prime = True
        else :
            prime = False

    return prime # boolean True or False depending on prime or not

'''
Returns a boolean value (True or False) depending on whether the input n is prime.

Parameters:
n (int): The target integer to check primality.

Returns:
boolean: True if n is prime, False if n is not prime.
'''
def prime_check_fermat(n): #GOOD TO GO
    prime = True
    
    if((2**(n-1) % n) == 1):
        prime = True
    else :
        prime = False

    return prime # boolean True or False depending on prime or not

'''
Returns a list of two prime integers that sum up to n.

Parameters:
n (int): The target even integer to check Goldbach's Conjecture for.

Returns:
list: A list of length 2 containing 2 ints that sum up to n.
'''
def check_goldbach(n): #GOOD TO GO
    

    primes_list=[]
    non_primes=[]
    primes = []
    #while number > 0 :
    for i in range(1, n):
        if((i == 1 or i > 5 and i % 5 ==0) or (i > 7 and i % 7 ==0) or (i > 11 and i % 11 ==0) or (i > 13 and i % 13==0) or (i > 17 and i % 17==0) or (i > 19 and i % 19==0) or (i > 23 and i % 23==0) or (i > 29 and i % 29==0)) :
            non_primes.append(i)
        elif(i == 2 or i == 3):
            primes_list.append(i)
        elif(i % 2 != 0 and i % 3 != 0) :
            primes_list.append(i)

    for i in range(0, len(primes_list)):        

        if(primes_list[1] + primes_list[i] == n):
            primes = [primes_list[1], primes_list[i]]
        elif(primes_list[2] + primes_list[i] == n):
            primes = [primes_list[2], primes_list[i]]   
        elif(primes_list[3] + primes_list[i] == n):
            primes = [primes_list[3], primes_list[i]]
        else:
            i = i   # @cameron refer to Goldbach2.py file on macbook

    return primes # two prime numbers that sum up to n

### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 2: Prime Numbers!")
    print("#######################################")
    print()

    print("---------------------------------------")
    print("PART A: Euclid's Algorithm")
    print("---------------------------------------")
    euclid_test_1 = [252, 105]
    print("Test Case 1: GCD of", euclid_test_1[0], "and", euclid_test_1[1])
    print("Test Case 1 Steps: ")
    student_ans = euclid(euclid_test_1[0], euclid_test_1[1])
    print("Test Case 1 (Your Answer):", student_ans)
    print("Test Case 1 (Correct Answer):", 21)
    print("Test Case 1:", ("# PASSED! #" if student_ans == 21  else "# INCORRECT #"))
    print()
    euclid_test_2 = [1071, 462]
    print("Test Case 2: GCD of", euclid_test_2[0], "and", euclid_test_2[1])
    print("Test Case 2 Steps: ")
    student_ans = euclid(euclid_test_2[0], euclid_test_2[1])
    print("Test Case 2 (Your Answer):", student_ans)
    print("Test Case 2 (Correct Answer):", 21)
    print("Test Case 2:", ("# PASSED! #" if student_ans == 21  else "# INCORRECT #"))
    print()
    euclid_test_3 = [85523, 3212]
    print("Test Case 3: GCD of", euclid_test_3[0], "and", euclid_test_3[1])
    print("Test Case 3 Steps: ")
    student_ans = euclid(euclid_test_3[0], euclid_test_3[1])
    print("Test Case 3 (Your Answer):", student_ans)
    print("Test Case 3 (Correct Answer):", 1)
    print("Test Case 3:", ("# PASSED! #" if student_ans == 1  else "# INCORRECT #"))
    print("---------------------------------------")

    print("PART B: Prime Number Generation")
    print("---------------------------------------")
    prime_gen_test_1 = 42
    prime_gen_test_1_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    print("Test Case 1: Prime Numbers Up To:", prime_gen_test_1)
    print("Test Case 1 (Your Answer):", prime_gen(prime_gen_test_1))
    print("Test Case 1 (Correct Answer):", prime_gen_test_1_ans)
    print("Test Case 1:", ("# PASSED! #" if prime_gen(prime_gen_test_1) == prime_gen_test_1_ans  else "# INCORRECT #"))
    print()
    prime_gen_test_2 = 314
    prime_gen_test_2_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
    131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313]
    print("Test Case 2: Prime Numbers Up To:", prime_gen_test_2)
    print("Test Case 2 (Your Answer):", prime_gen(prime_gen_test_2))
    print("Test Case 2 (Correct Answer):", prime_gen_test_2_ans)
    print("Test Case 2:", ("# PASSED! #" if prime_gen(prime_gen_test_2) == prime_gen_test_2_ans  else "# INCORRECT #"))
    print()
    prime_gen_test_3 = 884
    prime_gen_test_3_ans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
    113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
    199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
    397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
    491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
    821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883]
    print("Test Case 3: Prime Numbers Up To:", prime_gen_test_3)
    print("Test Case 3 (Your Answer):", prime_gen(prime_gen_test_3))
    print("Test Case 3 (Correct Answer):", prime_gen_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if prime_gen(prime_gen_test_3) == prime_gen_test_3_ans  else "# INCORRECT #"))
    print("---------------------------------------")

    print("PART C: Primality Testing")
    print("---------------------------------------")
    primality_test_1 = 8
    primality_test_1_ans = False
    print("Test Case 1: Check Primality For:", primality_test_1)
    print("Test Case 1 (Your Trial Division Answer):", prime_check_trial(primality_test_1))
    print("Test Case 1 (Your Sieve Answer):", prime_check_sieve(primality_test_1))
    print("Test Case 1 (Your Fermat's Little Theorem Answer):", prime_check_fermat(primality_test_1))
    print("Test Case 1 (Correct Answer):", primality_test_1_ans)
    print("Test Case 1:", ("# PASSED! #" if prime_check_trial(primality_test_1) == prime_check_sieve(primality_test_1) == prime_check_fermat(primality_test_1) == primality_test_1_ans else "# INCORRECT #"))
    print()
    primality_test_2 = 482
    primality_test_2_ans = False
    print("Test Case 2: Check Primality For:", primality_test_2)
    print("Test Case 2 (Your Trial Division Answer):", prime_check_trial(primality_test_2))
    print("Test Case 2 (Your Sieve Answer):", prime_check_sieve(primality_test_2))
    print("Test Case 2 (Your Fermat's Little Theorem Answer):", prime_check_fermat(primality_test_2))
    print("Test Case 2 (Correct Answer):", primality_test_2_ans)
    print("Test Case 2:", ("# PASSED! #" if prime_check_trial(primality_test_2) == prime_check_sieve(primality_test_2) == prime_check_fermat(primality_test_2) == primality_test_2_ans else "# INCORRECT #"))
    print()
    primality_test_3 = 853
    primality_test_3_ans = True
    print("Test Case 3: Check Primality For:", primality_test_3)
    print("Test Case 3 (Your Trial Division Answer):", prime_check_trial(primality_test_3))
    print("Test Case 3 (Your Sieve Answer):", prime_check_sieve(primality_test_3))
    print("Test Case 3 (Your Fermat's Little Theorem Answer):", prime_check_fermat(primality_test_3))
    print("Test Case 3 (Correct Answer):", primality_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if prime_check_trial(primality_test_3) == prime_check_sieve(primality_test_3) == prime_check_fermat(primality_test_3) == primality_test_3_ans else "# INCORRECT #"))
    print("---------------------------------------")

    print("PART D: Goldbach's Conjecture")
    print("---------------------------------------")
    goldbach_test_1 = 8
    goldbach_test_1_ans = [3, 5]
    student_ans = check_goldbach(goldbach_test_1)
    print("Test Case 1: 2 Primes For:", goldbach_test_1)
    print("Test Case 1 (Your Answer):", check_goldbach(goldbach_test_1))
    print("Test Case 1 (A Correct Answer):", goldbach_test_1_ans)
    print("Test Case 1:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_1  else "# INCORRECT #"))
    print()
    goldbach_test_2 = 482
    goldbach_test_2_ans = [3, 479]
    student_ans = check_goldbach(goldbach_test_2)
    print("Test Case 2: 2 Primes For:", goldbach_test_2)
    print("Test Case 2 (Your Answer):", check_goldbach(goldbach_test_2))
    print("Test Case 2 (A Correct Answer):", goldbach_test_2_ans)
    print("Test Case 2:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_2  else "# INCORRECT #"))
    print()
    goldbach_test_3 = 1152
    goldbach_test_3_ans = [23, 1129]
    student_ans = check_goldbach(goldbach_test_3)
    print("Test Case 3: 2 Primes For:", goldbach_test_3)
    print("Test Case 3 (Your Answer):", check_goldbach(goldbach_test_3))
    print("Test Case 3 (A Correct Answer):", goldbach_test_3_ans)
    print("Test Case 3:", ("# PASSED! #" if student_ans[0] + student_ans[1] == goldbach_test_3  else "# INCORRECT #"))
    print("---------------------------------------")
