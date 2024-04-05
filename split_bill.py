#######################################################
#  Program title:         Split Bill
#  Program Author:        Brendan Obilo
#  Date:                  11/03/2024
#
#  Description:           Display how a bill will be shared
#                         with the bill and shares entered
#                         by a user.
#########################################################

# varaible and constants
# HALF = 1/2
HALF = 1/2


def split_bill(amount: int, full_share: int, half_share: int = 0):
    # total_share = full_share + half_share * HALF
    total_share = full_share + half_share * HALF
    # amount_full_share = amount / total_share
    amount_full_share = amount / total_share
    # amount_half_share = amount_full_share * HALF
    amount_half_share = amount_full_share * HALF
    # print(amount_full_share)
    print(f"Full share: ${amount_full_share:.2f}")
    # print(amount_half_share)
    print(f"Half share: ${amount_half_share:.2f}")

split_bill(1300, 2, 2)