import PyPDF2
import pprint
from PyPDF2.pdf import PdfFileReader
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("tkinterTest")

entry1 = Entry(root)

pdfList = ["eng", "chapter1", "AZ1117E"]

selectPDF = StringVar()
selectPDF.set(pdfList[0])
opm = OptionMenu(root, selectPDF, *pdfList)
label = Label(root, text="Select_PDF :")
label2 = Label(root, text="Select_Page :")


def clickOK():
    File = PdfFileReader(open(selectPDF.get() + '.pdf', 'rb'))
    page_cound = File.getNumPages()
    pprint.pprint(page_cound)

    ageList = []
    for i in range(0, page_cound):
        try:
            if i == entry1.get():
                ageList.append(File.getPage(i).extractText())
                pprint.pprint(ageList[int(0)])
        except:
            print("except")


button = Button(root, text="OK", command=clickOK)
label.grid(row=0)
label2.grid(row=1, column=0)
opm.grid(row=0, column=1)
button.grid(row=2, column=1)
entry1.grid(row=1, column=1)
root.mainloop()