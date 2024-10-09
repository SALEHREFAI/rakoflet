from flet import *
import sqlite3
conn=sqlite3.connect("dato,db",check_same_thread=False)
cursor=conn.cursor()
cursor.execute(""" CREATE TABLE IF  NOT EXISTS student(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      stdname TEXT,
      stdmail TEXT,
      stdphone TEXT,
      stdaddress TEXT,
      stmath INTEGER,
      starabic INTEGER,
      stenglish INTEGER,
      stchirm INTEGER,
      stdrow INTEGER,
      stfrance INTEGER                                                                       
       ) 
""")
conn.commit()




def main(page:Page):
    page.title="صالح الرفاعي"
    page.scroll="auto"
    page.window.width=390
    page.window.height=740
    page.window.top=1
    page.window.left=960
    page.bgcolor='white'
    page.theme_mode=ThemeMode.LIGHT

    tabe_name= 'student'
    query=f'SELECT COUNT(*) FROM {tabe_name}'
    cursor.execute(query)
    result=cursor.fetchone()
    row_count=result[0]    

    def add(e):
        cursor.execute("INSERT INTO student (stdname,stdmail,stdphone,stdaddress,stmath,starabic,stenglish,stchirm,stdrow,stfrance)VALUES(?,?,?,?,?,?,?,?,?,?)",(tname.value,tmail.value,tphone.value,taddress.value,mathmatic.value,arabic.value,draw.value,france.value,englich.value,chimstry.value))
        conn.commit()
    def show(e):
        c=conn.cursor()
        c.execute("SElECT * FROM student")  
        users=c.fetchall()
        print(users) 

        if not users == "":
            keys =['id','stdname','stdmail','stdphone','stdaddress','stmath','starabic','stenglish','stchirm','stdrow','stfrance']
            result=[dict(zip(keys,values)) for values in users]
            for x in result:
              page.add(
                Card(
                    color='black',
                    content=Container(
                        content=Column([
                         ListTile(
                            leading=Icon(icons.PERSON),
                            title=Text('Name : ' + x['stdname'],color='white'),
                            subtitle=Text('Student Email : '+x['stdmail'],color='amber')
                         ),
                         Row([
                             Text('phone : '+ x['stdphone'],color='green' ),
                             Text('address : '+ x['stdaddress'],color='green' )
                         ],alignment=MainAxisAlignment.CENTER) ,
                         Row([
                             Text('عربي'+str(x['starabic']),color='blue'),
                             Text('رياضيات'+str(x['stmath']),color='blue'),
                             Text('انكليزي'+str(x['stenglish']),color='blue')
                         ]), 
                         Row([
                             Text('كيمياء'+str(x['stchirm']),color='blue'),
                             Text('فرنسي'+str(x['stfrance']),color='blue'),
                             Text('رسم'+str(x['stdrow']),color='blue')
                         ])                                        
                           ])  
                        )
                    )
 
                 )
            
        
    tname=TextField(label='اسم الطالب',icon=icons.PERSON,rtl=True,height=38)
    tmail=TextField(label='البريد الالكتروني',icon=icons.MAIL,rtl=True,height=38)
    tphone=TextField(label='رقم الهاتف',icon=icons.PHONE,rtl=True,height=38)
    taddress=TextField(label='العنوان ',icon=icons.LOCATION_CITY,rtl=True,height=38)

    marktext=Text("علامات الطالب",text_align='center',weight='bold')
    mathmatic=TextField(label='رياضيات',width=110,rtl=True,height=38)
    arabic=TextField(label='عربي',width=110,rtl=True,height=38)
    draw=TextField(label='رسم',width=110,rtl=True,height=38)
    france=TextField(label='فرنسي',width=110,rtl=True,height=38)
    englich=TextField(label='انكليزي',width=110,rtl=True,height=38)
    chimstry=TextField(label='كيمياء',width=110,rtl=True,height=38)

    addbuttun=ElevatedButton(
        "اضافة طالب جديد",
        width=170,
        style=ButtonStyle(bgcolor='blue',color='white',padding=15),
        on_click=add
    )
    showbuttun=ElevatedButton(
        "عرض كل الطلاب",
        width=170,
        style=ButtonStyle(bgcolor='blue',color='white',padding=15),
        on_click=show
    )

    page.add(
        Row([    
            Image(src="home.gif",width=280)
        ],alignment=MainAxisAlignment.CENTER),
          Row([    
            Text("تطبيق الطالب والمعلم",size=40,font_family="Aldhabi",color="black")
        ],alignment=MainAxisAlignment.CENTER), 
        Row([    
            Text("عدد الطلاب",size=20,color="BLUE"),
              Text(row_count,size=40,font_family="Aldhabi",color="black")
        ],alignment=MainAxisAlignment.CENTER,rtl=True),
        tname,
        tmail,
        tphone,
        taddress,
        Row([
            marktext
        ],alignment=MainAxisAlignment.CENTER,rtl=True), 
         Row([
            mathmatic,arabic,france
        ],alignment=MainAxisAlignment.CENTER,rtl=True),
         Row([
           englich,draw,chimstry
        ],alignment=MainAxisAlignment.CENTER,rtl=True),
          Row([
           addbuttun,showbuttun
        ],alignment=MainAxisAlignment.CENTER,rtl=True)
    )
  
  

    page.update()
app(main)    
