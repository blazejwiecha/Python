from tkinter import Tk, Button
root = Tk()

def click_action():
    print("Wow!")

root.title('Tester netu')
root.geometry("600x400")

click_button = Button(root, text="Google.com", width=8, command=click_action)
click_button.pack()
root.mainloop()