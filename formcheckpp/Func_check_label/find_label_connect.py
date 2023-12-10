def find_label_connect(arrows, labels,list_label):
    render_label =[]
    label_arrows = []
    # print("labels: ", labels)
    for arrow in arrows:
        for index_label,label in  enumerate(labels, 0):
            for point in label:
                if(point == arrow):
                    render_label.append((index_label, list_label[index_label].text_frame.text.replace(" ", "")))
                    label_arrows.append(list_label[index_label])
    return (label_arrows, render_label)