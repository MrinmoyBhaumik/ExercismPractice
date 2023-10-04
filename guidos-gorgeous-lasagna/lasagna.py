# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    Remaining_Bake_Time = EXPECTED_BAKE_TIME - elapsed_bake_time

    return Remaining_Bake_Time
#Returns the remaining baking time
def preparation_time_in_minutes(num_layers):
    return num_layers * PREPARATION_TIME
#Rteurns the lasagna preperation time

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    prep_time = number_of_layers * PREPARATION_TIME
    return prep_time + elapsed_bake_time
#Returns the elapsed time in minutes