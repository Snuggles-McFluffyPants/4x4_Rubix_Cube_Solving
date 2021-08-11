from frequent_list_functions import *

original_list = (0, 1, 2, 3, 4, 5, 6, 7)

possible_moves = {"Mirrored L Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around": ((0, 2), (3, 5)),
                       "Do_mirroring": "No",
                       "Nums_in_range": 2},
                  "X-Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around": ((1, 3), (2, 4)),
                       "Do_mirroring": "No"},
                  "Tip Touching L Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around": ((1, 3), (4, 5)),
                       "Do_mirroring": "No"},
                  "3-Way Switch":
                      {"Start_at": 0,
                       "Next_option": 1,
                       "Swap_around": ((0, 2, 4)),
                       "Do_mirroring": "Yes"},
                  }

def do_rubix_move(rubix_move, input_array, swap_around_shift=0):
    # Fetch Necessary values from possible moves dictionary
    rubix_move = possible_moves[rubix_move]

    moving = rubix_move["Swap_around"]
    moving = list(moving)
    print(moving)

    # Determine which items in the list to move around
    next_option = rubix_move["Next_option"]
    shift = next_option * swap_around_shift

    moving2 = []

    for item in moving:
        item = list(item)
        item2 = []
        for subitem in item:
            subitem = subitem + shift
            item2.append(subitem)
        moving2.append(item2)

    moving2 = put_nums_in_range(moving2)
    print(moving2)

    if moving2 == "no good nums in array":
        return "invalid move"

    moving = moving2

    # Final Moving the numbers around
    new_array = input_array

    for item in moving:
        output_array = swap_around(new_array, item)
        new_array = output_array

    return output_array




if __name__ == "__main__":

    original_list = (0, 1, 2, 3, 4, 5, 6, 7)
    print(original_list)

    # Possible names of moves are:
    # Mirrored L Switch, X-Switch, Tip Touching L Switch, 3-Way Switch
    name = "X-Switch"
    new_array = do_rubix_move(name, original_list, swap_around_shift=1)
    print(new_array)
