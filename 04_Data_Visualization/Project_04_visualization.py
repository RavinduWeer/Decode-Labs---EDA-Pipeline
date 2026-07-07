import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import warnings

# Suppress minor future warnings for a clean terminal output
warnings.filterwarnings("ignore")

# Set up global styling
sns.set_theme(style="white")

print("Loading data for strategic visualizations...")
file_path = "Dataset for Data Analytics.xlsx"
df = pd.read_excel(r"D:\Decode Labs\Project 04\Dataset for Data Analytics.xlsx")


# Ensure Date column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])


# ==========================================
# SLIDE 1: PRODUCT REVENUE (THE ARCHITECT)
# ==========================================
print("Generating Slide 1: Product Revenue...")
# Aggregate revenue by product and sort from highest to lowest
prod_revenue = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).reset_index()

# Create Canvas 1
fig1, ax1 = plt.subplots(figsize=(12, 6.5))
fig1.patch.set_facecolor('white')
ax1.set_facecolor('white')

# Apply Spotlight Rule
colors = ['#1f77b4', '#1f77b4'] + ['#d3d3d3'] * (len(prod_revenue) - 2)

# Generate Bar Chart
bars = ax1.barh(prod_revenue['Product'], prod_revenue['TotalPrice'], color=colors, height=0.6)
ax1.invert_yaxis()

# Eradicate Chartjunk
for spine in ax1.spines.values():
    spine.set_visible(False)
ax1.xaxis.set_visible(False)
ax1.tick_params(left=False)
ax1.set_yticklabels(prod_revenue['Product'], fontsize=12, color='#333333')

# Direct Labeling
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 3000, bar.get_y() + bar.get_height()/2, 
            f'${width:,.0f}', va='center', ha='left', fontsize=11, fontweight='bold', color='#333333')

# Action Title 1
fig1.text(0.05, 0.95, "Office Equipment Drives Our Revenue Engine", 
          fontsize=18, fontweight='bold', color='#1a1a1a')
fig1.text(0.05, 0.88, "Chairs and Printers are the dominant revenue drivers, vastly outpacing mobile devices.\nRecommendation: Reallocate Q3 marketing spend toward B2B office essentials.", 
          fontsize=13, color='#555555')

# Save Slide 1
plt.figure(fig1.number) # Set focus to fig1
plt.tight_layout(rect=[0, 0, 1, 0.85])
fig1.savefig('Boardroom_Slide_Project4.1.png', dpi=300, bbox_inches='tight')


# ==========================================
# SLIDE 2: SEASONALITY TREND (THE STORYTELLER)
# ==========================================
print("Generating Slide 2: Seasonality Trend...")
# Aggregate by month and calculate rolling average
monthly_revenue = df.resample('ME', on='Date')['TotalPrice'].sum().reset_index()
monthly_revenue['Rolling_Avg'] = monthly_revenue['TotalPrice'].rolling(window=3).mean()

# Create Canvas 2
fig2, ax2 = plt.subplots(figsize=(12, 6.5))
fig2.patch.set_facecolor('white')
ax2.set_facecolor('white')

# Plot Raw Revenue (Context)
ax2.plot(monthly_revenue['Date'], monthly_revenue['TotalPrice'], 
        color='#b0bec5', linewidth=2, marker='o', markersize=4, label='Monthly Revenue')

# Plot Moving Average (Insight)
ax2.plot(monthly_revenue['Date'], monthly_revenue['Rolling_Avg'], 
        color='#1f77b4', linewidth=4, label='3-Month Moving Average')

# Eradicate Chartjunk
for spine in ['top', 'right', 'left']:
    ax2.spines[spine].set_visible(False)

# Format X-axis Dates
ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax2.tick_params(axis='x', colors='#555555', labelsize=11)
ax2.tick_params(axis='y', left=False, labelleft=False)

# Direct Labeling for Peaks
peaks = monthly_revenue[monthly_revenue['TotalPrice'] > 60000]
for index, row in peaks.iterrows():
    ax2.text(row['Date'], row['TotalPrice'] + 2000, 
            f"${row['TotalPrice']:,.0f}", 
            color='#1f77b4', fontweight='bold', ha='center', va='bottom', fontsize=11)

# Current Trend Label
last_date = monthly_revenue['Date'].iloc[-1]
last_avg = monthly_revenue['Rolling_Avg'].iloc[-1]
if not pd.isna(last_avg):
    ax2.text(last_date, last_avg, "  Current Trend", color='#1f77b4', fontweight='bold', va='center')

# Action Title 2
fig2.text(0.05, 0.95, "Revenue Exhibits Distinct Summer Seasonality", 
          fontsize=18, fontweight='bold', color='#1a1a1a')
fig2.text(0.05, 0.88, "Moving averages reveal consistent purchasing spikes in Q2 (May/June).\nRecommendation: Shift inventory accumulation and ad spend to April to capture incoming demand.", 
          fontsize=13, color='#555555')

# Save Slide 2
plt.figure(fig2.number) # Set focus to fig2
plt.tight_layout(rect=[0, 0, 1, 0.85])
fig2.savefig('Boardroom_Slide_2_Seasonality.png', dpi=300, bbox_inches='tight')

# ==========================================
# 3. FINAL EXECUTION
# ==========================================
print("\nSuccess: Both strategic visuals have been generated and saved to your workspace!")

# Display both windows at the same time
plt.show()