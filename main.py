"""
The following program is something to help solve the final bit of
a 4x4 rubix cube where all but 2 cubes are in the right place

This program takes an original list with 8 items in it to represent
blocks that may need to be moved around. The final result of this program
should be the original list with all but 2 list items back in their
original place along with the solution with the least number of steps
to get there
"""
"""
Note: Possible Moves are: 
    Mirrored L Switch
    X-Switch
    Tip Touching L Switch
    3-Way Switch
"""

from Rubix_Cube_Movement import *

moves_list = ("Mirrored L Switch", "X-Switch", "Tip Touching L Switch", "3-Way Switch")

original_list = (0, 1, 2, 3, 4, 5, 6, 7)






def trymoves(rubix_move):
    run_func = True
    shift = 0
    mirroring = "No"
    while run_func == True:


        new_array = do_rubix_move(rubix_move,
                                  original_list,
                                  swap_around_shift=shift)

        if new_array == "no good nums in array":
            break

        print(new_array)

        shift+=1

cur_move = moves_list[0]

trymoves(cur_move)
