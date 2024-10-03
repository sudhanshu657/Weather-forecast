from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    try:
        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
        W_label1.config(text=data["weather"][0]["main"])
        Wb_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=f"{int(data['main']['temp']) - 273.15:.2f} °C")
        per_label1.config(text=data["main"]["pressure"])
    except requests.exceptions.RequestException as e:
        W_label1.config(text="Error")
        Wb_label1.config(text=str(e))
        temp_label1.config(text="")
        per_label1.config(text="")

win = Tk()
win.title("Weather App")
win.config(bg="pink")
win.geometry("500x550")

name_label = Label(win, text="Know Weather", font=("Times New Roman", 40, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
com = ttk.Combobox(win, text="weather", values=list_name, font=("Times New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

W_label = Label(win, text="Weather Climate", font=("Times New Roman", 10, "bold"))
W_label.place(x=25, y=260, height=50, width=150)

W_label1 = Label(win, text="", font=("Times New Roman", 10, "bold"))
W_label1.place(x=250, y=260, height=50, width=150)

Wb_label = Label(win, text="Weather Description", font=("Times New Roman", 10))
Wb_label.place(x=25, y=330, height=50, width=150)

Wb_label1 = Label(win, text="", font=("Times New Roman", 10))
Wb_label1.place(x=250, y=330, height=50, width=150)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 10))
temp_label.place(x=25, y=400, height=50, width=150)

temp_label1 = Label(win, text="", font=("Times New Roman", 10))
temp_label1.place(x=250, y=400, height=50, width=150)

per_label = Label(win, text="Pressure", font=("Times New Roman", 10))
per_label.place(x=25, y=470, height=50, width=150)

per_label1 = Label(win, text="", font=("Times New Roman", 10))
per_label1.place(x=250, y=470, height=50, width=150)

done_button = Button(win, text="SEARCH", font=("Times New Roman", 10, "bold"), command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()
