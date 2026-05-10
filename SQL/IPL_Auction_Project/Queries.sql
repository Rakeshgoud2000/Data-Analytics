USE IPL_AUCTION_2026;

CREATE TABLE auction (
    SL_no int primary key ,
    Player_name varchar(100),
    Team varchar(50),
    Nationality varchar(50),
    Base_price int,
    Sold_price int,
    Capped_status varchar(50)
);

--importing data from csv file--
LOAD DATA LOCAL INFILE 'C:/Users/Lenovo/Downloads/IPL_Auction_2026_Sold_Player (1).csv'
INTO TABLE auction
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


SELECT COUNT(*) FROM auction;
--77--


SELECT * FROM auction;


SELECT player_name FROM auction;


SELECT SUM(Sold_price) AS Total_Spent FROM auction;
--2154500000--

SELECT COUNT(*) AS Total_Indian_players FROM auction
where Nationality = "Indian"; 
--48--

SELECT COUNT(Nationality) AS Total_Overseas_players FROM auction
where Nationality = "Overseas";
--29--

SELECT CONCAT(player_name, ' ', Sold_price) AS Most_expensive_player FROM auction
order BY Sold_price DESC
limit 1;
--Cameron Green 2522000000--

SELECT Team, COUNT(*) AS Total_Indian_players FROM auction
where Nationality = "Indian"
GROUP BY Team
ORDER BY Team DESC;


SELECT Team, COUNT(*) AS Total_Overseas_players FROM auction
where Nationality = "Overseas"
GROUP BY Team
ORDER BY Team DESC;

SELECT Team, COUNT(*) AS Total_Capped_Overseasplayers FROM auction
where Nationality = "Overseas" AND Capped_status = "Capped"
GROUP BY Team
ORDER BY Total_Capped_Overseasplayers DESC;

SELECT Team, COUNT(*) AS Total_Capped_Indianplayers FROM auction
where Nationality = "Indian" AND Capped_status = "Capped"
GROUP BY Team
ORDER BY Total_Capped_Indianplayers DESC;

--Most Uncapped Players Sold Team--
SELECT Team, SUM(Sold_price) AS Most_Spend_on_Uncapped_Players FROM auction
WHERE Capped_status = "Uncapped"
GROUP BY Team
ORDER BY Most_Spend_on_Uncapped_Players DESC
LIMIT 1;
--Chennai Super Kings   288000000--

--Least Uncapped Players Sold Team--
SELECT Team, SUM(Sold_price) AS Least_Spend_on_Uncapped_Players FROM auction
WHERE Capped_status = "Uncapped"
GROUP BY Team
ORDER BY Least_Spend_on_Uncapped_Players ASC
limit 1;
--Punjab Kings  6000000-

--Average Expenditure by Teams--
SELECT Team, Avg(Sold_price) AS Average_Expenditure FROM auction;
GROUP BY Team
ORDER BY   Average_Expenditure DESC;
