def get_fibonacci_list(number_of_element):
    fibonacci_list =[0,1]
    for value in range(2,number_of_element):
        fibonacci_list.append(fibonacci_list[value - 1] + fibonacci_list[value - 2])
    return fibonacci_list


def get_fibonacci_number(number_of_element):
    start, second = 0, 1
    while start < number_of_element:
        print(start, end=' ')
        start, second = second, start + second
        print()


#
# print(get_fibonacci_list(10))
# print(get_fibonacci_number(10))