#print a list of favourite foods
foods = ["Biryani","Maggi","Mandi","Fries","Pizza","Pulao"]
print(foods)

#cities with indexing
cities = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"]
print(cities[0])
print(cities[1])

#Change an item
subjects = ["Python", "SQL", "Power BI"]
subjects[2]='Tableau'
print(subjects)

#add items
skills = ["Python", "SQL"]
skills.append("git")
skills.append("PowerBI")
skills.append("Pandas")
print(skills)

#remove items
languages = ["Python", "Java", "C++", "JavaScript"]
languages.remove("Python")
print(languages)

#loop
numbers = [10, 25, 40, 55, 70, 85]
for num in numbers:
    if num > 60:
        print(num)

#Count
marks = [45, 67, 32, 89, 76, 41, 90]
count =0
for mark in marks:
    if mark > 50:
        count =count+1
print(count)

