string to array?
def reverse_string():
# Reverse string using naive method
    right = len.string
    while right >= 0:
        left = 0
        string[right]
        new_string.len(right)
        new_string[left] = string[right]
        left += 1
        right -= 1

    return new_string

def reverse_string_recursion(string):
    length = len(string)
    if length == 0 or length == 1:
        return string
    else:
        string = reverse_string_recursion(string[1:]) + string[0]
        return string
if __name__ == '__main__':


