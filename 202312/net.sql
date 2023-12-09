WITH RankedScores AS (
  SELECT
    ID,
    date,
    type,
    score,
    ROW_NUMBER() OVER (PARTITION BY ID, type ORDER BY date DESC) AS rn
  FROM YourTableName
)
SELECT
  ID,
  type,
  MAX(date) AS last_changed_date
FROM RankedScores
WHERE rn = 1
GROUP BY ID, type;
