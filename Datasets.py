import pandas as pd

df_m = pd.read_csv('MathStudents.csv')
df_p = pd.read_csv('PortugueseStudents.csv')

dataset = []

for i in range(len(df_m.index)):

    dataset.append([ df_m['school'][i], df_m['sex'][i], df_m['age'][i], df_m['address'][i], df_m['famsize'][i], df_m['Pstatus'][i], df_m['Medu'][i], df_m['Fedu'][i], df_m['Mjob'][i], df_m['Fjob'][i], df_m['reason'][i], df_m['guardian'][i],df_m['traveltime'][i], df_m['studytime'][i], df_m['failures'][i], df_m['schoolsup'][i],df_m['famsup'][i], df_m['paid'][i], df_m['activities'][i], df_m['nursery'][i],df_m['higher'][i], df_m['internet'][i], df_m['romantic'][i], df_m['famrel'][i],df_m['freetime'][i], df_m['goout'][i], df_m['Dalc'][i], df_m['Walc'][i],df_m['health'][i], df_m['absences'][i], df_m['G1'][i], df_m['G2'][i], df_m['G3'][i] ])

for i in range(len(df_p.index)):

    dataset.append([ df_p['school'][i], df_p['sex'][i], df_p['age'][i], df_p['address'][i], df_p['famsize'][i], df_p['Pstatus'][i], df_p['Medu'][i], df_p['Fedu'][i], df_p['Mjob'][i], df_p['Fjob'][i], df_p['reason'][i], df_p['guardian'][i],df_p['traveltime'][i], df_p['studytime'][i], df_p['failures'][i], df_p['schoolsup'][i],df_p['famsup'][i], df_p['paid'][i], df_p['activities'][i], df_p['nursery'][i],df_p['higher'][i], df_p['internet'][i], df_p['romantic'][i], df_p['famrel'][i],df_p['freetime'][i], df_p['goout'][i], df_p['Dalc'][i], df_p['Walc'][i],df_p['health'][i], df_p['absences'][i], df_p['G1'][i], df_p['G2'][i], df_p['G3'][i] ])

print(pd.DataFrame(dataset))
print(len(dataset))
count = 0

for i in range(len(dataset)):

    for j in range(i, len(dataset)):

        if dataset[i] == dataset[j]:
            print(dataset[i])
            count += 1


"""
for i in range(len(dataset)):
    if dataset[2] == dataset[i]:
        count +=1
"""
print(f'{count} coincidences')
