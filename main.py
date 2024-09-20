import tkinter as tk
main = tk.Tk()

def choice():
    def dtbh():
        numberstr = dtbh_entry.get()
        try:
            out_dtbh1 = bin(int(numberstr))[2:]
            out_dtbh2 = hex(int(numberstr))[2:]
            ausgang_b.config(text="Binärcode ist: " + out_dtbh1)
            ausgang_h.config(text="Hexadezimale Code ist: " + out_dtbh2)
        except ValueError:
            ausgang_b.config(text="Gib bitte eine richige Nummer ein!")
            ausgang_h.config(text=" ")

    def btd():
        bin_str = btd_entry.get()
        try:
            out_btd = int(bin_str, 2)
            ausgang_btd.config(text="Die Nummer ist: " + str(out_btd))
        except ValueError:
            ausgang_btd.config(text="Gib bitte eine richige Code ein!")

    def htd():
        hex_str = htd_entry.get()
        try:
            out_htd = int(hex_str, 16)
            ausgang_htd.config(text="Die Nummer ist: " + str(out_htd))
        except ValueError:
            ausgang_htd.config(text="Gib bitte eine richige Code ein!")

    if x.get()==0:
        dtbh_window = tk.Toplevel()
        dtbh_window.geometry('500x140')
        dtbh_window.title("Decimal to Binary and Hexadecimal")

        dtbh_label = tk.Label(dtbh_window, text="Gib eine Nummer ein")
        dtbh_label.pack()

        dtbh_entry = tk.Entry(dtbh_window)
        dtbh_entry.pack()

        dtbh_button = tk.Button(dtbh_window, text="Submit", command=dtbh)
        dtbh_button.pack()

        ausgang_h = tk.Label(dtbh_window)
        ausgang_h.pack()
        ausgang_b = tk.Label(dtbh_window)
        ausgang_b.pack()

        dtbh_window.mainloop()

    elif x.get()==1:
        btd_window = tk.Toplevel()
        btd_window.geometry('500x140')
        btd_window.title("Binary to Decimal")
        btd_label = tk.Label(btd_window, text="Gib Binärcode ein")
        btd_label.pack()

        btd_entry = tk.Entry(btd_window)
        btd_entry.pack()

        btd_button = tk.Button(btd_window, text="Submit", command=btd)
        btd_button.pack()

        ausgang_btd = tk.Label(btd_window)
        ausgang_btd.pack()

        btd_window.mainloop()
    else:
        htd_window = tk.Toplevel()
        htd_window.geometry('500x140')
        htd_window.title("Hexadecimal to Decimal")
        htd_label = tk.Label(htd_window, text="Gib Hexadezimale Code ein")
        htd_label.pack()
        htd_entry = tk.Entry(htd_window)
        htd_entry.pack()

        htd_button = tk.Button(htd_window, text="Submit", command=htd)
        htd_button.pack()

        ausgang_htd = tk.Label(htd_window)
        ausgang_htd.pack()

        htd_window.mainloop()

main.geometry('1000x300')
main.title("Number and Machine")
main.configure(background="lightgrey")

label_start = tk.Label(main, text="Choose one of the following converter", font = "Helvetica 18 bold", bg= 'light grey')
label_start.pack()

choices = ['Decimal to Binary and Haxadecimal', 'Binary to Decimal', 'Hexadecimal to Decimal']
x = tk.IntVar()
for index in range(len(choices)):
    options = tk.Radiobutton(main,
                             text=choices[index],
                             variable=x,
                             value=index,
                             padx=10,
                             font=("Arial", 35),
                             indicatoron=0,
                             width=30,
                             command= choice
                             )
    options.pack()

main.mainloop()
