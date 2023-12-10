import re

def render_2shape_to_1shape(base_object):
    for k,v in base_object.items():
        for item in v:
            if (item.count('#') > 1):
                    # extract the relevant information using regex
                matches = re.findall(r'#\d+', item)
                matche_MPa = re.findall(r':\S+', item)
                result = [f"{x}{y}" for x in matches for y in matche_MPa]
                    # render list 
                v.remove(item)
                v.extend(result)