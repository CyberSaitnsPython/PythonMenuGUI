from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image


class DrGui:

    def __init__(self):
        main = Tk()
        m = main.maxsize()
        main.geometry('{}x{}+0+0'.format(*m))
        main.resizable(0, 0)
        main.attributes('-topmost', True)

        path = 'Images/BW.jpeg'
        path2 = 'Images/SD.jpg'
        path3 = 'Images/C&D.jpg'
        path4 = 'Images/CF.jpg'
        path5 = 'Images/SS.jpg'
        path6 = 'Images/GC.jpg'
        path7 = 'Images/BCB.jpg'
        path8 = 'Images/GS.jpg'
        path9 = 'Images/F.jpg'
        path10 = 'Images/IC.jpg'
        path11 = 'Images/S.jpg'
        path12 = 'Images/CK.jpg'
        
        img = ImageTk.PhotoImage(Image.open(path))
        img2 = ImageTk.PhotoImage(Image.open(path2))
        img3 = ImageTk.PhotoImage(Image.open(path3))
        img4 = ImageTk.PhotoImage(Image.open(path4))
        img5 = ImageTk.PhotoImage(Image.open(path5))
        img6 = ImageTk.PhotoImage(Image.open(path6))
        img7 = ImageTk.PhotoImage(Image.open(path7))
        img8 = ImageTk.PhotoImage(Image.open(path8))
        img9 = ImageTk.PhotoImage(Image.open(path9))
        img10 = ImageTk.PhotoImage(Image.open(path10))
        img11 = ImageTk.PhotoImage(Image.open(path11))
        img12 = ImageTk.PhotoImage(Image.open(path12))

        rows = 0
        while rows < 50:
            main.rowconfigure(rows, weight=1)
            main.columnconfigure(rows, weight=1)
            rows += 1

        column = 0
        while column < 50:
            main.rowconfigure(column, weight=1)
            main.columnconfigure(column, weight=1)
            column += 1

        # Title
        # Label(main, text="Diner", bg="navy blue", fg="white", font="Helvetica 30 bold").grid(row=0, column=19)
        # Label(main, text="Diner", bg="navy blue", fg="white", font="Helvetica 30 bold").grid(row=0, column=2)
        
        # APPETIZERS
        # Labels
        Label(main, text="Appetizers", bg="navy blue", fg="white", font="Variane 14 bold").grid(row=1, column=9)
        Label(main, text="Qty.", bg="navy blue", fg="white", font="Helvetica 8 bold").grid(row=1, column=10)
        Label(main, compound=TOP, text="Buffalo Wings\n $6.99:", fg="white", bg="navy blue",
              image=img).grid(row=2, column=9)
        Label(main, compound=TOP, text="Side Salad \n $4.99:", fg="white", bg="navy blue",
              image=img2).grid(row=3, column=9)
        Label(main, compound=TOP, text="Chips & Dip\n $5.99:", fg="white", bg="navy blue",
              image=img3).grid(row=4, column=9)
        Label(main, compound=TOP, text="Cheese Fries\n $5.99:", fg="white", bg="navy blue",
              image=img4).grid(row=5, column=9)
        # Entries
        num1 = Entry(main) 
        num2 = Entry(main)
        num3 = Entry(main)
        num4 = Entry(main)
        num1.grid(row=2, column=10)
        num2.grid(row=3, column=10)
        num3.grid(row=4, column=10)
        num4.grid(row=5, column=10)
        
        # ENTREES
        # Labels
        Label(main, text="Entrees", bg="navy blue", fg="white", font="Helvetica 14 bold").grid(row=1, column=19)
        Label(main, text="Qty.", bg="navy blue", fg="white", font="Helvetica 8 bold").grid(row=1, column=20)
        Label(main, compound=TOP, text="Sirloin Steak\n $14.99:", fg="white", bg="navy blue",
              image=img5).grid(row=2, column=19)
        Label(main, compound=TOP, text="Grilled Chicken\nw/ Vegetables\n $8.99:", fg="white", bg="navy blue",
              image=img6).grid(row=3, column=19)
        Label(main, compound=TOP, text="Bacon Cheeseburger\n $10.99:", fg="white", bg="navy blue",
              image=img7).grid(row=4, column=19)
        Label(main, compound=TOP, text="Grilled Salmon\n $9.99:", fg="white", bg="navy blue",
              image=img8).grid(row=5, column=19)
        # Entries
        num5 = Entry(main)
        num6 = Entry(main)
        num7 = Entry(main)
        num8 = Entry(main)
        num5.grid(row=2, column=20)
        num6.grid(row=3, column=20)
        num7.grid(row=4, column=20)
        num8.grid(row=5, column=20)
        
        # DESSERTS
        Label(main, text="Desserts", bg="navy blue", fg="white", font="Helvetica 14 bold").grid(row=1, column=29)
        Label(main, text="Qty.", bg="navy blue", fg="white", font="Helvetica 8 bold").grid(row=1, column=30)
        Label(main, compound=TOP, text="Flan\n $6.99:", fg="white", bg="navy blue",
              image=img9).grid(row=2, column=29)
        Label(main, compound=TOP, text="Ice Cream\n(Chocolate or Vanilla)\n $5.99:", fg="white", bg="navy blue",
              image=img10).grid(row=3, column=29)
        Label(main, compound=TOP, text="Sorbet\n $4.99:", fg="white", bg="navy blue",
              image=img11).grid(row=4, column=29)
        Label(main, compound=TOP, text="Cake\n $8.99:", fg="white", bg="navy blue",
              image=img12).grid(row=5, column=29)
        # Entries
        num9 = Entry(main)
        num10 = Entry(main)
        num11 = Entry(main)
        num12 = Entry(main)
        num9.grid(row=2, column=30)
        num10.grid(row=3, column=30)
        num11.grid(row=4, column=30)
        num12.grid(row=5, column=30)
        
        def average():
            if num1.get() != "":
                n1 = int(num1.get())
                return n1*6.99
            else:
                return 0

        def average2():
            if num2.get() != "":
                n2 = int(num2.get())
                return n2*4.99
            else:
                return 0

        def average3():
            if num3.get() != "":
                n3 = int(num3.get())
                return n3*5.99
            else:
                return 0

        def average4():
            if num4.get() != "":
                n4 = int(num4.get())
                return n4*5.99
            else:
                return 0

        def average5():
            if num5.get() != "":
                n5 = int(num5.get())
                return n5*14.99
            else:
                return 0

        def average6():
            if num6.get() != "":
                n6 = int(num6.get())
                return n6*8.99
            else:
                return 0

        def average7():
            if num7.get() != "":
                n7 = int(num7.get())
                return n7*10.99
            else:
                return 0

        def average8():
            if num8.get() != "":
                n8 = int(num8.get())
                return n8*9.99
            else:
                return 0

        def average9():
            if num9.get() != "":
                n9 = int(num9.get())
                return n9*6.99
            else:
                return 0

        def average10():
            if num10.get() != "":
                n10 = int(num10.get())
                return n10*5.99
            else:
                return 0

        def average11():
            if num11.get() != "":
                n11 = int(num11.get())
                return n11*4.99
            else:
                return 0

        def average12():
            if num12.get() != "":
                n12 = int(num12.get())
                return n12*8.99
            else:
                return 0

        def total():
            showinfo("Total", average() + average2() + average3() + average4() + average5() + average6() + average7() +
                     average8() + average9() + average10() + average11() + average12())

        Button(main, text='Check Please!', command=total, width=15).grid(row=6, column=19)
        Button(main, text='Just water for now', command=main.destroy, width=15).grid(row=7, column=19)
        main["bg"] = "navy blue"
        mainloop()


my_gui = DrGui()
