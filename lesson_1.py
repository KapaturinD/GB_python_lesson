def my_type(el):
    my_list = [6, list, -77, 'True', True, 9.5]
    for el in range(len(my_list)):
        print(type(my_list[el]))
        break
    return my_type(el)


