import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# -----------------------------
# READ DATA
# -----------------------------
data = pd.read_csv("data.csv")

# -----------------------------
# ANALYSIS
# -----------------------------
avg_marks = data["Marks"].mean()
max_marks = data["Marks"].max()
min_marks = data["Marks"].min()

subject_avg = data.groupby("Subject")["Marks"].mean()

# -----------------------------
# CREATE GRAPH
# -----------------------------
plt.figure(figsize=(6,4))
subject_avg.plot(kind="bar", color="skyblue")
plt.title("Subject-wise Average Marks")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("graph.png")
plt.close()

# -----------------------------
# CREATE PDF
# -----------------------------
pdf = FPDF()
pdf.add_page()

pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Student Performance Report", new_x="LMARGIN", new_y="NEXT", align="C")

pdf.ln(5)

pdf.set_font("Helvetica", size=12)
pdf.cell(0, 10, f"Average Marks: {avg_marks:.2f}", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 10, f"Maximum Marks: {max_marks}", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 10, f"Minimum Marks: {min_marks}", new_x="LMARGIN", new_y="NEXT")

pdf.ln(5)

pdf.set_font("Helvetica", "B", 14)
pdf.cell(0, 10, "Subject-wise Graph", new_x="LMARGIN", new_y="NEXT")

pdf.image("graph.png", w=150)

pdf.ln(5)

pdf.set_font("Helvetica", "B", 14)
pdf.cell(0, 10, "Detailed Data", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("Helvetica", size=10)

for _, row in data.iterrows():
    pdf.cell(0, 8, f"{row['Name']} - {row['Subject']} - {row['Marks']}", new_x="LMARGIN", new_y="NEXT")

pdf.output("report.pdf")

print("Report generated successfully with graph!")