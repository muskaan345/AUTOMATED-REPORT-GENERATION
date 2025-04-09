import pandas as pd
from fpdf import FPDF

# Update this to your actual CSV file path
file_path = "C:/Users/Admin/OneDrive/Desktop/fm/TASK2.PY/data.csv"

# Read the CSV file
data = pd.read_csv(file_path)

# Detect and print columns for debugging
print("Detected columns:", data.columns.tolist())

# Create a PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Data Analysis Report", ln=True, align="C")

pdf.set_font("Arial", '', 12)
pdf.ln(5)
pdf.cell(0, 10, f"Total Entries: {len(data)}", ln=True)

# Table Headers
pdf.set_fill_color(200, 200, 200)
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Name", border=1, fill=True)
pdf.cell(30, 10, "Age", border=1, fill=True)
pdf.cell(60, 10, "Department", border=1, ln=True, fill=True)

# Table Rows
pdf.set_font("Arial", '', 12)
for _, row in data.iterrows():
    pdf.cell(60, 10, str(row['Name']), border=1)
    pdf.cell(30, 10, str(row['Age']), border=1)
    pdf.cell(60, 10, str(row['Department']), border=1, ln=True)

# Save the PDF
pdf.output("report.pdf")
print("PDF Report Generated: report.pdf")
