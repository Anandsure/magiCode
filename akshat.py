intent='x'
if intent=='for_loop':
    to_send = """for(int x=a;x<b;x++) {
                    <code>; 
                }"""

elif intent=='print':
    to_send = """cout<<'Enter your string here !<<endl;' """

elif intent=='nested_for':
    to_send = """for(int x=a;x<b;x++) {
                    for(int y=c;y,d;y++) {
                        <code>;
                    }
                 }"""

elif intent=='if_condition':
    to_send = """int x;
                if(x==a) {
                    <code>;
                }"""

elif intent=='nested_if':
    to_send = """int x,y;
                 if(x==a) {
                    if(y==a) {
                        <code>;
                    }
                }"""

elif intent=='else_if':
    to_send = """int x;
                 if(x==a) {
                    <code1>;
                 }
                 else if(x==b) {
                    <code2>;
                 }
                 else if(x==c) {
                    <code3>;
                 }"""
            
elif intent=='else_condition':
    to_send = """int x;
                 if(x==a) {
                    <code1>;
                  }
                  else {
                    <code2>;
                  }"""
            
elif intent=='while_loop':
    to_send = """while(x!=a) {
                    <code>;
                 }"""

elif intent=='exit_loop':
    to_send = """break;"""

elif intent=='do_while_loop':
    to_send = """int x;
                 do {
                    <code>;
                 } while(x<a);"""

elif intent=='init_string':
    to_send = """string x;"""

elif intent=='init_int':
    to_send = """int x;"""

elif intent=='init_char':
    to_send = """char name[100];"""

elif intent=='init_float':
    to_send = """float x;"""

elif intent=='arith_addition':
    to_send = """#include <iostrean>
                #include <stdio.h>
                using namespace std;
                int main() {
                    int x,y;
                    cout<<'Sum is: '<<x+y<<endl;
                return 0;
                }"""

elif intent=='arith_subtraction':
    to_send = """#include <iostrean>
                #include <stdio.h>
                using namespace std;
                int main() {
                    int x,y;
                    cout<<'Difference is: '<<x-y<<endl;
                return 0;
                }"""

elif intent=='arith_multiplication':
    to_send = """#include <iostrean>
                #include <stdio.h>
                using namespace std;
                int main() {
                    int x,y;
                    cout<<'Product is: '<<x*y<<endl;
                return 0;
                }"""

elif intent=='arith_division':
    to_send = """#include <iostrean>
                #include <stdio.h>
                using namespace std;
                int main() {
                    int x,y;
                    cout<<'Quotient is: '<<x/y<<endl;
                return 0;
                }"""

elif intent=='arith_remainder':
    to_send = """#include <iostrean>
                #include <stdio.h>
                using namespace std;
                int main() {
                    int x,y;
                    cout<<'Remainder is: '<<x%y<<endl;
                return 0;
                }"""

elif intent=='def_function':
    to_send = """#include <iostream>
                using namespace std;
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
                    <code>;
                }"""

elif intent=='create_class':
    to_send = """class base { 
                // Access specifier 
                public:  
               // Data Members 
               string name; 
               // Member Functions() 
               void printname() { 
                    cout <<'Name is: '<<name; 
                } 
                };""" 

elif intent=='create_object':
    to_send = """// Declare an object of class base 
                 base obj1;"""

elif intent=='include_lib_basic':
    to_send = """#include <iostream>
                 #include <stdio>
                 #include <string>
                 #include <math>
                 #include <ctype>
                 #include <stdlib.h>"""

elif intent=='include_lib_adv':
    to_send = """#include <vector>
                 #include <string>
                 #include <file>
                 #include <complex>"""

elif intent=='create_array':
    to_send = """int a[100],x,b;
                 cout<<'Enter array size:'<<endl;
                 cin>>b;
                 cout<<'Enter array elements:'<<endl;
                 for(x=a;x<b;x++) {
                     cin>>a[x];
                 }
                 cout<<'Array is':<<endl;
                 for(x=a;x<b;x++) {
                     cout<<a[x];
                 }"""

elif intent=='switch_condition':
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
    to_send= 'nothing'