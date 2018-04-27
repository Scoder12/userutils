"""
userutils.py
Useful functions for a user interface.  

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
    while True:
        i = input(msg)
        if (i[0] in ["y", "Y"]):
            return 0
        elif (i[0] in ["n", "N"]):
            return 1
        else:
            print(incorrmsg)

class menu:
    """
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
