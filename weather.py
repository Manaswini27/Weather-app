from tkinter import*
from tkinter import ttk
import requests

def data_get():
 city=city_name.get()

 data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c4d0200d21b58dc5679daf87628b7a75").json()
 w1_label.config(text=data["weather"][0]["main"])
 d1_label.config(text=data["weather"][0]["description"])
 t1_label.config(text=str(int(data["main"]["temp"]-273.15)))
 p1_label.config(text=data["main"]["pressure"])

win=Tk()
win.title("MY Weather App")
win.config(bg="light blue")
win.geometry("500x500")

name_label=Label(win,text="WEATHER APP",
                 font=("Lucida Handwriting",40,"bold"))
name_label.place(x=25,y=50,height=45,width=450)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu& Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra &Nagar Haveli","Daman & Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com= ttk.Combobox(win,text="WEATHER APP", values= list_name,
                 font=("Century Schoolbook",25,"bold"),textvariable= city_name)
com.place(x=25,y=135,height=40,width=450)

w_label=Label(win,text="Weather Climate",
                 font=("Lucida Handwriting",15))
w_label.place(x=25,y=250,height=40,width=235)
w1_label=Label(win,text="",
                 font=("Times New Roman",15))
w1_label.place(x=275,y=250,height=40,width=200)

d_label=Label(win,text="Weather Description",
                 font=("Lucida Handwriting",15))
d_label.place(x=25,y=310,height=40,width=235)
d1_label=Label(win,text="",
                 font=("Times New Roman",15))
d1_label.place(x=275,y=310,height=40,width=200)

t_label=Label(win,text="Temperature",
                 font=("Lucida Handwriting",15))
t_label.place(x=25,y=370,height=40,width=235)
t1_label=Label(win,text="",
                 font=("Times New Roman",15))
t1_label.place(x=275,y=370,height=40,width=200)

p_label=Label(win,text="Pressure",
                 font=("Lucida Handwriting",15))
p_label.place(x=25,y=430,height=40,width=235)
p1_label=Label(win,text="",
                 font=("Times New Roman",15))
p1_label.place(x=275,y=430,height=40,width=200)

done_button = Button(win,text="Done",
                 font=("Times New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=110,x=195)



win.mainloop()