from tkinter import *
import ttkbootstrap as ttk
from datetime import date,datetime
import requests
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as tk
from ttkbootstrap import Style, Label, Entry, Button
from ttkbootstrap.scrolled import ScrolledFrame
import json
from tkinter import scrolledtext
import tkinter.messagebox


root = ttk.Window(themename="minty")
root.title("DKUB WATERPARK")
root.geometry("1920x1080")

member_id = 0
services_date = None
services_info = None
tickets = [None for i in range(4)]
group_tickets = [None for i in range(4)]
lockers = [None, None]
towels = None
cabanas = [None]

tickets_val = [IntVar() for i in range(4)]
group_tickets_val = [IntVar() for i in range(4)]
lockers_val = [IntVar() for i in range(2)]
towels_val = IntVar()
cabanas_val = IntVar()
discount_text = StringVar()
total_text = StringVar()
discount_text.set(f"Discount: 0")
total_text.set(f"Total: 0") 

def set_user_id(user_id):
    global member_id
    member_id = user_id
    return member_id

def get_member_info(member_id):
    get_member_detail(member_id)
    show_page(4,frame_home_member)

def get_member_info_service(member_id):
    get_member_detail(member_id)
    show_page(4,services_frame)

def get_booking_his():
    booking_his()
    show_page(12, frame_view_member)

def get_order(member_id): ### สร้างมาลอง เดะลบ
    show_page(1,services_frame)
    get_order_detail(member_id)
    get_order_detail_total(member_id)

API_ENDPOINT3 = "http://127.0.0.1:8000/subscription"
API_ENDPOINT1 = "http://127.0.0.1:8000/login"
API_ENDPOINT_LOGIN = "http://127.0.0.1:8000/login"
API_ENDPOINT_SUBSCRIPTION = "http://127.0.0.1:8000/subscription"
API_ENDPOINT_SERVICES = f"http://127.0.0.1:8000/{member_id}/services"
# API_ENDPOINT_SERVICES_DATE = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"
API_ENDPOINT_ADD_ITEM = f"http://127.0.0.1:8000//{member_id}/services/{services_date}"


image_path = "6963703.jpg"  # Provide the path to your image file
image_path2 ="Bank.jpg"
image_path3 ="DKUB_logo.jpg"
image_path4 ="Design3.png"
image_path5 = "2.png"
image_path6 = "waterpark.png"
image_path7 = "water.png"
image_path8 = "background.png"
image_path9 = "paymentsuccess.png"
image_path10 = "payment.png"
image50 = Image.open(image_path)
image2 = Image.open(image_path2)
image3 = Image.open(image_path3)
image4 = Image.open(image_path4)
image5 = Image.open(image_path5)
image_waterpark_home = Image.open(image_path6)
image_waterpark_register = Image.open(image_path7)
image_booking_his = Image.open(image_path8)
image_payment_succes = Image.open(image_path9)
image_payment = Image.open(image_path10)
resized_image = image50.resize((120, 120), Image.BICUBIC)  # Adjust the size as needed
image50 = ImageTk.PhotoImage(resized_image)
resized_image2 = image2.resize((120, 120), Image.BICUBIC)  # Adjust the size as needed
image2 = ImageTk.PhotoImage(resized_image2)
resized_image3 = image3.resize((1000, 150), Image.BICUBIC)  # Adjust the size as needed
image3 = ImageTk.PhotoImage(resized_image3)
resized_image4 = image4.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image4 = ImageTk.PhotoImage(resized_image4)
resized_image5 = image5.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image5 = ImageTk.PhotoImage(resized_image5)
resized_image6 = image_waterpark_home.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image_waterpark_home = ImageTk.PhotoImage(resized_image6)
resized_image7 = image_waterpark_register.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image_waterpark_register = ImageTk.PhotoImage(resized_image7)
resized_image8 = image_booking_his.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
background_image = ImageTk.PhotoImage(resized_image8)
resized_image9 = image_payment_succes.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image_payment_sus = ImageTk.PhotoImage(resized_image9)
resized_image10 = image_payment.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image_payment_show = ImageTk.PhotoImage(resized_image10)


bg_pic = PhotoImage(file='waterpark.png')
bg3_pic= PhotoImage(file='sea.png')
park=PhotoImage(file="zoom.png")

#slides family
fam1 = PhotoImage(file='fam.png')
fam2 = PhotoImage(file='fam2.png')
fam3 = PhotoImage(file='fam3.png')
family_list = ["Hanumans Splash", "River Slide","Mermaid Lagoon"]
fam_pic=[fam1,fam2,fam3]

#slides easy
easy1=PhotoImage(file='easy1.png')
easy2=PhotoImage(file='easy2.png')
easy3=PhotoImage(file='easy3.png')
easy_list=["Serpentine","Spiral","Mat Racer"]
easy_pic=[easy1,easy2,easy3]#listรูปภาพ easy

#slides medium
med1=PhotoImage(file='med1.png')
med2=PhotoImage(file='med2.png')
med3=PhotoImage(file='med3.png')
medium_list=["Aqua Coaster","Aqua Conda","Python"]
med_pic=[med1,med2,med3] #listรูปภาพ medium

hard1=PhotoImage(file='hard1.png')
hard2=PhotoImage(file='hard2.png')
hard3=PhotoImage(file='hard3.png')
hard_list=["Free Fall","Aqua Loop","Boomerango"]
hard_pic=[hard1,hard2,hard3] #listรูปภาพ hard

pool1=PhotoImage(file='pool1.png')
pool2=PhotoImage(file='pool2.png')
pool3=PhotoImage(file='pool3.png')
pool4=PhotoImage(file='pool4.png')
pool5=PhotoImage(file='pool5.png')
pool_list=["Double Wave Pool","Lazy River","Party Pool","Activity Pool","Relax Pool"]
pool_pic=[pool1,pool2,pool3,pool4,pool5]


# สร้างตัวแปร global สำหรับแสดงข้อมูล
name_label = None
email_label = None
telephone_label = None
date_of_visit_label = None

frame_home = ttk.Frame(root)
frame_order = ttk.Frame(root)
frame_order_detail_member = ScrolledFrame(root, autohide = True)
frame_home_1 = ttk.Frame(root)
frame_view_member = ttk.Frame(root)
frame_card_payment = ttk.Frame(root)
frame_bank_payment = ttk.Frame(root)
frame_payment_success = ttk.Frame(root)
frame_login = ttk.Frame(root)
frame_register = ttk.Frame(root)
frame_home_member = ttk.Frame(root)
frame_view_booking_his = ttk.Frame(root)
services_frame = ScrolledFrame(root, autohide = True)
frame_home_member_test = ttk.Frame(root)

def set_user_id(user_id):
    global member_id
    member_id = user_id
    return member_id

def log_out():
    set_user_id(0)
    print(member_id)
    show_page(3,frame_home_member)


def log_out_service():
    set_user_id(0)
    print(member_id)
    show_page(3,services_frame)




############################################################################################################

def show_page_home(page):
    if page == 8:
        frame_home_1.pack(fill="both", expand=True)
    
    
show_page_home(8)


def show_page(page, current_frame):
    current_frame.pack_forget()  # ซ่อน frame ปัจจุบัน

    if page == 1:
        frame_order_detail_member.pack(fill="both", expand=True)

    if page == 2:
        frame_order.pack()

    if page == 3:
        frame_home_1.pack(fill="both", expand=True)

    if page == 4:
        frame_view_member.pack(fill="both", expand=True)
    
    if page == 5:
        frame_card_payment.pack(fill="both", expand=True)
    
    if page == 6:
        frame_bank_payment.pack(fill="both", expand=True)

    if page == 7:
        frame_payment_success.pack(fill="both", expand=True)
    
    if page == 9:
        frame_login.pack(fill="both", expand=True)
    
    if page == 10:
        frame_register.pack(fill="both", expand=True)
    
    if page == 11:
        frame_home_member.pack(fill="both", expand=True)
    
    if page == 12:
        frame_view_booking_his.pack(fill="both", expand=True)
    
    if page == 13:
        frame_payment_success.pack(fill="both", expand=True)
    
    if page == 14:
        services_frame.pack(fill="both", expand=True)



def show_slides(my_frame):
    # เคลียร์ข้อความทั้งหมดใน my_frame
    my_frame.config(state=tk.NORMAL)
    my_frame.delete(1.0, tk.END)
    
    # เพิ่มข้อความ "OUR SLIDES" และรายการ family_list ลงใน my_frame
    my_frame.insert(tk.END, "\n")
    my_frame.insert(tk.END, "OUR SLIDES\n","tag1")
    my_frame.tag_configure("tag1", font = ( "Times New Roman" , 19, "bold"),justify='center')
    my_frame.insert(tk.END, "\n")
    my_frame.insert(tk.END, " Family Friendly\n", "tagname")
    my_frame.tag_configure("tagname", font=("Cambria", 16,"bold"))
    x=0
    for i in family_list:
        my_frame.insert(tk.END,f"\t- {i}\n\t")
        my_frame.image_create(tk.END, image=fam_pic[x],align='bottom')
        my_frame.insert(tk.END,"\n\n")
        x += 1
    x=0
    my_frame.insert(tk.END, " Easy Going\n", "tagname")
    for i in easy_list:
        my_frame.insert(tk.END,f"\t- {i}\n\t")
        my_frame.image_create(tk.END, image=easy_pic[x],align='bottom')
        my_frame.insert(tk.END,"\n\n")
        x += 1
    
    x=0
    my_frame.insert(tk.END, " Medium Range\n", "tagname")
    for i in medium_list:
        my_frame.insert(tk.END,f"\t- {i}\n\t")
        my_frame.image_create(tk.END, image=med_pic[x],align='bottom')
        my_frame.insert(tk.END,"\n\n")
        x += 1
        
    x=0
    my_frame.insert(tk.END, f" Completely Extreme\n", "tagname")
    for i in hard_list:
        my_frame.insert(tk.END,f"\t- {i}\n\t")
        my_frame.image_create(tk.END, image=hard_pic[x],align='bottom')
        my_frame.insert(tk.END,"\n\n")
        x += 1
        
    my_frame.config(state=tk.DISABLED)


def show_pool(my_frame):
    my_frame.config(state=tk.NORMAL)
    my_frame.delete(1.0, tk.END)
    
    my_frame.insert(tk.END, "\n")
    my_frame.insert(tk.END, "OUR POOLS\n","tag1")
    my_frame.tag_configure("tag1", font = ( "Times New Roman" , 19, "bold"),justify='center')
    my_frame.insert(tk.END, "\n")
    x=0
    my_frame.insert(tk.END, " Pool\n", "tagname")
    for i in pool_list:
        my_frame.insert(tk.END,f"\t- {i}\n\t")
        # แทรกรูปภาพใน ScrolledText widget
        my_frame.image_create(tk.END, image=pool_pic[x],align='bottom')
        my_frame.insert(tk.END,"\n\n")
        x += 1
        
    my_frame.config(state=tk.DISABLED)



width_button = 60
pading_button = 13
style = Style(theme='minty')
style.configure("TButton", foreground="black")
button_styles = {'home_mem': { 'foreground': 'black'},}
# Create and configure buttons with custom styles
for button_name, style_options in button_styles.items():
    button_style_name = f'{button_name}.TButton'
    style=ttk.Style()
    style.configure(button_style_name,
                        foreground = style_options['foreground'],
                        font=('Angsana New', 20)
                        )
   
   
label = Label(frame_home_member, image=bg_pic)
label.place(relheight=1, relwidth=1)


my_frame_home_member = scrolledtext.ScrolledText(frame_home_member, width=48, height=40)
my_frame_home_member.place(relx=0.1, rely=0.5, anchor=tk.CENTER, x=170, y=30)


show_slides(my_frame_home_member)
slides_button = ttk.Button(frame_home_member, text="Our Slides", command=lambda :show_slides(my_frame_home_member), width=24, bootstyle="success")
slides_button.place(relx=0.1,rely=0.1, anchor=ttk.NW,x=10,y=120)
pool_button = ttk.Button(frame_home_member, text="Pool", command=lambda :show_pool(my_frame_home_member), width=23, bootstyle="success")
pool_button.place(relx=0.2,rely=0.1, anchor=ttk.NW,x=-20,y=120)
contact = Frame(frame_home_member, relief="ridge",borderwidth=20,padx=20,pady=20)
contact.place(relx=0.3, rely=0.9, anchor=ttk.SW,x=160,y=20)


font_contact = ("Cambria", 12)




contact_label = ttk.Label(contact, text="CONTACT", font=("Cambria", 14, "bold"))
contact_label.pack()


location_label = ttk.Label(contact, text="Location : KMITL ECC Building, 1 Thanon Chalong Krung, Khwaeng Lam Prathew, Lat Krabang, Bangkok 10520", font=font_contact)
location_label.pack(anchor='w')


email_label_home_member = ttk.Label(contact, text="Email : Dkub@email.com", font=font_contact)
email_label_home_member.pack(anchor='w')


email_label_home_member = ttk.Label(contact, text="Phone number : 0-2329-8106", font=font_contact)
email_label_home_member.pack(anchor='w')


hour_label_home_member = ttk.Label(contact, text="Office hours : Monday - Sunday: 10:00-18:00", font=font_contact)
hour_label_home_member.pack(anchor='w')


home_button_member = ttk.Button(frame_home_member, text="Home", command=lambda : show_page(11,frame_home_member), width=width_button, padding=pading_button,style='home_mem.TButton')
home_button_member.place(x=0,y=0)


service_button_member = ttk.Button(frame_home_member, text="Service", command= lambda: show_page(14,frame_home_member), width=width_button, padding=pading_button,style='home_mem.TButton')
service_button_member.place(relx=0.2,x=102,y=0)


login_button_member = ttk.Button(frame_home_member, text="info", command=lambda: get_member_info(member_id), width=width_button, padding=pading_button,style='home_mem.TButton')
login_button_member.place(relx=0.5,x=12,y=0)


register_button_member = ttk.Button(frame_home_member, text="Log out", command=log_out, width=width_button, padding=pading_button,style='home_mem.TButton')
register_button_member.place(relx=0.7,x=102,y=0)


print(f"Member :{member_id}")





















############################################################################################################


width_botton = 70
column_position=0
pading_button=13

style.configure("service.TButton",font=('Angsana New', 20))

home_service = ttk.Frame(services_frame)
home_service.pack(pady=0)

home_button = ttk.Button(home_service, text="Home", command=lambda: show_page(11, services_frame), width=width_botton, padding=pading_button,style="service.TButton")
home_button.pack(side="left", padx=0, pady=10)

login_button = ttk.Button(home_service, text="info", command=lambda: get_member_info_service(member_id), width=width_botton, padding=pading_button,style="service.TButton")
login_button.pack(side="left", padx=0, pady=10)

register_button = ttk.Button(home_service, text="Log out", command=log_out_service, width=width_botton, padding=pading_button,style="service.TButton")
register_button.pack(side="left", padx=0, pady=10)

##########################################################################
# Show services info

def change_format_date(str_date):
    month, day, year = str_date.split("/")
    month = month if len(month)==2 else "0"+month
    day = day if len(day)==2 else "0"+day
    ymd = f"{year}-{month}-{day}"
    print(ymd)
    return ymd

def get_services_in_date():
    global member_id
    global services_date
    global services_info
    
    services_date = visit_date.entry.get()
    services_date = change_format_date(services_date)
    
    API_ENDPOINT_SERVICES_DATE  = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"
    response = requests.get(API_ENDPOINT_SERVICES_DATE)
    #print(f"{services_date} - {response.json()}")
    
    if response.status_code == 200:
        if response.json().get(f"Services in {services_date}") != "Please select the available date.":
            services_info = response.json().get(f"Services in {services_date}")
            show_visit_date.config(text = f"Your visit date: {services_date}", foreground = 'black')
            create_service()
            #show_services_in_date()
        else:
            show_visit_date.config(text = str(response.json().get(f"Services in {services_date}")), foreground = 'red')
    else:
        services_info = None
        print(f"API request failed with status code: {response.status_code}")
        #print(response.json())

def get_button_style(style_name, font_size):
    
    # Define custom styles for each button
    button_styles = {
        'default': {'background': 'darkblue', 'foreground': 'white'},
        'standard': {'background': 'green', 'foreground': 'white'},
        'medium': {'background': 'blue', 'foreground': 'white'},
        'large': {'background': 'orange', 'foreground': 'white'}
    }
    # Create and configure buttons with custom styles
    for button_name, style_options in button_styles.items():
        if style_name == button_name:
            button_style_name = f'{button_name}.TButton'
            ttk.Style().configure(button_style_name, 
                                background = style_options['background'], 
                                foreground = style_options['foreground'], 
                                font=('Arial', font_size)
                                )
            return button_style_name

def create_zone(zone_frame, image_path):
    image = Image.open(image_path)
    resized_image = image.resize((1000, 690))
    photo = ImageTk.PhotoImage(resized_image)

    label = ttk.Label(zone_frame, image=photo)
    label.photo = photo 
    label.place(anchor = NW) 
    
    s_size = ttk.Label(zone_frame, 
                    text="Standard Size\n(2 - 4 people)", 
                    font=("Arial", 17), 
                    background = 'green', 
                    foreground = 'white'
                    )
    
    m_size = ttk.Label(zone_frame, 
                    text="Medium Size\n(4 - 8 people)", 
                    font=("Arial", 17), 
                    background = 'blue', 
                    foreground = 'white'
                    )
    
    l_size = ttk.Label(zone_frame, 
                    text="Large Size\n(8 - 12 people)", 
                    font=("Arial", 17), 
                    background = 'orange', 
                    foreground = 'white'
                    )
    
    s_size.place( x = 113, y = 41, anchor = CENTER)
    m_size.place( x = 225, y = 41, anchor = CENTER)
    l_size.place( x = 338, y = 41, anchor = CENTER)
    
    back_button = ttk.Button(zone_frame, text="Back", bootstyle = 'info', command=lambda: back_to_selection(zone_frame))
    back_button.place( x = 28, y = 17, anchor = CENTER)
    close_button = ttk.Button(zone_frame, text="Close", bootstyle = 'danger', command=zone_frame.destroy)
    close_button.place( x = 970, y = 15, anchor = CENTER)
    
    return label

def back_to_selection(frame):
    frame.destroy()
    show_cabana_zone()

def show_cabana(cabana_list, frame):
    for button in cabana_list:
        flag = True
        for cabana in services_info["cabana"][frame.title()]:
            if cabana["id"] == button.cget('text'):
                flag = False
                break
        if flag :
            button.place_forget() 

def confirm_button_click(selected_cabana, cabana_list, frame, cabana_zone_frame):
    if selected_cabana is None:
        return

    for cabana in cabana_list:
        if selected_cabana.cget('text') == cabana.cget('text'):
            item = {}
            item['name'] = 'cabana'
            item['zone'] = frame.title()
            item['id'] = selected_cabana.cget('text') 
            add_item(item, cabanas_val)
            # Schedule destruction using after method
            frame.after(0, frame.destroy)
            cabana_zone_frame.after(0, cabana_zone_frame.destroy)

# Create Wave Pool Zone

# Create Wave Pool Zone
def wavepool_zone(cabana_zone_frame):
    global services_date
    cabana_zone_frame.destroy()
    wavepool_frame = Toplevel(root)
    wavepool_frame.title("Wave Pool")
    wavepool_frame.geometry('1000x690')
    wavepool = "wavepool_zone.png"
    wavepool_font_size = 7
    
    create_zone(wavepool_frame, wavepool)
    
    w01 = ttk.Button(wavepool_frame, text="W01", style = get_button_style('standard', wavepool_font_size))
    w01.place( x = 28, y = 545, anchor = CENTER) 
    w02 = ttk.Button(wavepool_frame, text="W02", style = get_button_style('standard', wavepool_font_size))
    w02.place( x = 71, y = 547, anchor = CENTER) 
    w03 = ttk.Button(wavepool_frame, text="W03", style = get_button_style('medium', wavepool_font_size + 3))
    w03.place( x = 120, y = 549, anchor = CENTER)
    w04 = ttk.Button(wavepool_frame, text="W04", style = get_button_style('medium', wavepool_font_size + 3))
    w04.place( x = 174, y = 553, anchor = CENTER) 
    w05 = ttk.Button(wavepool_frame, text="W05", style = get_button_style('medium', wavepool_font_size + 3))
    w05.place( x = 229, y = 554, anchor = CENTER) 
    w06 = ttk.Button(wavepool_frame, text="W06", style = get_button_style('medium', wavepool_font_size + 3))
    w06.place( x = 288, y = 551, anchor = CENTER)
    w07 = ttk.Button(wavepool_frame, text="W07", style = get_button_style('medium', wavepool_font_size + 3))
    w07.place( x = 360, y = 549, anchor = CENTER)
    w08 = ttk.Button(wavepool_frame, text="W08", style = get_button_style('medium', wavepool_font_size + 3))
    w08.place( x = 406, y = 541, anchor = CENTER)
    w09 = ttk.Button(wavepool_frame, text="W09", style = get_button_style('medium', wavepool_font_size + 3))
    w09.place( x = 452, y = 536, anchor = CENTER)
    w10 = ttk.Button(wavepool_frame, text="W10", style = get_button_style('standard', wavepool_font_size))
    w10.place( x = 494, y = 530, anchor = CENTER)
    w11 = ttk.Button(wavepool_frame, text="W11", style = get_button_style('standard', wavepool_font_size))
    w11.place( x = 532, y = 532, anchor = CENTER)
    w12 = ttk.Button(wavepool_frame, text="W12", style = get_button_style('standard', wavepool_font_size))
    w12.place( x = 571, y = 535, anchor = CENTER)
    w13 = ttk.Button(wavepool_frame, text="W13", style = get_button_style('standard', wavepool_font_size))
    w13.place( x = 608, y = 540, anchor = CENTER)
    w14 = ttk.Button(wavepool_frame, text="W14", style = get_button_style('standard', wavepool_font_size))
    w14.place( x = 646, y = 543, anchor = CENTER)
    w15 = ttk.Button(wavepool_frame, text="W15", style = get_button_style('large', wavepool_font_size + 4))
    w15.place( x = 778, y = 392, anchor = CENTER)
    w16 = ttk.Button(wavepool_frame, text="W16", style = get_button_style('standard', wavepool_font_size))
    w16.place( x = 845, y = 283, anchor = CENTER)
    w17 = ttk.Button(wavepool_frame, text="W17", style = get_button_style('medium', wavepool_font_size + 4))
    w17.place( x = 826, y = 240, anchor = CENTER)
    w18 = ttk.Button(wavepool_frame, text="W18", style = get_button_style('medium', wavepool_font_size))
    w18.place( x = 816, y = 190, anchor = CENTER)
    w19 = ttk.Button(wavepool_frame, text="W19", style = get_button_style('standard', wavepool_font_size))
    w19.place( x = 836, y = 155, anchor = CENTER)
    w20 = ttk.Button(wavepool_frame, text="W20", style = get_button_style('standard', wavepool_font_size))
    w20.place( x = 862, y = 195, anchor = CENTER)
    w21 = ttk.Button(wavepool_frame, text="W21", style = get_button_style('standard', wavepool_font_size))
    w21.place( x = 871, y = 236, anchor = CENTER)
    
    cabana_list = [w01, w02, w03, w04, w05, w06, w07, w08, w09, w10, w11, 
                w12, w13, w14, w15, w16, w17, w18, w19, w20, w21]
    show_cabana(cabana_list, wavepool_frame) 
    
    for cabana_button in cabana_list:
        cabana_button.config(command=lambda button=cabana_button: show_text(button))
    
    # selected_cabana = None
    
    selected_cabana = None  # Variable to store the selected cabana ID

    select_cabana = ttk.Label(wavepool_frame, 
                            text="  Please select the cabana.  ", 
                            foreground='white',
                            background='purple',
                            font=('Arial', 21)
                            )
    select_cabana.place(x = 480, y = 33)

    def show_text(cabana):
        nonlocal selected_cabana
        select_cabana.config(text=f"  Selected Cabana: {cabana.cget('text')}  ")
        selected_cabana = cabana

    confirm_button = ttk.Button(wavepool_frame,
                    text="Confirm",
                    bootstyle='success',
                    command=lambda: confirm_button_click(selected_cabana, cabana_list, wavepool_frame, cabana_zone_frame) if selected_cabana else None
                    )
    if services_date != None:
        confirm_button.place( x = 900, y = 15, anchor = CENTER)

# Create Activity and Relax Zone
def activity_zone(cabana_zone_frame):
    cabana_zone_frame.destroy()
    activity_frame = Toplevel(root)
    activity_frame.title("Activity and Relax")
    activity_frame.geometry('1000x690')
    activity = "activity_zone.png"
    activity_font_size = 17
    
    create_zone(activity_frame, activity)
    
    p01 = ttk.Button(activity_frame, text="P01", style = get_button_style('standard',activity_font_size))
    p01.place( x = 112, y = 388, anchor = CENTER) 
    p02 = ttk.Button(activity_frame, text="P02", style = get_button_style('standard',activity_font_size))
    p02.place( x = 181, y = 388, anchor = CENTER) 
    p03 = ttk.Button(activity_frame, text="P03", style = get_button_style('medium',activity_font_size))
    p03.place( x = 335, y = 402, anchor = CENTER) 
    p04 = ttk.Button(activity_frame, text="P04", style = get_button_style('medium',activity_font_size))
    p04.place( x = 414, y = 399, anchor = CENTER)
    
    cabana_list = [p01, p02, p03, p04]
    show_cabana(cabana_list, activity_frame)  
    
    for cabana_button in cabana_list:
        cabana_button.config(command=lambda button=cabana_button: show_text(button))
    
    selected_cabana = None  # Variable to store the selected cabana ID

    select_cabana = ttk.Label(activity_frame, 
                            text="  Please select the cabana.  ", 
                            foreground='white',
                            background='purple',
                            font=('Arial', 21)
                            )
    select_cabana.place(x = 480, y = 33)

    def show_text(cabana):
        nonlocal selected_cabana
        select_cabana.config(text=f"  Selected Cabana: {cabana.cget('text')}  ")
        selected_cabana = cabana

    confirm_button = ttk.Button(activity_frame,
                    text="Confirm",
                    bootstyle='success',
                    command=lambda: confirm_button_click(selected_cabana, cabana_list, activity_frame, cabana_zone_frame) if selected_cabana else None
                    )

    if services_date != None:
        confirm_button.place( x = 900, y = 15, anchor = CENTER)

# Create Hill Zone
def hill_zone(cabana_zone_frame):
    cabana_zone_frame.destroy()
    hill_frame = Toplevel(root)
    hill_frame.title("Hill")
    hill_frame.geometry('1000x690')
    hill = "hill_zone.png"
    hill_font_size = 16
    
    create_zone(hill_frame, hill)
    
    h01 = ttk.Button(hill_frame, text="H01", style = get_button_style('standard',hill_font_size - 3))
    h01.place( x = 545, y = 561, anchor = CENTER) 
    h02 = ttk.Button(hill_frame, text="H02", style = get_button_style('standard',hill_font_size - 3))
    h02.place( x = 515, y = 517, anchor = CENTER) 
    h03 = ttk.Button(hill_frame, text="H03", style = get_button_style('standard',hill_font_size - 3))
    h03.place( x = 484, y = 478, anchor = CENTER) 
    h04 = ttk.Button(hill_frame, text="H04", style = get_button_style('medium',hill_font_size))
    h04.place( x = 332, y = 536, anchor = CENTER)
    h05 = ttk.Button(hill_frame, text="H05", style = get_button_style('medium',hill_font_size))
    h05.place( x = 284, y = 587, anchor = CENTER)
    h06 = ttk.Button(hill_frame, text="H06", style = get_button_style('medium',hill_font_size))
    h06.place( x = 253, y = 544, anchor = CENTER)
    h07 = ttk.Button(hill_frame, text="H07", style = get_button_style('standard',hill_font_size - 3))
    h07.place( x = 232, y = 503, anchor = CENTER)
    h08 = ttk.Button(hill_frame, text="H08", style = get_button_style('medium',hill_font_size))
    h08.place( x = 214, y = 463, anchor = CENTER)
    h09 = ttk.Button(hill_frame, text="H09", style = get_button_style('medium',hill_font_size))
    h09.place( x = 187, y = 423, anchor = CENTER)
    h10 = ttk.Button(hill_frame, text="H10", style = get_button_style('standard',hill_font_size - 3))
    h10.place( x = 156, y = 383, anchor = CENTER)
    h11 = ttk.Button(hill_frame, text="H11", style = get_button_style('medium',hill_font_size))
    h11.place( x = 258, y = 325, anchor = CENTER)
    
    cabana_list = [h01, h02, h03, h04, h05, h06, h07, h08, h09, h10, h11]
    show_cabana(cabana_list, hill_frame) 
    
    for cabana_button in cabana_list:
        cabana_button.config(command=lambda button=cabana_button: show_text(button))
    
    selected_cabana = None  # Variable to store the selected cabana ID

    select_cabana = ttk.Label(hill_frame, 
                            text="  Please select the cabana.  ", 
                            foreground='white',
                            background='purple',
                            font=('Arial', 21)
                            )
    select_cabana.place(x = 480, y = 33)

    def show_text(cabana):
        nonlocal selected_cabana
        select_cabana.config(text=f"  Selected Cabana: {cabana.cget('text')}  ")
        selected_cabana = cabana

    confirm_button = ttk.Button(hill_frame,
                    text="Confirm",
                    bootstyle='success',
                    command=lambda: confirm_button_click(selected_cabana, cabana_list, hill_frame, cabana_zone_frame) if selected_cabana else None
                    )

    if services_date != None:
        confirm_button.place( x = 900, y = 15, anchor = CENTER)

# Create Family Zone
def family_zone(cabana_zone_frame):
    cabana_zone_frame.destroy()   
    family_frame = Toplevel(root)
    family_frame.title("Family")
    family_frame.geometry('1000x690')
    family = "family_zone.png"
    family_font_size = 18
    create_zone(family_frame, family)

    
    k01 = ttk.Button(family_frame, text="K01", style = get_button_style('medium', family_font_size + 3))
    k01.place(  x = 899, y = 449, anchor = CENTER) 
    k02 = ttk.Button(family_frame, text="K02", style = get_button_style('standard', family_font_size))
    k02.place(  x = 848, y = 490, anchor = CENTER) 
    k03 = ttk.Button(family_frame, text="K03", style = get_button_style('medium', family_font_size + 3))
    k03.place(  x = 784, y = 530, anchor = CENTER) 
    k04 = ttk.Button(family_frame, text="K04", style = get_button_style('standard', family_font_size))
    k04.place(  x = 704, y = 573, anchor = CENTER) 
    k05 = ttk.Button(family_frame, text="K05", style = get_button_style('standard', family_font_size))
    k05.place( x = 645, y = 595, anchor = CENTER) 
    k06 = ttk.Button(family_frame, text="K06", style = get_button_style('standard', family_font_size))
    k06.place(  x = 536, y = 647, anchor = CENTER) 
    k07 = ttk.Button(family_frame, text="K07", style = get_button_style('standard', family_font_size))
    k07.place(  x = 475, y = 645, anchor = CENTER) 
    k08 = ttk.Button(family_frame, text="K08", style = get_button_style('medium', family_font_size + 3))
    k08.place(  x = 325, y = 605, anchor = CENTER) 
    k09 = ttk.Button(family_frame, text="K09", style = get_button_style('medium', family_font_size + 3))
    k09.place(x = 160, y = 462, anchor = CENTER) 
    k10 = ttk.Button(family_frame, text="K10", style = get_button_style('standard', family_font_size))
    k10.place( x = 116, y = 402, anchor = CENTER) 
    k11 = ttk.Button(family_frame, text="K11", style = get_button_style('large', family_font_size + 6))
    k11.place( x = 181, y = 169 , anchor = CENTER) 
    k16 = ttk.Button(family_frame, text="K16", style = get_button_style('standard', family_font_size))
    k16.place(  x = 487, y = 423, anchor = CENTER) 
    k17 = ttk.Button(family_frame, text="K17", style = get_button_style('medium', family_font_size + 3))
    k17.place( x = 426, y = 460, anchor = CENTER)

    cabana_list = [k01, k02, k03, k04, k05, k09, k10, k11, k17]
    show_cabana(cabana_list, family_frame) 
    
    for cabana_button in cabana_list:
        cabana_button.config(command=lambda button=cabana_button: show_text(button))
    
    selected_cabana = None  # Variable to store the selected cabana 

    select_cabana = ttk.Label(family_frame, 
                            text="  Please select the cabana.  ", 
                            foreground='white',
                            background='purple',
                            font=('Arial', 21)
                            )
    select_cabana.place(x = 480, y = 33)

    def show_text(cabana):
        nonlocal selected_cabana
        select_cabana.config(text=f"  Selected Cabana: {cabana.cget('text')}  ")
        selected_cabana = cabana

    confirm_button = ttk.Button(family_frame,
                    text="Confirm",
                    bootstyle='success',
                    command=lambda: confirm_button_click(selected_cabana, cabana_list, family_frame, cabana_zone_frame) if selected_cabana else None
                    )

    if services_date != None:
        confirm_button.place( x = 900, y = 15, anchor = CENTER)


def show_cabana_zone():
    zone_frame = Toplevel(root)
    zone_frame.title("Zone in DKUB Waterpark")
    zone_frame.geometry('1000x690')

    cabana_zone = "cabana_zone.png"
    image = Image.open(cabana_zone)
    resized_image = image.resize((1000, 690))
    photo = ImageTk.PhotoImage(resized_image)

    label = ttk.Label(zone_frame, image=photo)
    label.photo = photo  # Keep a reference to the PhotoImage object
    label.place(anchor = NW)
    
    # Define custom styles for each button
    button_styles = {
        'default': {'background': 'darkblue', 'foreground': 'white'},
        'wavepool': {'background': 'blue', 'foreground': 'white'},
        'activity': {'background': 'green', 'foreground': 'white'},
        'hill': {'background': 'brown', 'foreground': 'white'},
        'family': {'background': 'purple', 'foreground': 'white'}
    }
    # Create and configure buttons with custom styles
    for button_name, style_options in button_styles.items():
        button_style_name = f'{button_name}.TButton'
        ttk.Style().configure(button_style_name, 
                            background = style_options['background'], 
                            foreground = style_options['foreground'], 
                            font=('Arial', 26)
                            )

    wavepool = ttk.Button(zone_frame, text="Wave Pool Zone", style = 'default.TButton', command = lambda : wavepool_zone(zone_frame))
    wavepool.place( x = 335, y = 210, anchor = CENTER)

    activity = ttk.Button(label, text="Activity and Relax Zone", style = 'default.TButton', command = lambda : activity_zone(zone_frame))
    activity.place( x = 320, y = 355, anchor = CENTER)

    hill = ttk.Button(zone_frame, text="Hill Zone", style = 'default.TButton', command = lambda : hill_zone(zone_frame))
    hill.place( x = 670, y = 240, anchor = CENTER)

    family = ttk.Button(zone_frame, text="Family Zone",style='default.TButton', command = lambda : family_zone(zone_frame))
    family.place( x = 540, y = 508, anchor = CENTER)

    close_button = ttk.Button(zone_frame, text="Close", bootstyle = 'danger', command=zone_frame.destroy)
    close_button.place( x = 970, y = 15, anchor = CENTER)

def add_item(item, val):
    global member_id
    global services_date

    global total_text
    global discount_text
    #print(item, end="\n\n")
    if services_date != None:
        API_ENDPOINT_SERVICES_DATE  = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"

        response = requests.post(API_ENDPOINT_SERVICES_DATE, data=json.dumps(item))
        try : 
            res = response.json()
            #print(res)
            if res["status"] == "Add success.":
                current_value = val.get()
                print(res["total"], res["discount"])
                discount_text.set(f"Discount: {res['discount']} THB.")
                total_text.set(f"Total: {res['total']} THB.") 
                if item["name"] == "cabana" :
                    val.set(1)
                    return
                else :
                    val.set(current_value+1)
                
        except:
            print(res)
    else:
        show_visit_date.config(text = "Select your visit date to create order.", foreground = 'red')
    
def reduce_item(item ,val):
    global member_id
    global services_date

    global total_text
    global discount_text
    
    if services_date != None:
        API_ENDPOINT_SERVICES_DATE  = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"
        print(item, end="\n\n")
        response = requests.delete(API_ENDPOINT_SERVICES_DATE, data=json.dumps(item))
        try : 
            res = response.json()
            #print(res)
            discount_text.set(f"Discount: {res['discount']}")
            total_text.set(f"Total: {res['total']}") 
            if res["status"] == "Delete success.":
                current_value = val.get()
                print(res["total"], res["discount"])
                if current_value == 0 :
                    return
                val.set(current_value-1)
        except:
            print(res)
        
    else:
        show_visit_date.config(text = "Select your visit date to create order.", foreground = 'red')
    
def create_service():
    ticket = services_info["ticket"]
    locker = services_info["locker"]
    towel = services_info["towel"]
    cabana = services_info["cabana"]
    global tickets
    global group_tickets
    global lockers
    global towels
    global cabanas

    global tickets_val
    global group_tickets_val
    global lockers_val 
    global towels_val 
    global cabanas_val 
    global total_text
    global discount_text
    tickets = [{
                    "name": "ticket",
                    "type": item["type"]
                } 
                    for item in ticket if item["amount_per_ticket"] == 1
    ]
    group_tickets = [{
                    "name": "ticket",
                    "type": item["type"]
                } 
                    for item in ticket if item["amount_per_ticket"] > 1
    ]
    lockers = [{
                    "name": "locker",
                    "size": item["size"]
                } 
                for item in locker
    ]
    towels = {
        "name": "towel"
    }
    cabanas = [
        {
            "name": "cabana",
            "zone": item["zone"],
            "id": item["id"]
        } 
        for zone in cabana.values() for item in zone
    ]
    for var in tickets_val: 
        var.set(0)
    for var in group_tickets_val: 
        var.set(0)
    for var in lockers_val: 
        var.set(0)
    towels_val.set(0)
    cabanas_val.set(0)
    discount_text.set(f"Discount: 0")
    total_text.set(f"Total: 0") 


### Select date ###
visit_date = ttk.DateEntry(services_frame, bootstyle = "danger", startdate = date.today())
visit_date.pack(pady = 15)

confirm_date_button = ttk.Button(services_frame, text = "Confirm visit date.", bootstyle = "danger, outline", command = get_services_in_date)
confirm_date_button.pack(pady = 15)

show_visit_date = ttk.Label(services_frame)
show_visit_date.pack(pady = 15)

##########################################################################
# Show services info

services_background = [
    "solo_ticket.png",
    "group_ticket.png",
    "cabana.png",
    "locker_towel.png"
]

#tickets, group_tickets, lockers, towels, cabanas = create_service()

services_background = [
    "solo_ticket.png",
    "group_ticket.png",
    "cabana.png",
    "locker_towel.png"
]

#tickets, group_tickets, lockers, towels, cabanas = create_service()
    
for i in range(len(services_background)):
    # Replace this with the path to your image file
    image = Image.open(services_background[i])
    resized_image = image.resize((1000, 450))
    photo = ImageTk.PhotoImage(resized_image)
    
    label = ttk.Label(services_frame, image = photo)
    label.pack(pady = 20)

    ## Create item button
    # solo ticket
    if i==0 :
        for j in range(len(tickets)):
            #print(tickets[j], end="  ")
            button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: add_item(tickets[j], tickets_val[j]))
            button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(tickets[j], tickets_val[j]))
            amount1 = ttk.Label(services_frame, textvariable=tickets_val[j], bootstyle="dark", font=("Arial", 18))
            button1.place(in_ = label, x = 790, y = 145 + j*80, anchor = CENTER)
            button2.place(in_ = label, x = 940, y = 145 + j*80, anchor = CENTER)
            amount1.place(in_ = label, x = 865, y = 145 + j*80, anchor = CENTER)
            
    # group ticket 
    elif i==1 :
        for j in range(len(group_tickets)):
            amount1 = ttk.Label(services_frame, textvariable=group_tickets_val[j], bootstyle="dark", font=("Arial", 18))
            button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: add_item(group_tickets[j], group_tickets_val[j]))
            button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(group_tickets[j], group_tickets_val[j]))
            button1.place(in_ = label, x = 790, y = 145 + j*78, anchor = CENTER)
            button2.place(in_ = label, x = 940, y = 145 + j*78, anchor = CENTER)
            amount1.place(in_ = label, x = 865, y = 145 + j*78, anchor = CENTER)
    # cabana
    elif i==2 : 
        button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: show_cabana_zone() if cabanas_val.get()==0 else None)
        button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(cabanas[0], cabanas_val) if cabanas_val.get()==1 else None)
        amount1 = ttk.Label(services_frame, textvariable=cabanas_val, bootstyle="dark", font=("Arial", 18))
        button1.place(in_ = label, x = 790, y = 270, anchor = CENTER)
        button2.place(in_ = label, x = 940, y = 270, anchor = CENTER)
        amount1.place(in_ = label, x = 865, y = 270, anchor = CENTER)
    #towel lockers
    elif i==3 :
        button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: add_item(towels, towels_val))
        button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(towels, towels_val))
        amount1 = ttk.Label(services_frame, textvariable=towels_val, bootstyle="dark", font=("Arial", 18))
        button1.place(in_ = label, x = 790, y = 180 , anchor = CENTER)
        button2.place(in_ = label, x = 940, y = 180, anchor = CENTER)
        amount1.place(in_ = label, x = 865, y = 180 , anchor = CENTER)

        for j in range(len(lockers)):
            button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: add_item(lockers[j], lockers_val[j]))
            button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(lockers[j], lockers_val[j]))
            amount1 = ttk.Label(services_frame, textvariable=lockers_val[j], bootstyle="dark", font=("Arial", 18))
            button1.place(in_ = label, x = 790, y = 270 + j*70, anchor = CENTER)
            button2.place(in_ = label, x = 940, y = 270 + j*70, anchor = CENTER)
            amount1.place(in_ = label, x = 865, y = 270 + j*70, anchor = CENTER)
        
    label.image = photo 
def coupon_use(member_id, date):
    global discount_text
    global total_text
    promocode = PromotioncodeEntry.get()
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/services/{date}"
    response = requests.put(API_ENDPOINT, json={"code": promocode})

    if response.status_code == 200:
        data = response.json()  # แก้ไขตรงนี้
        print("Response Data:", data)
        discount_text.set(f"Discount: {data['discount']}")
        total_text.set(f"Total: {data['total']}") 
    else:
        print("Error:", response.text)

promotioncode = ttk.Frame(services_frame, bootstyle = "light")

my_label = ttk.Label(promotioncode, 
                    text = "Enter Coupon Code",
                    foreground = 'black',
                    background = 'lightgray', 
                    font = ("Arial", 15)
                    )

PromotioncodeEntry = ttk.Entry(
    promotioncode,
    bootstyle = "success",
    font = ("Arial", 16),
    foreground = "blue",
    width = 25,
)

confirm_button = ttk.Button(services_frame, 
                text = "Confirm Code",
                bootstyle = 'info', 
                command = lambda: coupon_use(member_id, services_date)
                )

discount_label = ttk.Label(services_frame, 
                        textvariable = discount_text, 
                        bootstyle = "info",
                        foreground = 'red', 
                        font = ("Arial", 14)
                        )

total_label =  ttk.Label(services_frame, 
                        textvariable = total_text, 
                        bootstyle = "dark", 
                        foreground = 'darkblue',
                        font = ("Arial", 20)
                        )

my_button_confirm_order = ttk.Button(services_frame, 
                    text = " CONFIRM YOUR ORDER ", 
                    bootstyle = "success",
                    command= lambda: get_order(member_id)
                    )

promotioncode.pack(pady = 10)
my_label.pack(pady = 10)
PromotioncodeEntry.pack(pady = 15)
confirm_button.pack(pady = 10)
discount_label.pack(pady = 15)
total_label.pack(pady = 15)
my_button_confirm_order.pack(pady = 10)



############################################################################################################


############################################################################################################


def get_order_detail(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_confirm"
    response = requests.get(API_ENDPOINT)
    print(member_id)
    print(response.json())
    if response.status_code == 200:
        data = response.json()
        booking = data["booking"]
        order = booking["order"]
        order_total = order["total"]
        
        # Clear existing labels
        for widget in Order_detail_frame.winfo_children():
            widget.destroy()

        for order_detail in order["order_detail"]:
            item_name = order_detail["item"]
            name = item_name["name"]
            price = item_name["price"]
            subtotal = order_detail["total_price"]
            amount = order_detail["amount"]

            order_label = ttk.Label(
                Order_detail_frame,
                text=f"Item Name: {name},  Amount: {amount},     Price: {price},       Subtotal: {subtotal}",
                font=("Helvetica", 12),
                bootstyle="dark",
            )
            order_label.pack(pady=5, padx=10, ipadx=10)

        name_label.config(text=f"Name: {data['member']['name']}")
        email_label.config(text=f"Email: {data['member']['email']}")
        telephone_label.config(text=f"Telephone: {data['member']['phone_no']}")
        date_of_visit_label.config(text=f"Date of Visit: {order['visit_date']}")
        booking_id.config(text=f"Booking id: {data['booking']['booking_id']}")
        total_price_bank.config(text=f"Total Price:{order_total}")
        booking_id2.config(text=f"Booking id: {data['booking']['booking_id']}")
        total_price2.config(text=f"Total Price:{order_total}")
    else:
        print("Error")


############################################################################################################



def get_order_detail_total(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_confirm"
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        booking = data["booking"]
        order = booking["order"]
        order_total = order["total"]
        order_discount = order["discount"]
        Grand_Total.config(text=f"Grand Total: {order_total}")
        Discount.config(text=f"Discount:{order_discount}")
    else:
        print("Error")  

    # สร้าง Label สำหรับแสดงข้อมูล
    

# Contact Detail

Contact_Image = ttk.Label(frame_order_detail_member, image=image5)
Contact_Image.place(x=0, y=0, relwidth=1, relheight=1)

Contact_Detail_Frame = ttk.Frame(frame_order_detail_member)
Contact_Detail_Frame.pack(pady=120, ipadx=10)

contrat_label = ttk.Label(
    frame_order_detail_member, text="Contact Detail", font=("Helvetica", 25),foreground= "green"
)
contrat_label.pack(pady=5, padx=5)


name_label = ttk.Label(
    frame_order_detail_member, text="Name :", font=("Helvetica", 14)
)
name_label.pack(pady=5, padx=5)

email_label = ttk.Label(
    frame_order_detail_member, text="Email :", font=("Helvetica", 14)
)
email_label.pack(pady=5, padx=5)

telephone_label = ttk.Label(
    frame_order_detail_member, text="Telephone :", font=("Helvetica", 14)
)
telephone_label.pack(pady=5, padx=5)

date_of_visit_label = ttk.Label(
    frame_order_detail_member,
    text="Date of Visit :",
    font=("Helvetica", 14)
)
date_of_visit_label.pack(pady=5, padx=5)

# Order Detail
Order_detail = ttk.Label(
    frame_order_detail_member, text="Order Detail", font=("Helvetica", 25), foreground="green"
)
Order_detail.pack(pady=10)

Order_detail_frame = ttk.Frame(frame_order_detail_member)
Order_detail_frame.pack(pady=10)

Order_detail_frame1 = ttk.Frame(frame_order_detail_member)
Order_detail_frame1.pack(pady=10)

Grand_Total = ttk.Label(
    Order_detail_frame1, text="Grand Total :", font=("Helvetica", 14)
)
Grand_Total.pack(pady=5, padx=5)

Discount = ttk.Label(
    Order_detail_frame1, text="Discount :", font=("Helvetica", 14)
)
Discount.pack(pady=5, padx=5)

# Payment Method
Payment_Method = ttk.Label(
    Order_detail_frame1, text="Payment Method", font=("Helvetica", 25), foreground="green"
)
Payment_Method.pack(pady=10)

button1 = ttk.Button(Order_detail_frame1, image=image50, command=lambda: show_page(5,frame_order_detail_member))
button1.pack(side="left", pady=10, padx=10)

button2 = ttk.Button(Order_detail_frame1, image=image2, command=lambda: show_page(6,frame_order_detail_member))
button2.pack(side="right", pady=10, padx=10,ipadx=1)

Button_frame = ttk.Frame(frame_order_detail_member)
Button_frame.pack(pady=10)

cancel_order3 = ttk.Button(Button_frame, text="BACK", command=lambda: show_page(14, frame_order_detail_member))
cancel_order3.pack(side="bottom", pady=10, padx=1)

################################################################################################################################


def get_member_detail(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_member_info"
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        Member_name_view.config(text=f"Name: {data['name']}")
        Email_view.config(text=f"Email: {data['email']}")
        telephone_view.config(text=f"Telephone: {data['phone_no']}")
    else:
        print("Error_view_member")

Contact_Image = ttk.Label(frame_view_member, image=image4)
Contact_Image.place(x=0, y=0, relwidth=1, relheight=1)

Contact_Detail = ttk.Label(frame_view_member, text="Member Detail", font=("Helvetica", 45), foreground="green")
Contact_Detail.place(relx=0.5, rely=0.4, anchor="center")

Member_detail_frame = ttk.Frame(frame_view_member,bootstyle = "light")
Member_detail_frame.place(relx=0.5, rely=0.6, anchor="center")

Member_name_view = ttk.Label(Member_detail_frame, text="Name :", font=("Helvetica", 30))
Member_name_view.pack(pady=10, padx=10, ipadx=10)

Email_view = ttk.Label(Member_detail_frame, text="Email :", font=("Helvetica", 30))
Email_view.pack(pady=10, padx=10, ipadx=10)

telephone_view = ttk.Label(Member_detail_frame, text="Telephone :", font=("Helvetica", 30))
telephone_view.pack(pady=10, padx=10, ipadx=10)

cancel_order3 = ttk.Button(Member_detail_frame, text="VIEWORDERHISTORY", bootstyle="dark", command=lambda: get_booking_his())
cancel_order3.pack(pady=20, padx=2, ipadx=1)

cancel_order3 = ttk.Button(Member_detail_frame, text="BACK", bootstyle="dark", command=lambda: show_page(11, frame_view_member))
cancel_order3.pack(pady=20, padx=2, ipadx=1)


################################################################################################################################


def card_payment(member_id):
    card_no = Card_number.get()
    card_pin = Card_pin.get()

    if not card_no or not card_pin:
        print("Please fill in both card number and card pin.")
        return
    
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_payment/card"
    response = requests.put(
        API_ENDPOINT, json={"card_no": card_no,"card_pin" :card_pin }
    )

    if response.status_code  == 200:
         data = response.json()  # แก้ไขตรงนี้
         print("Response Data:", data)
         return data["booking_id"]
    else:
        print("Error:", response.text)


card_image = ttk.Label(frame_card_payment, image=image_payment_show)
card_image.place(x=0, y=0, relwidth=1, relheight=1)

booking_id2 = ttk.Label(frame_card_payment, text = "Booking id :", font=("Helvetica",15))
booking_id2.pack(pady=10,padx=2)

total_price2 = ttk.Label(frame_card_payment, text = "Total Price :", font=("Helvetica",15))
total_price2.pack(pady=10,padx=2)

Global_Card = ttk.Label(frame_card_payment, text = "GLOBAL CARD", font=("Helvetica",25),bootstyle="info")
Global_Card.pack(pady=10)

card_detail_frame = ttk.Frame(frame_card_payment,bootstyle ="light")
card_detail_frame.pack(pady=2)

Global_Card = ttk.Label(card_detail_frame, text = "Card Number", font=("Helvetica",20), bootstyle="info")
Global_Card.pack(pady=2)

def card_payment_click():
    if not Card_number.get() or not Card_pin.get():
        tkinter.messagebox.showinfo("Missing Information", "Please fill in both card number and card pin.")
    else:
        payment_success(card_payment(member_id), frame_card_payment)

Card_number = ttk.Entry(card_detail_frame, bootstyle="success",
                     font=("Helvetica",12),
                     foreground='blue',width = 20)
Card_number.pack(pady=5, padx=5)

Global_Card = ttk.Label(card_detail_frame, text = "Card pin", font=("Helvetica",20), bootstyle="info")
Global_Card.pack(pady=2)

Card_pin = ttk.Entry(card_detail_frame, bootstyle="success", 
                     font=("Helvetica",12),
                     foreground='blue',width = 20)
Card_pin.pack(pady=5, padx=5)

continue_payment = ttk.Button(card_detail_frame, text="CONTINUE PAYMENT", bootstyle="dark",command= lambda: card_payment_click())
continue_payment.pack(pady=2, padx=2,ipadx=1)

cancel = ttk.Button(card_detail_frame, text="CANCEL", bootstyle="dark",command=lambda : show_page(1,frame_card_payment)) #command=?)
cancel.pack(pady=2, padx=2,ipadx=1)






##############################################################################################################################















############################################################################################################################


def bank_payment(member_id):
    bank_no = Bank_entry.get()
    bank_name1 = bank_combo.get()


    if not bank_no or not bank_name1:
        print("Please fill in both card number and card pin.")
        return
    
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_payment/bank"
    response = requests.put(
        API_ENDPOINT, json={"account_no": int(bank_no), "bank_name": bank_name1}
    )

    if response.status_code  == 200:    
         data = response.json()  # แก้ไขตรงนี้
         print("Response Data:", data)
         return data
    else:
        print("Error:", response.text)


card_image = ttk.Label(frame_bank_payment, image=image_payment_show)
card_image.place(x=0, y=0, relwidth=1, relheight=1)

booking_detail_frame = ttk.Frame(frame_bank_payment, bootstyle="light")
booking_detail_frame.pack(pady=2)

booking_id = ttk.Label(booking_detail_frame, text = "Booking id :", font=("Helvetica",14), bootstyle="dark")
booking_id.pack(pady=2,padx=2)

total_price_bank = ttk.Label(booking_detail_frame, text = "Total Price :", font=("Helvetica",14), bootstyle="dark")
total_price_bank.pack(pady=2,padx=2)

bank_detail_frame = ttk.Frame(frame_bank_payment, bootstyle="light")
bank_detail_frame.pack(pady=10)

my_label = ttk.Label(bank_detail_frame, text = "Bank name", font=("Helvetica",20), bootstyle="PRIMARY")
my_label.pack(pady=5)

def click_bind(e):
        my_label.config(text=f"You Clinked on {bank_combo.get()}!")

banks = ['Kasikorn Bank','SCB','KrungThai Bank','KrungSri Bank','TMB BANK','UOB','Bangkok Bank']

bank_combo = ttk.Combobox(bank_detail_frame, bootstyle="info", values=banks)
bank_combo.pack(pady=5)

Global_Card = ttk.Label(bank_detail_frame, text = "Bank Number", font=("Helvetica",20), bootstyle="info")
Global_Card.pack(pady=2)

Bank_entry = ttk.Entry(bank_detail_frame, bootstyle="success",
                     font=("Helvetica",12),
                     foreground='blue',width = 20)
Bank_entry.pack(pady=5, padx=5)

def CONTINUE_PAYMENT():
    if not Bank_entry.get() or not bank_combo.get():
        tkinter.messagebox.showinfo("Missing Information", "Please fill in both bank name and bank number.")
    else:
        payment_success(bank_payment(member_id),frame_bank_payment)
    

continue_payment = ttk.Button(bank_detail_frame, text="CONTINUE PAYMENT", bootstyle="dark",command=lambda : CONTINUE_PAYMENT()) 
continue_payment.pack(pady=10, padx=2,ipadx=1)

cancel_order = ttk.Button(bank_detail_frame, text="CANCEL", bootstyle="dark",command=lambda: show_page(1,frame_bank_payment)) #command=?)
cancel_order.pack(pady=10, padx=2,ipadx=1)



#############################################################################################################################
    
def login():
        
        email_l = email_entry_login.get()
        password_l = password_entry_login.get()
        payload = {
            "email": email_l,
            "password": password_l
        }
        response = requests.post(API_ENDPOINT1, json=payload)
        if email_l== ""  or password_l== "":
            result_label_login.config(text="Please fill all")
        elif response.json().get("Result") != "Email or password is incorrect.":
            member_id=set_user_id(response.json().get("Result"))
            result_label_login.config(text="Login successful")
            print(member_id)
            show_page(11,frame_login)
        else:
            result_label_login.config(text="Incorrect username or password")


login_Image = ttk.Label(frame_login, image=park)
login_Image.place(relwidth=1, relheight=1)

login_detail_frame = ttk.Frame(frame_login, borderwidth=20, relief="ridge",padding =20)
login_detail_frame.place(relx=0.5, rely=0.3, anchor=ttk.CENTER,y=60)

to_register_frame = ttk.Frame(frame_login)
to_register_frame.place(relx=0.5, rely=0.54, anchor=ttk.CENTER)

x=2

message_label = ttk.Label(login_detail_frame, text="Log in",font = ("Cambria", 12, "bold"))
message_label.grid(row=x-2, columnspan=2)

blank_label = ttk.Label(login_detail_frame, text="")
blank_label.grid(row=x-1, columnspan=2)
    
    
email_entry_login = ttk.Label(login_detail_frame, text="Email : ")
email_entry_login.grid(row=x+0, column=0,sticky='w')

email_entry_login = ttk.Entry(login_detail_frame)
email_entry_login.grid(row=x+0, column=1, padx=10, pady=5,)

password_label_login = ttk.Label(login_detail_frame, text="Password : ")
password_label_login.grid(row=x+1, column=0,sticky='w')

password_entry_login = ttk.Entry(login_detail_frame, show="*")
password_entry_login.grid(row=x+1, column=1, padx=10, pady=5)

blank_label = ttk.Label(login_detail_frame, text="")
blank_label.grid(row=x+2, columnspan=2)

# สร้างปุ่มเข้าสู่ระบบ
login_button_login = ttk.Button(login_detail_frame, text="sign in", command=login)
login_button_login.grid(row=x+3, columnspan=2, padx=10, pady=5)

    # สร้าง Label สำหรับผลลัพธ์
result_label_login = ttk.Label(login_detail_frame, text="")
result_label_login.grid(row=x+4, columnspan=2, padx=10, pady=5)

be_member_button = ttk.Button(to_register_frame, text="register",command=lambda: show_page(10,frame_login))
be_member_button.grid(row=10, columnspan=2)
    
home_button_login = ttk.Button(frame_login, text="Home", command= lambda :show_page(3,frame_login),width=10,padding=10)
home_button_login.grid(row=0,column=0)




############################################################################################################################

############################################################################################################################
     
def become_member():
        
        name = name_entry_register.get()
        email = email_entry_register.get()
        phone_no = phone_no_entry_register.get()
        
        date_str = birthday.entry.get()
        try:
            datetime.strptime(date_str, '%m/%d/%Y')  # ตรวจสอบว่าสามารถแปลงวันที่เป็นรูปแบบที่ถูกต้องหรือไม่
        except ValueError:
            result_label_register.config(text="Incorrect date format", foreground="red")
            return
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")# แปลงสตริงเป็นวัตถุ datetime
        birth_day =  date_obj.strftime("%Y-%m-%d")
        
        password = password_entry.get()
        
        
        
        payload = {
            "name": name,
            "email": email,
            "phone_no": phone_no,
            "birthday": birth_day,
            "password": password
        }
        #print("Becoming a member...")
        
        
            
        response = requests.post(API_ENDPOINT3, json=payload)
        if name== "" or email== "" or phone_no== "" or birth_day== "" or password== "":
            result_label_register.config(text="Please fill in compete information", foreground="red")
            
        elif response.json().get("Result") ==  'Membership registration completed.':
            result_label_register.config(text="Membership registration completed.",foreground="black")
            name_entry_register.delete(0, tk.END)
            email_entry_register.delete(0, tk.END)
            phone_no_entry_register.delete(0, tk.END)
            birthday.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            #login_page()
        else :
            result_label_register.config(text=response.json().get("Result"),foreground="red")
            print(response.json().get("Result") )
        print(response.json().get("Result") )


background_label = ttk.Label(frame_register, image=bg3_pic)
background_label.place(relheight=1, relwidth=1)


register_detail_frame = ttk.Frame(frame_register, borderwidth=5, relief="ridge",padding =20)
register_detail_frame.place(relx=0.5, rely=0.3, anchor=ttk.CENTER,y=30)

row_position=1

register_label = Label(register_detail_frame, text="REGISTER",font = ("Cambria", 12, "bold"))
register_label.grid(row=row_position-1, columnspan=2, padx=10, pady=10)

name_label_register = Label(register_detail_frame, text="Name:")
name_label_register.grid(row=row_position, column=0, padx=10, pady=5,sticky='w')

name_entry_register = Entry(register_detail_frame)
name_entry_register.grid(row=row_position, column=1, padx=10, pady=5,sticky="news")

email_label_register = Label(register_detail_frame, text="Email:")
email_label_register.grid(row=row_position+1, column=0, padx=10, pady=5,sticky='w')

email_entry_register = Entry(register_detail_frame)
email_entry_register.grid(row=row_position+1, column=1, padx=10, pady=5,sticky="news")

phone_no_label_register = Label(register_detail_frame, text="Phone Number:")
phone_no_label_register.grid(row=row_position+2, column=0, padx=10, pady=5 ,sticky='w')

phone_no_entry_register = Entry(register_detail_frame)
phone_no_entry_register.grid(row=row_position+2, column=1, padx=10, pady=5,sticky="news")

birthday_label = Label(register_detail_frame, text="Birthday:")
birthday_label.grid(row=row_position+3, column=0, padx=10, pady=5,sticky='w')

birthday = ttk.DateEntry(register_detail_frame, bootstyle="danger", startdate=date.today())
birthday.grid(row=row_position+3, column=1, padx=10, pady=5,sticky="news")

password_label = Label(register_detail_frame, text="Password:")
password_label.grid(row=row_position+4, column=0, padx=10, pady=5,sticky='w')

password_entry = Entry(register_detail_frame)
password_entry.grid(row=row_position+4, column=1, padx=10, pady=5,sticky="news")


    # สร้างปุ่ม "Become a Member"
become_member_button = Button(register_detail_frame, text="Become a Member", command=become_member)
become_member_button.grid(row=10, columnspan=2, padx=10, pady=5)

result_label_register = ttk.Label(register_detail_frame, text="")
result_label_register.grid(row=12, columnspan=2)
    
home_button = ttk.Button(background_label, text="Home", command=lambda :show_page(3,frame_register),width=10,padding=10)
home_button.grid(row=0,column=0)


##############################################################################################################################






##############################################################################################################################

############################################################################################################################


    
width_botton = 105
c=0
pading_button=12


label_home = Label(frame_home_1, image=bg_pic)
label_home.place(relheight=1, relwidth=1)


my_frame = scrolledtext.ScrolledText(frame_home_1, width=48, height=40)
my_frame.place(relx=0.1, rely=0.5, anchor=tk.CENTER,x=170,y=30)

show_slides(my_frame)
slides_button = ttk.Button(frame_home_1, text="Our Slides", command=lambda :show_slides(my_frame),width=24)
slides_button.place(relx=0.1,rely=0.1, anchor=ttk.NW,x=10,y=120)
pool_button = ttk.Button(frame_home_1, text="Pool", command=lambda :show_pool(my_frame),width=23)
pool_button.place(relx=0.2,rely=0.1, anchor=ttk.NW,x=-20,y=120)
contact = Frame(frame_home_1, relief="ridge",borderwidth=20,padx=20,pady=20)
contact.place(relx=0.3, rely=0.9, anchor=ttk.SW,x=160,y=20)

                        
font_contact=("Cambria", 12)

contact_label_home = ttk.Label(contact, text="CONTACT",font = ("Cambria", 14, "bold"))
contact_label_home.grid(row=0, column=0,sticky='w',ipady=10,)

location_label_home = ttk.Label(contact, text="Location :  KMITL ECC Building, 1 Thanon Chalong Krung, Khwaeng Lam Prathew, Lat Krabang, Bangkok 10520",font=font_contact)
location_label_home.grid(row=1, column=0,sticky='w')

email_label_home = ttk.Label(contact, text="Email :  Dkub@email.com",font=font_contact)
email_label_home.grid(row=2, column=0,sticky='w')

phone_label_home = ttk.Label(contact, text="Phone number :   0-2329-8106",font=font_contact)
phone_label_home.grid(row=3, column=0,sticky='w')

hour_label = ttk.Label(contact, text="Office hours :  Monday - Sunday: 10:00-18:00",font=font_contact)
hour_label.grid(row=4, column=0,sticky='w')
    
home_button = ttk.Button(frame_home_1, text="Home", command= lambda :show_page(3,frame_home_1),width=width_botton,padding=pading_button)
home_button.grid(row=0,column=c)
    
login_button = ttk.Button(frame_home_1, text="Log in", command= lambda :show_page(9,frame_home_1),width=width_botton,padding=pading_button)
login_button.grid(row=0,column=c+2)
    
register_button = ttk.Button(frame_home_1, text="Register", command= lambda :show_page(10,frame_home_1),width=width_botton,padding=pading_button)
register_button.grid(row=0,column=c+3)

print(f"Home :{member_id}")

#############################################################################################

x_size, y_size = 1920, 1080

def get_all_services(member_id=""):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/services"
    if not member_id:
        API_ENDPOINT = "http://127.0.0.1:8000/services"
    req = requests.get(API_ENDPOINT)
    
    if req.status_code != 200:
        return "error"
    
    data = req.json()
    for key, val in data.items():
        print(key, val)

def get_show_all_booking(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{str(member_id)}/show_all_booking"
    req = requests.get(API_ENDPOINT)

    for widget in frame_payment_success.winfo_children():
            widget.destroy()
    
    if req.status_code != 200:
        return "error"
    
    return req.json()

def download(member_id, booking_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{(member_id)}/finish_booking/{(booking_id)}"
    req = requests.get(API_ENDPOINT, stream=True)
    
    try:
        print(req.json())
    except:
        print(req)
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not save_path:
            return
        
        req.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in req.iter_content(chunk_size=8192):
                file.write(chunk)

def booking_his():

    booking = get_show_all_booking(member_id)

    for widget in frame_view_booking_his.winfo_children():
        widget.destroy()
    
    # canvas = Canvas(root, width=x_size, height=y_size)
    #background_image = PhotoImage(file="background.png")
    # canvas.create_image(0, 0, anchor=NW, image=background_image)
    # canvas.pack()
    # Load your background image
    
    booking_frame = Frame(frame_view_booking_his)
    booking_frame.pack()
    label = ttk.Label(booking_frame, image=background_image)
    label.pack()

    # tab = ttk.Label(booking_frame, text="   ",padding=14, width=250, background='#009658')
    # tab.place(x=0,y=0)
    home_button = tk.Button(frame_view_booking_his, 
                bg='#ffffff',
                relief='flat',
                text='Home',
                width=20,
                command=lambda : show_page(4,frame_view_booking_his))
    home_button.place(x=x_size*0.02, y=16)
    for i in range(len(booking)):
        # Labels
        line = ttk.Label(booking_frame, text="___________________________________________________________________________________", font=("Helvetica", 15), background="#CDEDF4")
        l1 = ttk.Label(booking_frame, text=f"{str(booking[i]['booking_id'])}", font=("Helvetica", 15), background="#CDEDF4")
        l2 = ttk.Label(booking_frame, text=f"{str(booking[i]['visit_date'])}", font=("Helvetica", 15), background="#CDEDF4")
        b = ttk.Button(booking_frame, text="Download", bootstyle="success outline",padding="10 5",  # Adjust padding as needed
        command=lambda i=i: download(member_id, booking[i]["booking_id"]))
        
        # Positioning using place
        line.place(x=x_size*0.5, y=228 + i * 40, anchor = CENTER)
        l1.place(x=x_size*0.3, y=220 + i * 40, anchor = CENTER)
        l2.place(x=x_size*0.5, y=220 + i * 40, anchor = CENTER)
        b.place(x=x_size*0.71, y=220 + i * 40, anchor = CENTER)
    
    frame_view_booking_his.after(10000, booking_his)









#####################################################################################################

def payment_success(booking_id,frame):
    show_page(13,frame)
    booking = get_show_all_booking(member_id)
    payment_success_frame = Frame(frame_payment_success)
    payment_success_frame.pack()
    label = ttk.Label(payment_success_frame, image=image_payment_sus)
    label.pack()
    home_button = tk.Button(frame_payment_success, 
        bg='#ffffff',
        relief='flat',
        text='Home',
        width=20,
        command=lambda : show_page(11,frame_payment_success))
    home_button.place(x=x_size*0.02, y=16)
    for i in range(len(booking)):
        b = ttk.Button(payment_success_frame, text="Download_booking_detail", bootstyle="success outline",padding="100 50",  # Adjust padding as needed
        command=lambda i=i: download(member_id, booking[i]["booking_id"]))


        b.place(x=x_size*0.7, y=450, anchor = CENTER)





############################################################################################################################




# get_order_detail(member_id)

# get_order_detail_total(member_id)
get_member_detail(member_id)



root.mainloop()