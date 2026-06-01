import sqlite3

conn = sqlite3.connect(
    "database/gaming.db"
)

cursor = conn.cursor()

queries = [

# =====================================================
# PLAYER ANALYTICS
# =====================================================

(
"How many players exist?",
"SELECT COUNT(*) AS total_players FROM players;",
"player"
),

(
"How many VIP players exist?",
"SELECT COUNT(*) FROM players WHERE vip_status='Gold';",
"player"
),

(
"Average player level?",
"SELECT AVG(player_level) FROM players;",
"player"
),

(
"Highest player level?",
"SELECT MAX(player_level) FROM players;",
"player"
),

(
"Lowest player level?",
"SELECT MIN(player_level) FROM players;",
"player"
),

(
"Top 10 countries by player count?",
"""
SELECT country, COUNT(*) player_count
FROM players
GROUP BY country
ORDER BY player_count DESC
LIMIT 10;
""",
"player"
),

(
"Players registered this year?",
"""
SELECT COUNT(*)
FROM players
WHERE registration_date >= date('now','start of year');
""",
"player"
),

(
"Players registered this month?",
"""
SELECT COUNT(*)
FROM players
WHERE registration_date >= date('now','start of month');
""",
"player"
),

# =====================================================
# SESSION ANALYTICS
# =====================================================

(
"Total gaming sessions?",
"SELECT COUNT(*) FROM sessions;",
"session"
),

(
"Average session duration?",
"SELECT AVG(hours_played) FROM sessions;",
"session"
),

(
"Maximum session duration?",
"SELECT MAX(hours_played) FROM sessions;",
"session"
),

(
"Minimum session duration?",
"SELECT MIN(hours_played) FROM sessions;",
"session"
),

(
"Total hours played?",
"SELECT SUM(hours_played) FROM sessions;",
"session"
),

(
"Most active player by playtime?",
"""
SELECT player_id,
SUM(hours_played) total_hours
FROM sessions
GROUP BY player_id
ORDER BY total_hours DESC
LIMIT 1;
""",
"session"
),

(
"Top 10 players by playtime?",
"""
SELECT player_id,
SUM(hours_played) total_hours
FROM sessions
GROUP BY player_id
ORDER BY total_hours DESC
LIMIT 10;
""",
"session"
),

(
"Daily active users?",
"""
SELECT DATE(login_time),
COUNT(DISTINCT player_id)
FROM sessions
GROUP BY DATE(login_time)
ORDER BY DATE(login_time) DESC;
""",
"session"
),

(
"Average sessions per player?",
"""
SELECT COUNT(*) * 1.0 /
COUNT(DISTINCT player_id)
FROM sessions;
""",
"session"
),

(
"Players with more than 100 hours playtime?",
"""
SELECT player_id,
SUM(hours_played) total_hours
FROM sessions
GROUP BY player_id
HAVING total_hours > 100;
""",
"session"
),

# =====================================================
# REVENUE ANALYTICS
# =====================================================

(
"Total revenue generated?",
"SELECT SUM(amount) FROM transactions;",
"revenue"
),

(
"Average transaction amount?",
"SELECT AVG(amount) FROM transactions;",
"revenue"
),

(
"Highest transaction amount?",
"SELECT MAX(amount) FROM transactions;",
"revenue"
),

(
"Lowest transaction amount?",
"SELECT MIN(amount) FROM transactions;",
"revenue"
),

(
"Revenue generated this year?",
"""
SELECT SUM(amount)
FROM transactions
WHERE txn_date >= date('now','start of year');
""",
"revenue"
),

(
"Revenue generated this month?",
"""
SELECT SUM(amount)
FROM transactions
WHERE txn_date >= date('now','start of month');
""",
"revenue"
),

(
"Top spending player?",
"""
SELECT player_id,
SUM(amount) total_spend
FROM transactions
GROUP BY player_id
ORDER BY total_spend DESC
LIMIT 1;
""",
"revenue"
),

(
"Top 10 spending players?",
"""
SELECT player_id,
SUM(amount) total_spend
FROM transactions
GROUP BY player_id
ORDER BY total_spend DESC
LIMIT 10;
""",
"revenue"
),

(
"Revenue by game?",
"""
SELECT game_id,
SUM(amount) revenue
FROM transactions
GROUP BY game_id
ORDER BY revenue DESC;
""",
"revenue"
),

(
"Average spend per player?",
"""
SELECT player_id,
AVG(amount)
FROM transactions
GROUP BY player_id;
""",
"revenue"
),

# =====================================================
# GAME ANALYTICS
# =====================================================

(
"Total number of games?",
"SELECT COUNT(*) FROM games;",
"game"
),

(
"Most played game?",
"""
SELECT game_id,
COUNT(*) session_count
FROM sessions
GROUP BY game_id
ORDER BY session_count DESC
LIMIT 1;
""",
"game"
),

(
"Top 10 most played games?",
"""
SELECT game_id,
COUNT(*) session_count
FROM sessions
GROUP BY game_id
ORDER BY session_count DESC
LIMIT 10;
""",
"game"
),

(
"Game with highest revenue?",
"""
SELECT game_id,
SUM(amount) revenue
FROM transactions
GROUP BY game_id
ORDER BY revenue DESC
LIMIT 1;
""",
"game"
),

(
"Average playtime by game?",
"""
SELECT game_id,
AVG(hours_played)
FROM sessions
GROUP BY game_id;
""",
"game"
),

(
"Revenue per game?",
"""
SELECT game_id,
SUM(amount)
FROM transactions
GROUP BY game_id;
""",
"game"
),

(
"Games released after 2019?",
"""
SELECT *
FROM games
WHERE release_year > 2019;
""",
"game"
),

# =====================================================
# ACHIEVEMENT ANALYTICS
# =====================================================

(
"Total achievements unlocked?",
"""
SELECT COUNT(*)
FROM achievements;
""",
"achievement"
),

(
"Most common achievement?",
"""
SELECT achievement_name,
COUNT(*) achievement_count
FROM achievements
GROUP BY achievement_name
ORDER BY achievement_count DESC
LIMIT 1;
""",
"achievement"
),

(
"Top 10 achievements?",
"""
SELECT achievement_name,
COUNT(*) achievement_count
FROM achievements
GROUP BY achievement_name
ORDER BY achievement_count DESC
LIMIT 10;
""",
"achievement"
),

(
"Player with most achievements?",
"""
SELECT player_id,
COUNT(*) total_achievements
FROM achievements
GROUP BY player_id
ORDER BY total_achievements DESC
LIMIT 1;
""",
"achievement"
),

(
"Top 10 players by achievements?",
"""
SELECT player_id,
COUNT(*) total_achievements
FROM achievements
GROUP BY player_id
ORDER BY total_achievements DESC
LIMIT 10;
""",
"achievement"
),

(
"Achievements earned this month?",
"""
SELECT COUNT(*)
FROM achievements
WHERE achievement_date >= date('now','start of month');
""",
"achievement"
),

(
"Achievements earned this year?",
"""
SELECT COUNT(*)
FROM achievements
WHERE achievement_date >= date('now','start of year');
""",
"achievement"
),

# =====================================================
# CROSS DOMAIN ANALYTICS
# =====================================================

(
"Top player by revenue and playtime?",
"""
SELECT
t.player_id,
SUM(t.amount) revenue,
SUM(s.hours_played) hours
FROM transactions t
JOIN sessions s
ON t.player_id=s.player_id
GROUP BY t.player_id
ORDER BY revenue DESC
LIMIT 1;
""",
"cross_domain"
),

(
"Revenue generated by VIP players?",
"""
SELECT SUM(t.amount)
FROM transactions t
JOIN players p
ON t.player_id=p.player_id
WHERE p.vip_status='Gold';
""",
"cross_domain"
),

(
"Average playtime of VIP players?",
"""
SELECT AVG(s.hours_played)
FROM sessions s
JOIN players p
ON s.player_id=p.player_id
WHERE p.vip_status='Gold';
""",
"cross_domain"
),

(
"Top country by revenue?",
"""
SELECT p.country,
SUM(t.amount) revenue
FROM players p
JOIN transactions t
ON p.player_id=t.player_id
GROUP BY p.country
ORDER BY revenue DESC
LIMIT 1;
""",
"cross_domain"
),

(
"Top country by playtime?",
"""
SELECT p.country,
SUM(s.hours_played) hours
FROM players p
JOIN sessions s
ON p.player_id=s.player_id
GROUP BY p.country
ORDER BY hours DESC
LIMIT 1;
""",
"cross_domain"
),

(
"Average revenue per player?",
"""
SELECT SUM(amount)*1.0/
COUNT(DISTINCT player_id)
FROM transactions;
""",
"cross_domain"
),

(
"Players who spent more than 10000?",
"""
SELECT player_id,
SUM(amount) total_spend
FROM transactions
GROUP BY player_id
HAVING total_spend > 10000;
""",
"cross_domain"
)

]

cursor.executemany("""
INSERT INTO query_repository(
    question,
    sql_query,
    category
)
VALUES (?, ?, ?)
""", queries)

conn.commit()
conn.close()