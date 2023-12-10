# render data
def render_arrow(shapes):
    list_arrow_render = []
    for shape in shapes:
        coor_begin_arrow = (shape.begin_x, shape.begin_y)
        list_arrow_render.append(coor_begin_arrow)
        # print(coor_begin_arrow)  
    return list_arrow_render
def render_coor_label(shapes):
    list_label_render = [] 
    for shape in shapes:
        TC_cnt = (round(shape.left) + round(shape.width/2), round(shape.top) )
        BC_cnt = (round(shape.left) + round(shape.width/2), round(shape.top + shape.height))
        LC_cnt = (round(shape.left), round(shape.top) + (round(shape.height/2)))
        RC_cnt = (round(shape.left) + round(shape.width), round(shape.top) + round(shape.height/2))
        coor_label = (TC_cnt,BC_cnt,LC_cnt, RC_cnt)
        list_label_render.append(coor_label)
    return list_label_render