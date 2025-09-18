import math
import random
import datetime
import statistics

print(math.sqrt(16))
print(math.pi)

print([random.randint(1,10) for _ in range(10)])
print(random.choice(["red", "blue", "green", "yellow"]))


now = datetime.datetime.now()
print(now)

today = datetime.date.today()
print(today)


#Mini exercise combining all modules

#Exam date
exam_date = datetime.date.today()
print(f"Exam held on: {exam_date}" )


#Generate scores for 10 students
scores = [random.randint(1, 100) for _ in range(10)]
print("scores", scores )


mean_score = statistics.mean(scores) 
median_score = statistics.median(scores)
highest = max(scores)
lowest = min(scores)

print(f"Average score: {mean_score}")
print(f"Median score: {median_score}")
print(f"Highest score: {highest}")
print(f"Lowest score {lowest}")