Objective
Create an interactive dashboard to analyze IPL match, team, player, venue, batting, bowling, toss, and season performance.
Data Sources
IPL_Matches_Cleaned.csv
IPL_Deliveries_Cleaned.csv

Data Model
Explain the primary relationship:
IPL_Matches_Cleaned[id]
          1
          │
          *
IPL_Deliveries_Cleaned[match_id]

And for the Team slicer:
Teams
  1
  │
  *
MatchTeams
  *
  │
  1
IPL_Matches_Cleaned

DAX Measures
List the measures you created:
Total Matches
Total Runs
Total Wickets
Total Teams
Total Players
Total Wins
Average Runs
Average Winning Margin
Toss Winner Wins
Toss Winner Win %
Team Average Runs
Wickets Lost
Bowler Wickets

Dashboard Pages
Page 1 — IPL Performance Analytics Dashboard
- KPI cards
- Matches Played by Season
- Wins by Team
- Top 10 Batsmen
- Top 10 Bowlers
- Toss winner success
Page 2 — IPL Detailed Analysis
- Top 10 Player of the Match
- Toss Decision Distribution
- Season-wise Total Runs
- Season-wise Total Wickets
- Runs Distribution
- Team Average Runs
- Matches by Venue
- Runs vs Wickets
- Correlation Heatmap
Page 3 — IPL Report
- Key Insights
- Main findings from the analysis
Interactive Filters
Season
Team
Venue

Explain that these slicers allow users to interactively filter the dashboard.
Key Dashboard KPIs
Total Matches: 636
Total Runs: 194,313
Total Wickets: 6,673
Total Teams: 13
Total Players: 495
Average Runs: 305.52
Average Winning Margin: 17.14
