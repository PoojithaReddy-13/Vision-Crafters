import pandas as pd

# Load candidates
df = pd.read_csv("app/data/candidates.csv")

# Simple AI scoring based on Python skill
df["Score"] = df["Skills"].apply(lambda x: 100 if "Python" in x else 70)

# Sort candidates
df = df.sort_values(by="Score", ascending=False)

print("=== Candidate Ranking ===")
print(df)

# Save ranked output
df.to_csv("app/data/ranked_candidates.csv", index=False)