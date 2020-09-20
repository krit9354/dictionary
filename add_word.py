import csv
import tkinter

def addWord():
    add = word.get()
    Fmean = mean.get()
    with open('word.csv', mode='a',newline="",encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([add,Fmean])

window = tkinter.Tk()
text1 = tkinter.Label(window, text="word to add : ").grid(row=0,column=0)
text2 = tkinter.Label(window, text="mean of word : ").grid(row=1,column=0)
button=tkinter.Button(window,text="click",command=addWord).grid(row=3,column=1)
word = tkinter.Entry(window,width=10)
mean = tkinter.Entry(window,width=10)
word.grid(row=0,column=1)
mean.grid(row=1,column=1)
window.mainloop()
