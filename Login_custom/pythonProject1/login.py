import customtkinter as ct
from PIL import Image, ImageTk
def button_callback():
    print("button clicked")





app = ct.CTk()
app.title("GIIKA")
app.geometry("500x400")

label = ct.CTkLabel(app,text="Bienvenue à GIIKA Login", font=("Protest Revolution", 50))
label.pack(pady=20)

frame = ct.CTkFrame(master=app)
frame.pack(pady=20,padx=40, fill='both',expand=True)



label = ct.CTkLabel(master=frame,text='Formulaire à compléter',font=("Parkisans",30))
label.pack(pady=12, padx=10)

user_entry = ct.CTkEntry(master=frame,placeholder_text="Nom" ,font=("Parkisans",15),width=300,height=40)
user_entry.pack(pady=12,padx=10)

user_entry = ct.CTkEntry(master=frame,placeholder_text="Prenom",font=("Parkisans",15),width=300,height=40)
user_entry.pack(pady=12,padx=10)

user_pass = ct.CTkEntry(master=frame, placeholder_text="Mot de Passe",font=("Parkisans",15),  show="*",width=300,height=40)
user_pass.pack(pady=12,padx=10)

button = ct.CTkButton(master=frame, text='Login')
button.pack(pady=12, padx=10)

checkbox = ct.CTkCheckBox(master=frame,text='Se souvenir de moi')
checkbox.pack(pady=12,padx=10)


app.mainloop()