def create_an_empty_list(empty_list=[]):
    print(empty_list)
    return empty_list


def create_a_list():
    list_of_lenght=[1,2,3,4]
    return list_of_lenght
 

def add_element_to_end_of_list(list,element):
    list.append(element)
    return list

def add_element_to_start_of_list(list, element):
    list.insert(0,element)
    return list

def remove_element_from_end_of_list(list):
    list.pop()
    return list

def remove_element_from_start_of_list(list):
    list.pop(0)
    return list

def retrieve_first_element_from_list(list):
    if list:
        return list[0]
    else:
        return None

def retrieve_element_from_index(list, index):
    if 0 <= index < len(list):
        return list[index]
        return None

def retrieve_last_element_from_list(list):
    if list:
        return list[-1]
        return None
