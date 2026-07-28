import matplotlib.pyplot as plt
import numpy as np

# Mid-point year representing each bracket
years = [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023, 2025]

# Converted mean salaries in LPA
tcs_ninja = [2.00, 2.55, 3.00, 3.05, 3.15, 3.20, 3.25, 3.40, 3.40, 3.40, 3.45]
tcs_digital = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 6.50, 6.75, 7.15, 7.25, 7.30]
google_india = [5.25, 7.00, 9.00, 11.00, 13.50, 16.50, 21.00, 27.00, 30.50, 32.50, 35.00]

# Initialize Plot
plt.figure(figsize=(12, 7))

# Plot lines
plt.plot(years, google_india, marker='o', color='#4285F4', linewidth=2.5, label='Google India (L3 Tech)')
plt.plot(years, tcs_ninja, marker='s', color='#1B365D', linewidth=2, label='TCS Ninja (Mass-Hire)')
# Slicing handled automatically by matplotlib for NaN blocks
plt.plot(years, tcs_digital, marker='^', color='#FF9900', linewidth=2, linestyle='--', label='TCS Digital (Premium)')

# Annotate start and end points for context
plt.annotate(f'₹{google_india[0]} LPA', (years[0], google_india[0]), textcoords="offset points", xytext=(-10,10), ha='center', color='#4285F4', weight='bold')
plt.annotate(f'₹{google_india[-1]} LPA', (years[-1], google_india[-1]), textcoords="offset points", xytext=(0,10), ha='center', color='#4285F4', weight='bold')

plt.annotate(f'₹{tcs_ninja[0]} LPA', (years[0], tcs_ninja[0]), textcoords="offset points", xytext=(-10,-15), ha='center', color='#1B365D', weight='bold')
plt.annotate(f'₹{tcs_ninja[-1]} LPA', (years[-1], tcs_ninja[-1]), textcoords="offset points", xytext=(0,-15), ha='center', color='#1B365D', weight='bold')

# Annotate TCS Digital Launch
plt.annotate(f'₹{tcs_digital[6]} LPA\n(Launched)', (years[6], tcs_digital[6]), textcoords="offset points", xytext=(25,-5), ha='center', arrowprops=dict(arrowstyle="->", color='#FF9900'))
plt.annotate(f'₹{tcs_digital[-1]} LPA', (years[-1], tcs_digital[-1]), textcoords="offset points", xytext=(20,0), ha='center', color='#FF9900', weight='bold')

# Graph details & styling
plt.title('20-Year Trend of Entry-Level Tech Salaries in India (Mean LPA)', fontsize=14, weight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Compensation (Lakhs Per Annum - LPA)', fontsize=12)
plt.xticks(years, [f"'{str(y)[2:]}" for y in years])
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', frameon=True, shadow=True)

# Layout adjustments and display
plt.tight_layout()
plt.show()
