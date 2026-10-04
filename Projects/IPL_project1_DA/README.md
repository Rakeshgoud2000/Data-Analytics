
IPL Data Analysis & Performance Dashboard
Project Overview
This project analyzes Indian Premier League (IPL) match and ball-by-ball data using Python and Power BI. The goal is to understand team performance, player performance, batting and bowling trends, toss outcomes, venue patterns, and season-wise scoring.
Dataset
The project uses two cleaned CSV files:
- IPL_Matches_Cleaned.csv – match-level information such as season, teams, toss, winner, venue, and Player of the Match.
- IPL_Deliveries_Cleaned.csv – ball-by-ball information such as batting team, bowling team, batsman, bowler, runs, extras, and dismissals.
Dataset size after cleaning
- Matches: 636 rows
- Deliveries: 150,459 rows
- Seasons covered: 2008–2017
- Standardized teams: 13
Data Cleaning
The Python workflow included:
- Loading the match and delivery CSV files with Pandas.
- Checking shape, data types, statistics, missing values, and duplicates.
- Removing one duplicate delivery record.
- Standardizing the team name Rising Pune Supergiants to Rising Pune Supergiant.
- Converting the match date column to datetime.
- Removing the empty umpire3 column from the match table.
- Rechecking duplicates, missing values, and team names after cleaning.
Missing values in delivery-level dismissal fields were retained where they represented balls on which no dismissal occurred.
Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Power BI
- DAX
- Excel/CSV files
Python Analysis
The Python analysis covered:
- Total matches and matches per season
- Team wins and toss wins
- Player of the Match awards
- Most played venues and cities
- Top batsmen by runs
- Top bowlers by bowler-credited wickets
- Highest individual scores
- Season-wise total runs
- Season-wise bowler wickets
- Team-wise average runs per innings
- Highest winning margins
- Average runs per match
- Toss winner vs match winner relationship
- Runs distribution
- Runs vs wickets
- Correlation analysis
Power BI Dashboard
The Power BI file contains three main pages:
1. IPL Performance Analytics Dashboard
Contains the main KPI cards and overview visuals:
- Total Matches
- Total Runs
- Total Wickets
- Total Teams
- Total Players
- Total Wins
- Average Runs
- Average Winning Margin
- Matches Played by Season
- Wins by Teams
- Top 10 Batsmen by Runs
- Top 10 Bowlers by Wickets
- Toss Winner Win Percentage card
2. IPL Detailed Analysis
Contains:
- Top 10 Player of the Match Awards
- Toss Decision Distribution
- Matches by Venue
- Season-wise Total Runs
- Season-wise Total Wickets
- Runs Distribution
- Team Average Runs
- Runs vs Wickets
- Correlation Heatmap
- Season, Team, and Venue slicers
3. IPL Report
Contains the project key insights and findings.
DAX Measures
The dashboard includes measures for:
- Total Matches
- Total Runs
- Total Wickets
- Total Teams
- Total Players
- Total Wins
- Average Runs
- Average Winning Margin
- Toss Winner Wins
- Toss Winner Win %
- Bowler Wickets
- Team Average Runs
- Wickets Lost
Key Results
- 636 matches were analyzed.
- 194,313 total runs were recorded.
- 6,673 bowler-credited wickets were counted using the selected dismissal types: caught, bowled, lbw, stumped, caught and bowled, and hit wicket.
- 13 teams and 495 unique players were identified using the dashboard's player definition.
- 2013 had the highest number of matches with 76 matches.
- 2013 also had the highest total runs with 22,602.
- 2013 had the highest season total of bowler-credited wickets with 831.
- Mumbai Indians recorded the highest number of wins in the analyzed data with 92 wins.
- SK Raina was the highest run scorer with 4,548 runs.
- SL Malinga led the bowler-credited wicket count with 154 wickets.
- CH Gayle had the most Player of the Match awards with 18.
- M Chinnaswamy Stadium was the most frequently used venue with 66 matches.
- The toss winner also won the match in 325 of 633 matches with a recorded winner, giving a rate of 51.34%.
- Average total scoring was approximately 305.52 runs per match.
Project Structure
IPL_project1_DA/
│
├── Dataset/
│   ├── IPL_Deliveries_Cleaned.csv
│   ├── IPL_Matches_Cleaned.csv
│   └── README.md
│
├── Python/
│   ├── IPL_Data_Analysis.py
│   └── README.md
│
├── PowerBI/
│   ├── IPL_Analytics_Dashboard.pbix
│   └── README.md
│
├── Report/
│   └── IPL_Project_Report.pdf
│
└── README.md
How to Use
1. Open the Python file to review the data loading, cleaning, analysis, and visualization workflow.
2. Open the cleaned CSV files for the final datasets used in Power BI.
3. Open IPL_Analytics_Dashboard.pbix in Power BI Desktop to explore the dashboard and slicers.
4. Open IPL_Project_Report.pdf for the complete project documentation and findings.
Conclusion
The project demonstrates a complete beginner-to-intermediate data analytics workflow: data loading, exploration, cleaning, analysis, visualization, DAX-based reporting, dashboard development, and insight generation. Python was used for data preparation and analytical exploration, while Power BI was used to build an interactive dashboard for business-style reporting.
