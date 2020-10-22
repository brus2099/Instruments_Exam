import pandas as pd

df_m = pd.read_csv('Students.csv')
df_p = pd.read_csv('PortugueseStudents.csv')

dataset = []

for i in range(len(df_m.index)):

    dataset.append([ df_m['school'][i], df_m['sex'][i], df_m['age'][i], df_m['address'][i], df_m['famsize'][i], df_m['Pstatus'][i], df_m['Medu'][i], df_m['Fedu'][i], df_m['Mjob'][i], df_m['Fjob'][i], df_m['reason'][i], df_m['guardian'][i],df_m['traveltime'][i], df_m['studytime'][i], df_m['failures'][i], df_m['schoolsup'][i],df_m['famsup'][i], df_m['paid'][i], df_m['activities'][i], df_m['nursery'][i],df_m['higher'][i], df_m['internet'][i], df_m['romantic'][i], df_m['famrel'][i],df_m['freetime'][i], df_m['goout'][i], df_m['Dalc'][i], df_m['Walc'][i],df_m['health'][i], df_m['absences'][i], df_m['G1'][i], df_m['G2'][i], df_m['G3'][i] ])

print(pd.DataFrame(dataset))
print(len(dataset))
count = 0

