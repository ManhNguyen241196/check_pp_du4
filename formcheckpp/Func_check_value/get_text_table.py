def get_text_table(table):
    list_text = []
    rows_obj = table.rows

    for i in range(len(rows_obj)):
        cell = rows_obj[i].cells
        first_CELL = cell[0]        
        if(first_CELL.text.isdigit() or len(first_CELL.text) == 0):   # check Stt co chua gia tri 
            (check_is_merge, num_merge) = (first_CELL.is_merge_origin,first_CELL.span_height )

            # checkdieuf kien merge. Chi cell goc merge mowis tra lai true
            if(not check_is_merge and first_CELL.text.isdigit()):
                list_text.append(f"#{cell[0].text}:{cell[2].text}[MPa]")
            
            if(check_is_merge):
                list_text.append(f"#{cell[0].text}:{cell[2].text}[MPa]")
            
            if(not check_is_merge and first_CELL.text == ""):
                print("o chua merge la: ", cell[2].text)
                cell_origin = rows_obj[i-1].cells
                list_text.append(f"#{cell_origin[0].text}:{cell[2].text}[MPa]")
    return list_text