from tkinter import*
from PIL import Image, ImageTk
import speech_to_txt
import action 

root=Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")
#ask
def ask():
    user_val=speech_to_txt.speech_to_txt()
    print(f"Captured user input: {user_val}")
    if not user_val:
        text.insert(END, "user---> Could not recognize input.\n")
        return
    user_val = user_val.strip().lower()

    # Call the action.Action function
    bot_val = action.action(user_val)
    print(f"Action function returned: {bot_val}")
    text.insert(END,"user--->"+user_val+"\n")
    if bot_val!=None:
        text.insert(END,"BOT<---"+str(bot_val)+"\n")
    if bot_val=="ok sir":
        root.destroy()

def delete():
    text.delete("1.0","end")
    
    
def send():
    send=entry.get()
    bot=action.action(send)
    text.insert(END,"user--->"+send+"\n")
    if bot!=None:
        text.insert(END,"BOT<---"+str(bot)+"\n")
    if bot=="ok sir":
        root.destroy()


# frame
frame=LabelFrame(root, padx=100,pady=7, borderwidth=3,relief="raised")
frame.config(bg="#FFA500")
frame.grid(row=0,column=1,padx=55,pady=10)
# text label
text_label=Label(frame, text="AI Assistant", font=("comic sans ms",14, "bold"), bg="#00FFFF")
text_label.grid(row=0, column=0,padx=60,pady=10)

original_image = Image.open("assistant.png")
resized_image = original_image.resize((150, 150))  # Adjust width and height as needed
image = ImageTk.PhotoImage(resized_image)

#image=ImageTk.PhotoImage(Image.open("assistant.png"))
image_label=Label(frame, image=image,bg="#6F8FAF")
image_label.grid(row=1,column=0,pady=20)

# adding a text widget
text=Text(root, font=("courier 10 bold"), bg="#356696")
text.grid(row=2, column=0)
text.place(x=50,y=300,width=460,height=100)

# adding entry widget
entry=Entry(root, justify=CENTER)
entry.place(x=50,y=420,width=460,height=30)

#button 1
Button1=Button(root,text="ASK",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID, command=ask)
Button1.place(x=50, y=500)

#button2
Button2=Button(root,text="delete",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID, command=delete)
Button2.place(x=225, y=500)

#button3
Button3=Button(root,text="send",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID, command=send)
Button3.place(x=400, y=500)

root.mainloop()
