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

# Test to make sure that the code is working ok
if __name__ == "__main__":
    original_list = (0, 1, 2, 3, 4, 5, 6, 7)

    swap_list = [0,2,4]

    swap_list = mirror_array(swap_list)
    print(swap_list)

    final_list = swap_around(original_list, swap_list)

    print(original_list)
    print(final_list)