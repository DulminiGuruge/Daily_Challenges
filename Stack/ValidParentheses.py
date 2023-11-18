"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Approach -

Create a hashmap whcih contains the closing parantheses as the keys and the corresponding openeing parntheses are the
values. Then create a stack to add open parenthesis. Once a closing parenthesis is encountered see whether the last element of the stack after pop is the open 
parenthesis of the closing parenthesis by using the hash map.

Time complexity - O(n)

Space complexity - O(n)

"""

def isValid(s):
     """
        :type s: str
        :rtype: bool
        """
     stack = []
     parenthesesMap = {")":"(","}":"{","]":"["}
     
     for c in s:
            if c in parenthesesMap: # if a closing parentheses
                # if stack is not empty and he value at the top of the stack is the matching open parenthesis
                if stack and stack[-1] == parenthesesMap[c]:
                    stack.pop()
                else:
                     return False
            else:
               stack.append(c)    # if an open parenthesis add to the stack
               
     return True if not stack else False






print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(])"))