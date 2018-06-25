"""
main.py
Main file for package containing basic functions.   
This file is part of the userutils package https://github.com/Scoder12/userutils

Copyright 2018 Scoder12

Licensed under the MIT License.  

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the
following conditions: 

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
def yesNo(msg, incorrmsg="Please answer yes or no. "):
    """yesNo(msg, incorrmsg="Please answer yes or no. ")
    Asks a user msg where the reponse shoud be yes or no.
    Parameters:
    msg (str): message to be asked of user
    incorrmsg (str) [optional]: message to be printed if the user enters an invalid
    input.
    Returns:
    0 if the user answers yes
    1 if the user answers no
    """
    i = input(msg)
    if (i[0] in ["y", "Y"]):
        return True
    elif (i[0] in ["n", "N"]):
        return False
    else:
        print(incorrmsg)
