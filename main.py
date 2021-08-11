"""
The following program is something to help solve the final bit of
a 4x4 rubix cube where all but 2 cubes are in the right place

This program takes an original list with 8 items in it to represent
blocks that may need to be moved around. The final result of this program
should be the original list with all but 2 list items back in their
original place along with the solution with the least number of steps
to get there
"""

from frequent_list_functions import *

original_list = (0, 1, 2, 3, 4, 5, 6, 7)

possible_moves = {"Mirrored L Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around":((0,2),(3,5)),
                       "Do_mirroring":"No",
                       "Nums_in_range": 2},
                  "X-Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around":((1,3),(2,4)),
                       "Do_mirroring":"No"},
                  "Tip Touching L Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around": ((1, 3),(4, 5)),
                       "Do_mirroring": "No"},
                  "3-Way Switch":
                      {"Start_at": 0,
                       "Next_option": 1,
                       "Swap_around": ((0, 2, 4)),
                       "Do_mirroring":"Yes"},
                  }

def do_rubix_move(rubix_move, input_array, swap_around_shift = 0):
    rubix_move = possible_moves[rubix_move]

    moving = rubix_move["Swap_around"]
    moving = list(moving)
    print(moving)

    # Determine which items in the list to move around
    next_option = rubix_move["Next_option"]
    shift = next_option * swap_around_shift
    # print('shift: ',shift)

    moving2 = []

    for item in moving:
        item = list(item)
        item2 = []
        for subitem in item:
            subitem = subitem + shift
            item2.append(subitem)
            # print('*item: ', item)
        # print('item: ', item)
        moving2.append(item2)

    # print('moving2: ',moving2)
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
        # print(',',output_array)

    return output_array

print(original_list)

# Possible names are:
# Mirrored L Switch, X-Switch, Tip Touching L Switch, 3-Way Switch
name = "X-Switch"
asdf = do_rubix_move(name, original_list, swap_around_shift=1)
print(asdf)
# print(mirrored_L_switch(original_list,0))