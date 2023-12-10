def check_label(texts, labels,list_label):
    true_label = []
    for label in labels:
        for text in texts:
            if(label[1] in text):
                texts.remove(text)
                true_label.append(list_label[int(label[0])])
                
    print("texts: ",texts)
    print("true_label: ", true_label)
    return true_label