student_dict = {
    "student":["Diwas", "Ram", "Shyam"],
    "score":[45,66,78]
}
# for (key,value) in student_dict.items():
#     print(key)
#     print(value)
import pandas as pd
student_df = pd.DataFrame(student_dict)
print(student_df)
print()
# for (key,value) in student_df.items():
#
#     # print(key)
#     print(value)

# instead of looping through columns names and items inside columns we can loop through rows of dataframe
for (index,row) in student_df.iterrows():
    # print(index)
    if row.student == "Diwas":
        print(row.score)