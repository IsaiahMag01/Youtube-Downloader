import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = Youtube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("Youtube link is invalid") #Sends to the consol
    print("Download Complete!")


#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10) #puts our UI Element on the frame

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack()

#run app
app.mainloop()