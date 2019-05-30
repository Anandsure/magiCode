intent=input()

if intent=='for_loop':
    to_send = """for x in range (a,b):
    <code>"""
elif intent=='nested_for':
    to_send = """for x in range(a,b):
    for y in range(a,b):
        <code>"""
elif intent=='if_condition':
    to_send = """"if a==b:
        <code>"""

elif intent=='nested_if':
    to_send = """if a==b:
        if a==b:
            <code>"""

elif intent=='else_if':
    to_send = """"elif a==b:
        <code>"""

elif intent=='else_condition':
    to_send = """"else:
        <code>"""

elif intent=='while_loop':
    to_send = """while x == y:
        <code>"""

elif intent=='print':
    to_send = """print('Enter your string here !') """

elif intent=='init_string' or intent=='init_char':
        to_send="""var=input()"""

elif intent=='init_int':
        to_send="""var=int(input())"""

elif intent=='init_double':
        to_send="""var=double(input())"""

elif intent=='arith_addition':
        to_send="""def add(a,b):
        return a+b
ans=add(var1,var2)"""

elif intent=='arith_subtraction':
        to_send="""def sub(a,b):
        return a-b
ans=sub(var1,var2)"""

elif intent=='arith_multiplication':
        to_send="""def mult(a,b):
        return a*b
ans=mult(var1,var2)"""

elif intent=='arith_division':
        to_send="""def divi(a,b):
        return a/b
ans=divi(var1,var2)"""

else:
    to_send ='hey'

print(to_send)
