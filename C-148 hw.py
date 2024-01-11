from tkinter import * 
import random

root = Tk()
root.geometry("400x400")
root.title("Picnic List Bag")


Label1 = Label(root)
Label2 = Label(root)

List = ['Bottle' ,'Tiffin' , "ID Card" , 'Chocolates' ,'Chips' , 'Ticket' ,'Hanky']
Label1['text'] = "Listed items : " + str(List)

def random_function():
    ran_list = random.sample(range(0,7),1)
    Label2['text'] = "Put item number " + str(ran_list) + " in the bag"
    


Label1.place(relx = 0.5 , rely = 0.3 , anchor = CENTER)
btn = Button(root , text = 'Which nubmer to put in bag?' , command = random_function)
btn.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
Label2.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)


root.mainloop()
