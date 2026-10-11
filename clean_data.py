import pandas as pd
import os

# Define data folder path
DATA_DIR = 'data'

print("Starting data cleaning process...")

# 1. Clean Section 2: University STEM Enrolments 2024
sec2_path = os.path.join(DATA_DIR, '2024_Section2_All_Students.xlsx')
if os.path.exists(sec2_path):
    df_sec2 = pd.read_excel(sec2_path, sheet_name='2.11', skiprows=1)
    df_sec2.columns = [
        'State', 'Institution', 'Natural_Physical_Sciences', 'IT', 
        'Engineering', 'Architecture_Building', 'Agriculture_Environment', 
        'Health', 'Education', 'Management_Commerce', 'Society_Culture', 
        'Creative_Arts', 'Food_Hospitality', 'Mixed_Field', 'Non_Award', 'Total'
    ]
    
    # Clean non-numeric values ('np', blanks) to 0
    stem_cols = ['Natural_Physical_Sciences', 'IT', 'Engineering', 'Agriculture_Environment']
    for col in stem_cols:
        df_sec2[col] = pd.to_numeric(df_sec2[col].replace(['np', ' ', ''], 0), errors='coerce').fillna(0)

    # Compute Total STEM Enrolments
    df_sec2['Total_STEM'] = df_sec2[stem_cols].sum(axis=1)
    
    # Drop header metadata rows
    df_sec2_clean = df_sec2.dropna(subset=['State', 'Institution'])
    
    output_path = os.path.join(DATA_DIR, 'university_stem_2024.csv')
    df_sec2_clean.to_csv(output_path, index=False)
    print(f"--> Generated: {output_path}")

# 2. Clean Section 11: Equity Group Enrolments 2024
sec11_path = os.path.join(DATA_DIR, '2024_Section11_Equity_Groups.xlsx')
if os.path.exists(sec11_path):
    df_sec11 = pd.read_excel(sec11_path, sheet_name='11.7', skiprows=2)
    df_sec11 = df_sec11.iloc[:, :7]
    df_sec11.columns = [
        'State', 'Institution', 'Non_English_Speaking', 
        'Disability', 'Women_In_Non_Traditional', 'First_Nations', 'Low_SES'
    ]
    
    equity_cols = ['Non_English_Speaking', 'Disability', 'Women_In_Non_Traditional', 'First_Nations', 'Low_SES']
    for col in equity_cols:
        df_sec11[col] = pd.to_numeric(df_sec11[col].replace(['np', ' ', ''], 0), errors='coerce').fillna(0)

    df_sec11_clean = df_sec11.dropna(subset=['State', 'Institution'])
    
    output_path = os.path.join(DATA_DIR, 'equity_groups_2024.csv')
    df_sec11_clean.to_csv(output_path, index=False)
    print(f"--> Generated: {output_path}")

# 3. Clean Industry Workforce Data 2026
ind_path = os.path.join(DATA_DIR, 'industry_data_-_february_2026.xlsx')
if os.path.exists(ind_path):
    df_ind = pd.read_excel(ind_path, sheet_name='Table_1', skiprows=5)
    df_ind = df_ind.iloc[:, :7]
    df_ind.columns = [
        'Industry', 'Employed', 'Female_Share_Pct', 'Part_Time_Share_Pct', 
        'Median_Weekly_Earnings', 'Workforce_Share_Pct', 'Median_Age'
    ]
    df_ind_clean = df_ind.dropna(subset=['Industry'])
    
    output_path = os.path.join(DATA_DIR, 'industry_workforce_2026.csv')
    df_ind_clean.to_csv(output_path, index=False)
    print(f"--> Generated: {output_path}")

# 4. Clean State & Field Trends (2020–2024)
piv_path = os.path.join(DATA_DIR, 'Perturbed Student Enrolments Pivot Table 2024.xlsx')
if os.path.exists(piv_path):
    df_piv = pd.read_excel(piv_path, sheet_name='Pivot_BFOE', header=23)
    
    # Forward-fill state names across institution rows
    df_piv['State'] = df_piv['State'].ffill()
    df_piv_clean = df_piv.dropna(subset=['Institution'])
    
    output_path = os.path.join(DATA_DIR, 'state_field_trends_2020_2024.csv')
    df_piv_clean.to_csv(output_path, index=False)
    print(f"--> Generated: {output_path}")

print("Data cleaning complete! All CSV files are ready in the 'data/' folder.")