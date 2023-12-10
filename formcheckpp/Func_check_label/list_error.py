def list_error(all_labels, true_labels ):
        err_labels = all_labels.copy()
        for i in true_labels:
            for y in err_labels:
                if(y.shape_id == i.shape_id):
                    err_labels.remove(y)
        print((len(all_labels), len(true_labels), len(err_labels)))
        return err_labels