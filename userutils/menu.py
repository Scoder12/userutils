"""
menu.py
File containing menu class.  
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
class Menu:
    """
    Menu(): A class to let users choose what they want to do.  Fully customizable for your needs.  
    Each item in the menu has an id, name, and callback.  Example: 
    
    Can be initialized with no paramaters or with customizations.  
    q (str): Message to be asked of user.  Default: "What would you like to do? "
    sep (str): The seperator between the id and option name.  Default: ". "
    prompt (str): The prompt to ask the user after printing options.  Default: "Type an option: "
    failmsg (str): The message to be displayed if the user provides an invalid option.  Default: "Invalid Option! "
    trnline (bool): Whether to print an empty line before excuting the callback.  Default: False
    
    >>> def hi():
    ..     print("Hello, World! ")
    ..     
    >>> def bye():
    ..     print("Goodbye, World! ")
    ..     
    >>> menu = userutils.Menu(q="Which function? ", sep=": ", prompt="> ", failmsg="That's not an option! ", trnline=True)
    >>> menu.addItem("1", "Say hi", hi) # Third paramter is function object, not call
    >>> menu.addItem("2", "Say goodbye", bye)
    >>> menu.addItem("3", "asdf", None)
    >>> menu.removeItem("3")
    >>> menu.addItem("1", "Say hello", hi) # Overrides if already exists
    >>> menu.data
    [['1', 'Say hello', <function hi at 0x7fce3152fd90>], ['2', 'Say goodbye', <function bye at 0x7fce3152fbf8>]]
    >>> menu.show()
    Which function? 
    2:Say goodbye
    1:Say hello
    >  good afternoon
    That's not an option! 
    Which function? 
    2:Say goodbye
    1:Say hello
    >  1
    Hello, World! 
    """
    defq = "What would you like to do? "
    defsep = ". "
    defprompt = "Type an option: "
    deffailmsg = "Invalid Option! "
    def __init__(self, data=[], q=defq, sep=defsep, prompt=defprompt, failmsg=deffailmsg, trnline=False):
        self.q = q
        self.sep = sep
        self.prompt = prompt
        self.failmsg = failmsg
        self.trnline = trnline
        if (data != []) and self.verify(data):
            self.data = []
        else:
            self.data = []
    def verify(self, ar):
        """
        for i in ar:
            if not (hasattr(i[1], "punctuation")):
                raise ValueError("name must be str")
                return False
            if not (hasatrr(i[2], "__code__")):
                raise ValueError("callback must be a function")
                return False
        """
        return True
    def addItem(self, id, name, callback):
        for question in self.data:
            if question[0] == id:
                self.removeItem(id)
        if self.verify([[id, name, callback]]):
            self.data.append([id, name, callback])
    def removeItem(self, id):
        for i in self.data:
            if (i[0] == id):
                self.data.remove(i)
                return
        raise IndexError("No such id "+id+" in items")
    def changeData(self, q=defq, sep=defsep, prompt=defprompt, failmsg=deffailmsg, trnline=False):
        self.q = q
        self.sep = sep
        self.prompt = prompt
        self.failmsg = failmsg
        self.trnline = trnline
    def show(self):
        if (self.data == []):
            print("Error: No data")
            return
        while True:
            print(self.q)
            for i in self.data:
                print(str(i[0])+self.sep+i[1])
            inp = input(self.prompt)
            for i in self.data:
                if (inp == str(i[0])):
                    if self.trnline:
                        print()
                    exec(i[2].__code__)
                    return
            print(self.failmsg)
