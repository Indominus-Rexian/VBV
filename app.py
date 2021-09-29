import tkinter as tk

while True:
    window1 = tk.Tk()
    window1.geometry("500x500")
    window1.title("Total safe Button")
    text1 = tk.Label(master=window1,text=" ",foreground="red")
    btn1 = tk.Button(text="Please Press me",relief=tk.RIDGE)

    def button_click(event):
        while True:
            text1["text"] = "U pressed the wrong button!! Muahaha!"
            window2 = tk.Tk()
            window2.geometry("800x800")
            window2.title("Try to close me")
            text2 = tk.Label(master=window1,text="Dont worry! U cannot close this screen now!",foreground="red")
            text3 = tk.Label(master=window2,text="Can you even close me now??",foreground="white")
            text2.pack()
            text3.pack()
            window2.mainloop()

            

    def button_close(event) :
        window1.destroy()

    
    btn1.pack()
    btn1.bind("<Button-1>",button_click)
    window1.bind("<c>",button_close)
    text1.pack()
    window1.mainloop()