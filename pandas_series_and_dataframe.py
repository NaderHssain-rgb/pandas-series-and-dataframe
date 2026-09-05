import pandas as pd

# ============================================
# Pandas Series vs DataFrame
# ============================================


# 1. Pandas Series

age = pd.Series(
    [11, 22, 33],
    index=["A", "B", "C"]
)

print("Series:")
print(age)

print("#" * 50)


# 2. Pandas DataFrame

student_data = pd.DataFrame(
    {
        "Name": ["Nder", "Ahmed", "Abdallah"],
        "Age": [24, 13, 11],
        "IsGraduated": [True, False, False]
    },
    index=["A", "AA", "AAA"]
)

print("DataFrame:")
print(student_data)