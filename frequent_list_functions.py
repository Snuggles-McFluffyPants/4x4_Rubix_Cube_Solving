# output a new array with
def swap_around(input_array, items_to_change):
    new_list = list(input_array)

    start = 0
    end_point = len(items_to_change) - 1

    while start <= end_point:
        item1 = items_to_change[start]

        if start + 1 <= end_point:
            item2 = items_to_change[start + 1]
        else:
            item2 = items_to_change[0]
        x = input_array[item1]
        new_list[item2] = x

        start += 1

    new_list = tuple(new_list)
    return new_list

# Rearrange an input list from last to first
def mirror_array(input_array):
    mirrored_array = [x for x in input_array[::-1]]
    return mirrored_array

def put_nums_in_range(set_o_nums, num_min = 0, num_max = 7, remainders_of = 8):

    goodness_check = []

    for subset in set_o_nums:
        for num in subset:
            # print('num:',num)
            # print(type(num))
            if num >= num_min and num <= num_max:
                goodness_check.append(num)

    if len(goodness_check) == 0:
        return "no good nums in array"

    else:
        final_array = []

        for subset in set_o_nums:
            part_array = []
            for num in subset:

                num = num % remainders_of
                part_array.append(num)
            final_array.append(part_array)

        final_array = tuple(final_array)
        return final_array


# Test to make sure that the code abover is working ok
if __name__ == "__main__":
    original_list = (0, 1, 2, 3, 4, 5, 6, 7)

    swap_list = [0,2,4]
    print('\n-----------------------------------------------------')
    print("Original Swap List: ", swap_list)

    swap_list = mirror_array(swap_list)
    print("Mirrored Swap List: ", swap_list)

    final_list = swap_around(original_list, swap_list)

    print("First List: ",original_list)
    print("Final List: ",final_list)

    print('-----------------------------------------------------\n')
