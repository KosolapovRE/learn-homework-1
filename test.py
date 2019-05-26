school_grades = [
{'school_class': '1a', 'scores': [3, 4, 4, 2, 3, 5, 3, 2, 5]}, 
{'school_class': '1b', 'scores': [5, 5, 4, 4, 3, 4, 5]}, 
{'school_class': '2b', 'scores': [3, 3, 3, 2, 5]}
]

all_scores = (school_grades[0]['scores'] + school_grades[1]['scores'] + school_grades[2]['scores'])
sum_scores = 0
for element in all_scores:
    sum_scores += element
average_score = sum_scores / len(all_scores)
print(average_score)

def average_score_test(scores):
        sum_scores_test = 0
        for element in scores:
            sum_scores_test += element
        average_score_test = sum_scores_test / len(scores)
        return average_score_test

average_score_1a = average_score_test(school_grades[0]['scores'])
print(average_score_1a)