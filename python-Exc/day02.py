# this is a file where i have to practice my python

# 1. squares of even numbers only
# 2. unique values, sorted descending
# 3. index + value pairs printed as "0 -> 4"
# 4. all words lowercased, joined with "-"
# 5. dict {word: length} for words longer than 2 chars
# 6. the person dict with the max age
# 7. sort people by age, youngest first
# 8. average age, rounded to 1 decimal
# 9. names as a comma-separated string, title-cased
# 10. split nums into evens/odds in a single pass
# 11. count how many times each value appears in nums
# 12. safely read key "city" from the first person with default "unknown"


nums   = [4, 8, 15, 16, 23, 42, 8, 15]
words  = ["Data", "science", "IS", "not", "magic"]
people = [{"name": "ali", "age": 31}, {"name": "sara", "age": 24}, {"name": "reza", "age": 45}]

#1 
sqr = [n**2 for n in nums if n % 2 == 0]
print(sqr)

#2 
decending_list = sorted(set(nums), reverse=True)
print(decending_list)

#3 
pairs = [f"{i} -> {v}" for i,v in enumerate(nums)]
print(pairs)

#4 
joined = "-".join(w.lower() for w in words)
print(joined)

#5
dict = {w: len(w) for w in words if len(w) > 2}
print(dict)

#6
per_dict = max(people, key=lambda d: d["age"])
#7
per_sort = sorted(people, key=lambda d: d["age"])
print(per_dict)
print(per_sort)

#8
avg_per = round(sum(p["age"] for p in people) / len(people), 2)
print(avg_per)

#9
name_per = ",".join(p["name"].title() for p in people)
print(name_per)

#10
even, odds = [n for n in nums if n % 2 == 0], [n for n in nums if n % 1 == 0], 
print(even, odds)

#11
from collections import Counter
counts = Counter(nums)
print(counts)

#13
city = people[0].get("city", "unknown")
print(city)