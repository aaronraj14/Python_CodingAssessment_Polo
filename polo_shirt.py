'''
----------------
Overview
----------------
This Python program is used to determine if employees are matching the office dress code.
Complete the function that checks the employee's clothes match.

----------------   
Instruction
----------------
The rules are as follows:
- The 'Tops' can only be of these colors: (white, blue, black) unless it is a Polo shirt, then any color is allowed.
- Employees are not allowed to wear a T-Shirt; other types are allowed.
- For 'Bottoms,' the only colors permitted are black and blue, and shorts are not allowed.
- Lastly, the 'Top' and 'Bottom' color cannot be the same.

----------------
Optional task
----------------
Optimize code for maintanability and readability before performance. Some tips and suggestions are to:
- Reduce the number lines without obscuring too much logic (not too short)
- Use built-in functions
- Minimize indentations or nested statements
'''

class Top:
    def __init__(self, color, type):
        # Can be any color
        self.color = color

        # Available types: ['polo', 'tshirt', 'shirt']
        self.type = type

class Bottom:
    def __init__(self, color, length):
        # Can be any color
        self.color = color

        # Length is either: ['short', 'long']
        self.length = length


t1 = Top('red', 'polo')
t2 = Top('gray', 'tshirt')
t3 = Top('white', 'shirt')
t4 = Top('blue', 'shirt')
t5 = Top('black', 'shirt')

b1 = Bottom('black', 'long')
b2 = Bottom('white', 'long')
b3 = Bottom('black', 'short')
b4 = Bottom('blue', 'long')
b5 = Bottom('gray', 'short')


def match_dress_code(top, bottom):
    # Complete the code here. Return True/False

    # This line here checks if the Employee wears a polo or not.
    #if employee wears polo but the pants is short, reject and return false.
    if top.type == 'polo' and bottom.length == 'long':
        #if bottom.length == 'long':
        # if the Bottom pants is black or blue, return true else, return false
        if bottom.color == 'black' or bottom.color == 'blue':
            print("Employee wears a Polo shirt")
            return True
        else:
            return False

    # This line here checks if the Employee wears a shirt or not and wears long bottoms.
    #if Employee wears a t-shirt or the pants is short or wearing both of them, reject and return false
    elif top.type == 'shirt' and bottom.length == 'long':
        if top.color == 'black' or top.color == 'white' or top.color == 'blue':
            #if bottom.length == 'long':
            if bottom.color == 'black' or bottom.color == 'blue':
                # Check if the shirt and pants are same color. If yes, reject and return false
                # Else, return True
                if bottom.color == top.color:
                    return False
                else:
                    print("Employee wears a " + top.color + " shirt and long " + bottom.color + " pants.")
                    return True
            else:
                return False
        else:
            return False
    else:
        return False
    print(top.color)


# Do not edit any of these.
# Pass all these assertions to pass the test
# Ensure no errors
assert match_dress_code(t1, b1) == True
assert match_dress_code(t1, b2) == False
assert match_dress_code(t1, b3) == False
assert match_dress_code(t1, b4) == True
assert match_dress_code(t1, b5) == False

assert match_dress_code(t2, b1) == False
assert match_dress_code(t2, b2) == False
assert match_dress_code(t3, b3) == False
assert match_dress_code(t4, b4) == False
assert match_dress_code(t5, b5) == False

assert match_dress_code(t3, b1) == True
assert match_dress_code(t3, b2) == False
assert match_dress_code(t3, b3) == False
assert match_dress_code(t3, b4) == True
assert match_dress_code(t3, b5) == False

assert match_dress_code(t4, b1) == True
assert match_dress_code(t4, b2) == False
assert match_dress_code(t4, b3) == False
assert match_dress_code(t4, b4) == False
assert match_dress_code(t4, b5) == False

assert match_dress_code(t5, b1) == False
assert match_dress_code(t5, b2) == False
assert match_dress_code(t5, b3) == False
assert match_dress_code(t5, b4) == True
assert match_dress_code(t5, b5) == False

print('Test passed!')
