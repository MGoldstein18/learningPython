#function to get middle element of list
def middle_element(lst):
    length = len(lst)

    if length % 2 == 0:
        average = lst[int(length / 2)] + lst[int(length / 2 - 1)]
        return average / 2

    else:
        return lst[int(length / 2)]

#function to take an element of an list, double it and then return it the list
def double_index(lst, index):
    if index >= len(lst) - 1:
        return lst
    else:
        new_list = lst[0:index]
        new_num = lst[index] * 2
        new_list.append(new_num)
        new_list = new_list + lst[index + 1:]
        return new_list

#function to check which item is more frequently listed in a list and return it
def more_frequent_item(lst, item1, item2):
    count_item1 = lst.count(item1)
    count_item2 = lst.count(item2)

    if count_item1 >= count_item2:
        return item1
    else:
        return item2

#function to remove the middle of a list
def remove_middle(lst, start, end):
    begin = lst[:start]
    ending = lst[end+1:]
    return begin + ending

#function to create a list of a range of numbers, incrementing in 3, up to and including 100
def every_three_nums(start):
    result = list(range(start, 101, 3))
    return result
