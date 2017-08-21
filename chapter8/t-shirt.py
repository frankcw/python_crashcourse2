# t-shirt



def make_shirt(size,text):
	print("You have a selected a shirt size " + size.upper() + ".")
	print("It also includes the following text on it: " + text.title())

# postional arguments
make_shirt('M','This is an Awesome Shirt')

# keyword arguments
make_shirt(size='L',text='This is an ugly shirt')
