import csv
import tkinter
dict = {}


with open("word.csv",mode="r",encoding='utf-8')as cvs_file:
    reader = csv.reader(cvs_file, delimiter=',')
    for row in reader:
        if row != []:
            dict[row[0]] = row[1]
        else:
            pass

def searchWord():
    sellect = user.get()
    if sellect in dict.keys():
        print("mean :", dict[sellect])
        text = tkinter.Label(window, text="mean : "+dict[sellect]).grid(row=0,column=1)
    else:
        print("errror!.try again")

window = tkinter.Tk()
button=tkinter.Button(window,text="click",command=searchWord).grid(row=1)
user = tkinter.Entry(window,width=10)
user.grid(row=0,column=0)
window.mainloop()