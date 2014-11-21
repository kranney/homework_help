# create a text box that says input file
# create a text box that says output file
# create two browse buttons
# create two text entry fields
# create a process file button.
# need to write functions for each of the buttons
# ask for help on how to move objects to particular locations
import tkinter
import tkinter.filedialog as dialog

class File:
	""" A simple counter GUI using object-oriented programming."""

	def __init__(self, parent):

self.window = tkinter.Tk()

# input file label
# need to margin it to the left
self.input_file_label = tkinter.Label(window, text='Input File:')
self.input_file_label.grid(row=0, column=0)

# output file label
# directly under the input file text
self.output_file_label = tkinter.Label(window, text='Output File:')
self.output_file_label.grid(row=1, column=0)

# text entry for input file
# needs to be right next to the input text
self.input_text_entry = tkinter.Entry(window)
self.input_text_entry.grid(row=0, column=1)

# text entry for output file
# needs to be directly under input file entry
self.output_text_entry = tkinter.Entry()
self.output_text_entry.grid(row=1, column=1)

# the input file button
# needs to be to the right of the input entry
def output_file():
	""" The function for the output file button. Will allows user to 
	choose what he/she would like the output file to be and will 
	display the output file in the output file entry box.
	"""

	data = text.get('0.0', tkinter.END)
	filename = dialog.asksaveasfilename(parent=root, filetypes=[('Text', '*.txt')], title='Save as...')
	writer = open(filename, 'w')
	writer.write(data)
	writer.close()

def input_file():
	""" The function for the input file button. Will allow the user to 
	choose what he/she would like the input file to be and will
	display the input file in the input file entry box.
	"""
	date = text.get('0.0', tkinter.END)
	filename = dialog.asksaveasfilename(parent=root, filetypes=[('Text', '*txt')], title='Save as...')
	writer = 
	
	
self.input_file_browse_button = tkinter.Button(window, text='Browse...')
self.input_file_browse_button.grid(row=0, column=2)

# the output file button
# needs to be to the right of the output entry
def output_file():
	""" The function for the output file button. Will allows user to 
	choose what he/she would like the output file to be and will 
	display the output file in the output file entry box.
	"""

	pass

self.output_file_browse_button = tkinter.Button(window, text='Browse...')
self.output_file_browse_button.grid(row=1, column=2)

# process file button
self.process_file_button = tkinter.Button(window, text='Process File')
self.process_file_button.grid(row=3, column=0)

if __name__ == '__main__':
	window.mainloop()