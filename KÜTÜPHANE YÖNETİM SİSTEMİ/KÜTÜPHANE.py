from tkinter import *
from datetime import date
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import sqlite3
import time
import datetime
from datetime import datetime
from datetime import timedelta
import smtplib

db=sqlite3.connect('admin.db')
dd=sqlite3.connect('kitaplar.db')
dc=sqlite3.connect('ogrenciler.db')

root = Tk()
root.title("Kütüphane Yönetim Sistemi")
root.iconbitmap("aa.ico")
root.geometry("900x500+300+150")
root.resizable(0, 0)
img=PhotoImage(file="bb.png")

class maincode:

     def login(self):

         self.var1 = self.e1.get()
         self.var2 = self.e2.get()
         cursor=db.cursor()
         cursor.execute("SELECT * FROM adm WHERE tc_kimlik_no='"+self.var1+"' and sifre='"+self.var2+"'")
         db.commit()
         self.ab = cursor.fetchone()
         if self.ab!=None:
               
             self.under_fm=Frame(root,height=500,width=900,bg='#fff')
             self.under_fm.place(x=0,y=0)
             self.fm2=Frame(root,bg='#3c5a99',height=80,width=900)
             self.fm2.place(x=0,y=0)

             

             self.lbb=Label(self.fm2,bg='#3c5a99')
             self.lbb.place(x=15,y=5)
             self.ig=PhotoImage(file='library.png')
             self.lbb.config(image=self.ig)
             self.lb3=Label(self.fm2,text='KÜTÜPHANE',fg='White',bg='#3c5a99',font=('Arial',30,'bold'))
             self.lb3.place(x=325,y=17)


             #----------------------------isim------------------------

             self.name=Label(root,text="Kullanıcı : ",bg='#fff',fg="black",font=('Arial',10,'bold'))
             self.name.place(x=15,y=83)
             self.name1=Label(root,text=self.ab[1],fg='black',bg='#fff',font=('Arial',10,'bold'))
             self.name1.place(x=85,y=83)

             #------------------------tarih-------------------------

             self.today=date.today()
             self.dat=Label(root,text='Tarih : ',bg='#fff',fg='black',font=('Arial',10,'bold'))
             self.dat.place(x=740,y=83)
             self.dat2 = Label(root, text=self.today, bg='#fff', fg='black', font=('Arial', 10, 'bold'))
             self.dat2.place(x=790, y=83)

             self.cur()

         else:
               messagebox.showerror('Kütüphane Yönetim Sistemi', 'TC KİMLİK NUMARASI VEYA ŞİFRE GEÇERLİ DEĞİL!')
             #---------------------------------------------------------
     def cur(self):
             self.fm3=Frame(root,bg='#fff',width=900,height=390)
             self.fm3.place(x=0,y=110)

             #------------------------saat---------------------------

             def clock():
                 h = str(time.strftime("%H"))
                 m = str(time.strftime("%M"))
                 s = str(time.strftime("%S"))

                 if int(h) >=12 and int(m) >=0:
                       self.lb7_hr.config(text="PM")

                 

                 self.lb1_hr.config(text=h)
                 self.lb3_hr.config(text=m)
                 self.lb5_hr.config(text=s)

                 self.lb1_hr.after(200, clock)

             self.lb1_hr = Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#2c4762', fg='white')
             self.lb1_hr.place(x=560, y=0, width=60, height=30)


             self.lb3_hr = Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#2c4762', fg='white')
             self.lb3_hr.place(x=630, y=0, width=60, height=30)


             self.lb5_hr = Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#2c4762', fg='white')
             self.lb5_hr.place(x=700, y=0, width=60, height=30)


             self.lb7_hr = Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='slategray', fg='white')
             self.lb7_hr.place(x=770, y=0, width=60, height=30)


             clock()

             #-------------------------------resim------------------------

             
             
             self.canvas8 = Button(self.fm3,image=img ,bg='lightgrey',width=400, height=282)
             self.canvas8.place(x=475, y=37)

             

             #-----------------ekle butonu-----------------

             self.bt1=Button(self.fm3,text=' Kitap Ekle',fg='#fff',bg='dimgray',font=('Arial',15,'bold'),width=170,
                          height=0,bd=4,command=self.addbook,cursor='hand2')
             self.bt1.place(x=40,y=40)
             self.logo = PhotoImage(file='bt1.png')
             self.bt1.config(image=self.logo, compound=LEFT)
             self.small_logo = self.logo.subsample(1,1)
             self.bt1.config(image=self.small_logo)

             #-------------------------verme butonu--------------

             self.bt2 = Button(self.fm3, text='  Kitap Verme', fg='#fff', bg='dimgray', font=('Arial', 15, 'bold'),
                            width=170,height=0, bd=4,command=self.issuebook,cursor='hand2')
             self.bt2.place(x=250, y=40)
             self.log = PhotoImage(file='bt2.png')
             self.bt2.config(image=self.log, compound=LEFT)
             self.small_log = self.log.subsample(1, 1)
             self.bt2.config(image=self.small_log)

             #---------------------------güncelle butonu----------------

             self.bt3 = Button(self.fm3, text=' Kitap Güncelle', fg='#fff', bg='dimgray', font=('Arial', 15, 'bold'),
                           width=170,height=0,bd=4,cursor='hand2',command=self.edit)
             self.bt3.place(x=40, y=120)
             self.logb = PhotoImage(file='bt3.png')
             self.bt3.config(image=self.logb, compound=LEFT)
             self.small_logb = self.logb.subsample(1, 1)
             self.bt3.config(image=self.small_logb)

             #-----------------------------iade butonu----------------

             self.bt4 = Button(self.fm3, text='  Kitap İadesi', fg='#fff', bg='dimgray', font=('Arial', 15, 'bold'),
                          width=170,height=0,bd=4,cursor='hand2',command=self.return_book)
             self.bt4.place(x=250, y=120)
             self.log4 = PhotoImage(file='bt4.png')
             self.bt4.config(image=self.log4, compound=LEFT)
             self.small_log4 = self.log4.subsample(1, 1)
             self.bt4.config(image=self.small_log4)

             #----------------------silme butonu---------------------

             self.bt5 = Button(self.fm3, text=' Kitap Silme', fg='#fff', bg='dimgray', font=('Arial', 15, 'bold'),
                          width=170,height=0,bd=4,cursor='hand2',command=self.delete)
             self.bt5.place(x=40, y=200)
             self.log5 = PhotoImage(file='bt5.png')
             self.bt5.config(image=self.log5, compound=LEFT)
             self.small_log5 = self.log5.subsample(1, 1)
             self.bt5.config(image=self.small_log5)

             #--------------------kitaplar butonu-----------------------------

             self.bt6 = Button(self.fm3, text=' Kitaplar', fg='#fff', bg='dimgray', font=('Arial', 15, 'bold'),
                           width=170,height=0,bd=4,cursor='hand2',command=self.show)
             self.bt6.place(x=250, y=200)
             self.log6 = PhotoImage(file='bt6.png')
             self.bt6.config(image=self.log6, compound=LEFT)
             self.small_log6 = self.log6.subsample(1, 1)
             self.bt6.config(image=self.small_log6)

             #-------------------------arama butonu------------------

             self.bt7 = Button(self.fm3, text=' Kitap Arama', fg='#fff', bg='dimgray', font=('Arial', 15, 'bold'),
                          width=170,height=0,bd=4,cursor='hand2',command=self.search)
             self.bt7.place(x=40, y=280)
             self.log7 = PhotoImage(file='bt7.png')
             self.bt7.config(image=self.log7, compound=LEFT)
             self.small_log7 = self.log7.subsample(1, 1)
             self.bt7.config(image=self.small_log7)

             #---------------------çıkış butonu-----------------------
             try:

                self.bt8 = Button(self.fm3, text='  Çıkış', fg='#fff', bg='dimgray', font=('Arial', 15, 'bold'),
                               width=170,
                          height=0, bd=4,cursor='hand2',command=self.code)
                self.bt8.place(x=250, y=280)
                self.log8 = PhotoImage(file='bt8.png')
                self.bt8.config(image=self.log8, compound=LEFT)
                self.small_log8 = self.log8.subsample(1, 1)
                self.bt8.config(image=self.small_log8)

             except:

               self.bt9 = ttk.Button(self.fm3, text="ram", bg='#11d09a', font=('Arial', 15, 'bold'), width=150,
                                     height=0)
               self.bt9.place(x=40, y=350)
               self.log9 = PhotoImage(file='bt8.png')
               self.bt9.config(image=self.log9, compound=LEFT)
               self.small_log9 = self.log9.subsample(3, 3)
               self.bt9.config(image=self.small_log9)






     def mainclear(self):
         self.e1.delete(0,END)
         self.e2.delete(0,END)


    #-----------------------kitap ekle butonu----------------------

     def addbook(self):
         class temp(maincode):

             def book(self):

                 self.fm=Frame(root,bg='lightgray',width=900,height=390)
                 self.fm.place(x=0,y=110)
                 self.fm1=Frame(self.fm,bg='#fff',width=500,height=360,bd=5,relief='flat')
                 self.fm1.place(x=200,y=15)
                 self.backbt = Button(self.fm, width=60, bg='lightgray',activebackground='lightgray', bd=0, relief='flat',\
                                                                                                 command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(1, 1)
                 self.backbt.config(image=self.small_log)

                 #---------------------------Label---------------------------------
                 self.f=Frame(self.fm1,bg='#3c5a99',width=490,height=35)
                 self.f.place(x=0,y=0)
                 self.ll=Label(self.f,text='Kitap Ekle',fg='#fff',bg='#3c5a99',font=('Arial',12,'bold'))
                 self.ll.place(x=200,y=6)
                 self.lb=Label(self.fm1,text='Kitap ID',fg='black',bg='#fff',font=('Arial',10,'bold'))
                 self.lb.place(x=70,y=70)
                 self.lb2 = Label(self.fm1, text='Kitap Adı', fg='black', bg='#fff', font=('Arial', 10, 'bold'))
                 self.lb2.place(x=70, y=110)
                 self.lb3 = Label(self.fm1, text='Yazar', fg='black', bg='#fff', font=('Arial', 10, 'bold'))
                 self.lb3.place(x=70, y=150)
                 self.lb4= Label(self.fm1, text='Basım Yılı', fg='black', bg='#fff', font=('Arial', 10, 'bold'))
                 self.lb4.place(x=70, y=190)
                 self.lb5 = Label(self.fm1, text='Fiyat', fg='black', bg='#fff', font=('Arial', 10, 'bold'))
                 self.lb5.place(x=70, y=230)

                 #-------------------------------Entry-------------------------------------

                 self.ee1=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee1.place(x=180,y=68)
                 self.ee2=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee2.place(x=180,y=110)
                 self.ee3=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee3.place(x=180,y=150)
                 self.ee4=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee4.place(x=180,y=190)
                 self.ee5=Entry(self.fm1,width=25,bd=4,relief='groove',font=('arial',12,'bold'))
                 self.ee5.place(x=180,y=230)

                 self.bt=Button(self.fm1,text='Onayla',width=41,bg='grey',fg='#fff',font=('Arial',10,'bold'),bd=3,
                          command=self.submit1)
                 self.bt.place(x=70,y=290)
                 
                 #---------------------geri buton ----------------------------------




             def submit1(self):

                 self.id=self.ee1.get()
                 self.ttl=self.ee2.get()
                 self.aut=self.ee3.get()
                 self.edi=self.ee4.get()
                 self.pri=self.ee5.get()
                 cursor=dd.cursor()
                 cursor.execute("INSERT INTO kitap_bilgi(kitap_id,kitap_adi,yazar,baski,fiyat) values(?,?,?,?,?)",(self.id,
                                                                                                      self.ttl,self.aut,self.edi,self.pri))
                 dd.commit()
                 self.clear()
                 messagebox.showinfo('Kütüphane Yönetim Sistemi','Kitap başarıyla eklendi!')
             def clear(self):
                 self.ee1.delete(0,END)
                 self.ee2.delete(0,END)
                 self.ee3.delete(0,END)
                 self.ee4.delete(0,END)
                 self.ee5.delete(0,END)
         
         obj=temp()
         obj.book()


        

        #--------------------------------kitap verme---------------------------------
     def issuebook(self):
         class test(maincode):
              max=0
              n = 1
              def issue(self):
                  self.f = Frame(root, bg='#a7ecd9', width=900, height=390)
                  self.f.place(x=0, y=110)

                  self.fmi=Canvas(self.f,bg='lightgray',width=900,height=390,bd=0,relief='flat')
                  self.fmi.place(x=0,y=0)
             

                  self.fc=Frame(self.fmi,bg='#fff',width=338,height=225,bd=4,relief='flat')
                  self.fc.place(x=70,y=20)

                  self.ffb=Frame(self.fc,bg='#3c5a99',bd=2,relief='flat',width=330,height=35)
                  self.ffb.place(x=0,y=0)

                  self.lc=Label(self.ffb,text='Öğrenci Bilgileri',bg='#3c5a99',fg='#fff',font=('Arial',12,'bold'))
                  self.lc.place(x=95,y=5)

                  self.lb=Label(self.fc,text='Tc No',bg='#fff',fg='black',font=('Arial',10,'bold'))
                  self.lb.place(x=15,y=60)
                  self.ob=Label(self.fc,text='veya',bg='#fff',fg='black',font=('cursive',12,'bold'))
                  self.ob.place(x=180,y=90)
                  self.em = Entry(self.fc, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                  self.em.place(x=105, y=60)
                  self.lb = Label(self.fc, text='Öğrenci No', bg='#fff', fg='black', font=('Arial', 10, 'bold'))
                  self.lb.place(x=15, y=120)
                  self.em2 = Entry(self.fc, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                  self.em2.place(x=105, y=120)
                  self.bt = Button(self.fc, text='Onayla', width=14, bg='red', fg='#fff', font=('Arial', 10, 'bold'),
                                 bd=3,command=self.check)
                  self.bt.place(x=25,y=180)

                  self.bt3=Button(self.fc,text='Temizle',width=14,bg='blue',fg='#fff',font=('arial',10,'bold'),bd=3
                                  ,command=self.clr)
                  self.bt3.place(x=175,y=180)

                  self.backbt = Button(self.fmi,width=60, bg='lightgray',activebackground='lightgray',bd=0, relief='flat',
                                       command=self.cur)
                  self.backbt.place(x=5, y=5)
                  self.log = PhotoImage(file='back.png')
                  self.backbt.config(image=self.log, compound=LEFT)
                  self.small_log = self.log.subsample(1, 1)
                  self.backbt.config(image=self.small_log)

              def check(self):
                  self.ai=self.em.get()
                  self.b=self.em2.get()
                  cursor=dc.cursor()
                  cursor.execute("SELECT * FROM ogrenci WHERE tc_no='"+self.ai+"' or ogrenci_no='"+self.b+"'")
                  self.var=cursor.fetchone()
                  if self.var!=None:
                        self.fc=Frame(self.fmi,bg='#fff',width=338,height=130,bd=4,relief='flat')
                        self.fc.place(x=70,y=250)
                        self.lb1=Label(self.fmi,text='Ad Soyad :',bg='#fff',fg='black',font=('Arial',10,'bold'))
                        self.lb1.place(x=100,y=265)
                        self.lb2 = Label(self.fmi, text=self.var[1],bg='#fff', fg='black', font=('Arial', 10, 'bold'))
                        self.lb2.place(x=180, y=265)
                        self.lb3 = Label(self.fmi, text='Bölüm :',bg='#fff',fg='black', font=('Arial', 10, 'bold'))
                        self.lb3.place(x=100, y=285)
                        self.lb4 = Label(self.fmi, text=self.var[2],bg='#fff',fg='black', font=('Arial', 10, 'bold'))
                        self.lb4.place(x=180, y=285)
                        self.lb5 = Label(self.fmi, text='Sınıf :',bg='#fff', fg='black', font=('Arial', 10, 'bold'))
                        self.lb5.place(x=100, y=305)
                        self.lb6 = Label(self.fmi, text=self.var[3],bg='#fff', fg='black', font=('Arial', 10, 'bold'))
                        self.lb6.place(x=180, y=305)
                        self.lb7 = Label(self.fmi, text='İletişim :',bg='#fff', fg='black', font=('Arial', 10, 'bold'))
                        self.lb7.place(x=100, y=325)
                        self.lb8 = Label(self.fmi, text=self.var[6],bg='#fff',fg='black', font=('Arial', 10, 'bold'))
                        self.lb8.place(x=180, y=325)
                        self.lb9 = Label(self.fmi, text='Üniversite :',bg='#fff', fg='black', font=('Arial', 10, 'bold'))
                        self.lb9.place(x=100, y=345)
                        self.lb10 = Label(self.fmi, text=self.var[7],bg='#fff',fg='black', font=('Arial', 10, 'bold'))
                        self.lb10.place(x=180, y=345)


                        self.fr=Frame(self.fmi,bg='#fff',bd=5,relief='flat',width=460,height=359)
                        self.fr.place(x=420,y=20)
                        self.ff=Frame(self.fr,bg='#3c5a99',bd=2,relief='flat',width=450,height=35)
                        self.ff.place(x=0,y=0)
                        self.lb=Label(self.ff,text='Kitap Verme',bg='#3c5a99',fg='#fff',font=('Arial',12,'bold'))
                        self.lb.place(x=165,y=5)
                        self.tt=Label(self.fr,text='Kitap ID',bg='#fff',fg='black',font=('arial',10,'bold'))
                        self.tt.place(x=50,y=60)
                        self.e1 = Entry(self.fr, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                        self.e1.place(x=160, y=60)
                        self.ttp = Label(self.fr, text='Kitap Adı', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                        self.ttp.place(x=50, y=110)
                        self.e2 = Entry(self.fr, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                        self.e2.place(x=160, y=110)
                        self.bt1 = Button(self.fr, text='Onayla', width=35, bg='grey', fg='#fff', font=('Arial', 10,
                                                                    'bold'),bd=3,command=self.data)
                        self.bt1.place(x=60, y=179)

                        '''self.bt1 = Button(self.fr, text='Clear', width=13, bg='blue', fg='#fff', font=('Arial', 10,
                                                                                                  'bold'), bd=5,
                                    relief='flat', command=self.clr1)
                        self.bt1.place(x=215, y=160)'''
                  else:
                       messagebox.showwarning('Kütüphane Yönetim Sistemi','YANLIŞ VEYA EKSİK BİLGİ GİRDİNİZ!')


              def clr(self):
                  self.em.delete(0, END)
                  self.em2.delete(0, END)
              '''def clr1(self):
                  self.e1.delete(0,END)
                  self.e2.delete(0,END)
                  self.boot.destroy()
                  self.data()'''


              def data(self):
                   self.vva=self.e1.get()
                   self.vvb=self.e2.get()
                   cursor=dd.cursor()
                   cursor.execute("SELECT * FROM kitap_bilgi WHERE kitap_id='"+self.vva+"' and kitap_adi='"+self.vvb+"'")

                   dd.commit()
                   self.value=cursor.fetchone()
                   if self.value!=None:
                        if self.max==0:
                              self.boot=Tk()
                              self.boot.title("Kitap Verme")
                              self.boot.iconbitmap("aa.ico")
                              self.boot.configure(bg='lightgray')
                              self.boot.geometry("300x680+600+10")
                              self.boot.resizable(0,0)

                              self.lb=Label(self.boot,text='Kitap Adı :',bg='lightgray',fg='black',font=('Arial',10,'bold'))
                              self.lb.place(x=30,y=30)
                              self.lbn = Label(self.boot, text=self.value[1], bg='lightgray', fg='black', font=('Arial', 10, 'bold'))
                              self.lbn.place(x=120,y=30)
                              self.lb = Label(self.boot, text='Yazar :', bg='lightgray', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lb.place(x=30, y=60)
                              self.lbn = Label(self.boot, text=self.value[2], bg='lightgray', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbn.place(x=120, y=60)
                              self.lb = Label(self.boot, text='Basım Yılı :', bg='lightgray', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lb.place(x=30, y=90)
                              self.lbn = Label(self.boot, text=self.value[3], bg='lightgray', fg='black', font=('Arial', 10,
                                                                                                    'bold'))
                              self.lbn.place(x=120, y=90)
                              self.plan = Label(self.boot, text='---------------------------------------------------',
                                        bg='lightgray')
                              self.plan.place(x=15, y=120)
                              self.planx = Label(self.boot, text='---------------------------------------------------',
                                        bg='lightgray')

                              self.planx.place(x=15, y=240)
                              self.planx = Label(self.boot, text='---------------------------------------------------',
                                        bg='lightgray')

                              self.planx.place(x=15, y=360)

                        

                        #------------------------kitap veriş düğmesi-----------------------------
                        self.button1 = Button(self.boot, text='Onayla', bg='red', fg='#fff', width=30, height=0,bd=2,
                                              font=('Arial', 8, 'bold'), command=self.issued)
                        self.button1.place(x=40, y=610)

                        self.btn = Button(self.boot, text='Mail Gönder', bg='blue', fg='#fff', width=30, height=0,bd=2,
                                              font=('Arial', 8, 'bold'), command=self.mail)
                        self.btn.place(x=40, y=650)

                        #-----------------------tarih seçimi-------------------------


                        self.x = date.today()


                        self.cal = Calendar(self.boot, selectmode="day", bg='black',year=2021,month=1,day=1)
                        self.cal.place(x=20,y=380)


                        btn1 = Button(self.boot, text="Tarih Seç",command=self.get_data,  bg='grey',bd=2,
                                      font=('arial', 10,
                                                                                                    'bold'),
                                      fg='#fff')
                        btn1.place(x=115,y=575)


                        self.boot.mainloop()

                   else:
                        messagebox.showwarning('Kütüphane Yönetim Sistemi','VERİLER BULUNAMADI !')


              def get_data(self):
                  self.datecon=self.cal.selection_get()


              def yes(self):

                    self.n=self.n+1
                    self.bt1 = Button(self.fr, text='Onayla', width=35, bg='#0f624c', fg='#fff', font=('Arial', 10,
                                                        'bold'), bd=5,relief='flat',command=self.data, state=ACTIVE)
                    self.bt1.place(x=60, y=160)

                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.max=self.max+1


              def no(self):

                    self.bt1 = Button(self.fr, text='Onayla', width=35, bg='#0f624c', fg='#fff', font=('Arial', 10,
                                                   'bold'), bd=5,relief='flat',state=DISABLED)
                    self.bt1.place(x=60, y=160)


              def issued(self):

                    self.ac=self.e1.get()
                    cursor=dd.cursor()
                    cursor.execute("UPDATE kitap_bilgi SET durum='Verildi', ogrenci_num='"+self.b+"', tc_num='"+self.ai+"' WHERE "
                                                                                   "kitap_id='"+self.ac+"'")
                    dd.commit()

                    if self.n<=3:
                       book=dc.cursor()
                       book.execute("UPDATE ogrenci SET rakam='"+str(self.n)+"' WHERE tc_no='"+self.ai+"' or "
                                                                                                             "ogrenci_no='"+self.b+"' ")
                       dc.commit()

                    comm=dc.cursor()
                    comm.execute("UPDATE ogrenci SET verilis_tarihi='"+str(self.x)+"', alinacak_tarih='"+str(self.datecon)+"',teslim_tarihi='' "
                                                                                                               "WHERE tc_no='"+self.ai+"' or ogrenci_no='"+self.b+"'")
                    dc.commit()

                    messagebox.showinfo('Kütüphane Yönetim Sistemi', 'Kitap verme işlemi tamamlandı !')
              def mail(self):
                   
                    self.dady=self.em.get()
                    self.baby=self.em2.get()
                    cursor=dc.cursor()
                    cursor.execute("SELECT * FROM ogrenci WHERE tc_no='"+self.dady+"' or ogrenci_no='"+self.baby+"'")
                    self.var=cursor.fetchone()
                    reciever =self.var[5]
                    subject="Kütüphane Kuralları"
                    message = """Merhaba sayın okuyucu; kütüphanemizden ödünç aldığın kitap için bazı kuralları hatırlatmak isteriz :


ÖDÜNÇ ALAN ÜYENİN SORUMLULUKLARI :

-Ödünç alınan kitabın iade süresi bu maili aldığınız tarihten itibaren 1 aydır.

-Ödünç alınan her kitabın sorumluluğu, kütüphaneye iade edilinceye kadar ödünç alan üyeye aittir.

-Üye ödünç alacağı herhangi bir kitabı, ödünç almadan önce hasarlı olup olmadığı konusunda kontrol etmelidir.
Ödünç alınan herhangi bir kitabın iade edildiğinde hasarlı olması durumunda bunun sorumluluğu ödünç alan üyeye aittir.

-Ödünç alınan kitabı zamanında kütüphaneye iade etmek ödünç alan üyenin sorumluluğundadır.

-Üye ödünç aldığı herhangi bir kitabı, kayıp veya hasar sebebi ile iade edemeyecekse,
konu ile ilgili olarak kütüphaneyi derhal bilgilendirmesi gerekmektedir.

-Ödünç verilen herhangi bir kitabın geç iade edilmesi, kaybı ya da tahrip edildiği durumlarda oluşan bedelin üye tarafından ödenmemesi halinde,
üyenin ödünç alma hakları geçici olarak engellenir. Üye ilgili sorun çözümlendiği takdirde tekrar ödünç alma hakkına sahip olur.


GECİKEN İADELER, KAYIP VE HASARLAR / CEZALAR :

-Gününde iadesi gerçekleşmeyen herhangi bir kitap için günlük gecikme cezası uygulanır. Gecikme cezası her yıl başında o yıl için
Kütüphane Yönetim Kurulu tarafından tespit edilir. (2021-2022 yılı için gecikme cezası günlük 50 kuruştur.)

-Ödünç alan üye, ödünç aldığı kitabın iadesini; iade tarihinden itibaren 2 ay geçmesine rağmen henüz gerçekleştirmemişse,
ödünç alınan söz konusu kitap "kayıp" kabul edilir ve iadesi gerçekleştirilmediği takdirde kayıp işlemi uygulanır.

-Ödünç alınan herhangi bir kitabın, iade tarihinden itibaren, 2 ayı aşan bir gecikme sonrasında iade edildiği durumlarda;
2 aylık gecikme cezası tutarına, tutarın yarı miktarı da eklenerek, oluşan toplam gecikme cezası tutarı üyeden tahsil edilir.

-Ödünç alınan herhangi bir kitabın kaybı veya tahribi durumunda,
ilgili kitabın aynısını veya yeni baskısını (edisyon) kütüphaneye sağlamak ödünç alan üyenin sorumluluğundadır.
Bu iki seçenekten hiçbirisinin sağlanamadığı hallerde, Kütüphane Yönetim Kurulu tarafından onaylanmış ölçütler uyarınca kitabın bedeli tespit edilir ve
bu bedele, cezai olarak bedelin yarı miktarı da eklenerek, oluşan toplam tutar, tazmin bedeli olarak, üyeden nakden tahsil edilir.


ÖDÜNÇ SÜRESİNİ UZATMA :

Üye, ödünç aldığı üzerindeki herhangi bir kitabın ödünç süresini uzatmak istediği takdirde, ödünç aldığı üzerindeki
kitap ile birlikte, şahsen Kütüphanemize başvurmalıdır.

Anlayışın için teşekkür eder keyifli okumalar dileriz.

													                                                                                                              -Kütüphane Yönetimi"""
                    content="Subject:{0}\n\n{1}".format(subject,message)
                    mail = smtplib.SMTP("smtp.gmail.com", 587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login("kutuphane.yonetim.sistemi@gmail.com", "kutuphane123")
                    mail.sendmail("kutuphane.yonetim.sistemi@gmail.com", reciever, content.encode("utf-8"))
                    
                    messagebox.showinfo("Kütüphane Yönetim Sistemi"," Mail başarıyla gönderildi !")
                    
         obk=test()
         obk.issue()



     def edit(self):
         class editing(maincode):
               def edbooks(self):


                     self.ffm=Frame(root,bg='lightgray',width=900,height=390)
                     self.ffm.place(x=0,y=110)
                     self.fm1 = Frame(self.ffm, bg='#fff', width=500, height=200, bd=5, relief='flat')
                     self.fm1.place(x=200, y=15)
                     self.ed = Frame(self.fm1, bg='#3c5a99', bd=0, relief='flat', width=490, height=35)
                     self.ed.place(x=0,y=0)
                     self.lab = Label(self.ed, text='Kitap Güncelleme', bg='#3c5a99', fg='#fff', font=('Arial', 12,
                                                                                                    'bold'))
                     self.lab.place(x=180, y=5)
                     self.label3=Label(self.fm1,text='Kitap ID',bg='#fff',fg='black',font=('arial',10,'bold'))
                     self.label3.place(x=85,y=65)
                     self.entry=Entry(self.fm1,width=30,bd=4,relief='groove',font=('arial',8,'bold'))
                     self.entry.place(x=188,y=65)
                     self.button7 = Button(self.fm1, text='Ara', bg='grey', fg='#fff', width=24, height=0,
                                  font=('Arial', 10, 'bold'),command=self.searchh)
                     self.button7.place(x=140,y=120)

                     self.backbt = Button(self.ffm, width=60, bg='lightgray',activebackground='lightgray',
                                          bd=0, relief='flat', command=self.cur)
                     self.backbt.place(x=0, y=0)
                     self.log = PhotoImage(file='back.png')
                     self.backbt.config(image=self.log, compound=LEFT)
                     self.small_log = self.log.subsample(1, 1)
                     self.backbt.config(image=self.small_log)


                #----------------------veritabanı----------------------------------


               def searchh(self):
                     self.datas=self.entry.get()
                     cursor=dd.cursor()
                     cursor.execute("SELECT * FROM kitap_bilgi WHERE kitap_id='"+self.datas+"'" )
                     dd.commit()
                     self.val=cursor.fetchone()
                     if self.val!=None:

                          self.edcat=Tk()
                          self.edcat.title("Kütüphane Yönetim Sistemi")
                          self.edcat.geometry("300x320+590+320")
                          self.edcat.configure(bg='lightgray')
                          self.edcat.iconbitmap("aa.ico")


                          self.fc=Frame(self.edcat,bg='#3c5a99',width=300,height=30)
                          self.fc.place(x=0,y=0)
                          self.lab=Label(self.fc,bg='#3c5a99',fg='#fff',text='Kitap Düzenle',font=('arial',10,'bold'))
                          self.lab.place(x=102,y=5)
                          self.labid = Label(self.edcat, bg='lightgray', fg='black', text='Kitap ID', font=('arial', 10,
                                                                                                    'bold'))
                          self.labid.place(x=30, y=45)
                          self.labti = Label(self.edcat, bg='lightgray', fg='black', text='Kitap Adı', font=('arial', 10,
                                                                                                    'bold'))
                          self.labti.place(x=30, y=90)
                          self.labaut = Label(self.edcat, bg='lightgray', fg='black', text='Yazar', font=('arial', 10,
                                                                                                    'bold'))
                          self.labaut.place(x=30, y=135)
                          self.labed = Label(self.edcat, bg='lightgray', fg='black', text='Basım Yılı', font=('arial', 10,
                                                                                                    'bold'))
                          self.labed.place(x=30, y=180)
                          self.labpr = Label(self.edcat, bg='lightgray', fg='black', text='Fiyat', font=('arial', 10,
                                                                                                    'bold'))
                          self.labpr.place(x=30, y=225)

                         #------------------------------Entry------------------------


                          self.en1=Entry(self.edcat,width=25,bd=4,relief='groove',font=('arial',8,'bold'))
                          self.en1.place(x=100,y=45)
                          self.en2 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en2.place(x=100, y=90)
                          self.en3 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en3.place(x=100, y=135)
                          self.en4 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en4.place(x=100, y=180)
                          self.en5 = Entry(self.edcat, width=25, bd=4, relief='groove',font=('arial',8,'bold'))
                          self.en5.place(x=100, y=225)
                          self.butt = Button(self.edcat, text='Kaydet', bg='grey', fg='#fff', width=20, height=0,
                                      font=('Arial', 10, 'bold'),command=self.savedit)
                          self.butt.place(x=67, y=270)

                         # -------------------düzenle sayfasında doldurulan entryler--------------------

                          self.en1.insert(0, self.val[0])
                          self.en2.insert(0, self.val[1])
                          self.en3.insert(0, self.val[2])
                          self.en4.insert(0, self.val[3])
                          self.en5.insert(0, self.val[4])

                          self.edcat.mainloop()

                     else:
                          messagebox.showerror('Kütüphane Yönetim Sistemi','LÜTFEN KİTAP IDYİ DÜZELTİN !')

                #-----------------veritabanında güncelleme-----------------


               def savedit(self):
                     self.id = self.en1.get()
                     self.ti = self.en2.get()
                     self.au = self.en3.get()
                     self.ed = self.en4.get()
                     self.pi = self.en5.get()

                     cursor= dd.cursor()
                     cursor.execute("UPDATE kitap_bilgi SET kitap_id='"+self.id+"', kitap_adi='"+self.ti+"',yazar='"+self.au+"',baski='"+self.ed+"',fiyat='"+self.pi+"' WHERE kitap_id='"+self.datas+"'")
                     dd.commit()
                     messagebox.showinfo('Kütüphane Yönetim Sistemi','Kitap başarıyla güncellendi!')

         obj=editing()
         obj.edbooks()

      


         # ------------------------------kitap iade--------------------------------------------------
     def return_book(self):
         class retu(maincode):

             def __init__(self):
                 self.frame=Frame(root,bd=0,relief='flat',bg='lightgray',width=900,height=390)
                 self.frame.place(x=0,y=110)
                 self.f1 = Frame(self.frame, bg='#fff', width=500, height=300, bd=5, relief='flat')
                 self.f1.place(x=200, y=15)
                 self.ed = Frame(self.f1, bg='#3c5a99', bd=0, relief='flat', width=490, height=35)
                 self.ed.place(x=0, y=0)
                 self.lac = Label(self.ed, text='Kitap İadesi ', bg='#3c5a99', fg='#fff', font=('Arial', 12, 'bold'))
                 self.lac.place(x=195, y=5)


                 self.lb=Label(self.f1,text='Tc No',bg='#fff',fg='black',font=('Arial',10,'bold'))
                 self.lb.place(x=85,y=65)
                 self.em = Entry(self.f1, width=30, bd=4, relief='groove', font=('Arial', 8, 'bold'))
                 self.em.place(x=188, y=65)

                 self.ob=Label(self.f1,text='veya',bg='#fff',fg='black',font=('cursive',12,'bold'))
                 self.ob.place(x=260,y=93)
                 


                 self.label8 = Label(self.f1, text='Öğrenci No', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label8.place(x=85, y=125)
                 self.entry4 = Entry(self.f1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entry4.place(x=188, y=125)
                    
                 self.button9 = Button(self.f1, text='İade Et', bg='grey', fg='#fff', width=24, height=0,
                                       font=('Arial', 10, 'bold'),command=self.retbook)
                 self.button9.place(x=140, y=195)

                 self.backbt = Button(self.frame, width=60, bg='lightgray', activebackground='lightgray',
                                      bd=0, relief='flat', command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(1, 1)
                 self.backbt.config(image=self.small_log)

             def retbook(self):
                 self.charge=0
                 self.entryi=self.em.get()
                 self.entry=self.entry4.get()
                 cursor=dc.cursor()
                 cursor.execute("SELECT * FROM ogrenci WHERE tc_no='"+self.entryi+"' or ogrenci_no='"+self.entry+"'")
                 dc.commit()
                 self.data=cursor.fetchone()
                 if self.data!=None:
                     self.get_date = date.today()
                     cursor = dc.cursor()
                     cursor.execute("UPDATE ogrenci SET teslim_tarihi='" +str(self.get_date)+ "' WHERE tc_no='"+self.entryi+"' or ogrenci_no='" + self.entry + "'")
                     dc.commit()

                     cursor=dd.cursor()
                     cursor.execute("UPDATE kitap_bilgi SET durum='', ogrenci_num='', tc_num='' WHERE ogrenci_num='"+self.entry+"' or tc_num='"+self.entryi+"'")
                     dd.commit()

                     from datetime import datetime


                     self.tom=Tk()
                     self.tom.geometry("300x250+590+348")
                     self.tom.iconbitmap("aa.ico")
                     self.tom.title("Kütüphane Yönetim Sistemi")
                     self.tom.resizable(0,0)
                     self.tom.configure(bg="black")

                     cursor=dc.cursor()
                     cursor.execute("SELECT * FROM ogrenci WHERE tc_no='"+self.entryi+"' or ogrenci_no='"+self.entry+"'")
                     dc.commit()
                     self.var=cursor.fetchone()
                     if self.var!=None:


                 #-----------------iki tarih arası gün hesabı---------------------
                         
                         self.a=self.var[9]
                         self.b=self.var[10]
                         formatStr='%Y-%m-%d'
                         delta1=datetime.strptime(self.a,formatStr)
                         delta2=datetime.strptime(self.b, formatStr)
                         delta=delta2-delta1
                         chm=delta.days
                         

                         #------------------ceza ücretini hesaplama------------------
                         self.lb=Label(self.tom,text="Gecikme Ücreti",bg="black",fg="Blue",font=('arial',17,'bold'))
                         self.lb.place(x=65,y=80)


                         if chm<=0:
                             self.lc1 = Label(self.tom, text="0 TL", bg="black", fg="#fff", font=('arial', 12,
                                                                                                    'bold'))
                             self.lc1.place(x=130,y=120)

                         else:

                             self.charge=(1/2*chm)*self.var[12]

                            

                             self.lc2 = Label(self.tom, text=self.charge, bg="black", fg="#fff", font=('arial',12,
                                                                                                      'bold'))
                             self.lc2.place(x=125, y=120)
                             self.lc3 = Label(self.tom, text='TL', bg="black", fg="#fff",
                                              font=('arial', 12, 'bold'))
                             self.lc3.place(x=160, y=120)

                         cursor1 = dc.cursor()
                         cursor1.execute("UPDATE ogrenci SET verilis_tarihi='',alinacak_tarih='',rakam='',"
                                         "borc='"+str(self.charge)+"' WHERE tc_no='"+self.entryi+"' or ogrenci_no='"+self.entry+"'")
                         dc.commit()


                     self.tom.mainloop()



                 else:
                     messagebox.showwarning("Kütüphane Yönetim Sistemi","NUMARANIZ BULUNAMADI !")


         object=retu()

   


     #-------------------------------------kitap silme---------------------------------------------

     def delete(self):
         class dele(maincode):
               def deleteee(self):
                     self.ff = Frame(root, bg='lightgray', width=900, height=390)
                     self.ff.place(x=0, y=110)
                     self.f1 = Frame(self.ff, bg='#fff', width=500, height=200, bd=5, relief='flat')
                     self.f1.place(x=200, y=15)
                     self.ed = Frame(self.f1, bg='#3c5a99', bd=0, relief='flat', width=490, height=35)
                     self.ed.place(x=0, y=0)
                     self.lac = Label(self.ed, text='Kitap Silme ', bg='#3c5a99', fg='#fff', font=('Arial', 12,'bold'))
                     self.lac.place(x=200, y=5)
                     self.label8 = Label(self.f1, text='Kitap ID', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                     self.label8.place(x=85, y=65)
                     self.entry4 = Entry(self.f1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                     self.entry4.place(x=188, y=65)
                     self.button9 = Button(self.f1, text='Sil', bg='grey', fg='#fff', width=24, height=0,bd=3,
                                  font=('Arial', 10, 'bold'),command=self.deldata)
                     self.button9.place(x=140, y=120)

                     self.backbt = Button(self.ff,width=60, bg='lightgray',activebackground='lightgray',
                                          bd=0, relief='flat', command=self.cur)
                     self.backbt.place(x=0, y=0)
                     self.log = PhotoImage(file='back.png')
                     self.backbt.config(image=self.log, compound=LEFT)
                     self.small_log = self.log.subsample(1, 1)
                     self.backbt.config(image=self.small_log)


               def deldata(self):
                     self.a=self.entry4.get()
                     cursor=dd.cursor()
                     cursor.execute("DELETE FROM kitap_bilgi WHERE kitap_id='"+self.a+"'")
                     dd.commit()
                     self.da=cursor.fetchone()
                     if self.a!=None:
                          
                          messagebox.showinfo('Kütüphane Yönetim Sistemi','Kitap başarıyla silindi !')
                     else:
                          messagebox.showerror('Kütüphane Yönetim Sistemi','YANLIŞ VEYA EKSİK BİLGİ GİRDİNİZ!')

         occ=dele()
         occ.deleteee()

   


     #---------------------------------------kitap arama---------------------------------------------

     def search(self):
         class demt(maincode):
             def delmdata(self):

                 self.fc = Frame(root, bg='lightgray', width=900, height=390)
                 self.fc.place(x=0, y=110)
                 self.fc1 = Frame(self.fc, bg='#fff', width=500, height=200, bd=5, relief='flat')
                 self.fc1.place(x=200, y=15)
                 self.edm = Frame(self.fc1, bg='#3c5a99', bd=0, relief='flat', width=490, height=35)
                 self.edm.place(x=0, y=0)
                 self.lac = Label(self.edm, text='Kitap Arama ', bg='#3c5a99', fg='#fff', font=('Arial', 12, 'bold'))
                 self.lac.place(x=195, y=5)
                 self.label8 = Label(self.fc1, text='Kitap Adı', bg='#fff', fg='black', font=('arial', 10, 'bold'))
                 self.label8.place(x=85, y=65)
                 self.entryl= Entry(self.fc1, width=30, bd=4, relief='groove', font=('arial', 8, 'bold'))
                 self.entryl.place(x=188, y=65)
                 self.butto = Button(self.fc1, text='Ara', bg='grey', fg='#fff', width=24, height=0,
                                       font=('Arial', 10, 'bold'),command=self.srch)
                 self.butto.place(x=140, y=120)

                 self.backbt = Button(self.fc,width=60, bg='lightgray',activebackground='lightgray',bd=0, relief='flat', command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(1, 1)
                 self.backbt.config(image=self.small_log)


             def srch(self):
                 self.emp=self.entryl.get()
                 cursor=dd.cursor()
                 cursor.execute("SELECT * FROM kitap_bilgi WHERE kitap_adi='"+self.emp+"'")
                 dd.commit()
                 self.srval=cursor.fetchone()
                 if self.srval!=None:

                     self.top=Tk()
                     self.top.title("Kütüphane Yönetim Sistemi")
                     self.top.iconbitmap("aa.ico")
                     self.top.geometry("300x300+600+300")
                     self.top.resizable(0, 0)
                     self.top.configure(bg='black')

                     self.frm=Frame(self.top,bg='#3c5a99',width=300,height=35)
                     self.frm.place(x=0,y=0)

                     self.mnlb=Label(self.frm,bg='#3c5a99',fg='#fff',text="Mevcut Kitap",font=('arial',11,'bold'))
                     self.mnlb.place(x=100,y=5)

                     self.lb1 = Label(self.top, text='Kitap ID:', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb1.place(x=40,y=65)
                     self.lb2=Label(self.top,text=self.srval[0],bg='black',fg='white',font=('arial',12,'bold'))
                     self.lb2.place(x=130,y=65)

                     self.lb3 = Label(self.top, text='Yazar:', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb3.place(x=40, y=125)
                     self.lb4 = Label(self.top, text=self.srval[2], bg='black', fg='white', font=('arial', 12, 'bold'))
                     self.lb4.place(x=130, y=125)

                     self.lb5 = Label(self.top, text='Basım Yılı:', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb5.place(x=40, y=185)
                     self.lb6 = Label(self.top, text=self.srval[3], bg='black', fg='white', font=('arial', 12, 'bold'))
                     self.lb6.place(x=130, y=185)

                     self.lb7 = Label(self.top, text='Fiyatı:', bg='black', fg='blue', font=('arial', 12, 'bold'))
                     self.lb7.place(x=40, y=245)
                     self.lb8 = Label(self.top, text=self.srval[4] , bg='black', fg='white', font=('arial', 12, 'bold'))
                     self.lb8.place(x=130, y=245)

                     self.lb9 = Label(self.top, text='TL' , bg='black', fg='white', font=('arial', 12, 'bold'))
                     self.lb9.place(x=155, y=245)


                 else:
                     messagebox.showwarning('Kütüphane Yönetim Sistemi','KİTAP MEVCUT DEĞİL !')

         object=demt()
         object.delmdata()




    #-------------------------------------------kitap gösterimi_------------------------------------------------

     def show(self):
         class tst(maincode):
             def __init__(self):
                 self.fc = Frame(root, bg='lightgray', width=900, height=390)
                 self.fc.place(x=0, y=110)
                 self.popframe=Frame(self.fc,width=900,height=30,bg='#3c5a99')
                 self.popframe.place(x=0,y=0)
                 self.lbn=Label(self.popframe,bg='#3c5a99',text='Kitap Bilgileri',fg='#fff',font=('arial',10,
                                                                                                      'bold'))
                 self.lbn.place(x=400,y=5)

                 self.backbt = Button(self.popframe,width=30, bg='#3c5a99',activebackground='#3c5a99',
                                      bd=0, relief='flat', command=self.cur)
                 self.backbt.place(x=0, y=0)
                 self.log = PhotoImage(file='back.png')
                 self.backbt.config(image=self.log, compound=LEFT)
                 self.small_log = self.log.subsample(2, 2)
                 self.backbt.config(image=self.small_log)


                 self.table_frame=Frame(self.fc,bg='lightgray',bd=1,relief='flat')
                 self.table_frame.place(x=0,y=30,width=900,height=360)

                 self.scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
                 self.scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
                 self.book_table=ttk.Treeview(self.table_frame,columns=("kitap_id","kitap_adi","yazar","baski",
                                                                           "fiyat"),
                                      xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
                 self.scroll_x.pack(side=BOTTOM,fill=X)
                 self.scroll_y.pack(side=RIGHT, fill=Y)
                 self.scroll_x.config(command=self.book_table.xview)
                 self.scroll_y.config(command=self.book_table.yview)

                 self.book_table.heading("kitap_id",text="Kitap ID")
                 self.book_table.heading("kitap_adi", text="Kitap Adı")
                 self.book_table.heading("yazar", text="Yazar")
                 self.book_table.heading("baski", text="Basım Yılı")
                 self.book_table.heading("fiyat", text="Fiyat")
                 self.book_table['show']='headings'
                 self.book_table.column("kitap_id",width=200)
                 self.book_table.column("kitap_adi", width=200)
                 self.book_table.column("yazar", width=200)
                 self.book_table.column("baski", width=120)
                 self.book_table.column("fiyat", width=110)
                 self.book_table.pack(fill=BOTH,expand=1)
                 self.fetch_data()

             def fetch_data(self):
                 cursor=dd.cursor()
                 cursor.execute("SELECT * FROM kitap_bilgi")
                 self.rows=cursor.fetchall()
                 if len(self.rows)!=0:
                      for self.row in self.rows:
                           self.book_table.insert('',END,values=self.row)
                 dd.commit()


         oc=tst()

 


     #---------------------------------------giriş sistemi--------------------------------------

     def code(self):

         self.fm=Frame(root,height=500,width=900,bg='white')
         self.fm.place(x=0,y=0)

         self.canvas=Canvas(self.fm,height=500,width=900,bg='#3c5a99')
         self.canvas.place(x=0,y=0)
         
       

         self.fm1=Frame(self.canvas,height=310,width=300,bg='white',bd=3,relief='ridge')
         self.fm1.place(x=300,y=90)
         
       


         self.lb333=Label(self.fm1,text='       KÜTÜPHANE       ',fg='white',bg='#3c5a99',font=('Arial',20,'bold'))
         self.lb333.place(x=2,y=2)

         self.b1=Label(self.fm1,text='Tc No :',bg='white',font=('Arial',10,'bold'))
         self.b1.place(x=20,y=77)

         self.e1=Entry(self.fm1,width=22,font=('arial',9,'bold'),bd=4,relief='groove')
         self.e1.place(x=100,y=75)

         self.lb2=Label(self.fm1,text='Şifre :',bg='white',font=('Arial',10,'bold'))
         self.lb2.place(x=20,y=137)

         self.e2=Entry(self.fm1,width=22,show='*',font=('arial',9,'bold'),bd=4,relief='groove')
         self.e2.place(x=100,y=135)


         self.btn1=Button(self.fm1,text='  Giriş',fg='white',bg='red',width=100,font=('Arial',11,'bold'),
                 activebackground='white',activeforeground='black',command=self.login,bd=3,cursor='hand2')
         self.btn1.place(x=25,y=190)
         self.logo = PhotoImage(file='user.png')
         self.btn1.config(image=self.logo, compound=LEFT)
         self.small_logo = self.logo.subsample(1, 1)
         self.btn1.config(image=self.small_logo)


         self.btn2=Button(self.fm1,text='  Temizle',fg='white',bg='blue',width=100,font=('Arial',11,'bold'),
                 activebackground='white',activeforeground='black',bd=3,cursor='hand2',
                          command=self.mainclear)
         self.btn2.place(x=155,y=190)
         self.log = PhotoImage(file='cart.png')
         self.btn2.config(image=self.log, compound=LEFT)
         self.small_log = self.log.subsample(1, 1)
         self.btn2.config(image=self.small_log)

         
         #-----------------------şifremi unuttum---------------------

         self.forgot=Label(self.fm1,text='Şifremi Unuttum',fg='red',bg='#fff',activeforeground='black',
                           font=('cursive',9,'bold'))
         self.forgot.place(x=95,y=260)
         self.forgot.bind("<Button>",self.mouseClick)


         root.mainloop()

     def mouseClick(self,event):
         self.rog=Tk()
         self.rog.title("Şifre Değiştirme Ekranı")
         self.rog.geometry("400x300+540+260")
         self.rog.iconbitmap("aa.ico")
         self.rog.resizable(0,0)
         self.rog.configure(bg='lightgray')

         
         
         self.label=Label(self.rog,text="*Bu sayfayı açtıysanız giriş yapmak için uygulamayı kapatıp \nyeniden açmanız gerekmektedir!",bg='lightgray',fg='red',font=("cursive",9,'bold'))
         self.label.place(x=30,y=250)

         self.user=Label(self.rog,text='Tc No :',bg='lightgray',fg='black',font=("cursive",10,'bold'))
         self.user.place(x=50,y=55)

         self.user = Label(self.rog, text='Yeni Şifre :', bg='lightgray', fg='black', font=("cursive", 10, 'bold'))
         self.user.place(x=50, y=110)

         self.e1 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e1.place(x=160, y=55)

         self.e2 = Entry(self.rog, width=24, font=('arial', 9, 'bold'), bd=4, relief='groove')
         self.e2.place(x=160, y=110)

         self.btn1 = Button(self.rog, text='Onayla', fg='white', bg='grey', width=20, font=('Arial', 13, 'bold'),
                            activebackground='white', activeforeground='black',bd=3,
                            cursor='hand2',command=self.chan_pas)
         self.btn1.place(x=95, y=170)

     def chan_pas(self):
         self.a=self.e1.get()
         self.b=self.e2.get()
         import sqlite3
         conn=sqlite3.connect('admin.db')
         cursor=conn.cursor()
         cursor.execute("SELECT * FROM adm WHERE tc_kimlik_no='"+self.a+"'")
         conn.commit()
         self.data=cursor.fetchone()

         if self.data!=None:
             cursor = conn.cursor()
             cursor.execute("UPDATE adm SET sifre='" + self.b + "' WHERE tc_kimlik_no='" + self.a + "'")
             conn.commit()
             messagebox.showinfo("Kütüphane Yönetim Sistemi","Şifreniz başarıyla değiştirildi !")
         else:
             self.er = Label(self.rog, text='TC Gerekli Değil', bg='#fff', fg='red', font=("cursive", 8, 'bold'))
             self.er.place(x=170, y=125)

         

         self.rog.mainloop()
          






     '''def new_password(self):
         self.tok=Tk()
         self.tok.title("New Password")
         self.tok.iconbitmap("aa.ico")
         self.tok.geometry("400x300+400+300")
         self.tok.resizable(0,0)
         self.tok.configure(bg='#fff')
         self.tok.mainloop()'''




ob=maincode()
ob.code()
