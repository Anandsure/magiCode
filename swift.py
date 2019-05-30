while intent[0]=='swift':
        if intent=='for_loop':
            to_send = """for i in a...b {
    //enter your code here
} """

        elif intent[-1]=='print':
            to_send = """ print(//enter your code) """

        elif intent[-1]=='nested_for':
            to_send = """for i in a...b {
    for j in a...b{
        //enter your code here
    }
}"""

        elif intent[-1]=='if_condition':
            to_send = """let a = 10
if a &lt; b {
	//enter your code
}
//print("This statement is always executed.")"""

        elif intent[-1]=='nested_if':
            to_send = """let a = 10
if a &gt; b {
	if a &gt; b {
	    //enter your code
    }
}
//print("This statement is always executed.")
"""

        elif intent[-1]=='else_if':
            to_send = """let a = 10
if a &gt; b {
	//enter your code
} else if a &gt; b {
	//enter your code
}
//print("This statement is always executed.")
"""
                    
        elif intent[-1]=='else_condition':
            to_send = """let a = 10
if a &gt; b {
    //enter your code
}
else {
    //enter your code
}"""
                    
        elif intent[-1]=='while_loop':
            to_send = """while a <= b {
    //enter your code 
}"""

        elif intent[-1]=='exit_loop':
            to_send = """if a &gt; b {
    break
}"""

        elif intent[-1]=='do_while_loop':
            to_send = """repeat {
    var i = 1
    //enter your code here.
    i = i + 1
} while a &lt; b"""

        elif intent[-1]=='init_string':
            to_send = """var your_string = 'change it here' """

        elif intent[-1]=='init_int':
            to_send = """var your_integer = 0 """

        elif intent[-1]=='init_char':
            to_send = """var your_char = 'C' """

        elif intent[-1]=='init_float':
            to_send = """var your_float = 0.00 """

        elif intent[-1]=='arith_addition':
            to_send = """func add(a: Int , b: Int) -> Int {
    let sum = a + b
    return sum
}
print("sum is" , add(a: 2, b: 4), separator: " ")"""

        elif intent[-1]=='arith_subtraction':
            to_send = """func sub(a: Int , b: Int) -> Int {
    let diff = a - b
    return diff
}
print("diff is" , sub(a: 10, b: 4), separator: " ")"""

        elif intent[-1]=='arith_multiplication':
            to_send = """func multi(a: Int , b: Int) -> Int {
    let prod = a * b
    return prod
}
print("product is" , multi(a: 2, b: 4), separator: " ")"""

        elif intent[-1]=='arith_division':
            to_send = """func divi(a: Int , b: Int) -> Int {
    let diff = a / b
    return diff
}
print("quotient is" , divi(a: 19, b: 4), separator: " ")"""

        elif intent[-1]=='arith_remainder':
            to_send = """func modu(a: Int , b: Int) -> Int {
    let mod = a % b
    return mod
}
print("reminder is" , modu(a: 18, b: 4), separator: " ")"""

        elif intent[-1]=='def_function':
            to_send = """func your_func_name(a: Int , b: Int) -> String {
    //enter your code
    if a &gt; b{
        The_final_output = "Edit this function"
    }
    return The_final_output
}
print("output:" , your_func_name(a: 18, b: 4), separator: " ")"""


        elif intent[-1]=='create_array':
            to_send = """var your_array = [1,2,3,4,5,6]
print(your_array)"""

        elif intent[-1]=='switch_condition':
            to_send = """let someCharacter: Character = "z" // or someinteger: Int = 2
switch someCharacter {
case "a": // case 1:
    // enter your code
case "z": // case 2:
    // enter your code
default:
    // default reply
}"""

        else:
            to_send= """running swift"""

        c+=1
        return json.dumps({"response": to_send}), 200