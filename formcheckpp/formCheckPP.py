from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import filedialog
from main_check_label import check_2
from main_check_value import *

link=""
psr =''
#sample function
def run_with_method_1():
    print("form da chọn la: 1" )
def run_with_method_2():
    print("form da chọn la: 2" )

def func0():
    print("Chaỵ func check  giá trị của # trong các silde")
def func1():
    print("Check tên trong slide menu")


# định nghĩa chương trình chính
root = Tk()
root.title("Window With a Title Bar")
root.geometry("700x500")
root.resizable(False,False)


def load_checkboxes(checkboxes, psr):
    for index, ele in enumerate(checkboxes):
        if ele == 1:
            if index == 0:
                check_1(psr)
            elif index == 1:
                check_2(psr)
            
#Button run function
def printMessage():
    global psr
    psr = Presentation(link)
    sel()
    load_checkboxes(listCheckBoxRender, psr)
    messagebox.showinfo(title="show mess", message="Done. Xem kết quả ở file result")
    psr.save('Dummy data/result.pptx')
#define element
frame_form = LabelFrame(root, text="Chọn form powerpoint để check", padx=5,pady=5, font=('Arial', 10, 'bold'))
frame_method = LabelFrame(root, text="Chọn hạng mục check", padx=5,pady=5, font=('Arial', 10, 'bold'))
frame_image = LabelFrame(root, text="Preview form pp", padx=5,pady=5, font=('Arial', 10, 'bold'))        
frame_file = LabelFrame(root, text="Search file", padx=5,pady=5, font=('Arial', 10, 'bold'))                      
label = Label(frame_form)  # vi du de check selection form

#---------------------creat lable empty
def creat_space_grid_y(frame, grid_y, num_space):
    label_space = Label(frame, text=f'{" "*num_space}')
    label_space.grid(row=4,column=grid_y)
    
def creat_space_grid_x(frame, grid_x):
    label_space = Label(frame, text=" ")
    label_space.grid(row=grid_x,column=1)
#----------------------------------

#---------------------open file
def clickFunc():
    text_widget.config(state=NORMAL)
    filename = filedialog.askopenfilename(initialdir ='/', title="select a file powerpoint", filetypes=(("Powerpoint Files", "*.pptx"),("All Files", "*.*")))
    text_widget.insert(END, filename)
    text_widget.config(xscrollcommand=scrollbar.set, state=DISABLED)
    global link
    link = filename
    
text_widget = Text(frame_file, height=1, width=17, wrap="none", state=DISABLED)
text_widget.grid(row=0,column=5)
scrollbar = Scrollbar(frame_file, orient=HORIZONTAL)
scrollbar.grid(row=1,column=5)
scrollbar.config(command=text_widget.xview)
searchBtn = Button(frame_file, text="chon file", command=clickFunc, padx=5, pady=3) # Print the result
searchBtn.grid(row=0,column=0)
#----------------------------------


#--------------------selection form
var = IntVar()
var.set(1) 
def sel():
    if(var.get() == 1):
        run_with_method_1()     
    if(var.get() == 2):
        run_with_method_2()

#show photo preview
label_image = Label(frame_image)
def image( link_img):
    python_image = PhotoImage(file=link_img)
    original_image = python_image.subsample(3,3)
    label_image.config(image=original_image)
    label_image.image = original_image
    label_image.pack(fill=BOTH, expand=1)
image('C:/Users/ADMIN/Desktop/code/python/Tkinter/formcheckpp/Dummy data/Dummy_shape.png') #xuat hien ban dau mac dinh la 1
def showImg():
    Link = ''
    if(var.get() == 1):  
        Link = 'C:/Users/ADMIN/Desktop/code/python/Tkinter/formcheckpp/Dummy data/Dummy_shape.png'
        image ( Link)
    if(var.get() == 2):   
        Link = 'C:/Users/ADMIN/Desktop/code/python/Tkinter/formcheckpp/Dummy data//Dummy_table.png'
        image ( Link)
    print(Link)

R1 = Radiobutton(frame_form, text="Form battery chứa dạng #x:xxx[MPa]", variable=var, value=1, command= showImg)
R1.pack( anchor = W )
R2 = Radiobutton(frame_form, text="Form chứa bảng", variable=var, value=2, command= showImg)
R2.pack( anchor = W )
# label.pack()
#----------------------------------

#------------------- checkbox form
listCheckBoxRender = []
def isChecked():
    myListCheckBox = [cb.get() for cb in checkboxes]
    if((1 in myListCheckBox) and (link != "")):
        runBtn.config(state=NORMAL)
    print(myListCheckBox)
    global listCheckBoxRender
    listCheckBoxRender=myListCheckBox

checkboxes = []
for i in range(2):
    cb = IntVar()
    checkboxes.append(cb)
    if(i ==0):       
        Checkbutton(frame_method, text=f"Check giá trị #", variable=cb, onvalue=1, offvalue=0,command=isChecked).pack( anchor = W)
    if(i ==1):       
        Checkbutton(frame_method, text=f"Check chỉ vị trí chi tiết", variable=cb, onvalue=1, offvalue=0,command=isChecked).pack( anchor = W)
#----------------------------------

#------------------- Button Run form
runBtn = Button(root, text="RUN",state=DISABLED,activebackground='green',padx=8,pady=8,  font=("Arial", 15),command=printMessage)
runBtn.flash()

#----------------------------------
#layout Element
creat_space_grid_y(root, 0, 5)
creat_space_grid_y(root,2, 2)
creat_space_grid_x(root,0)
creat_space_grid_x(root,2)
creat_space_grid_x(root,4)

frame_file.grid(row=1,column=1)
frame_method.grid(row=3,column=1)
frame_form.grid(row=3,column=3)
frame_image.grid(row=5,column=3)
runBtn.grid(row=5,column=1)
 

#vào lặp để đảm bảo giao diện luôn hiển thị vì nếu k có loop no se hiện lên tắt luôn
root.mainloop()


