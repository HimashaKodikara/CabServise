import tkinter
from tkinter import  *
from tkinter import ttk, Listbox
root = Tk()


root.config(background="red",highlightbackground='black',bd=5,bg='grey')
root.geometry("1800x1000")
root.title('Dashboard')





Car = [["2345","3", "AC"], ["2456","3","NonAC"],[ "2598","6","AC"], ["2987","6","NonAC"], ]
Van = [["5615","6","AC"], ["9867","6","NonAC"], ["5679","8","AC"], ["9875","8","NonAC"]]
ThreeWheeler = [["6798","3"]]
Lorry = [["3697","2500kg"], ["9875","3500kg"]]
Truck = [["9875","7ft"], ["9875","12ft"]]
hireJobs = [["Gayan","25","18946799v","gayan@gamil.com","5497B","0749872587",]
    ,["Wanidu","24","587945541V","wandu@gamil.com","97845A","0798451454"]]



carlen=(len(Car))
Vanlen=(len(Van))
ThreeWheelerslen=(len(ThreeWheeler))
Lorrylen=(len(Lorry))
Trukslen=(len(Truck))

details = ttk.Frame(root)
details.grid(row=6,column=10)
def CarFunc():
    addWin = Toplevel(root)
    addWin.geometry("700x500")
    addWin.title("Car details")
    row = 2
    ttk.Label(addWin, text="---Car Details---", font=('Arial', 18)).grid(row=1, column=2, padx=40, pady=20)

    for num in Car:
       ttk.Label(addWin,font=(13),text="Vehicle No : "+num[0]).grid(row=row,column=1,padx=40, pady=10)
       ttk.Label(addWin,font=(13),text="Passengers : "+num[1]).grid(row=row,column=2)
       ttk.Label(addWin,font=(13),text="AC Type : "+num[2]).grid(row=row,column=3)
       row+=1


def VanFunc():
    addWin = Toplevel(root)
    addWin.geometry("700x500")
    addWin.title('Van details')
    row=2
    ttk.Label(addWin, text="---Van Details---", font=('Arial', 18)).grid(row=1, column=2, padx=40, pady=10)

    for num in Van:
        ttk.Label(addWin, font=(13), text="Vehicle No : " + num[0]).grid(row=row, column=1,padx=40, pady=10)
        ttk.Label(addWin, font=(13), text="Passengers : " + num[1]).grid(row=row, column=2)
        ttk.Label(addWin, font=(13), text="AC Type : " + num[2]).grid(row=row, column=3)
        row += 1

def LorryFunc():
    addWin = Toplevel(root)
    addWin.geometry("700x500")
    addWin.title('Lorry details')

    row = 2
    ttk.Label(addWin, text="---Lorry details---", font=('Arial', 18)).grid(row=1, column=2, padx=40, pady=10)

    for num in Lorry:
        ttk.Label(addWin, font=(13), text="Vehicle No : " + num[0]).grid(row=row, column=1,padx=40, pady=10)
        ttk.Label(addWin, font=(13), text="Weight : " + num[1]).grid(row=row, column=2)

        row += 1


def TruckFunc():
    addWin = Toplevel(root)
    addWin.geometry("700x500")
    addWin.title('Truck details')
    ttk.Label(addWin, text="---Truck Details---", font=('Arial', 18)).grid(row=1, column=2, padx=40, pady=10)
    row = 2

    for num in Truck:
        ttk.Label(addWin, font=(13), text="Vehicle No : " + num[0]).grid(row=row, column=1, padx=40, pady=10)
        ttk.Label(addWin, font=(13), text="Feet of Truck : " + num[1]).grid(row=row, column=2)

        row += 1


def ThreewheelFunc():
    addWin = Toplevel(root)
    addWin.geometry("700x500")
    addWin.title('ThreeWeel details')
    ttk.Label(addWin, text="---Threewhel Details---", font=('Arial', 18)).grid(row=1, column=2, padx=40, pady=10)
    row=2
    for num in ThreeWheeler:
        ttk.Label(addWin, font=(13), text="Vehicle No : " + num[0]).grid(row=row, column=1, padx=40, pady=10)
        ttk.Label(addWin, font=(13), text="Passengers : " + num[1]).grid(row=row, column=2)

        row += 1




def addvehicle():

    if vehicle_type.get() =="Car":
        Adddetails=Toplevel(root)
        Adddetails.geometry("300x100")
        Adddetails.title('Add car')
        Adddetails.config(background="purple")
        vehicle_n=vehicle_no.get()
        newVehicle = Ac_type.get()
        passenger=Passenger.get()
        list=[vehicle_n,passenger,newVehicle]
        Car.append(list)
        print(Car)
        newlen=len(Car)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=12, column=2, padx=10, pady=10)

        ttk.Label(Adddetails, text="New Car add succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50, pady=50)

    elif vehicle_type.get() =="Van":
        Adddetails = Toplevel(root)
        Adddetails.geometry("300x100")
        Adddetails.title('Add van')
        Adddetails.config(background="purple")
        vehicle_n = vehicle_no.get()
        newVehicle = Ac_type.get()
        passenger = Passenger.get()
        vanlist=[vehicle_n,passenger,newVehicle]
        Van.append(vanlist)
        print(Van)
        newlen=len(Van)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=13, column=2, padx=10, pady=10)

        ttk.Label(Adddetails, text="New Van add succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50,
                                                                                        pady=50)
    elif vehicle_type.get() =="Lorry":
        Adddetails = Toplevel(root)
        Adddetails.geometry("300x100")
        Adddetails.title('Lorry details')
        Adddetails.config(background="purple")
        vehicle_n = vehicle_no.get()
        Max_Kgs=Max_Kg.get()
        lorrylist=[vehicle_n,Max_Kgs]
        Lorry.append(lorrylist)
        print(Lorry)
        newlen=len(Lorry)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=15, column=2, padx=10, pady=10)

        ttk.Label(Adddetails, text="New Lorry add succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50,pady=50)
    elif vehicle_type.get() =="Truck":
        Adddetails = Toplevel(root)
        Adddetails.geometry("300x100")
        Adddetails.title('Truck details')
        Adddetails.config(background="purple")
        vehicle_n=vehicle_no.get()
        FT_Siz=FT_Size.get()
        Truck.append([vehicle_n,FT_Siz])
        print(Truck)
        newlen=len(Truck)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=16, column=2, padx=10, pady=10)

        ttk.Label(Adddetails, text="New Trucks add succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50,pady=50)
    elif vehicle_type.get() == "Threeweel":
        Adddetails = Toplevel(root)
        Adddetails.title('ThreeWeel Details')
        Adddetails.geometry("300x100")
        Adddetails.config(background="purple")
        vehicle_n=vehicle_no.get()
        passenger = Passenger.get()
        ThreeWheeler.append([vehicle_n,passenger])
        print(ThreeWheeler)
        newlen=len(ThreeWheeler)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=14, column=2, padx=10, pady=10)
        ttk.Label(Adddetails, text="New Threeweel add succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50,
                                                                                        pady=50)
    else:
        Adddetails = Toplevel(root)
        Adddetails.geometry("300x100")
        Adddetails.config(background="purple")
        ttk.Label(Adddetails, text="Please enter correct value", font=('Arial', 13)).grid(row=6, column=10, padx=50,
                                                                                       pady=50)

def RemoveVehicle():

    if vehicle_type.get() =="Car":
        Redetails = Toplevel(root)
        Redetails.geometry("300x100")
        Redetails.config(background="purple")
        vehicle_n=vehicle_no.get()
        newVehicle = Ac_type.get()
        passenger=Passenger.get()
        Car.remove([vehicle_n,passenger,newVehicle])
        print(Car)
        newlen=len(Car)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=12, column=2, padx=10, pady=10)
        ttk.Label(Redetails, text="Car remove succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50, pady=50)

    elif vehicle_type.get() =="Van":
        Redetails = Toplevel(root)
        Redetails.geometry("300x100")
        Redetails.config(background="purple")
        vehicle_n = vehicle_no.get()
        newVehicle = Ac_type.get()
        passenger = Passenger.get()
        Van.remove([vehicle_n,passenger, newVehicle])
        print(Van)
        newlen=len(Van)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=13, column=2, padx=10, pady=10)
        ttk.Label(Redetails, text="Van remove succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50,
                                                                                        pady=50)
    elif vehicle_type.get() =="Lorry":
        Redetails = Toplevel(root)
        Redetails.geometry("300x100")
        Redetails.config(background="purple")
        vehicle_n = vehicle_no.get()
        Max_Kgs=Max_Kg.get()
        Lorry.remove([vehicle_n,Max_Kgs])
        print(Lorry)
        newlen=len(Lorry)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=15, column=2, padx=10, pady=10)
        ttk.Label(Redetails, text="Lorry remove succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50,pady=50)
    elif vehicle_type.get() =="Truck":
        Redetails = Toplevel(root)
        Redetails.geometry("300x100")
        Redetails.config(background="purple")
        vehicle_n = vehicle_no.get()
        FT_Siz=FT_Size.get()
        Truck.remove([vehicle_n,FT_Siz])
        print(Truck)
        newlen=len(Truck)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=16, column=2, padx=10, pady=10)
        ttk.Label(Redetails, text="Trucks remove succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=10,pady=10)
    elif vehicle_type.get() == "Threeweel":
        Redetails = Toplevel(root)
        Redetails.geometry("300x100")
        Redetails.config(background="purple")
        vehicle_n = vehicle_no.get()
        passenger = Passenger.get()
        ThreeWheeler.remove([vehicle_n,passenger])
        print(ThreeWheeler)
        newlen=len(ThreeWheeler)
        ttk.Label(details, text=newlen, font=('Arial', 13)).grid(row=14, column=2, padx=10, pady=10)
        ttk.Label(Redetails, text="Treeweel remove succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50,
                                                                                        pady=50)
    else:
        Redetails = Toplevel(root)
        Redetails.geometry("300x100")
        Redetails.config(background="purple")
        ttk.Label(Redetails, text="Please enter correct value", font=('Arial', 13)).grid(row=6, column=10, padx=50,
                                                                                       pady=50)

def delete():
    vehicle_type.set(" ")
    vehicle_no.set(" ")
    Ac_type.set(" ")
    Passenger.set(" ")
    FT_Size.set(" ")
    Max_Kg.set(" ")

def deletehire():
    name.set("")
    age.set("")
    ID.set("")
    email.set("")
    DID.set("")
    Mobile.set("")
    vehicle.set("")

def SelectVehicle():

    if vehicle_type.get() == "Car":
        CarFunc()

    elif vehicle_type.get() == "Van":
        VanFunc()

    elif vehicle_type.get() == "Lorry":
        LorryFunc()

    elif vehicle_type.get()== "Truck":
        TruckFunc()

    elif vehicle_type.get()== "ThreeWheeler":
        ThreewheelFunc()

    else:
        Searchvehicle = Toplevel(root)
        Searchvehicle.geometry("300x100")
        Searchvehicle.config(background="purple")
        ttk.Label(Searchvehicle, text="Please enter correct value", font=('Arial', 13)).grid(row=6, column=10,pady=50,padx=50)

def AssignJobs():
    if ID.get()=="":
        addWi = Toplevel(root)
        addWi.geometry("400x200")
        addWi.config(background="yellow")
        ttk.Label(addWi, font=(13), text="Please fill the form").grid(row=1, column=1, padx=50, pady=50)
    else:
        AssignJob = Toplevel(root)
        AssignJob.geometry("300x100")
        AssignJob.config(background="purple")
        AssignJob.title('Assign Job')
        Name = name.get()
        Age = age.get()
        id = ID.get()
        Email = email.get()
        did = DID.get()
        mobile = Mobile.get()
        list = [Name, Age, id, Email, did, mobile]
        hireJobs.append(list)
        print(hireJobs)
        ttk.Label(AssignJob, text="New Driver add succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50,
                                                                                         pady=50)

def AvailableDirvers():
    addWin = Toplevel(root)
    addWin.geometry("1500x400")
    addWin.config(background="yellow")
    addWin.title('Available Driver Details')
    ttk.Label(addWin, text="---Available Drivers---", font=('Arial', 18)).grid(row=1, column=4, padx=50, pady=50)
    row=2
    for num in hireJobs:
        ttk.Label(addWin, font=(13), text="Name : " + num[0]).grid(row=row, column=1, padx=30, pady=10)
        ttk.Label(addWin, font=(13), text="Age : " + num[1]).grid(row=row, column=2, padx=30, pady=10)
        ttk.Label(addWin, font=(13), text="ID : " + num[2]).grid(row=row, column=3, padx=30, pady=10)
        ttk.Label(addWin, font=(13), text="Email : " + num[3]).grid(row=row, column=4, padx=30, pady=10)
        ttk.Label(addWin, font=(13), text="Driving license No : " + num[4]).grid(row=row, column=5, padx=30, pady=10)
        ttk.Label(addWin, font=(13), text="Mobile No : " + num[5]).grid(row=row, column=6, padx=30, pady=10)


        row += 1


def RemoveJobs():
    if ID.get() == "":
        addWi = Toplevel(root)
        addWi.geometry("400x200")
        addWi.config(background="yellow")
        ttk.Label(addWi, font=(13), text="Please Enter ID that you want to remove").grid(row=1, column=1, padx=50, pady=50)
    else:
        ReJob = Toplevel(root)
        ReJob.geometry("300x100")
        ReJob.config(background="purple")
        Name = name.get()
        Age = age.get()
        id = ID.get()
        Email = email.get()
        did = DID.get()
        mobile = Mobile.get()
        list = [Name, Age, id, Email, did, mobile]
        hireJobs.remove(list)
        print(hireJobs)
        ttk.Label(ReJob, text="Driver record remove succesfully", font=('Arial', 13)).grid(row=6, column=10, padx=50, pady=50)

def Count():
    if n.get() == "Car":
        ReJob = Toplevel(root)
        ReJob.geometry("300x100")

        Kilo=Km.get()
        count=Kilo*120
        ttk.Label(ReJob, text="RS", font=('Arial', 13)).grid(row=6, column=1, padx=50, pady=50)
        ttk.Label(ReJob, text=count, font=('Arial', 13)).grid(row=6, column=2, padx=50, pady=50)

    elif n.get() == "Van":
        ReJob = Toplevel(root)
        ReJob.geometry("300x100")

        Kilo = Km.get()
        count = Kilo * 200
        ttk.Label(ReJob, text="RS", font=('Arial', 13)).grid(row=6, column=1, padx=50, pady=50)
        ttk.Label(ReJob, text=count, font=('Arial', 13)).grid(row=6, column=2, padx=50, pady=50)
    elif n.get() == "ThreeWheeler":
        ReJob = Toplevel(root)
        ReJob.geometry("300x100")

        Kilo = Km.get()
        count = Kilo * 60
        ttk.Label(ReJob, text="RS", font=('Arial', 13)).grid(row=6, column=1, padx=50, pady=50)
        ttk.Label(ReJob, text=count, font=('Arial', 13)).grid(row=6, column=2, padx=50, pady=50)
    elif n.get() == "Trucks":
        ReJob = Toplevel(root)
        ReJob.geometry("300x100")

        Kilo = Km.get()
        count = Kilo * 210
        ttk.Label(ReJob, text="RS", font=('Arial', 13)).grid(row=6, column=1, padx=50, pady=50)
        ttk.Label(ReJob, text=count, font=('Arial', 13)).grid(row=6, column=2, padx=50, pady=50)
    elif n.get() == "Lorry":
        ReJob = Toplevel(root)
        ReJob.geometry("300x100")

        Kilo = Km.get()
        count = Kilo * 190
        ttk.Label(ReJob, text="RS", font=('Arial', 13)).grid(row=6, column=1, padx=50, pady=50)
        ttk.Label(ReJob, text=count, font=('Arial', 13)).grid(row=6, column=2, padx=50, pady=50)


header = ttk.Frame(root)
header.grid(row=1,column=2)


ttk.Label(header, text="Welocome to cab service ",background='red', font=('Arial',25,'underline'), justify=CENTER).grid()

body = ttk.Frame(root)
body.grid(row=3,column=1,pady=0,padx=0)

ttk.Label(body,text="Vehicle No",font=('Arial',13)).grid(row=1,column=1,padx= 10, pady= 5)
vehicle_no=StringVar()
entry = ttk.Entry(body,textvariable=vehicle_no,width=30,).grid(row=1,column=4,padx= 10, pady= 10)

ttk.Label(body,text="Vehicle type",font=('Arial',13)).grid(row=2,column=1,padx= 10, pady= 5)
vehicle_type = StringVar()
monthchoosen = ttk.Combobox(body, width=27, textvariable=vehicle_type)

# Adding combobox drop down list
monthchoosen['values'] = ("Car", "Van", "ThreeWheeler", "Lorry", "Truck")

monthchoosen.grid(column=4, row=2)
monthchoosen.current()


ttk.Label(body,text="AC or Non AC",font=('Arial',13)).grid(row=3,column=1,padx= 10, pady= 10)
Ac_type=StringVar()
ttk.Entry(body,textvariable=Ac_type,width=30,).grid(row=3,column=4,padx= 10, pady= 10)

ttk.Label(body,text="Passenger",font=('Arial',13)).grid(row=4,column=1,padx= 10, pady= 10)
Passenger=StringVar()
ttk.Entry(body,textvariable=Passenger,width=30,).grid(row=4,column=4,padx= 10, pady= 10)

ttk.Label(body,text="FT Size (ft)",font=('Arial',13)).grid(row=5,column=1,padx= 10, pady= 10)
FT_Size=StringVar()
ttk.Entry(body,textvariable=FT_Size,width=30,).grid(row=5,column=4,padx= 10, pady= 10)

ttk.Label(body,text="MAX KG (Kg)",font=('Arial',13)).grid(row=6,column=1,padx= 10, pady= 10)
Max_Kg=StringVar()
ttk.Entry(body,textvariable=Max_Kg,width=30,).grid(row=6,column=4,padx= 10, pady= 10)

SelectVehicle=Button(body,text="Search",activebackground='red',activeforeground='yellow',
  bd=5,bg='green',fg='white' ,command=SelectVehicle,width=10).grid(row=7,column=1,padx= 10, pady= 50)
Button(body,text="ADD",activebackground='red',activeforeground='yellow',
  bd=5,bg='green',fg='white',command=addvehicle,width=10).grid(row=7,column=2,padx= 10, pady= 10)
Button(body,text="Remove Vehicle",activebackground='red',activeforeground='yellow',
  bd=5,bg='green',fg='white' ,command=RemoveVehicle,width=15).grid(row=7,column=3,padx= 10, pady= 10)
Button(body,text="Delete",activebackground='red',activeforeground='yellow',
  bd=5,bg='green',fg='white' ,command=delete,width=10).grid(row=7,column=4,padx= 10, pady= 10)
details= ttk.Frame(root)
details.grid(row=9,column=1)


#Details
ttk.Label(details,text="Available Vehicles",background='yellow',font=('Arial',15,'underline')).grid(row=11,column=1,padx= 10, pady= 10)
ttk.Label(details,text="Car",font=('Arial',13)).grid(row=12,column=1,padx= 10, pady= 10)
AC=StringVar()
ttk.Entry(details,textvariable=AC,width=10,).grid(row=12,column=2,padx= 10, pady= 10)
ttk.Label(details,text=carlen,font=('Arial',13)).grid(row=12,column=2,padx= 10, pady= 10)


ttk.Label(details,text="Van",font=('Arial',13)).grid(row=13,column=1,padx= 10, pady= 10)
AC=StringVar()
ttk.Entry(details,textvariable=AC,width=10,).grid(row=13,column=2,padx= 10, pady= 10)
ttk.Label(details,text=Vanlen,font=('Arial',13)).grid(row=13,column=2,padx= 10, pady= 10)

ttk.Label(details,text="Three Wheel",font=('Arial',13)).grid(row=14,column=1,padx= 10, pady= 10)
AC=StringVar()
ttk.Entry(details,textvariable=AC,width=10,).grid(row=14,column=2,padx= 10, pady= 10)
ttk.Label(details,text=ThreeWheelerslen,font=('Arial',13)).grid(row=14,column=2,padx= 10, pady= 10)

ttk.Label(details,text="Lorry",font=('Arial',13)).grid(row=15,column=1,padx= 10, pady= 10)
AC=StringVar()
ttk.Entry(details,textvariable=AC,width=10,).grid(row=15,column=2,padx= 10, pady= 10)
ttk.Label(details,text=Lorrylen,font=('Arial',13)).grid(row=15,column=2,padx= 10, pady= 10)

ttk.Label(details,text="Truks",font=('Arial',13)).grid(row=16,column=1,padx= 10, pady= 10)
AC=StringVar()
ttk.Entry(details,textvariable=AC,width=10,).grid(row=16,column=2,padx= 10, pady= 10)
ttk.Label(details,text=Trukslen,font=('Arial',13)).grid(row=16,column=2,padx= 10, pady= 10)


hire = ttk.Frame(root)
hire.grid(row=3,column=3,padx=0,pady=0)

ttk.Label(hire,text="Fill this Form for asign job ",background='yellow',font=('Arial',18)).grid(row=1,column=7,padx=10,pady=5)
ttk.Label(hire,text="Name",font=('Arial',13)).grid(row=2,column=6,padx= 10, pady= 10)
name=StringVar()
ttk.Entry(hire,textvariable=name,width=30).grid(row=2,column=7,padx= 10, pady= 10)

ttk.Label(hire,text="Age",font=('Arial',13)).grid(row=3,column=6,padx= 10, pady= 10)
age=StringVar()
ttk.Entry(hire,textvariable=age,width=30).grid(row=3,column=7,padx= 10, pady= 10)

ttk.Label(hire,text="ID",font=('Arial',13)).grid(row=4,column=6,padx= 10, pady= 10)
ID=StringVar()
ttk.Entry(hire,textvariable=ID,width=30).grid(row=4,column=7,padx= 10, pady= 10)

ttk.Label(hire,text="email",font=('Arial',13)).grid(row=5,column=6,padx= 10, pady= 10)
email=StringVar()
ttk.Entry(hire,textvariable=email,width=30).grid(row=5,column=7,padx= 10, pady= 10)

ttk.Label(hire,text="Driving licene number",font=('Arial',13)).grid(row=6,column=6,padx= 10, pady= 10)
DID=StringVar()
ttk.Entry(hire,textvariable=DID,width=30).grid(row=6,column=7,padx= 10, pady= 10)

ttk.Label(hire,text="Mobile No",font=('Arial',13)).grid(row=7,column=6,padx= 10, pady= 10)
Mobile=StringVar()
ttk.Entry(hire,textvariable=Mobile,width=30).grid(row=7,column=7,padx= 10, pady= 10)

ttk.Label(hire,text="Vehicle No(For assign Job)",font=('Arial',13)).grid(row=8,column=6,padx= 10, pady= 10)
vehicle=StringVar()
ttk.Entry(hire,textvariable=vehicle,width=30).grid(row=8,column=7,padx= 10, pady= 10)

Button(hire,text="Asign",activebackground='red',activeforeground='yellow',
  bd=5,bg='green',fg='white',command=AssignJobs,width=10).grid(row=9,column=6,padx= 10, pady= 10)

Button(hire,text="Relese",activebackground='red',activeforeground='yellow',
  bd=5,bg='green',fg='white' ,command=RemoveJobs,width=10).grid(row=9,column=7,padx= 10, pady= 10)

Button(hire,text="Delete",activebackground='red',activeforeground='yellow',
  bd=5,bg='green',fg='white',command=deletehire,width=10).grid(row=10,column=7,padx= 10, pady= 10)
Button(hire,text="Search Available Drivers",activebackground='red',activeforeground='yellow',
  bd=5,bg='green',fg='white',command=AvailableDirvers,width=20).grid(row=10,column=6,padx= 10, pady= 10)


det=ttk.Frame(root)
det.grid(row=9,column=2)
ttk.Label(det,text=" Current Vehicle Rates",background='yellow',font=('Arial',18,'underline')).grid(row=8,column=2,padx= 10, pady= 10)
ttk.Label(det,text=" Car = Rs 120 (Per Km)",font=('Arial',13)).grid(row=9,column=2,padx= 10, pady= 10)
ttk.Label(det,text=" Van = Rs 200 (Per Km)",font=('Arial',13)).grid(row=10,column=2,padx= 10, pady= 10)
ttk.Label(det,text=" Lorry = Rs 190 (Per Km)",font=('Arial',13)).grid(row=11,column=2,padx= 10, pady= 10)
ttk.Label(det,text=" Trucks = Rs 210 (Per Km)",font=('Arial',13)).grid(row=12,column=2,padx= 10, pady= 10)
ttk.Label(det,text=" ThreeWeel = Rs 60 (Per Km)",font=('Arial',13)).grid(row=13,column=2,padx= 10, pady= 10)

payment = ttk.Frame(root)
payment.grid(row=9,column=3,padx=0,pady=0)

ttk.Label(payment,text=" Total Amount for pay",background='yellow',font=('Arial',18,'underline')).grid(row=7,column=2,padx= 10, pady= 0)
ttk.Label(payment,text=" Vehicle Type",font=('Arial',13)).grid(row=8,column=1,padx= 10, pady= 10)

n = StringVar()
monthchoosen = ttk.Combobox(payment, width=27, textvariable=n)

# Adding combobox drop down list
monthchoosen['values'] = ("Car", "Van", "ThreeWheeler", "Lorry", "Trucks")

monthchoosen.grid(column=2, row=8)
monthchoosen.current()

ttk.Label(payment,text=" How many Kilometers",font=('Arial',13)).grid(row=9,column=1,padx= 10, pady= 10)
Km=IntVar()
ttk.Entry(payment,textvariable=Km,width=30).grid(row=9,column=2,padx= 10, pady= 10)
Button(payment,text="Prosess",activebackground='red',activeforeground='yellow',
  bd=5,bg='green',fg='white',command=Count,width=10).grid(row=10,column=2,padx= 10, pady= 10)
root.mainloop()