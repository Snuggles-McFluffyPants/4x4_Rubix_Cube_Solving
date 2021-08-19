from frequent_list_functions import *

possible_moves = {"Mirrored L Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around": ((0, 2), (3, 5)),
                       "Do_mirroring": "No",
                       "Nums_in_range": 2,
                       'Max_Shift': 4},
                  "X-Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around": ((1, 3), (2, 4)),
                       "Do_mirroring": "No",
                       'Max_Shift': 4},
                  "Tip Touching L Switch":
                      {"Start_at": 0,
                       "Next_option": 2,
                       "Swap_around": ((1, 3), (4, 5)),
                       "Do_mirroring": "No",
                       'Max_Shift': 4},
                  "3-Way Switch":
                      {"Start_at": 0,
                       "Next_option": 1,
                       "Swap_around": ((0, 2, 4)),
                       "Do_mirroring": "Yes",
                       'Max_Shift': 8},
                  }

def do_rubix_move(rubix_move,
                  input_array,
                  swap_around_shift=0,
                  do_mirroring = "No"):
    # Fetch necessary values from possible moves dictionary
    rubix_move = possible_moves[rubix_move]

    moving = rubix_move["Swap_around"]
    moving = list(moving)
    # print('moving1:',moving)

    # Determine which items in the list to move around
    next_option = rubix_move["Next_option"]
    shift = next_option * swap_around_shift

    moving2 = []

    for item in moving:
        try:
        # if isinstance(item, int) == False:
            item = list(item)
            item2 = []
            for subitem in item:
                subitem = subitem + shift
                item2.append(subitem)
            moving2.append(item2)
        except TypeError:
            item = item + shift
            try:
                # item = item + shift
                moving2[0].append(item)
            except IndexError:
                # item = item + shift

                moving2 = [[]]
                moving2[0].append(item)

    moving2 = put_nums_in_range(moving2)

    if moving2 == "no good nums in array":
        return "no good nums in array"

    moving2 = list(moving2)

    moving = moving2

    # Do mirroring if necessary

    if do_mirroring != "No":
        if rubix_move["Do_mirroring"] == "Yes":
            moving2 = []
            sublist = []
            for item in moving:
                # print("i=",moving)
                item = mirror_array(item)
                moving2.append(item)
            moving = moving2
        else:
            return "mirroring not available"

    # print("moving = ",moving)

    # Final Moving the numbers around
    new_array = input_array

    for item in moving:
        output_array = swap_around(new_array, item)
        new_array = output_array

    return output_array


# if __name__ == "__main__":
#
#     original_list = (0, 1, 2, 3, 4, 5, 6, 7)
#     # print(original_list)
#
#     # Possible names of moves are:
#     # Mirrored L Switch, X-Switch, Tip Touching L Switch, 3-Way Switch
#     name = "X-Switch"
#     new_array = do_rubix_move(name, original_list, swap_around_shift=1)
#     # print(new_array)
#
#     # Test the mirroring in the 3-way switch
#
#     # print('\n\n')
#     name = "3-Way Switch"
#     # print(name)
#     new_array = do_rubix_move(name,
#                               original_list,
#                               swap_around_shift=8,
#                               do_mirroring="Yes")
#     # print(new_array)
#
#     # print('\n\n')
#     name = "3-Way Switch"
#     new_array = do_rubix_move(name,
#                               original_list,
#                               swap_around_shift=2)
#     # print(new_array)



if __name__ == "__main__":

    rubix_moves_max = {"Mirrored L Switch":
                           {"Max_Shift": 0},
                       "X-Switch":
                           {"Max_Shift": 0},
                       "Tip Touching L Switch":
                           {"Max_Shift": 0},
                       "3-Way Switch":
                           {"Max_Shift": 0}
                       }

    original_list = (0, 1, 2, 3, 4, 5, 6, 7)

    moves_list = ("Mirrored L Switch", "X-Switch", "Tip Touching L Switch", "3-Way Switch")
    for move in moves_list:
        # print('\n\n')
        name = move
        # print(name)

        shift = 0
        new_array = 0

        while new_array != "no good nums in array":

            new_array = do_rubix_move(name,
                                      original_list,
                                      swap_around_shift=shift)

            rubix_moves_max[move]["Max_Shift"] = shift

            shift += 1

    print(rubix_moves_max)

    # move_name = moves_list[0]

    # print(rubix_moves_max[move_name]["Max_Shift"])
    for move in moves_list:
        # print(move)
        over_shift = rubix_moves_max[move]["Max_Shift"]
        # over_shift += 1
        # print(over_shift)

        new_array = do_rubix_move(name,
                                  original_list,
                                  swap_around_shift=shift)

        assert new_array == "no good nums in array"

