"""
consider to python:
=================
1.identifier
2.indentation
3.keywords
4.comments


1.identifier:
============
user defined text.
variable,function name, class name,object name


Example In c++:
===============
#include<iostream.h>
#include<conio.h>


class fruits//class name
{
  
}
void add()//function name
{

}
void main()
{
  int a=10;//variable name
  fruits f;//f-->object name
}

rules:
======
1.identifier must be contain with alphabet,numbers and underscore(_).
2.identifier are case sentivity.(upper and lower are not equal)
3.do not start with number.
4.space b/w identifier are not allowed.
5.symbols are not allowed.
6.keywords are not used as a identier.
7.if declare a function name starting letter should be lowercase.(show,getData,studentDetails)
8.if declare a class name starting  letter should be uppercase.(Show,GetData,StudentDetails)
"""

a=10
value=20
a1=25
a1=a
#a1=A----case sensitive
#1ststudent="livewire"---do not start with number
#first  student="livewire"--->do not contain space between single variable.
firststudent="siva"
first_student="Maha"

#m@123="password"---->symbols  are not allowed in identifier
#if=10--->do not use variable as a keyword
"""

2.indentation:
============
allocate 4 space or 1 tab key
    
if(condition)#other language
{
    statement1
    statement2
}

 python
if condition:
    statements#tab---block
    statements
else:
    statements
    statements

3.Keyword:
==========
reserved word for the program

ex:
for,if,True,False,while,pass


4.comments:
===========
1.single line comment
2.multi line comment

1.single line comment(#):
======================
hide the details for that line.

#details

2.Multiline comment:
====================

""""""multiline comment""""""
'''multiline comment'''


a=10
#a=a+10
print(a)


b=20
print(b)
"""

#single line comment

'''
write a
information
multiple line
'''

"""
multi
line
code
write
*/
"""
