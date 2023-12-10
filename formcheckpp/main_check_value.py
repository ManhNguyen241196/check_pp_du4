from Func_check_value.Render_textbox import renderData
from Func_check_value.check_slide import check_slide
from Func_check_value.draw_symbol import draw_symbol
from Func_check_value.getAll_textbox import get_all_textBox
from Func_check_value.getMenuTable import getTable
from Func_check_value.get_text_table import get_text_table
from Func_check_value.list_error_slides import mark_X
from Func_check_value.render_2shape import render_2shape_to_1shape

from pptx import Presentation

link_pp = 'C://Users//ADMIN//Desktop//code//python//Tkinter//formcheckpp//Dummy data//Dummy_pp.pptx'

def check_1(psr):
    # khai bao bien dung chung
    

    # Create a presentation object
    # psr = Presentation(link)
    listSlides = psr.slides 
    
    # đặc thù của tiêu chuẩn check 1
    my_table = None
        # get all text_box from slides
    data_textBox = get_all_textBox(listSlides, {})
        #_-----------------------------------
    print('data_textBox: ',data_textBox)

        # đặc thù cho form 1

            # render all data_textbox
    (textbox_render, slide_my_table_id)  = renderData(data_textBox)
            #_-----------------------------------
    print('textbox_render: ',renderData(data_textBox))

            #render 2 # to 1 #:
    textbox_getShape = textbox_render
    render_2shape_to_1shape(textbox_getShape)
    print("re render text box :", textbox_getShape)
        #--------------------------------------------------------------------đặc thù cho form 1

        #-------------------------get data table --------------------
        #select table       
    my_table = getTable(listSlides, slide_my_table_id)


        #lay text in all rows table
    data_table = get_text_table(my_table)
    print("data table:  ",data_table)
        #-----------------------------------

        #check slide error
    check_list = check_slide(textbox_getShape,data_table)
        #-----------------------------------
    print("check_list :  ",check_list)

        #print slide error
    list_error_slides = mark_X(check_list)
    print("list error slides:  ",list_error_slides)

        #test insert shape
    draw_symbol(list_error_slides, psr)
        #----------------------------------
