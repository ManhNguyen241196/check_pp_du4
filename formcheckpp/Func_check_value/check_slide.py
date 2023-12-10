def check_slide(textBox_obj_var,tableList_var, check_list={}):
    textBox_obj, tableList = textBox_obj_var, tableList_var
    count_textbox = 0 
    for k,v in textBox_obj.items():
        if(len(v) > 0 ):
            newlist = []
            for item in v:
                if(item in tableList):    # neu item ton tai trong table list
                    index  = tableList.index(item)
                    newlist.append(index)
                    count_textbox = count_textbox+1
                else:
                    newlist.append("undef")  

            textBox_obj.update({k:newlist})
    
    check_list = textBox_obj
    return check_list


# textbox_render = {257: ['#1:12.4[MPa]', '#2:34.5[MPa]'], 259: ['#3:25.7[MPa]', '#4:25.7[MPa]'], 258: ['#7:45.7[MPa]', '#7:56.9[MPa]']}
# data_table  = ['#1:12.4[MPa]', '#2:34.5[MPa]', '#3:25.7[MPa]', '#4:25.7[MPa]', '#5:66.7[MPa]', '#6:78.9[MPa]', '#7:45.7[MPa]', '#8:56.4[MPa]', '#8:1234[MPa]']
# check_list = check_slide(textbox_render,data_table)

# print("check_list: ", check_list)