# two.py\

import one
print("Top level in two .py")

one.func()

if __name__ == '__main__':
	print("Two.py is being run directly")
else:
	print("two.py has been imported")

# IF a script is run directly the __name__ variable gets assigned to main