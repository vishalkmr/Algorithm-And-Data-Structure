'''
 Evaluate the given postfix expression

 Example
 postfix_evaluation('453*+2-')
 Returns: 17

 i.e. equivalent infix expression for postfix expression '453*+2-' is '4+5*3-2' which evaluates to 17
'''

from Stack import Stack

def postfix_evaluation(expression):
    ''' 
    Funtion to evaluate given postfix expression
    Syntax: reverse(expression)
    Time Complexity: O(n)   
    ''' 
    operand_stack=Stack() #stack to hold the operand for evaluation

    for item in expression:

        #if item is operator
        if is_operator(item):
            first_operand=int(operand_stack.pop()) #pop the first_operand of expression element from operand_stack
            second_operand=int(operand_stack.pop()) #pop the second_operand of expression element from operand_stack
            result=operation(first_operand,second_operand,item) #perform the operation between operands
            operand_stack.push(result) #push the oprations result back to push
        
        #if item is operand
        else:
            operand_stack.push(item) #push that item on operand_stack

    #finally top of operand_stack contains the evaluated result        
    return operand_stack.peek()        




#funtion to check whether the element is operator or not
def is_operator(operator):
    if(operator=='+' or  operator=='-' or operator=='/' or operator=='*' or operator=='^'or operator=='('or operator==')' ):
        return True
    else:
        return False

#funtion to perform the opration acording to passed operator
def operation(first_operand,second_operand,operator):
    if operator=='+':
        return first_operand+second_operand
    elif operator=='-':
        return second_operand-first_operand
    elif operator=='-':
        return second_operand-first_operand
    elif operator=='*':
        return second_operand*first_operand
    elif operator=='/':
        return second_operand/first_operand
    elif operator=='^':
        return second_operand**first_operand




expression='223414^^*+24*2/-5+'

result=postfix_evaluation(expression)
print(result)
