import pandas as pd
import os

# Define data folder path
DATA_DIR = 'data'

# Coordinate lookup dictionary for Australian Higher Education Institutions (Latitude, Longitude)
CAMPUS_COORDINATES = {
    'Avondale University': (-33.1182, 151.4651),
    'Charles Sturt University': (-33.4318, 149.5606),
    'Macquarie University': (-33.7738, 151.1126),
    'Southern Cross University': (-28.8188, 153.3031),
    'The University of New England': (-30.4852, 151.6429),
    'The University of Newcastle': (-32.8931, 151.7042),
    'The University of Sydney': (-33.8886, 151.1873),
    'University of New South Wales(1.03)': (-33.9173, 151.2313),
    'University of New South Wales': (-33.9173, 151.2313),
    'University of Technology Sydney': (-33.8837, 151.2007),
    'University of Wollongong': (-34.4053, 150.8784),
    'Western Sydney University': (-33.7547, 150.7380),
    'Deakin University': (-38.1969, 144.3015),
    'Federation University Australia': (-37.6256, 143.8906),
    'La Trobe University': (-37.7214, 145.0483),
    'Monash University': (-37.9105, 145.1362),
    'RMIT University': (-37.8080, 144.9631),
    'Swinburne University of Technology': (-37.8221, 145.0389),
    'The University of Melbourne': (-37.7982, 144.9605),
    'University of Divinity': (-37.8236, 144.9822),
    'Victoria University': (-37.7925, 144.8927),
    'Bond University': (-28.0736, 153.4163),
    'CQUniversity': (-23.3255, 150.5188),
    'Griffith University': (-27.5534, 153.0526),
    'James Cook University': (-19.3278, 146.7578),
    'Queensland University of Technology': (-27.4782, 153.0283),
    'The University of Queensland': (-27.4975, 153.0137),
    'University of Southern Queensland': (-27.6041, 151.9325),
    'University of the Sunshine Coast': (-26.7176, 153.0629),
    'Curtin University': (-32.0038, 115.8948),
    'Edith Cowan University': (-31.7512, 115.7681),
    'Murdoch University': (-32.0673, 115.8360),
    'The University of Notre Dame Australia(1.09)': (-32.0569, 115.7441),
    'The University of Notre Dame Australia': (-32.0569, 115.7441),
    'The University of Western Australia': (-31.9807, 115.8172),
    'Flinders University': (-35.0426, 138.5731),
    'The University of Adelaide': (-34.9206, 138.6062),
    'Torrens University Australia': (-34.9275, 138.6053),
    'University of South Australia': (-34.9222, 138.5947),
    'University of Tasmania': (-42.9038, 147.3245),
    'Batchelor Institute of Indigenous Tertiary Education': (-13.0525, 131.0205),
    'Charles Darwin University': (-12.3718, 130.8688),
    'The Australian National University': (-35.2777, 149.1185),
    'University of Canberra': (-35.2382, 149.0838),
    'Australian Catholic University': (-37.8085, 144.9801)
}

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
    
    df_sec2['Total'] = pd.to_numeric(df_sec2['Total'].replace(['np', ' ', ''], 0), errors='coerce').fillna(0)

    # Compute Total STEM Enrolments
    df_sec2['Total_STEM'] = df_sec2[stem_cols].sum(axis=1)
    
    # Keep valid university records mapped in CAMPUS_COORDINATES
    df_sec2_clean = df_sec2[df_sec2['Institution'].isin(CAMPUS_COORDINATES.keys())].copy()
    
    # Assign Latitude and Longitude columns
    df_sec2_clean['Latitude'] = df_sec2_clean['Institution'].map(lambda x: CAMPUS_COORDINATES[x][0])
    df_sec2_clean['Longitude'] = df_sec2_clean['Institution'].map(lambda x: CAMPUS_COORDINATES[x][1])
    
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

# Export State-Level STEM Participation Rates
state_summary = df_sec2_clean.groupby('State').agg(
    Total_STEM=('Total_STEM', 'sum'),
    Total_Students=('Total', 'sum')
).reset_index()

# Filter out non-state summary rows
state_summary_clean = state_summary[~state_summary['State'].isin(['Multi-State', 'State'])].copy()
state_summary_clean['STEM_Participation_Pct'] = (
    state_summary_clean['Total_STEM'] / state_summary_clean['Total_Students'] * 100
).round(2)

# Rename 'State' to 'STATE_NAME'
state_summary_clean = state_summary_clean.rename(columns={'State': 'STATE_NAME'})

output_path_state = os.path.join(DATA_DIR, 'state_stem_participation.csv')
state_summary_clean.to_csv(output_path_state, index=False)
print(f"--> Generated: {output_path_state}")

print("Data cleaning complete! All CSV files are ready in the 'data/' folder.")