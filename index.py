import pandas as pd
import matplotlib.pyplot as plt

#creating dataset
data={
    "Name" : ['Rahul', 'Priya','Mohit','Karan','Ram','Seema','Rohan',"Kreeti"],
    "Math" : [75,78,100,95,80,93,87,94],
    "English" :[98,83,86,94,93,70,88,91],
    "Hindi" :[65,72,92,90,91,80,81,90],
    "Computer" :[79,90,89,83,91,85,74,97],
    "Science" :[80,83,98,91,90,88,81,89]
}
df=pd.DataFrame(data)
#calculating total marks
df['Total_Marks']=df['Math']+df['English']+df['Hindi']+df['Computer']+df['Science']

#calculating average marks
df['Average_marks']=df['Total_Marks']/5

#calculating percentage
df['Percentage']=df['Total_Marks']/500*100

#calculating grade
def grade(percentage):
    if percentage>=90:
        return 'A'
    elif percentage>=80:
        return 'B'
    elif percentage>=70:
        return 'C'
    else:
        return 'D'
df['Grade']=df['Percentage'].apply(grade)

#Finding topper student
topper=df['Total_Marks'].idxmax()
print('Topper Student:',df.loc[topper,'Name'])

#ranking student  based on total marks
df["Rank"] = df["Total_Marks"].rank(ascending=False)
print(df)

plt.figure(figsize=(10,5))
plt.bar(df['Name'], df['Total_Marks'], color='red',label='Comparison of Total Marks')
plt.title('Student Marks Analysis')
plt.xlabel('Students Name')
plt.ylabel('Total Marks')
plt.legend(fontsize=7,loc='upper left')
plt.xticks(rotation=40)

plt.show()
