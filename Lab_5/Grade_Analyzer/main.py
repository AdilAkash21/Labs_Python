"""
Student Grade Analyzer
Reads a CSV file of student grades, calculates statistics,
classifies grades, and generates a report with optional chart.
"""

import csv
import os

# ============================================================
# Task 1: Read the CSV File
# ============================================================

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'students.csv')

students = []

with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        student = {
            'name': row['name'],
            'student_id': row['student_id'],
            'score': int(row['score'])
        }
        students.append(student)

# ============================================================
# Task 2: Calculate Basic Statistics
# ============================================================
total_students = len(students)
scores = [s['score'] for s in students]

average_score = sum(scores) / total_students
highest_score = max(scores)
lowest_score = min(scores)

passing_students = sum(1 for s in students if s['score'] >= 60)
failing_students = sum(1 for s in students if s['score'] < 60)

# ============================================================
# Task 3: Classify Grade Levels
# ============================================================
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

for student in students:
    student['grade'] = get_grade(student['score'])

# ============================================================
# Task 4: Count Grade Distribution
# ============================================================
grade_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

for student in students:
    grade_distribution[student['grade']] += 1

# Print results to screen
print("Student Grade Analyzer")
print("----------------------")
print(f"Total students: {total_students}")
print(f"Average score: {average_score:.2f}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Passing students: {passing_students}")
print(f"Failing students: {failing_students}")
print()
print("Grade Distribution:")
for grade in ['A', 'B', 'C', 'D', 'F']:
    print(f"{grade}: {grade_distribution[grade]}")

# ============================================================
# Task 5: Generate a Text Report
# ============================================================
with open('grade_report.txt', 'w') as f:
    f.write("Student Grade Analyzer\n")
    f.write("----------------------\n")
    f.write(f"Total students: {total_students}\n")
    f.write(f"Average score: {average_score:.2f}\n")
    f.write(f"Highest score: {highest_score}\n")
    f.write(f"Lowest score: {lowest_score}\n")
    f.write(f"Passing students: {passing_students}\n")
    f.write(f"Failing students: {failing_students}\n")
    f.write("\n")
    f.write("Grade Distribution:\n")
    for grade in ['A', 'B', 'C', 'D', 'F']:
        f.write(f"{grade}: {grade_distribution[grade]}\n")
    f.write("\n")
    f.write("Individual Student Grades:\n")
    f.write("-" * 40 + "\n")
    for student in students:
        f.write(f"{student['name']} (ID: {student['student_id']}): Score={student['score']}, Grade={student['grade']}\n")

print("\nReport saved to grade_report.txt")

# ============================================================
# Task 6 (Optional): Data Visualization
# ============================================================
try:
    import matplotlib.pyplot as plt
    
    grades = ['A', 'B', 'C', 'D', 'F']
    counts = [grade_distribution[g] for g in grades]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(grades, counts, color=['#2ecc71', '#3498db', '#f1c40f', '#e67e22', '#e74c3c'])
    
    ax.set_title('Grade Distribution', fontsize=16, fontweight='bold')
    ax.set_xlabel('Grade', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_ylim(0, max(counts) + 1)
    ax.set_yticks(range(0, max(counts) + 2))
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('grade_chart.png', dpi=150, bbox_inches='tight')
    print("Chart saved to grade_chart.png")
    
except ImportError:
    print("matplotlib not installed. Skipping chart generation.")