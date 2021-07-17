import csv
import statistics
import math

with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  school_data = list(reader)

school_data.pop(0)

marks=[]
for a in school_data:
    marks.append(int(a[1]))

mean=statistics.mean(marks)

deviation=[]
for b in marks:
    d=b-mean
    deviation.append(int(d))

squaredDeviations=[]
for c in deviation:
    e=c*c
    squaredDeviations.append(int(e))

sum=0
for t in squaredDeviations:
    sum=sum+t
print(sum)

totalNumberOfMarks=len(marks)
result=sum/totalNumberOfMarks
standardDeviation=math.sqrt(result)
print(standardDeviation)