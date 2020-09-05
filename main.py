# Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os
from tkinter import *
from tkinter import messagebox


def main():
    def Mp3():

        url = url_input.get()
        # Get the article
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Get the articles text
        mytext = article.text
        language = 'en'  # English
        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=mytext, lang=language, slow=False)
        # myobj.save("read_article.mp3")

      # save Mp3
        urlSplit = url.split("/")[-1:]
        urlToString = ' '.join([str(elem) for elem in urlSplit])
        myobj.save(filename_input.get()+'.mp3')

        # display succesful message box
        url_input.delete(0, "end")
        filename_input.delete(0, "end")
        messagebox.showinfo("Successfully", "Document saved")

    root = Tk()
    root.geometry('500x500')
    root.title("Save news to Mp3 from URL ")

    # Label for url
    url_label = Label(root, text='URL', font=('Arial', 16))
    url_label.place(x=50, y=100)

    # Input box for url
    url_input = Entry(root, bd=2, font=('Arial', 12), width=30)
    url_input.place(x=180, y=100)

    # Label for filename
    filename_label = Label(root, text='MP3 name', font=('Arial', 16))
    filename_label.place(x=50, y=150)

    # Input box for filename
    filename_input = Entry(root, bd=2, font=('Arial', 12), width=30)
    filename_input.place(x=180, y=150)

    # save button
    btn_save = Button(root, text="Save", font=(
        'Bold', 18), bg="Yellow", command=Mp3)
    btn_save.place(x=200, y=250)

    root.mainloop()


main()
