import openpyxl
import  requests
# import readWord
import docx
from docx import Document

book = openpyxl.open("Links.xlsx", "read_only=True")
sheet = book.active



def download_file(valueLink, filename):
    filename = 'allFiles/'+filename
    # filename='«МСЧ МВД России по г. Москве» 20.07.2017.docx'
    r= requests.get(valueLink,allow_redirects = True)
    open(filename, "wb").write(r.content)
    # readWord.checkFile(filename)

i=1
while(i!=-1):
    a = 'A' + str(i)
    b = 'B' + str(i)
    valueLink = sheet[b].value
    if (valueLink) != None:
        name = sheet[a].value+'.doc'
        download_file(valueLink, name)
        i+=1
    else:
        print(i-1)
        i=-1

























