#创建一个学生管理系统交互界面的项目

from tkinter import *
import tkinter.messagebox as messagebox

#第二部分：设置初始教师和学生信息并定义login
teacher={'admin':{'Pwd':'123456','Name':'Admin'},'admin2':{'Pwd':'987654321','Name':'Admin2'}}
student={'BZB':100,'Bzb':80,'bzb':95}
#字典分别保存教师和学生信息
def login(name,password):  #判断是否登录成功的指令
    if name.get() not in teacher.keys():
        defeat()
    elif name.get() in teacher.keys():
        if teacher[name.get()]['Pwd']!=password.get():
            defeat()
        else:
            access()

#第一部分：设计学生管理系统登录界面
top=Tk()   #学生管理系统登录界面
top.geometry('320x220')
top.title('学生管理系统登录界面')
Label(top,text='用户名:').place(x=50,y=50)
Label(top,text='密码:').place(x=50,y=100)
name=Entry(top,bd=5)  #将输入的用户名保存在变量name中
name.place(x=100,y=50)
password=Entry(top,bd=5)
password.place(x=100,y=100)
Button(top,text='Login',width=5,height=1,command=lambda:login(name,password)).place(x=100,y=150)
Button(top,text='退出',width=5,height=1,command=top.destroy).place(x=200,y=150)
top.mainloop()
