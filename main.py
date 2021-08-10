"""
The following program is something to help solve the final bit of
a 4x4 rubix cube where all but 2 cubes are in the right place

This program takes an original list with 8 items in it to represent
blocks that may need to be moved around. The final result of this program
should be the original list with all but 2 list items back in their
original place along with the solution with the least number of steps
to get there
"""

import frequent_list_functions

original_list = (0, 1, 2, 3, 4, 5, 6, 7)

possible_moves = {"Mirrored L Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around":((0,2)(3,5)),
                       "Do mirroring":"No"},
                  "X-Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around":((1,3)(2,4)),
                       "Do mirroring":"No"},
                  "Tip Touching L Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around": ((1, 3)(4, 5)),
                       "Do mirroring":"No"},
                  "3-Way Switch":
                      {"Start_at": 0,
                       "Next_option": 1,
                       "Swap_around": ((0, 2, 4)),
                       "Do mirroring":"Yes"},
                  }

def mirrored_L_switch(input_array, start_at):
    if start_at > 7:
        return "do not use"
    second_switch_num = start_at + 2
    third_switch_num = start_at + 3
    fourth_switch_num = start_at + 5

    swap_one = [start_at, second_switch_num]
    print(swap_one)

    swap_two = [third_switch_num, fourth_switch_num]
    print(swap_two)

    # new_array = swap_around()

def do_rubix_move(rubix_move):
    rubix_move = possible_moves[rubix_move]
    print(rubix_move)



print(mirrored_L_switch(original_list,0))