from tkinter import *
from tkinter.font import families
from Busquedas import *


def proceso(frame,i,nombre,n):
         #------------------LOGO------------------
        img = PhotoImage(file="LogosFrame/"+nombre[0]+".png")
        lblLogo = Label(frame, image=img,background="white").place(x=50,y=40)

        #------------------Valores------------------
        
        #Precio
        precio=Label(frame,text=i[n])
        precio.place(x=200,y=300, anchor="center")
        precio.config(font=("Bahnschrift SemiBold SemiConden", 45))
        precio.config(fg="green",background="white")
 
        frame.mainloop()

def frame_botones(root,nombre):
    frame=Toplevel(root)

    ancho_ventana =400
    alto_ventana=500

    x_ventana = frame.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = frame.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    frame.geometry(posicion)
    frame.config(background="white")
    frame.resizable(0,0)
    frame.title(nombre[0])
    frame.iconbitmap("Iconos/"+nombre[0]+".ico")
    return frame

def main():

    def primer_boton():
        i=buscar_datos()
        nombre=i[0]
        frame=frame_botones(root,nombre)
        proceso(frame,i,nombre,1)
    
    def segundo_boton():
        i=buscar_datos()
        nombre=i[2]
        frame=frame_botones(root,nombre)
        proceso(frame,i,nombre,3)
        
    def tercer_boton():
        i=buscar_datos()
        nombre=i[4]
        frame=frame_botones(root,nombre)
        proceso(frame,i,nombre,5)

    def cuarto_boton():
        i=buscar_datos()
        nombre=i[6]
        frame=frame_botones(root,nombre)
        proceso(frame,i,nombre,7)

    def quinto_boton():
        i=buscar_datos()
        nombre=i[8]
        frame=frame_botones(root,nombre)
        proceso(frame,i,nombre,9)

    def sexto_boton():
        i=buscar_datos()
        nombre=i[10]
        frame=frame_botones(root,nombre)
        proceso(frame,i,nombre,11)
    
    #------------------Data------------------
    i=buscar_datos()
    nombre1=i[0]
    nombre2=i[2]
    nombre3=i[4]
    nombre4=i[6]
    nombre5=i[8]
    nombre6=i[10]

    #------------------Frame------------------
    root=Tk()

    ancho_ventana =400
    alto_ventana=500

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    root.geometry(posicion)
    root.configure(background="white")
    root.title("Crypto View")
    root.iconbitmap('Iconos/Logo.ico')
    #root.resizable(width=False,height=False)

    logo=PhotoImage(file="LogosMain/Logo.png")

    img1=PhotoImage(file="LogosMain/"+nombre1[0]+".png")
    img2=PhotoImage(file="LogosMain/"+nombre2[0]+".png")
    img3=PhotoImage(file="LogosMain/"+nombre3[0]+".png")
    img4=PhotoImage(file="LogosMain/"+nombre4[0]+".png")
    img5=PhotoImage(file="LogosMain/"+nombre5[0]+".png")
    img6=PhotoImage(file="LogosMain/"+nombre6[0]+".png")
    

    btnLogo=Label(root,image=logo,height=170,width=300,background="black").place(x=50,y=50)

    btn1=Button(root,image=img1,height=70,width=70,command=primer_boton).place(x=50,y=250)
    btn2=Button(root,image=img2,height=70,width=70,command=segundo_boton).place(x=165,y=250)
    btn3=Button(root,image=img3,height=70,width=70,command=tercer_boton).place(x=280,y=250)
    btn4=Button(root,image=img4,height=70,width=70,command=cuarto_boton).place(x=50,y=350)
    btn5=Button(root,image=img5,height=70,width=70,command=quinto_boton).place(x=165,y=350)
    btn6=Button(root,image=img6,height=70,width=70,command=sexto_boton).place(x=280,y=350)

    root.mainloop()     

if __name__ == '__main__':
    main()



