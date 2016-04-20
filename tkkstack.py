#!/usr/bin/python

from Tkinter import *
import tkMessageBox

class Stack:
	win = Tk()
	import tkSimpleDialog
	f = Frame(win)
	f.master.title("Stack")
	position=0
	dict1 = {}
	n = int(raw_input( "Enter the size of stack "))
	
	for i in range(n):
		Label(f, bg="green",width=14,height=2).grid(row=i+2, column=2)
	def push(self):
		if Stack.position == Stack.n:
			tkMessageBox.showinfo("CAN NOT PUSH", "stack is full")
		else:
			message = self.tkSimpleDialog.askstring('Dictonary', 'Enter the element')
			if(message):
				Stack.position +=1
				Stack.dict1[Stack.position] = message
				Label(self.f, bg="red",width=14,height=2,text= Stack.dict1[Stack.position]).grid(row = ((Stack.n+2)-Stack.position), column=2)
			
	def pop(self):
		if Stack.position == 0:
			tkMessageBox.showinfo("CAN NOT POP", "stack is empty")
		else:
			Label(self.f, bg="green",width=14,height=2).grid(row = ((Stack.n+2)-Stack.position), column=2)
			Stack.position -=1

	def top(self):
		if Stack.position == 0:
		  tkMessageBox.showinfo("TOP", "It is empty")
		else:
			tkMessageBox.showinfo("TOP",Stack.dict1[Stack.position])
			
class Stackepliment(Stack):
		
	
	def generate(self):
	# Define UI
		Button(self.f,text= "PUSH", bg = "blue",width=8,height=2,command=self.push).grid(row=0, column=1)
		Button(self.f,text= "POP",width=8,height=2, bg = "blue",command=self.pop).grid(row=0, column=2)
		Button(self.f,text= "TOP",width=8,height=2, bg = "blue",command=self.top).grid(row=0, column=3)
		Label(self.f,width=8,height=2).grid(row=0, column=0)
		Label(self.f,width=8,height=2).grid(row=0, column=4)
		Label(self.f,width=14,height=2).grid(row=1, column=2)
		Stack.l = Label(self.win,text ="This is STACK TUTORIAL")
		Stack.l.pack()
		Stack.f.pack()
		Stack.win.mainloop()
if __name__ == "__main__":
	o=Stackepliment()
	o.generate()
