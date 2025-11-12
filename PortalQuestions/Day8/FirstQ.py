import pandas as pd
import os
import sys

filename = input().strip()
if not filename:
    print("No filename entered. Exiting program.")
    sys.exit()

filePath = os.path.join(sys.path[0], filename)
if not os.path.exists(filePath):
    print(f"Error: File '{filename}' not found.")
    sys.exit()

try:
    df = pd.read_csv(filePath)
except Exception as e:
    print(f"Error loading file: {e}")
    sys.exit()

required_columns = [
    'employee_id', 'department', 'region', 'education', 'gender',
    'recruitment_channel', 'no_of_trainings', 'age', 'previous_year_rating',
    'length_of_service', 'awards_won', 'avg_training_score', 'is_promoted',
    'performance_score', 'years_since_last_promotion',
    'is_eligible_for_promotion', 'experience_level',
    'training_effectiveness_ratio', 'is_promoted_text', 'age_group'
]

missing_cols = [col for col in required_columns if col not in df.columns]
if missing_cols:
    print(f"Warning: Missing columns in dataset: {missing_cols}")

if 'gender' in df.columns:
    df['gender'] = df['gender'].map({'f': 'Female', 'm': 'Male'})
else:
    print("Warning: 'gender' column missing in dataset.")

if {'department', 'gender', 'avg_training_score'}.issubset(df.columns):
    avg_training = df.groupby(['department', 'gender'])['avg_training_score'].mean().round(2).unstack()
    print("\nAverage Training Score by Department and Gender:")
    print(avg_training)
else:
    print("\nWarning: Missing columns for 'Average Training Score by Department and Gender'")

if {'department', 'education', 'training_effectiveness_ratio'}.issubset(df.columns):
    training_eff = df.groupby(['department', 'education'])['training_effectiveness_ratio'].mean().round(2).unstack()
    print("\nTraining Effectiveness Ratio by Department and Education:")
    print(training_eff)
else:
    print("\nWarning: Missing columns for 'Training Effectiveness Ratio by Department and Education'")

if {'experience_level', 'department', 'is_promoted'}.issubset(df.columns):
    promotion_rate = df.groupby(['experience_level', 'department'])['is_promoted'].mean().round(2).unstack()
    print("\nPromotion Rate by Experience Level and Department:")
    print(promotion_rate)
else:
    print("\nWarning: Missing columns for 'Promotion Rate by Experience Level and Department'")

if {'awards_won', 'avg_training_score', 'is_promoted'}.issubset(df.columns):
    try:
        df['training_score_bin'] = pd.qcut(df['avg_training_score'], 4)
        promo_bins = df.groupby(['awards_won', 'training_score_bin'])['is_promoted'].mean().round(2).unstack()
        print("\nPromotion Rate by Awards Won and Avg Training Score Bins:")
        print(promo_bins)
    except Exception as e:
        print(f"\nError computing quartile bins: {e}")
else:
    print("\nWarning: Missing columns for 'Promotion Rate by Awards Won and Avg Training Score Bins'")

print("\nDone.")
