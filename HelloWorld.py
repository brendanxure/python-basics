print("Hello World!")

print("Brendan Obilo")
print("Computer Programming")
print("2 years")

score_list = [21,32,43,54,65,76,87]

def rank_player(score_list = score_list):
    remaining_slot = 10 - len(score_list)
    for element in range(remaining_slot):
        print('-')

rank_player()