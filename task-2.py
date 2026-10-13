import sys
sys.stdout.reconfigure(encoding="utf-8")

import json
import requests

URL="https://api.slingacademy.com/v1/sample-data/files/student-scores.json"

response=requests.get(URL,timeout=10)

info=response.json()


marks=info[0]


print("Status Response:",response.status_code)
print("Type:",type(info))
print("Marks:",marks.get("math_score"))

print("preview:",str(info)[:500])

length=len(info)

print(length)



all_marks=[]

students_name=[]


for mark in info:
    all_marks.append(mark.get("math_score"))
    students_name.append(mark.get("first_name"))


total=sum(all_marks)
avg=total/length


# print(all_marks)
#print(students_name)

print(avg)


import matplotlib.pyplot as plt

plt.bar(students_name[:10],all_marks[:10])
plt.xlabel("student_name")
plt.ylabel("marks")
plt.xticks(rotation=45)
plt.show()




