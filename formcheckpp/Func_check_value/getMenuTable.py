def getTable(list_Slides,id):
    slide = list_Slides.get(id)
    for shape in slide.shapes:
        if shape.has_table:
            my_menu_table = shape.table
            return my_menu_table