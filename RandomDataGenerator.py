
import random
import string


letters = string.ascii_lowercase
stringLength = 7

name = []
age = []
gender = []
g = ['Male', 'Female']
percent_10 = []
percent_12 = []
jee_rank = []
c = ['Yes', 'No']
coaching = []
backup = []
certificate = []
reason = []
r = ['College Infrastructure', 'College Reputation', 'Course Preference']
familyIncome = []
dependentMembers = []
m = ['May', 'June', 'July', 'Aug']
month = []
s = ['Advertisement', 'Relative', 'Direct Interaction']
source = []
l = ['Urban', 'Town', 'Rural']
home = []



def randomString():
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    temp = ''.join(random.choice(letters) for _ in range(stringLength))
    name.append(temp)

for j in range(50000):
    randomString()


for i in range(50000):
    age.append(random.randint(18, 21))
    gender.append(random.choice(g))
    percent_10.append(round(random.uniform(60.0, 99.9), 2))
    percent_12.append(round(random.uniform(60.0, 99.9), 2))
    jee_rank.append(random.randint(1, 300000))
    coaching.append(random.choice(c))
    backup.append(random.choice(c))
    certificate.append(random.randint(0, 5))
    reason.append(random.choice(r))
    familyIncome.append(random.randint(200000, 5000000))
    dependentMembers.append(random.randint(0, 5))
    month.append(random.choice(m))
    source.append(random.choice(s))
    home.append(random.choice(l))



import pandas


score = 0
jee_num = []
for rank in jee_rank:
    if 1<= rank < 20000: score = 10

    elif 20000<= rank < 40000: score = 9
    elif 40000<=rank < 60000: score = 8
    elif 60000<=rank < 80000: score = 7
    elif 80000 <=rank < 100000: score = 6
    elif 100000 <=rank < 120000: score = 5
    elif 120000 <=rank < 140000: score = 4
    elif 140000 <=rank < 160000: score = 3
    elif 160000 <= rank < 180000: score = 2
    elif 180000 <=rank < 200000: score = 1
    else: score = 0
    jee_num.append(score)

score = 0
percent_12_num = []
for two in percent_12:
    if 95 <= two < 100:
        score = 10
    elif 90 <= two < 95:
        score = 9
    elif 85 <= two < 90:
        score = 8
    elif 80 <= two < 85:
        score = 7
    elif 75 <= two < 80:
        score = 6
    elif 70 <= two < 75:
        score = 5
    elif 65 <= two < 70:
        score = 4
    elif 60 <= two < 65:
        score = 3
    else:
        score = 0
    percent_12_num.append(score)


score = 0
percent_10_num = []
for ten in percent_10:
    if 95 <= ten < 100:
        score = 10

    elif 90 <= ten < 95:
        score = 9
    elif 85 <= ten < 90:
        score = 8
    elif 80 <= ten < 85:
        score = 7
    elif 75 <= ten < 80:
        score = 6
    elif 70 <= ten < 75:
        score = 5
    elif 65 <= ten < 70:
        score = 4
    elif 60 <= ten < 65:
        score = 3

    else:
        score = 0

    percent_10_num.append(score)


score = 0
familyIncome_num = []
for money in familyIncome:

    if 3000000 <= money:
        score = 10

    elif 2000000 <= money < 3000000:
        score = 9

    elif 1700000 <= money < 2000000:
        score = 8
    elif 1500000 <= money < 1700000:
        score = 7
    elif 1300000 <= money < 1500000:
        score = 6
    elif 1100000 <= money < 1300000:
        score = 5
    elif 900000 <= money < 1100000:
        score = 4
    elif 700000 <= money < 900000:
        score = 3
    elif 500000 <= money < 700000:
        score = 2

    else:
        score = 1

    familyIncome_num.append(score)


# s = ['Advertisement', 'Relative', 'Direct Interaction']
source_num = []
score = 0
for medium in source:
    if medium is 'Advertisement':
        score = 3
    elif medium is 'Relative':
        score = 4
    else:
        score = 5

    source_num.append(score)


# l = ['Urban', 'Town', 'Rural']
home_num = []
score = 0
for ho in home:
    if ho is 'Urban':
        score = 1
    elif ho is 'Town':
        score = 2
    else:
        score = 3
    home_num.append(score)


score = 0
coaching_num = []
for co in coaching:
    if co is 'Yes':
        score = 6
    else:
        score = 3
    coaching_num.append(score)



score = 0
backup_num = []
for ba in backup:
    if ba is 'Yes':
        score = 3
    else:
        score = 6
    backup_num.append(score)


score = 0
certificate_num = []
for cer in certificate:
    if cer >= 4:
        score = 3
    elif 2 <= cer <4:
        score = 2
    else:
        score = 1
    certificate_num.append(score)



score = 0
dependentMembers_num = []
for dep in dependentMembers:
    if dep >= 4:
        score = 1
    elif 2 <= dep <4:
        score = 2
    else:
        score = 3
    dependentMembers_num.append(score)


score = 0
month_num = []
# m = ['May', 'June', 'July', 'Aug']
for mon in month:
    if mon is 'May':
        score = 3
    elif mon is 'June':
        score = 4
    elif mon is 'July':
        score = 5
    elif mon is 'Aug':
        score = 5
    else:
        score = 0

    month_num.append(score)




# print(month)
# print(month_num)



df = pandas.DataFrame(data={"Name": name, "Age": age, "Gender": gender, "10th Percent": percent_10, "12th Percent": percent_12,
                            "JEE Rank":jee_rank, "Opted for Coaching": coaching, "Backup Options": backup, "Extra Curricular Activities(Distinct)": certificate,
                            "Reason to Choose BMU": reason, "Family Income(INR)": familyIncome, "Dependent Members": dependentMembers,
                            "Month of Visit": month, "Source of Information": source, "Home Location": home})



df.to_csv("./ProjectData.csv", sep=',', index=False)





df1 = pandas.DataFrame(data={"Name": name, "Age": age, "Gender": gender, "10th Percent": percent_10_num, "12th Percent": percent_12_num,
                            "JEE Rank":jee_num, "Opted for Coaching": coaching_num, "Backup Options": backup_num, "Extra Curricular Activities(Distinct)": certificate_num,
                            "Family Income(INR)": familyIncome_num, "Dependent Members": dependentMembers_num,
                            "Month of Visit": month_num, "Source of Information": source_num, "Home Location": home_num})

df1.to_csv("./ProjectData_num.csv", sep=',', index=False)


# print(len(jee_num))
# print(len(percent_12_num))
# print(len(percent_10_num))
# print(len(coaching_num))
# print(len(backup_num))
# print(len(certificate_num))
# print(len(reason))
# print(len(familyIncome_num))
# print(len(dependentMembers_num))
# print(len(home_num))
# print(len(month_num))
# print(len(source_num))
#
