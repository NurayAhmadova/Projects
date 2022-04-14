import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
# print(student_df)

# Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)
