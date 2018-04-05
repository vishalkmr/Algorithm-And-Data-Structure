'''
 Convert the given Infix expression to Postfix expression

 Example
 postfix_evaluation('4+5*3-2')
 Returns: '453*+2-'
'''

from Stack import Stack

def convert_to_postfix_notation(expression):
    ''' 
    Funtion to convert the given Infix expression to Postfix expression
    Syntax: convert_to_postfix_notation(expression)
    Time Complexity: O(n)   
    ''' 
    operator_stack = Stack() #stack to hold the operator for evaluation
    operator_stack.push('$') #intializing the bottom of operator_stack
    postfix_expression = '' #to store the equivalent postfix expression

    for element in expression:

        # if element is operand 
        if (not is_operator(element)):
            postfix_expression = postfix_expression+element # append the operand to postfix_expression
        
        #if element is operator
        else:

            # if element is (  
            if (element == '('):
                operator_stack.push(element) #push that element onto operator_stack

            # if element is ) 
            elif (element == ')'):
                temp = operator_stack.pop()
                #then pop the elements from operator_stack until we get the (
                while (temp is not '('):
                    postfix_expression = postfix_expression + temp
                    temp = operator_stack.pop()

             # if element(incoming operator) have higher priority than top element of operator_stack
            elif (priority(element) > priority(operator_stack.peek())):
                operator_stack.push(element) #then push that element onto operator_stack

            # if element(incoming operator) have lower priority than top element of operator_stack 
            else:
                #then pop the elemtns from operator_stack until element(incoming operator) have higher priority
                while (priority(element) <= priority(operator_stack.peek())):
                    postfix_expression = postfix_expression + operator_stack.pop()
                #finnaly push that element onto operator_stack
                operator_stack.push(element)

    #pop the remaining items from operator_stack
    temp = operator_stack.pop()
    while (temp != '$'):
        postfix_expression = postfix_expression + temp
        temp = operator_stack.pop()
    return postfix_expression



#funtion to assign priority to each operator
def priority(operator):
    if(operator=='('):
        return 0
    if(operator=='^'):
        return 3
    if(operator=='/' or operator=='*'):
        return 2
    if(operator=='+' or operator=='-'):
        return 1
    if(operator=='$'):
       return -1



#funtion to check whether the element is operator or not
def is_operator(operator):
    if(operator=='+' or  operator=='-' or operator=='/' or operator=='*' or operator=='^'or operator=='('or operator==')' ):
        return True
    else:
        return False






expression='4+5*3-2'

result=convert_to_postfix_notation(expression)
print(result)
