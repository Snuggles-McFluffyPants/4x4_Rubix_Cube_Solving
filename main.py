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
from generate_all_move_options import all_options

# Check whether or not 2 arrays are the same arrays but with 2 items
# in different places
def array_diff_check(array1, array2, diff_items = 2):

    # Complete a check to make sure everything is ok with arrays to examine
    precheck ="in progress"
    while precheck == "in progress":
        if len(array1) != len(array2):
            raise TypeError("\n------  Lengths of array's imported are not equal")

        array1_set = set(array1)
        array2_set = set(array2)

        check_array = array1_set - array2_set
        check_array2 = array2_set - array1_set

        assert len(check_array) == 0, "Arrays contain different items"
        assert len(check_array2) == 0, "Arrays contain different items"

        precheck = "Done"

    diff_evaluate = 0
    for (a, b) in zip(array1, array2):
        if a != b:
            diff_evaluate += 1
            # print(a, b)

    if diff_evaluate == diff_items:
        return ("arrays all good")
    else:
        return("needs more processing")


for rubix_move in all_options:
    move = rubix_move[0]
    shift = rubix_move[1]
    mirroring = rubix_move[2]

    # output_array = do_rubix_move(move,original_list,shift,mirroring)
