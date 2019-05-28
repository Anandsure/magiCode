if intent=='for_loop':
    to_send = """for ($x = a; $x <= b; $x++) {
                        < Code > 
                        } """

elif intent=='print':
    to_send = """ echo " Enter your string here ! " ; """

elif intent=='nested_for':
    to_send = """for ($x = a; $x <= b; $x++) {
                    for ($y = c; $y <= d; $y++) {
                        <Code>;
                        }
                 }"""

elif intent=='if_condition':
    to_send = """$t = "varable";
                 if ($t < "Condition") {
                    <code>;
                    }"""

elif intent=='nested_if':
    to_send = """$x = "variable";
                 $y = "Variable"
                 if($x=="condition") {
                    if($y=="condition") {
                        <code>;
                    }
                }"""

elif intent=='else_if':
    to_send = """$x = "variable";
                 if($x==a) {
                    <code1>;
                 }
                 else if($x==b) {
                    <code2>;
                 }
                 else if($x==c) {
                    <code3>;
                 }"""
            
elif intent=='else_condition':
    to_send = """$x = "Variable";
                 if($x==a) {
                    <code1>;
                  }
                  else {
                    <code2>;
                  }"""
            
elif intent=='while_loop':
    to_send = """while($x!="condition") {
                    <code>;
                 }"""

elif intent=='exit_loop':
    to_send = """break;"""

elif_intent=='do_while_loop':
    to_send = """$x = "variable";
                 do {
                    <code>;
                 } while($x<"condition");"""

elif_intent=='init_string':
    to_send = """string $x; """

elif intent=='init_int':
    to_send = """int $x; """

elif intent=='init_char':
    to_send = """char name[100];"""

elif intent=='init_float':
    to_send = """float $x; """

elif intent=='arith_addition':
    to_send = """<?php
                function add(float $x,float $y){
                    return $x+$y;
                }
                ?>"""

elif intent=='arith_subtraction':
    to_send = """<?php
                function add(float $x,float $y){
                    return $x-$y;
                }
                ?>"""

elif intent=='arith_multiplication':
    to_send = """<?php
                function add(float $x,float $y){
                    return $a*$b;
                }
                ?>"""

elif intent=='arith_division':
    to_send = """<?php
                function add(float $x,float $y){
                    return $a/$b;
                }
                ?>"""

elif intent=='arith_remainder':
    to_send = """<?php
                function add(float $x,float $y){
                    return $a%$b;
                }
                ?>"""

elif intent=='def_function':
    to_send = """<?php
                function add(float $x,float $y){
                    <code>
                    return "Your Output";
                }
                add($x,$y);
                
                ?>"""


elif intent=='create_array':
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

elif intent='switch_condition':
    to_send = """$x = "variable";

                 switch ($x) {
                    case "1":
                        <code>;
                        break;
                    case "2":
                        <code>;
                        break;
                    case "3":
                        <code>;
                        break;
                    default:
                        <default return code>;
                }"""