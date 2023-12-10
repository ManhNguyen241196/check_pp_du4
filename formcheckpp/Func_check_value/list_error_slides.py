def mark_X(textBox_obj):
    list_slide_error = []
    for k,v in textBox_obj.items():
        if("undef" in v ):         
            list_slide_error.append(k)
    return list_slide_error