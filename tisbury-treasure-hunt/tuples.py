"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    coord = tuple(coordinate)
    return coord


def compare_records(azara_record, rui_record):
    azara_coordinate = tuple(azara_record[1])
    if azara_coordinate == rui_record[1]:
        return True
    return False


def create_record(azara_record, rui_record):
    azara_coordinate = tuple(azara_record[1])
    both_records = azara_record + rui_record
    if azara_coordinate == rui_record[1]:
        return both_records
    return "not a match"


def clean_up(combined_record_group):
    record_list = []
    record = ""
    for tupe in combined_record_group:
        new_tuple = ()
        for index,item in enumerate(tupe):
            if index != 1:
                new_tuple += (item,)
        record_list.append(new_tuple)
    for item in record_list:
        record += str(item) + "\n"
    return record