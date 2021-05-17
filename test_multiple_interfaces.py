
from tkinter import *
import tkinter.ttk as ttk
import base64
import enigma

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NSEW')
        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        self.cvs = Canvas(self, width="500", height="300")
        ttk.Label(self, text='ENCODE DECODE', font='arial 20 bold').pack()
        ttk.Label(self, text='DataFlair', font='arial 20 bold').pack(side=BOTTOM)
        self.cvs.pack()

        # define variables

        Text = StringVar()
        private_key = StringVar()
        mode = StringVar()
        Result = StringVar()
        RadioButton = StringVar()

        #######define function#####

        # function to encode

        def Encode(key, message):
            enc = []
            for i in range(len(message)):
                key_c = key[i % len(key)]
                enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

            return base64.urlsafe_b64encode("".join(enc).encode()).decode()

        # function to decode

        def Decode(key, message):
            dec = []
            message = base64.urlsafe_b64decode(message).decode()
            for i in range(len(message)):
                key_c = key[i % len(key)]
                dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

            return "".join(dec)

        # function to set mode
        def Mode():
            if (mode.get() == 'e'):
                Result.set(Encode(private_key.get(), Text.get()))
            elif (mode.get() == 'd'):
                Result.set(Decode(private_key.get(), Text.get()))
            else:
                Result.set('Invalid Mode')

        # Function to exit window

        def Exit():
            self.destroy()

        # Function to reset
        def Reset():
            Text.set("")
            private_key.set("")
            mode.set("")
            Result.set("")

        def Change():
            print("TEST")

        #################### Label and Button #############

        # Message
        Label(self, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
        Entry(self, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)

        # key
        Label(self, font='arial 12 bold', text='KEY').place(x=60, y=90)
        Entry(self, font='arial 10', textvariable=private_key, bg='ghost white').place(x=290, y=90)

        # mode
        Label(self, font='arial 12 bold', text='MODE(e-encode, d-decode)').place(x=60, y=120)
        Entry(self, font='arial 10', textvariable=mode, bg='ghost white').place(x=290, y=120)

        # result
        Entry(self, font='arial 10 bold', textvariable=Result, bg='ghost white').place(x=290, y=150)

        ######result button
        Button(self, font='arial 10 bold', text='RESULT', padx=2, bg='LightGray', command=Mode).place(x=60, y=150)

        # reset button
        Button(self, font='arial 10 bold', text='RESET', width=6, command=Reset, bg='LimeGreen', padx=2).place(x=80,
                                                                                                               y=190)

        # change encription button
        Button(self, font='arial 10 bold', text='CHANGE', width=6, command=lambda: self.controller.show_frame(PageTwo), bg='LimeGreen', padx=2).place(x=280,
                                                                                                                 y=190)

        # # exit button
        # Button(self, font='arial 10 bold', text='EXIT', width=6, command=Exit, bg='OrangeRed', padx=2, pady=2).place(
        #     x=180, y=190)
        Button(self, font='arial 10 bold', text="Algo 2", fg="black", width="5", height="1", command=lambda: self.controller.show_frame(PageTwo)).place(x=0, y=0)
        Button(self, font='arial 10 bold', text="Algo 3", fg="black", width="5", height="1", command=lambda: self.controller.show_frame(PageTwo)).place(x=50, y=0)

        # def change_page(self):
        #     pass



class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()
    def make_widget(self):
        # ttk.Label(self, text='This is page two').grid(padx=(20,20), pady=(20,20))
        # button1 = ttk.Button(self, text='Previous Page', command=lambda: self.controller.show_frame(PageOne))
        # button1.grid()
        Text = StringVar()
        private_key = StringVar()
        mode = StringVar()
        Result = StringVar()
        RadioButton = StringVar()
        def Mode():
            Result.set(enigma.enigma(Text.get()))
        Button(self, font='arial 10 bold', text="Algo 2", fg="black", width="5", height="1",
               command=lambda: self.controller.show_frame(PageOne)).place(x=0, y=0)
        Button(self, font='arial 10 bold', text="Algo 3", fg="black", width="5", height="1",
               command=lambda: self.controller.show_frame(PageOne)).place(x=50, y=0)
        # result
        Entry(self, font='arial 10 bold', textvariable=Result, bg='ghost white').place(x=290, y=150)

        ######result button
        Button(self, font='arial 10 bold', text='RESULT', padx=2, bg='LightGray', command=Mode).place(x=60, y=150)


        Label(self, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
        Entry(self, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)

if __name__ == '__main__':
    app = App()
    app.title("Message Encode and Decode")
    app.mainloop()