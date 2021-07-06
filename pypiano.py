from tkinter import *
import pygame

pygame.init()


def note_C1():
	num1.set("C_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/c1.wav")
	sound.play()


def note_CC1():
	num1.set("C#_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/c1s.wav")
	sound.play()

def note_D1():
	num1.set("D_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/d1.wav")
	sound.play()

def note_DD1():
	num1.set("D#_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/d1s.wav")
	sound.play()

def note_E1():
	num1.set("E_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/e1.wav")
	sound.play()

def note_F1():
	num1.set("F_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/f1.wav")
	sound.play()

def note_FF1():
	num1.set("F#_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/f1s.wav")
	sound.play()

def note_G1():
	num1.set("G_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/g1.wav")
	sound.play()

def note_GG1():
	num1.set("G#_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/g1s.wav")
	sound.play()

def note_A1():
	num1.set("A_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/a1.wav")
	sound.play()

def note_AA1():
	num1.set("A#_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/a1s.wav")
	sound.play()

def note_B1():
	num1.set("B_1")
	sound = pygame.mixer.Sound("wav-piano-sound-master/wav/b1.wav")
	sound.play()



class MypianoGUI:
	def __init__(self, master):
		self.master = master
		master.title("Gaurav's__piano_GUI")        

		self.Label = Label(master , text="8 octave grand piano")
		self.Label.grid(row=0 , columnspan=11)  


		#Buttons for octave 1         
		self.C_1_button = Button(master, bg="white",text="C_1", command=note_C1 ,height=10 , width=3)

		self.C_1_button.grid(row=5,column=0)

		self.CC_1_button = Button(master ,bg="black" , fg="white",text="C#_1" ,command=note_CC1 ,height=10 ,width=2)
		self.CC_1_button.grid(row=1,columnspan=2)

		self.DD_1_button = Button(master ,bg="black" , fg="white",text="D#_1" ,command=note_DD1,height=10 ,width=2)
		self.DD_1_button.grid(row=1,columnspan=4)

		self.D_1_button = Button(master, bg="white", text="D_1" ,command=note_D1,height=10 , width=3)
		self.D_1_button.grid(row=5 , column=1)

		self.E_1_button = Button(master, bg="white", text="E_1" ,command=note_E1,height=10 , width=3)
		self.E_1_button.grid(row=5 , column=2)

		self.F_1_button = Button(master, bg="white", text="F_1" ,command=note_F1,height=10 , width=3)
		self.F_1_button.grid(row=5 , column=3)

		self.FF_1_button = Button(master , bg="black", fg="white",text="F#_1" , command=note_FF1,height=10 ,width=2)
		self.FF_1_button.grid(row=1,column=3 ,columnspan=2)

		self.G_1_button = Button(master, bg="white",text="G_1" ,command=note_G1,height=10 , width=3)
		self.G_1_button.grid(row=5 , column=4)

		self.GG_1_button = Button(master,bg="black" ,fg="white",text="G#_1" , command=note_GG1,height=10 ,width=2)
		self.GG_1_button.grid(row=1, column = 4 , columnspan=2)

		self.A_1_button = Button(master, bg="white",text="A_1" ,command=note_A1,height=10 , width=3)
		self.A_1_button.grid(row=5 , column=5)

		self.AA_1_button = Button(master,bg="black" ,fg="white",text="A#_1" , command=note_AA1,height=10 ,width=2)
		self.AA_1_button.grid(row=1, column = 5 , columnspan=2)

		self.B_1_button = Button(master, bg="white",text="B_1" ,command=note_B1,height=10 , width=3)
		self.B_1_button.grid(row=5 , column=6)



           

		

root = Tk()
my_gui = MypianoGUI(root)
num1 = StringVar()






root.mainloop()   
