import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([
    [80, 75, 90],
    [65, 85, 70],
    [90, 95, 85],
    [70, 60, 80]
])

print(marks.shape)
student_avg=np.mean(marks,axis=1)
print("student average: ",student_avg)
subject_averages = np.mean(marks, axis=0)
print("Subject averages:", subject_averages)

grace_marks=marks+5
print("Grace Marks :",grace_marks)

weight=np.array([0.5,0.3,0.2])
weighted_scores=np.dot(marks,weight)
print("Weighted Scores :",weighted_scores)

employees = pd.read_csv("employees.csv")
print(employees.info())
print(employees.describe())
print(employees.loc[0,"name"])
print(employees.iloc[0:4,1:4])

Higher_salary=employees[employees["salary"]>50000]
print(Higher_salary)

employees_dirty = employees.copy()


employees_dirty.loc[1, "salary"] = None
employees_dirty.loc[4, "salary"] = None

employees_dirty = pd.concat(
    [employees_dirty, employees_dirty.iloc[[0]]],
    ignore_index=True
)

median_salary = employees_dirty["salary"].median()

employees_dirty["salary"] = employees_dirty["salary"].fillna(median_salary)

print(employees_dirty)
print("Before removing duplicates:", len(employees_dirty))
employees_dirty = employees_dirty.drop_duplicates()
print("After removing duplicates:", len(employees_dirty))

employees_dirty["salary"] = employees_dirty["salary"].astype(int)

department_summary = employees_dirty.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print(department_summary)

departments = pd.read_csv("departments.csv")
inner_join = pd.merge(
    employees_dirty,
    departments,
    on="department",
    how="inner"
)
print(inner_join)

left_join=pd.merge(employees_dirty,departments,on="department",how="left")
print(left_join)

outer_join = pd.merge(
    employees_dirty,
    departments,
    on="department",
    how="outer"
)

print(outer_join)

print("Headcount:")
print(
    department_summary["headcount"].to_string()
)

headcount = department_summary["headcount"].reindex(
    ["Sales", "HR", "IT", "Finance"]
)

bars=plt.bar(headcount.index, headcount.values)

plt.title("Headcount by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.bar_label(bars)
plt.savefig("01_headcount_bar_chart.png")
plt.show()

plt.hist(employees_dirty["salary"], bins=5)

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.savefig("02_salary_histogram.png")
plt.show()
print(employees_dirty)

plt.scatter(employees_dirty["id"], employees_dirty["salary"])

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")

plt.savefig("03_salary_scatter_plot.png")
plt.show()

average_salary = department_summary["average_salary"].reindex(
    ["Sales", "HR", "IT", "Finance"]
)

plt.plot(
    average_salary.index,
    average_salary.values,
    marker="o",
    label="Average Salary"
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend()

plt.savefig("04_average_salary_line_chart.png")
plt.show()