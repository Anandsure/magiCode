from flask import Flask, flash, redirect, render_template, url_for, request
from flask_cors import CORS
import ibm_watson
#from gtts import gTTS
#import os
import re
import webbrowser
#import smtplib
import requests,json
import urllib
#import boto3
import os
#import cv2

#import assistant


app = Flask(__name__)

CORS(app)# to let the webapp know that this backend is ready to accept stuff.

@app.route('/')
def home():
    return render_template('compiler.html')


@app.route('/print/name', methods=['POST', 'GET'])

def get_names():

    global c
    global intent
    c=1
    if request.method == 'POST':
        resp_json = request.get_json()
        command = resp_json['text']
        if command=='cplusplus':
            command='open c++'
    assistant = ibm_watson.AssistantV1(
    version='2019-02-28',
    iam_apikey='u1N9ThXmpZUk_-1_F1AaAw-11BbBXFtCbonmmerHbnFI',
    url='https://gateway-wdc.watsonplatform.net/assistant/api'
    )

    response = assistant.message(
        workspace_id='7cb1c0fc-6e91-4b63-9e93-8a30028bd58e',
        input={
            'text': command #use the <text> we get with flask
        }
    ).get_result()


    a=response
    b=a['intents']
    if b==[]:
        if c==1:
            
            intent.append('nothing')
        else:
            intent.append('nothing')
    else:
        if c==1:
            
            intent.append(b[0]['intent'])
        else:
            intent.append(b[0]['intent'])
    print(intent)
    
    while intent[0]=='python':
        
        if intent[-1]=='for_loop':
            to_send = """for x in range (a,b):
    #enter your code here"""
        elif intent[-1]=='nested_for':
            to_send = """for x in range(a,b):
    for y in range(a,b):
        #enter your code here"""
        elif intent[-1]=='if_condition':
            to_send = """if a==b:
    #enter your code here"""

        elif intent[-1]=='nested_if':
            to_send = """if a==b:
    if a==b:
        #enter your code here"""

        elif intent[-1]=='else_if':
            to_send = """elif a==b:
    #enter your code here"""

        elif intent[-1]=='else_condition':
            to_send = """else:
    #enter your code here"""

        elif intent[-1]=='while_loop':
            to_send = """while x == y:
    #enter your code here"""

        elif intent[-1]=='print':
            to_send = """print(#your variable) """

        elif intent[-1]=='exit_loop':
            to_send ="""    if (condition):
    break"""
        
        elif intent[-1]=='init_string' or intent=='init_char':
            to_send="""var=input()"""

        elif intent[-1]=='init_int':
            to_send="""var=int(input())"""

        elif intent[-1]=='init_double':
            to_send="""var=double(input())"""

        elif intent[-1]=='arith_addition':
            to_send="""def add(a,b):
    return a+b
x=int(input())
y=int(input())
ans=add(x,y)
print(ans)"""

        elif intent[-1]=='arith_subtraction':
            to_send="""def sub(a,b):
    return a-b
x=int(input())
y=int(input())
ans=sub(x,y)
print(ans)"""

        elif intent[-1]=='arith_multiplication':
            to_send="""def mult(a,b):
    return a*b
x=int(input())
y=int(input())
ans=multi(x,y)
print(ans)"""

        elif intent[-1]=='arith_division':
            to_send="""def divi(a,b):
    return a/b
x=int(input())
y=int(input())
ans=divi(x,y)
print(ans)"""
        
        elif intent[-1]=='create_array':
            to_send="""var=[]
n=int(input())
for i in range(n):
    app=int(input())
    var.append(app)
print('the array is:',var)"""

        elif intent[-1]=='def_function':
            to_send="""def func_name(#arguments):
    #write your code here
    return #any variable
x=func_name(#arguments)"""

        else:
            to_send ='python running!'
            
        c+=1
        return json.dumps({"response": to_send}), 200
    
########################################################c++######################################################################################################################### 
    while intent[0]=='cplus':
        if intent[-1]=='for_loop':
            to_send = """for(int x=a ; x&lt;b ; x++) {
    //enter your code; 
}"""

        elif intent[-1]=='print':
            to_send = """cout<<'Enter your string here !<<endl;' """

        elif intent[-1]=='nested_for':
            to_send = """for(int x=a;x&lt;b;x++) {
for(int y=c;y&lt;d;y++) {
    //enter your code; 
}
}"""

        elif intent[-1]=='if_condition':
            to_send = """int x;
if(x==a) {
    //enter your code; 
}"""

        elif intent[-1]=='nested_if':
            to_send = """int x,y;
    if(x==a) {
    if(y==a) {
       //enter your code;  
    }
}"""

        elif intent[-1]=='else_if':
            to_send = """int x;
if(x==a) {
//enter your code; 
}
else if(x==b) {
//enter your code; 
}
else if(x==c) {
//enter your code;  
}"""
                
        elif intent[-1]=='else_condition':
            to_send = """int x;
if(x==a) {
//enter your code;  
}
else {
//enter your code;  
}"""
                
        elif intent[-1]=='while_loop':
            to_send = """while(x!=a) {
//enter your code; 
}"""

        elif intent[-1]=='exit_loop':
            to_send = """break;"""

        elif intent[-1]=='do_while_loop':
            to_send = """int x;
do {
//enter your code;  
} while(x&lt;a);"""

        elif intent[-1]=='init_string':
            to_send = """string x;"""

        elif intent[-1]=='init_int':
            to_send = """int x;"""

        elif intent[-1]=='init_char':
            to_send = """char name[100];"""

        elif intent[-1]=='init_float':
            to_send = """float x;"""

        elif intent[-1]=='arith_addition':
            to_send = """#include &lt;iostream&gt; 
using namespace std;
int main() {
    int x,y;
    cin>>x>>y;
    cout<<"Sum is: "<< x+y << endl;
return 0;
}"""

        elif intent[-1]=='arith_subtraction':
            to_send = """#include &lt;iostream&gt;
using namespace std;
int main() {
    int x,y;
    cin>>x>>y;
    cout<<"Difference is: "<< x-y << endl;
return 0;
}"""

        elif intent[-1]=='arith_multiplication':
            to_send = """#include &lt;iostream&gt;
using namespace std;
int main() {
    int x,y;
    cin>>x>>y;
    cout<<"Product is: "<< x*y <<endl;
return 0;
}"""

        elif intent[-1]=='arith_division':
            to_send = """#include &lt;iostream&gt;
using namespace std;
int main() {
    int x,y;
    cout<<"Quotient is: "<< x/y <<endl;
return 0;
}"""

        elif intent[-1]=='arith_remainder':
            to_send = """#include &lt;iostream&gt;
using namespace std;
int main() {
    int x,y;
    cout<<"Remainder is: "<< x%y << endl;
return 0;
}"""

        elif intent[-1]=='def_function':
            to_send = """#include &lt;iostream&gt;
// function declaration
int func(int x, int y);
int main () {
    // local variable declaration
    int a,b;
    // calling a function.
    func(a,b);
return 0;
}
// function
int func(int x, int y) {
    //enter your code;
}"""

        elif intent[-1]=='create_class':
            to_send = """class base { 
// Access specifier 
public:  
// Data Members 
string name; 
// Member Functions() 
void printname() { 
    cout <<"Name is: "<<name; 
} 
};""" 

        elif intent[-1]=='create_object':
            to_send = """// Declare an object of class base 
base obj1;"""

        elif intent[-1]=='include_lib_basic':
            to_send = """#include &lt;iostream&gt;
#include &lt;conio.h&gt;
#include &lt;string.h&gt;
#include &lt;math.h&gt;
#include &lt;ctype.h&gt;
#include &lt;stdlib.h&gt;"""

        elif intent[-1]=='include_lib_adv':
            to_send = """#include <vector>
#include &lt;string&gt;
#include &lt;file&gt;
#include &lt;map&gt;
#include &lt;complex&gt;"""

        elif intent[-1]=='create_array':
            to_send = """int a[100] , x , b;
cout << "Enter array size:" << endl;
cin >> b;
cout << " Enter array elements: " << endl;
for (x=a ; x &lt; b ; x++) {
    cin >> a[x] ;
}
cout << "Array is: " << endl;
for(x=a ; x &lt; b ; x++) {
    cout << a[x] ;
}"""

        elif intent[-1]=='switch_condition':
            to_send = """char variable;
switch(variable) { 
case valueOne: 
//statements 
break; 
case valueTwo: 
//statements
break; 
default: //optional
//statements
}"""
        else:
            to_send= """running c++"""

        c+=1
        return json.dumps({"response": to_send}), 200

########################################################PHP######################################################################################################################### 
    while intent[0]=='php':
        if intent=='for_loop':
            to_send = """for ($x = a; $x <= b; $x++) {
//enter your code
} """

        elif intent[-1]=='print':
            to_send = """ echo " Enter your string here ! " ; """

        elif intent[-1]=='nested_for':
            to_send = """for ($x = a; $x <= b; $x++) {
    for ($y = c; $y <= d; $y++) {
        //enter your code;
        }
}"""

        elif intent[-1]=='if_condition':
            to_send = """$t = "varable";
if ($t < "Condition") {
    //enter your code;
    }"""

        elif intent[-1]=='nested_if':
            to_send = """$x = "variable";
$y = "Variable"
if($x=="condition") {
    if($y=="condition") {
        //enter your code;
    }
}"""

        elif intent[-1]=='else_if':
            to_send = """$x = "variable";
if($x==a) {
    //enter your code;
}
else if($x==b) {
    //enter your code;
}
else if($x==c) {
    //enter your code;
}"""
                    
        elif intent[-1]=='else_condition':
            to_send = """$x = "Variable";
if($x==a) {
    //enter your code;
}
else {
    //enter your code;
}"""
                    
        elif intent[-1]=='while_loop':
            to_send = """while($x!="condition") {
    //enter your code;
}"""

        elif intent[-1]=='exit_loop':
            to_send = """break;"""

        elif intent[-1]=='do_while_loop':
            to_send = """$x = "variable";
do {
    //enter your code;
} while($x<"condition");"""

        elif intent[-1]=='init_string':
            to_send = """string $x; """

        elif intent[-1]=='init_int':
            to_send = """int $x; """

        elif intent[-1]=='init_char':
            to_send = """char name[100];"""

        elif intent[-1]=='init_float':
            to_send = """float $x; """

        elif intent[-1]=='arith_addition':
            to_send = """<?php
function add(float $x,float $y){
    return $x+$y;
}
?>"""

        elif intent[-1]=='arith_subtraction':
            to_send = """<?php
function add(float $x,float $y){
    return $x-$y;
}
?>"""

        elif intent[-1]=='arith_multiplication':
            to_send = """<?php
function add(float $x,float $y){
    return $a*$b;
}
?>"""

        elif intent[-1]=='arith_division':
            to_send = """<?php
function add(float $x,float $y){
    return $a/$b;
}
?>"""

        elif intent[-1]=='arith_remainder':
            to_send = """<?php
function add(float $x,float $y){
    return $a%$b;
}
?>"""

        elif intent[-1]=='def_function':
            to_send = """<?php
function add(float $x,float $y){
    //enter your code
    return "Your Output";
}
add($x,$y);

?>"""


        elif intent[-1]=='create_array':
            to_send = """int a[100],x,b;
echo 'Enter array size:';
$handle = fopen ("php://stdin","r");
$line = fgets($handle);
echo 'Enter array elements:';
for(x=a;x<b;x++) {
    a[x]=fgets($handle);
}
echo 'Array is: ' ;
for($x=a;$x<b;$x++) {
    echo $a[$x];
}"""

        elif intent[-1]=='switch_condition':
            to_send = """$x = "variable";
switch ($x) {
    case "1":
        //enter your code
        break;
    case "2":
        //enter your code
        break;
    case "3":
        //enter your code
        break;
    default: //optional
        //default return code;
}"""

        else:
            to_send= """running php"""

        c+=1
        return json.dumps({"response": to_send}), 200



    c+=1
    return json.dumps({"response": ' '}), 200
    

if __name__=='__main__':
    c=1
    intent=[]
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=False)
    

