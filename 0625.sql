
-- method 1

-- Create a new table with three columns
CREATE TABLE SplitValues (
    ID INT,
    Enumerator INT,
    Value VARCHAR(50)
);

-- Insert sample data into the original table
INSERT INTO OriginalTable (Column1, Column2)
VALUES (1, 'a, b, c'),
       (2, 'a, b, c, d, e');

-- Split and insert the values into the new table
WITH SplitRows AS (
    SELECT
        Column1 AS ID,
        CAST('<S>' + REPLACE(Column2, ',', '</S><S>') + '</S>' AS XML) AS Data
    FROM OriginalTable
)
INSERT INTO SplitValues (ID, Enumerator, Value)
SELECT
    ID,
    ROW_NUMBER() OVER (PARTITION BY ID ORDER BY (SELECT NULL)) AS Enumerator,
    LTRIM(RTRIM(Split.a.value('.', 'VARCHAR(50)'))) AS Value
FROM SplitRows
CROSS APPLY Data.nodes('/S') AS Split(a);

-- Select data from the split table
SELECT * FROM SplitValues;


-- method 2

-- Create a new table with three columns
CREATE TABLE SplitValues (
    ID INT,
    Enumerator INT,
    Value VARCHAR(50)
);

-- Insert sample data into the original table
INSERT INTO OriginalTable (Column1, Column2)
VALUES (1, 'a, b, c'),
       (2, 'a, b, c, d, e');

-- Split and insert the values into the new table
WITH SplitRows AS (
    SELECT
        Column1 AS ID,
        Column2,
        CHARINDEX(',', Column2) AS CommaIndex
    FROM OriginalTable
)
INSERT INTO SplitValues (ID, Enumerator, Value)
SELECT
    ID,
    ROW_NUMBER() OVER (PARTITION BY ID ORDER BY (SELECT NULL)) AS Enumerator,
    CASE
        WHEN CommaIndex > 0 THEN LTRIM(RTRIM(SUBSTRING(Column2, 1, CommaIndex - 1)))
        ELSE LTRIM(RTRIM(Column2))
    END AS Value
FROM SplitRows
CROSS APPLY (VALUES (Column2, CommaIndex)) AS X(Column2, CommaIndex)
WHERE LEN(Column2) > 0
UNION ALL
SELECT
    ID,
    ROW_NUMBER() OVER (PARTITION BY ID ORDER BY (SELECT NULL)) AS Enumerator,
    LTRIM(RTRIM(SUBSTRING(Column2, CommaIndex + 1, LEN(Column2) - CommaIndex)))
FROM SplitRows
CROSS APPLY (VALUES (Column2, CommaIndex)) AS X(Column2, CommaIndex)
WHERE CommaIndex > 0;

-- Select data from the split table
SELECT * FROM SplitValues;


-- method 3:

-- Create the original table
CREATE TABLE YourTable (
    id INT,
    OriginalValue VARCHAR(100)
);

-- Insert sample data into the original table
INSERT INTO YourTable (id, OriginalValue)
VALUES (1, 'a, b, c, d'), (2, '1, 2, 3, 4');

-- Create the new table for storing the split values
CREATE TABLE SplitTable (
    id INT,
    Column1 VARCHAR(100),
    Column2 VARCHAR(100)
);

-- Split the values into two columns based on even occurrences and insert into the new table
DECLARE @Delimiter CHAR(1) = ',';

WITH CTE AS (
    SELECT 
        id,
        OriginalValue,
        LTRIM(RTRIM(SUBSTRING(',' + OriginalValue, (N - 1) * CHARINDEX(@Delimiter, ',' + OriginalValue, N * 2) + 1, CHARINDEX(@Delimiter, ',' + OriginalValue, N * 2) - (N - 1) * CHARINDEX(@Delimiter, ',' + OriginalValue, N * 2) - 1))) AS SplitValue,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY N) AS RowNumber
    FROM YourTable
    CROSS JOIN (VALUES (1), (2)) AS Numbers(N)
)
INSERT INTO SplitTable (id, Column1, Column2)
SELECT 
    id,
    MAX(CASE WHEN RowNumber = 1 THEN SplitValue END) AS Column1,
    MAX(CASE WHEN RowNumber = 2 THEN SplitValue END) AS Column2
FROM CTE
GROUP BY id, OriginalValue;

-- Select the data from the new table
SELECT * FROM SplitTable;