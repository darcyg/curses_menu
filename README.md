### About

This is curses menu maker.
It can make menu.

### How To
```bash
$ pip install pyqt5
$ pip install curses
```
##### curses download from here:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses

### Example

```python
from curses_menu import *

# write your items in a list
items = ['home', 'contact', 'exit']
choose = menu(items, x_co=5, y_co=5, box=False)
# x_co, y_co and box are optionals

if choose == 1:
	gotohome()
elif choose == 2:
	gotocontact()
elif choose == 3:
	exit()
```

### Screen Shots

![screen-shot](https://user-images.githubusercontent.com/22606403/39956062-17fcdfaa-55f9-11e8-817f-e5823c43edfe.PNG)
