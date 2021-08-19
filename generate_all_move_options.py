from Rubix_Cube_Movement import *

moves_list = []

for movement in possible_moves.keys():
    moves_list.append(movement)

moves_list = tuple(moves_list)
# print(moves_list,'\n\n\n')

all_options = []

for move in moves_list:
    for num in range(possible_moves[move]["Max_Shift"]):
        if possible_moves[move]["Do_mirroring"] != "No":
            option = (move, num, "Yes")
            all_options.append(option)
        option = (move, num, "No")
        all_options.append(option)

all_options = tuple(all_options)

