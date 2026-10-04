
# ==========================================
# IPL DATA ANALYSIS PROJECT
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# PART 1 — LOAD DATA
# ==========================================

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")


# ==========================================
# PART 2 — EXPLORE DATA
# ==========================================

print("===== MATCHES DATA =====")

print(matches.head())
print(matches.tail())
print("Matches shape:", matches.shape)


print("\n===== DELIVERIES DATA =====")

print(deliveries.head())
print(deliveries.tail())
print("Deliveries shape:", deliveries.shape)


print("\n===== MATCHES INFORMATION =====")

matches.info()

print("\n===== MATCHES STATISTICS =====")

print(matches.describe())


print("\n===== DELIVERIES INFORMATION =====")

deliveries.info()

print("\n===== DELIVERIES STATISTICS =====")

print(deliveries.describe())


# Check duplicates

print("\nMatches duplicates:", matches.duplicated().sum())
print("Deliveries duplicates:", deliveries.duplicated().sum())


# Check important categorical columns

print("\n===== TEAM 1 =====")
print(matches["team1"].unique())

print("\n===== TEAM 2 =====")
print(matches["team2"].unique())

print("\n===== WINNERS =====")
print(matches["winner"].unique())

print("\n===== TOSS DECISIONS =====")
print(matches["toss_decision"].value_counts())

print("\n===== RESULTS =====")
print(matches["result"].value_counts())

print("\n===== MATCHES BY SEASON =====")
print(matches["season"].value_counts().sort_index())


# ==========================================
# PART 2B — CLEANING DATA
# ==========================================

print("\n================================")
print("DATA CLEANING")
print("================================")


# 1. Remove duplicate delivery row

deliveries = deliveries.drop_duplicates()

print(
    "Deliveries shape after removing duplicates:",
    deliveries.shape
)


# 2. Standardize team names

old_name = "Rising Pune Supergiants"
new_name = "Rising Pune Supergiant"


# Matches table

for column in ["team1", "team2", "toss_winner", "winner"]:
    matches[column] = matches[column].replace(
        old_name,
        new_name
    )


# Deliveries table

for column in ["batting_team", "bowling_team"]:
    deliveries[column] = deliveries[column].replace(
        old_name,
        new_name
    )


# 3. Convert date to datetime

matches["date"] = pd.to_datetime(matches["date"])


# 4. Remove umpire3 because it contains no values

matches = matches.drop(columns=["umpire3"])


# ==========================================
# PART 2C — FINAL CHECK
# ==========================================

print("\n================================")
print("FINAL CHECK")
print("================================")


print("Matches shape:", matches.shape)
print("Deliveries shape:", deliveries.shape)


print("\nMatches duplicates:")
print(matches.duplicated().sum())


print("\nDeliveries duplicates:")
print(deliveries.duplicated().sum())


print("\nMissing values in matches:")
print(matches.isnull().sum())


print("\nMissing values in deliveries:")
print(deliveries.isnull().sum())


print("\nDate data type:")
print(matches["date"].dtype)


print("\nTeam names:")
print(matches["team1"].unique())


print("\nWinner team names:")
print(matches["winner"].unique())


# ==========================================
# PART 3 — DATA ANALYSIS
# ==========================================


# 1. Total number of matches

total_matches = matches["id"].nunique()

print("\n1. Total number of matches:")
print(total_matches)


# 2. Matches per season

matches_per_season = (
    matches.groupby("season")["id"].nunique()
)

print("\n2. Matches per season:")
print(matches_per_season)


# 3. Matches won by each team

team_wins = matches["winner"].value_counts()

print("\n3. Matches won by each team:")
print(team_wins)


# 4. Matches won by each team per season

matches_won_by_team_per_season = (
    matches.groupby("season")["winner"].value_counts()
)

print("\n4. Matches won by each team per season:")
print(matches_won_by_team_per_season)


# 5. Toss wins by each team

toss_wins_by_team = matches["toss_winner"].value_counts()

print("\n5. Toss wins by each team:")
print(toss_wins_by_team)


# 6. Toss wins by each team per season

toss_wins_by_team_per_season = (
    matches.groupby("season")["toss_winner"].value_counts()
)

print("\n6. Toss wins by each team per season:")
print(toss_wins_by_team_per_season)


# 7. Team with highest wins

highest_match_won = team_wins.idxmax()
highest_wins = team_wins.max()

print("\n7. Team with highest number of wins:")
print(highest_match_won)
print("Number of wins:", highest_wins)


# 8. Team with lowest wins

lowest_match_won = team_wins.idxmin()
lowest_wins = team_wins.min()

print("\n8. Team with lowest number of wins:")
print(lowest_match_won)
print("Number of wins:", lowest_wins)


# 9. Team with highest toss wins

highest_toss_won = toss_wins_by_team.idxmax()
highest_toss_wins = toss_wins_by_team.max()

print("\n9. Team with highest toss wins:")
print(highest_toss_won)
print("Number of toss wins:", highest_toss_wins)


# 10. Team with lowest toss wins

lowest_toss_won = toss_wins_by_team.idxmin()
lowest_toss_wins = toss_wins_by_team.min()

print("\n10. Team with lowest toss wins:")
print(lowest_toss_won)
print("Number of toss wins:", lowest_toss_wins)


# 11. Most Player of the Match awards

pom = matches["player_of_match"].value_counts()

player_of_the_match = pom.idxmax()
player_of_the_match_count = pom.max()

print("\n11. Player of the Match:")
print(player_of_the_match)
print("Number of awards:", player_of_the_match_count)


# 12. Most played venue

venue_counts = matches["venue"].value_counts()

venue = venue_counts.idxmax()
venue_count = venue_counts.max()

print("\n12. Most played venue:")
print(venue)
print("Number of matches:", venue_count)


# 13. Most played city

city_counts = matches["city"].value_counts()

city = city_counts.idxmax()
city_count = city_counts.max()

print("\n13. Most played city:")
print(city)
print("Number of matches:", city_count)


# 14. Top 10 batsmen

top_batsmen = (
    deliveries.groupby("batsman")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n14. Top 10 batsmen:")
print(top_batsmen)


# 15. Top 10 wicket takers

bowler_wicket_dismissals = [
    "caught",
    "bowled",
    "lbw",
    "stumped",
    "caught and bowled",
    "hit wicket"
]

wicket_deliveries = deliveries[
    deliveries["dismissal_kind"].isin(
        bowler_wicket_dismissals
    )
]


top_bowlers = (
    wicket_deliveries
    .groupby("bowler")["player_dismissed"]
    .count()
    .sort_values(ascending=False)
    .head(10)
)

print("\n15. Top 10 wicket takers:")
print(top_bowlers)


# 16. Top 10 individual scores

highest_run_scorers = (
    deliveries
    .groupby(["match_id", "batsman"])["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n16. Top 10 highest individual scores:")
print(highest_run_scorers)


# 17. Season-wise total runs

match_runs = (
    deliveries
    .groupby("match_id")["total_runs"]
    .sum()
)


season_runs = matches[
    ["id", "season"]
].merge(
    match_runs,
    left_on="id",
    right_index=True
)


season_total_runs = (
    season_runs
    .groupby("season")["total_runs"]
    .sum()
)

print("\n17. Season-wise total runs:")
print(season_total_runs)


# 18. Season-wise bowler wickets

# Add season to wicket data

wicket_deliveries = wicket_deliveries.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id"
)


season_wickets = (
    wicket_deliveries
    .groupby("season")["player_dismissed"]
    .count()
)

print("\n18. Season-wise bowler wickets:")
print(season_wickets)


# 19. Team-wise average runs per innings

team_innings_runs = (
    deliveries
    .groupby(
        ["match_id", "inning", "batting_team"]
    )["total_runs"]
    .sum()
    .reset_index()
)


team_average_runs = (
    team_innings_runs
    .groupby("batting_team")["total_runs"]
    .mean()
    .sort_values(ascending=False)
)

print("\n19. Team-wise average runs per innings:")
print(team_average_runs)


# 20. Highest winning margin by runs

highest_run_win_match = matches.loc[
    matches["win_by_runs"].idxmax()
]

print("\n20. Highest winning margin by runs:")

print(
    highest_run_win_match[
        ["id", "season", "winner", "win_by_runs"]
    ]
)


# 21. Highest winning margin by wickets

highest_win_by_wickets = matches[
    "win_by_wickets"
].max()

highest_wicket_win_match = matches.loc[
    matches["win_by_wickets"].idxmax()
]

print("\n21. Highest winning margin by wickets:")

print(
    highest_wicket_win_match[
        ["id", "season", "winner", "win_by_wickets"]
    ]
)


# 22. Average runs per match

average_runs_per_match = (
    season_runs["total_runs"].mean()
)

print("\n22. Average runs per match:")
print(average_runs_per_match)


# 23. Toss winner also won the match

toss_match_result = matches[
    matches["toss_winner"].notna() &
    matches["winner"].notna()
]


toss_winner_won = (
    toss_match_result["toss_winner"]
    == toss_match_result["winner"]
)


toss_winner_won_count = toss_winner_won.sum()

total_valid_matches = len(
    toss_match_result
)


toss_win_percentage = (
    toss_winner_won_count
    / total_valid_matches
) * 100


print("\n23. Toss winner also won the match:")
print(toss_winner_won_count)

print("Total valid matches:")
print(total_valid_matches)

print("Percentage:")
print(toss_win_percentage)

# ========================================
# VISUALIZATIONS
# ========================================

# 1. Matches Played per Season

matches_per_season = matches.groupby("season")["id"].count()

plt.figure(figsize=(10, 5))

plt.bar(matches_per_season.index, matches_per_season.values)

plt.title("Matches Played per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")

plt.show()

# 2. Wins by Team

wins_by_team = matches["winner"].value_counts()

plt.figure(figsize=(10, 5))

plt.bar(wins_by_team.index, wins_by_team.values)

plt.title("Wins by Team")
plt.xlabel("Team")
plt.ylabel("Number of Wins")

plt.xticks(rotation=90)

plt.show()

# 3. Top 10 Batsmen

top_10_batsmen = (
    deliveries.groupby("batsman")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.barh(top_10_batsmen.index, top_10_batsmen.values)

plt.title("Top 10 Batsmen by Total Runs")
plt.xlabel("Total Runs")
plt.ylabel("Batsman")

plt.gca().invert_yaxis()

plt.show()

# 4. Top 10 Wicket Takers

top_10_wicket_takers = (
    wicket_deliveries.groupby("bowler")["player_dismissed"]
    .count()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_10_wicket_takers.index,
    top_10_wicket_takers.values
)

plt.title("Top 10 Wicket Takers")
plt.xlabel("Wickets")
plt.ylabel("Bowler")

plt.gca().invert_yaxis()

plt.show()

# 5. Player of the Match Awards

player_of_match = matches["player_of_match"].value_counts().head(10)

plt.figure(figsize=(10, 6))

plt.barh(player_of_match.index, player_of_match.values)

plt.title("Top 10 Players by Player of the Match Awards")
plt.xlabel("Number of Awards")
plt.ylabel("Player")

plt.gca().invert_yaxis()

plt.show()

# 6. Toss Decision Distribution

toss_decision = matches["toss_decision"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    toss_decision.values,
    labels=toss_decision.index,
    autopct="%1.1f%%"
)

plt.title("Toss Decision Distribution")

plt.show()

# 7. Toss Winner vs Match Winner

toss_match = matches.dropna(subset=["winner"])

toss_match["toss_won_match"] = (
    toss_match["toss_winner"] == toss_match["winner"]
)

result = toss_match["toss_won_match"].value_counts()

labels = ["Toss Winner Lost", "Toss Winner Won"]

plt.figure(figsize=(8, 5))

plt.bar(labels, result.values)

plt.title("Toss Winner vs Match Winner")
plt.xlabel("Result")
plt.ylabel("Number of Matches")

plt.show()

# 8. Season-wise Total Runs


deliveries = deliveries.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id",
    how="left"
)

season_runs = deliveries.groupby("season")["total_runs"].sum()

plt.figure(figsize=(10, 5))

plt.plot(season_runs.index, season_runs.values, marker="o")

plt.title("Season-wise Total Runs")
plt.xlabel("Season")
plt.ylabel("Total Runs")

plt.show()

# 9. Season-wise Wickets

wicket_deliveries = deliveries[
    deliveries["dismissal_kind"].isin(bowler_wicket_dismissals)
]

season_wickets = (
    wicket_deliveries.groupby("season")["player_dismissed"]
    .count()
)

plt.figure(figsize=(10, 5))

plt.plot(
    season_wickets.index,
    season_wickets.values,
    marker="o"
)

plt.title("Season-wise Wickets")
plt.xlabel("Season")
plt.ylabel("Total Wickets")

plt.show()

# 10. Distribution of Runs per Delivery

plt.figure(figsize=(10, 5))

plt.hist(deliveries["total_runs"], bins=8)

plt.title("Distribution of Runs per Delivery")
plt.xlabel("Runs per Delivery")
plt.ylabel("Number of Deliveries")

plt.show()

# 11. Team Average Runs Comparison

team_average_runs = (
    deliveries
    .groupby("batting_team")["total_runs"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

plt.bar(
    team_average_runs.index,
    team_average_runs.values
)

plt.title("Team Average Runs Comparison")
plt.xlabel("Team")
plt.ylabel("Average Runs per Innings")

plt.xticks(rotation=90)

plt.show()

# 12. Matches by Venue

venue_matches = matches["venue"].value_counts().head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    venue_matches.index,
    venue_matches.values
)

plt.title("Top 10 Venues by Number of Matches")
plt.xlabel("Number of Matches")
plt.ylabel("Venue")

plt.gca().invert_yaxis()

plt.show()

# 13. Runs vs Wickets

runs_wickets = (
    deliveries
    .groupby("match_id")
    .agg({
        "total_runs": "sum",
        "player_dismissed": "count"
    })
)

plt.figure(figsize=(10, 6))

plt.scatter(
    runs_wickets["total_runs"],
    runs_wickets["player_dismissed"]
)

plt.title("Runs vs Wickets")
plt.xlabel("Total Runs")
plt.ylabel("Wickets Lost")

plt.show()

# 14. Correlation Heatmap

correlation = deliveries[
    [
        "over",
        "ball",
        "batsman_runs",
        "extra_runs",
        "total_runs"
    ]
].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")

plt.savefig("IPL_Correlation_Heatmap.png", dpi=300, bbox_inches="tight")

plt.show()

# ========================================
# PREPARE FINAL CLEANED DATA FOR POWER BI
# ========================================

# Remove extra id column created during merge
deliveries = deliveries.drop(columns=["id"])

# Save cleaned files
matches.to_csv("IPL_Matches_Cleaned.csv", index=False)

deliveries.to_csv("IPL_Deliveries_Cleaned.csv", index=False)

print("Final cleaned files saved successfully!")
