#创建一个学生管理系统交互界面的项目

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