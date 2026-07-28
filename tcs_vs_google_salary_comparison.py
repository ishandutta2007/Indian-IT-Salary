import matplotlib.pyplot as plt
import numpy as np

# Mid-point year representing each bracket
years = [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023, 2025]

# Converted mean salaries in LPA
tcs_ninja = [2.00, 2.55, 3.00, 3.05, 3.15, 3.20, 3.25, 3.40, 3.40, 3.40, 3.45]
tcs_digital = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 6.50, 6.75, 7.15, 7.25, 7.30]
google_india = [5.25, 7.00, 9.00, 11.00, 13.50, 16.50, 21.00, 27.00, 30.50, 32.50, 35.00]

# Initialize Plot
plt.figure(figsize=(15, 9))

# Plot lines
plt.plot(years, google_india, marker='o', color='#4285F4', linewidth=2.5, label='Google India (L3 Tech)')
plt.plot(years, tcs_ninja, marker='s', color='#1B365D', linewidth=2, label='TCS Ninja (Mass-Hire)')
# plt.plot(years, tcs_digital, marker='^', color='#FF9900', linewidth=2, linestyle='--', label='TCS Digital (Premium)')

# Annotate ALL individual points on the Google India line
for y, g in zip(years, google_india):
    plt.text(y, g + 0.8, f'₹{g}', ha='center', va='bottom', color='#4285F4', weight='bold', fontsize=9)

# Annotate ALL individual points on the TCS Ninja line
for y, n in zip(years, tcs_ninja):
    plt.text(y, n - 1.2, f'₹{n}', ha='center', va='top', color='#1B365D', weight='bold', fontsize=9)

# Annotate ALL individual valid points on the TCS Digital line
for y, d in zip(years, tcs_digital):
    if not np.isnan(d):
        plt.text(y, d + 0.6, f'₹{d}', ha='center', va='bottom', color='#D97706', weight='bold', fontsize=9)

# 1. Double-ended vertical arrow at the START (2005)
plt.annotate('', 
             xy=(years[0], google_india[0]), 
             xytext=(years[0], tcs_ninja[0]), 
             arrowprops=dict(arrowstyle='<->', color='red', lw=2, linestyle=':'))
plt.text(years[0] + 0.25, (google_india[0] + tcs_ninja[0]) / 2, '2.6x\nGap', 
         color='red', weight='bold', va='center', ha='left', fontsize=10)

# 2. Double-ended vertical arrow at the END (2025)
plt.annotate('', 
             xy=(years[-1], google_india[-1]), 
             xytext=(years[-1], tcs_ninja[-1]), 
             arrowprops=dict(arrowstyle='<->', color='red', lw=2, linestyle=':'))
plt.text(years[-1] - 0.25, (google_india[-1] + tcs_ninja[-1]) / 2, '10.1x\nGap', 
         color='red', weight='bold', va='center', ha='right', fontsize=11)

# Graph styling
plt.title('20-Year Trend & Widening Income Gap: Entry-Level Tech Salaries in India (Values in LPA)', fontsize=14, weight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Compensation (Lakhs Per Annum - LPA)', fontsize=12)
plt.xticks(years, [f"'{str(y)[2:]}" for y in years])
plt.ylim(0, 40)  # Extended y-limit to avoid clipping annotations
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='upper left', frameon=True, shadow=True)

# Layout adjustments and display
plt.tight_layout()
plt.show()
