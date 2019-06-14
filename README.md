# Userutils

## A package for working with human users
Userutils makes the repititive code neccessary for working with humans from the console simple.  
### Features:
+ Yes/no questions (no more copy+pasting that one function again)
+ Getting objects from the user using JSON (optionally type enforced)
+ Menus for the user to choose an option
+ More coming soon! [Drop me a line](https://scoder12.com/contact.html) if there is something you want to see! 

***
# API Reference
## Basic functions
### yesNo()
`yesNo(msg, loop=True, incorrmsg="Please answer yes or no. ")`
Asks a yes/no question of the user (duh).
#### Args:
+ `msg` (`str`): message to be asked of user
+ `loop` (`bool`): Whether to loop on invalid input or not
+ `incorrmsg` (`str`) [optional]: message to be printed if the user enters an invalid input.

#### Returns:
+ `True` if the user answers yes
+ `False` if the user answers no

### getJSON()
`getJSON(msg, loop=True, smart=True, 
printerror=True, invalidjsonmsg="Please input some valid JSON!", enforcedtype=None, invalidtypemsg="Please enter the requested type. ")`
#### Args:
+ `msg` (`str`): Message to be shown for the prompt
+ `loop` (`bool`): Loop if invalid input recieved
+ `smart` (`bool`): Detect common errors and prompt user to fix them. Default True
+ `invalidmsg` (`str`): Message to be shown on invalid input
+ `enforcedtype` (`any`): If not None, then it will fail if it is a different type. **Default:** `None`

#### Returns:
+ The JSON object provided.

## Menus
### Structure
Each menu is represented by a `Menu` object. Each choice in the menu is represented by a `MenuItem` (or a subclass of it, for example `CallbackMenuItem`). You can mix and match different item types in a menu. Each menu is initialized with its menu items and is shown to the user with `show` which renders the menu. Everything about the menu can be customized. 
### MenuItem
`MenuItem(desc, value, choice=None)`
#### Attributes:
+ `desc` (`str`): Description of the item.
+ `value` (`any`): Value to be returned.
+ `choice` (`str`): what must be typed to select it. f None, it will be chosen automatically by the Menu. Default `None`. 

### CallbackMenuItem()
`CallbackMenuItem(desc, callback, args=(), kwargs={}, choice=None)`
A menuitem where a callback is run on select. 
#### Attributes/Arguments
+ `desc` (`str`): The description to be shown in the menu. 
+ `callback` (`func`): The callback to be run when option is selected. 
+ `args` (`tuple`): Optional arguments to be passed to the callback function. 
+ `kwargs` (`dict`): Optional keyword arguments to be passed to the callback function. 
+ `choice` (`str`): The string to be typed at the prompt for the option to be selected. If None, it will be chosen automatically by the Menu. Default None. 

#### Raises
`TypeError`: when args is not a tuple. Commonly caused by forgetting a comma with only one argument

### CallbackMenuItem().run()
`run()`
Runs the item's callback with its args and kwargs. 

### Menu()
`Menu(*items, q="What would you like to do?\n", sep=". ", prompt="Type an option: ", failmsg="Invalid Option! ", repeat=False,before='\n')`
A menu to let users choose what they want to do.  
Every aspect is fully customizeable. All fields are printed without an ending newline so that if left blank they will not show. 

#### Attributes
+ `sep` (`str`): The seperator between the id and option name.  Default: ". "
+ `prompt` (`str`): The prompt to ask the user after printing options.  Default: "Type an option: "
+ `failmsg` (`str`): The message to be displayed if the user provides an invalid option.  Default: "Invalid Option! "
+ `repeat` (`bool`): If True, repeats the options every prompt. If False, there will be an option to re-show the options. Default False. 
+ `before` (`str`): The text to be printed before running an option. Default: '\n'
+ `items` (`dict`): The choice and MenuItem for each item in the menu. 

#### Arguments
`Menu(*items, sep=". ", prompt="Type an option: ", failmsg="Invalid Option! ", repeat=False,before='\n')`
All arguments same as attributes. All non-keyword arguments are interpreted as `MenuItem`s. 

### Menu().show()
`Menu().show()`
Displays the menu.  
Returns the item selected and executes it's run() method if it has one. 

### Overrideable internal methods
In case you want to change some behavior or do some additional processing, you may be able to override one of these methods rather the the entire `show()` method. 

+ `Menu._get_input()`: This function gets the choice from the user. It defaults to just `return input(self.prompt)` but you can override this for additional input processing. 
+ `Menu._show_options()`: This function is called to show just the MenuItems. The default is to print `{choice}{self.sep}{item.desc}` for each item. 
+ `Menu._on_show()`: If you want some custom behavior before the menu is shown, you can use this method rather than changing the entire show method. By default this does nothing. 
+ `Menu._on_run()`: Run before the items callback or exiting the menu. Defaults to printing `self.before`

**That's all! [Contact me](https://scoder12.com/contact.html) with any suggestions!**