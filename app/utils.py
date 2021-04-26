

def obj_to_dict(obj, exclude = None):
    dict = obj.__dict__
    dict.pop('_sa_instance_state')
    if exclude:
        for key in exclude:
            if key in dict:
                dict.pop(key)
    return dict

def query_to_list(query, exclude = None):
    list = []
    for obj in query:
        dict = obj_to_dict(obj, exclude)
        list.append(dict)
    return list

def dict_to_obj(dict, obj, exclude = None):
    for key in dict:
        if exclude:
            if key in exclude:
                continue
        setattr(obj, key, dict[key])
    return obj