def reverse_string(string):
    '''
    Reverse string using naive method

    Time: O(n)
    Space: O(n)
    '''

    
    right = len(string) - 1
    new_string = ''
    while right >= 0:
        new_string = new_string + string[right]
        right -= 1

    return new_string

def reverse_string_recursion(string):
    '''
    Reverse string using recursion

    Time: O(n)
    Space: O(n)
    '''
    length = len(string)
    if length == 0 or length == 1:
        return string
    else:
        string = reverse_string_recursion(string[1:]) + string[0]
        return string

if __name__ == '__main__':
    print(reverse_string('Hello World!'))
    print(reverse_string_recursion('Hello World'))


