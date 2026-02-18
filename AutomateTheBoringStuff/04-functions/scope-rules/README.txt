
Scope Rules:

When working with local and global variables, 
keep the following rules in mind:

1.) Code that is in the global scope, outside all 
 functions, can’t use local variables.

2.) Code that is in one function’s local scope 
 can’t use variables in any other local scope.

3.) Code in a local scope can access 
 global variables.

4.) You can use the same name for different 
 variables if they are in different scopes. 
 That is, there can be a local variable named
 spam and a global variable also named spam.


Scope Identification Rules:


Use these four rules to tell whether a variable
belongs to a local scope or the global scope:

1.) A variable in the global scope (that is, 
 outside all functions) is always a global 
 variable.

2.) A variable in a function with a global 
 statement is always a global variable in that 
 function.

3.) Otherwise, if a function uses a variable in 
 an assignment statement, it is a local variable.

4.) However, if the function uses a variable but 
 never in an assignment statement, it is a global 
 variable.
