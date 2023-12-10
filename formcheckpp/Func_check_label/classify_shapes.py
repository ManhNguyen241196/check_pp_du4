from pptx.enum.shapes import MSO_SHAPE_TYPE
def classify_kind_of_shape(shapes): 
        list_arrow = []
        list_label = [] 
        for shape in shapes:
            # arrow shape
            if shape.shape_type == MSO_SHAPE_TYPE.LINE:
                list_arrow.append(shape)
            # Text box
            if shape.has_text_frame:
                list_label.append(shape)
        return (list_arrow,list_label)