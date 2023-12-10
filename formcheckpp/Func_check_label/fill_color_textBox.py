from pptx.dml.color import RGBColor
def fill_color_textBox(listTextBox):
        for error_label in listTextBox:
            fill = error_label.fill
            fill.solid()
            fill.fore_color.rgb = RGBColor(255, 0, 0)  # red