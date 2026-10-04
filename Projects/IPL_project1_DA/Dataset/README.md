
Dataset Description
Explain that the project uses two datasets:
IPL Matches
- Match ID
- Season
- Date
- City
- Teams
- Toss information
- Winner
- Winning margins
- Player of Match
- Venue
IPL Deliveries
- Match ID
- Inning
- Batting team
- Bowling team
- Over
- Ball
- Batsman
- Bowler
- Runs
- Extras
- Total runs
- Dismissal information
Files
IPL_Matches_Cleaned.csv
IPL_Deliveries_Cleaned.csv

Data Cleaning
Mention the actual cleaning performed:
- Removed one duplicate delivery record
- Standardized Rising Pune Supergiants to Rising Pune Supergiant
- Converted match date to datetime
- Removed umpire3 because it contained no usable values
- Added season to delivery data for analysis
- Checked duplicate records and missing values
Your Python code performs these cleaning steps.   Pasted code
Important Missing Values
Explain that fields such as:
- player_dismissed
- dismissal_kind
- fielder
are naturally blank for most deliveries because not every delivery results in a dismissal.
Final Dataset Size
Matches: 636 rows
Deliveries: 150,459 rows

Usage
Explain that the cleaned CSVs are used as the input to Power BI.
