import pandas as pd
from datetime import datetime

def normalize_columns(df):
    df = df.copy()
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df

def clean_jobs_dataframe(df, source):
    df = normalize_columns(df)

    required_columns = [
        "job_title", "company", "location"
    ]

    for col in required_columns:
        if col not in df.columns:
            df[col] = "N/A"

    df["source"] = source
    df["scraped_at"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    df = df.drop_duplicates(subset=["job_title", "company"])
    df = df.reset_index(drop=True)

    return df

def merge_job_dataframes(static_df, api_df):
    static_clean = clean_jobs_dataframe(static_df, "static")
    api_clean = clean_jobs_dataframe(api_df, "api")

    merged = pd.concat([static_clean, api_clean], ignore_index=True)
    return merged

if __name__ == "__main__":
    static_df = pd.read_csv("data/static_jobs.csv")
    api_df = pd.read_csv("data/himalayas_remote_jobs.csv")

    final_df = merge_job_dataframes(static_df, api_df)
    final_df.to_csv("data/cleaned_jobs.csv", index=False)

    print(f"Final dataset contains {len(final_df)} jobs")
    print(final_df.head())
