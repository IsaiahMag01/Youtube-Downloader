import tkinter
import customtkinter
from pytube import YouTube

#Credit to : https://youtu.be/NI9LXzo0UY0 for idea for base application

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title)
        finishLabel.configure(text="")

        video.download()
        finishLabel.configure(text="Downloaded!", text_color="green")
    except:
        finishLabel.configure(text="Youtube link is invalid", text_color="red")
    
def on_progress(stream, chunk, bytes_remaining): #Comes from the youtube class in pytube
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion)) #Removes all floating poitns and converts to a string so we can add it to the UI
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #Update progress bar
    progressBar.set(float(percentage_of_completion) /100) #Gives us a value between 0 and 1 for our percentage bar to use to fill itself

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

#finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(padx=10, pady=10)

#Progres Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack(padx=10, pady=10)

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack()


#Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)


#run app
app.mainloop()


#Test Youtube Video Link : https://youtu.be/XLiVVS6nTHo
