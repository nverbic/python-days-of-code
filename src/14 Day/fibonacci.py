'''
    Day 14:
    Write a program to print the first n numbers of a Fibonacci sequence

    Fibonacci:
        Fn = Fn-1 + Fn-2
        with seed values : F0 = 0 and F1 = 1.

    In Python 3, integers have unlimited precision (the available system memory)
    sys.maxsize - check maximum representable integer on the system

    Output:
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 
    121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 
    102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 
    20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 
    1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 
    72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 
    2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 
    61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 
    1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 
    31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026]

    The 100-th number in the Fibonacci seq. is:
    218922995834555169026


    Performances measured on a list of 10000 items, running code 1000 times.

    Total execution time using list: 4.5557057 seconds
    Average time per execution: 0.0045557057 seconds
'''
import timeit

PREFORMANCE_SAMPLE = 1000
NUMBER_OF_RUNS = 1000

def fibonacci_list_append(n):
    ''' Fibonacci iterative '''
    fibonacci_list = [0, 1]

    for i in range(2, n):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])

    return fibonacci_list

def fibonacci_recursive(n, fibonacci_list):
    ''' Fibonacci recursive '''
    if n > 1:
        fibonacci_recursive(n-1, fibonacci_list)
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list

def wrapper_fibonacci_list_append():
    fibonacci_list_append(PREFORMANCE_SAMPLE)

def wrapper_fibonacci_recursive():
    fibonacci_recursive(PREFORMANCE_SAMPLE, [0,1])

def measure_performance():
    ''' Measure performances '''
    execution_time_fibonacci_list_append = round(timeit.timeit(wrapper_fibonacci_list_append, number=NUMBER_OF_RUNS), 10)
    average_time_fibonacci_list_append = execution_time_fibonacci_list_append / NUMBER_OF_RUNS

    execution_time_fibonacci_recursive = round(timeit.timeit(wrapper_fibonacci_recursive, number=NUMBER_OF_RUNS), 10)
    average_time_fibonacci_recursive = execution_time_fibonacci_recursive / NUMBER_OF_RUNS

    print(f"\nPerformances measured on a list of {PREFORMANCE_SAMPLE} items, " \
          f"running code {NUMBER_OF_RUNS} times.\n")
    print(f"Total execution time using list: {execution_time_fibonacci_list_append} seconds")
    print(f"Average time per execution: {average_time_fibonacci_list_append} seconds\n")

    print(f"Total execution time using recursion: {execution_time_fibonacci_recursive} seconds")
    print(f"Average time per execution: {average_time_fibonacci_recursive} seconds\n")

if __name__ == "__main__":
    SEQUENCE_LENGTH = 100
    fibonacci_list = fibonacci_list_append(SEQUENCE_LENGTH)
    print(fibonacci_list)
    print(f"\nThe {SEQUENCE_LENGTH}-th number in the Fibonacci seq. is:\n{fibonacci_list[SEQUENCE_LENGTH-1]}\n")

    fibonacci_list = fibonacci_recursive(SEQUENCE_LENGTH - 1 , [0, 1])
    print(fibonacci_list)

    # Measure performances of different solutions
    measure_performance()
