"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    new_score = []
    while student_scores:
        new_score.append(round(student_scores.pop(0)))
    return new_score



def count_failed_students(student_scores):
    count = 0
    for num in student_scores:
        if num <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    best = []
    for num in student_scores:
        if num >= threshold:
            best.append(num)
    return best


def letter_grades(highest):
    change = round((highest - 40)/4)
    grades = [41]
    grade = 41
    while grade + change < highest:
        grade += change
        grades.append(grade)
    return grades


def student_ranking(student_scores, student_names):
    rank = []
    rank_final = []
    while student_scores:
        index = student_scores.index(max(student_scores))
        rank.append([student_names[index],student_scores[index]])
        student_scores.pop(index)
        student_names.pop(index)
    for index,info in enumerate(rank):
        rank_final.append(f"{index +1}. {info[0]}: {info[1]}")
    return rank_final




def perfect_score(student_info):
    none = []
    for student in student_info:
        if student[1] == 100:
            return student
    return none
