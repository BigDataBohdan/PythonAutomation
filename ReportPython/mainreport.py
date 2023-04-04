import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas

# Read the dataset from an xlsx file
df = pd.read_excel("del_winners.xlsx")

# Perform some basic analysis
industries = df["PRIMARY INDUSTRY"].value_counts()
top_cities = df["CITY"].value_counts().head(5)
growth = df["GROWTH"].str.replace("%", "").str.replace(",", "").astype(float) / 100
avg_growth = growth.mean()
max_growth = growth.max()
min_growth = growth.min()

# Create a PDF report
pdf = canvas.Canvas("report.pdf")
pdf.setFont("Helvetica-Bold", 24)

# Add the logo
pdf.drawImage("logo.png", 50, 750, width=100, height=100)

# Add introduction
pdf.setFont("Helvetica", 16)
pdf.drawString(200, 780, "Data Analysis Report")
pdf.drawString(50, 700, f"Total Number of Companies: {len(df)}")
pdf.drawString(50, 670, f"Number of Industries: {len(industries)}")
pdf.drawString(50, 640, "Top 5 Cities by Number of Companies:")
for i, city in enumerate(top_cities.index):
    pdf.drawString(80, 610 - i*30, f"{i+1}. {city}: {top_cities[city]} companies")

# Add growth analysis
pdf.drawString(50, 460, "Growth Analysis")
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(50, 440, "Average Growth Rate:")
pdf.drawString(250, 440, f"{avg_growth:.2f}%")
pdf.drawString(50, 420, "Maximum Growth Rate:")
pdf.drawString(250, 420, f"{max_growth:.2f}%")
pdf.drawString(50, 400, "Minimum Growth Rate:")
pdf.drawString(250, 400, f"{min_growth:.2f}%")

# Create a bar chart of the number of companies per industry
fig, ax = plt.subplots(figsize=(8, 6))
industries.plot(kind="bar", ax=ax)
ax.set_title("Number of Companies per Industry")
ax.set_xlabel("INDUSTRY")
ax.set_ylabel("Number of Companies")
plt.tight_layout()
plt.savefig("industries.png")

# Add the bar chart to the PDF report
pdf.showPage()
pdf.setFont("Helvetica-Bold", 20)
pdf.drawString(50, 750, "Number of Companies per Industry")
pdf.drawImage("industries.png", 50, 400, width=500, height=300)
pdf.showPage()

# Save and close the PDF report
pdf.save()      
