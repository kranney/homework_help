# create a text box that says input file
# create a text box that says output file
# create two browse buttons
# create two text entry fields
# create a process file button.
# need to write functions for each of the buttons
# ask for help on how to move objects to particular locations
import tkinter

window = tkinter.Tk()

# input file label
# need to margin it to the left
input_file_label = tkinter.Label(window, text='Input File:')
input_file_label.grid(row=0, column=0)

# output file label
# directly under the input file text
output_file_label = tkinter.Label(window, text='Output File:')
output_file_label.grid(row=1, column=0)

# text entry for input file
# needs to be right next to the input text
input_text_entry = tkinter.Entry(window)
input_text_entry.grid(row=0, column=1)

# text entry for output file
# needs to be directly under input file entry
output_text_entry = tkinter.Entry()
output_text_entry.grid(row=1, column=1)

# the input file button
# needs to be to the right of the input entry
def output_file():
	""" The function for the output file button. Will allows user to 
	choose what he/she would like the output file to be and will 
	display the output file in the output file entry box.
	"""

	pass

def input_file():
	""" The function for the input file button. Will allow the user to 
	choose what he/she would like the input file to be and will
	display the input file in the input file entry box.
	"""

	pass
	
input_file_browse_button = tkinter.Button(window, text='Browse...')
input_file_browse_button.grid(row=0, column=2)

# the output file button
# needs to be to the right of the output entry
def output_file():
	""" The function for the output file button. Will allows user to 
	choose what he/she would like the output file to be and will 
	display the output file in the output file entry box.
	"""

	pass

output_file_browse_button = tkinter.Button(window, text='Browse...')
output_file_browse_button.grid(row=1, column=2)

# process file button
process_file_button = tkinter.Button(window, text='Process File')
process_file_button.grid(row=3, column=0)

window.mainloop()
