def get_label_in_table(table):    
        list_text = []
        rows_obj = table.rows
        
        #trich xuat text from table
        for i in range(len(rows_obj)):
            cell = rows_obj[i].cells
            (Stt_cell, text_cell) =  (cell[0], cell[1])
            if(Stt_cell.text.isdigit() and (Stt_cell.is_spanned == False)):
                list_text.append(text_cell.text.replace(" ", ""))
        return list_text