import curses

class Menu:
	def menu(self,items, x_co=5,y_co=5, box=False):
		stdscr = curses.initscr()
		curses.cbreak()
		curses.noecho()
		stdscr.keypad(True)
		stdscr.refresh()
		if box == False:
			pass
		else:
			pass
			# Do later in here...
		try:
			place = 0
			c = 0
			while(1):
				stdscr.clear()
				xco = x_co
				yco = y_co
				if c == curses.KEY_DOWN:
					place += 1
					if place == len(items): place = 0
				if c == curses.KEY_UP:
					place -= 1
					if place < 0: place = len(items) - 1
				if c == curses.KEY_ENTER or c == 10 or c == 13:
					return (place + 1)

				for n,menu in enumerate(items):
					if place == n:
						stdscr.addstr(yco, xco, '->'+items[n])
					else:
						stdscr.addstr(yco, xco, '  '+items[n])
					yco += 1
				c = stdscr.getch()
		except Exception as e:
				print(e)