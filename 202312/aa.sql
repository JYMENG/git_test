-- Declare variables
DECLARE @tableName NVARCHAR(128)
DECLARE @sqlQuery NVARCHAR(MAX)
DECLARE @counter INT = 0

-- Initialize the query
SET @sqlQuery = ''

-- Loop through tables and build dynamic SQL
WHILE @counter <= 99
BEGIN
    -- Generate the table name
    SET @tableName = 'YourTableNamePrefix_' + RIGHT('00' + CAST(@counter AS NVARCHAR(2)), 2)

    -- Build dynamic SQL to union tables
    SET @sqlQuery = @sqlQuery + 'SELECT * FROM ' + QUOTENAME(@tableName) + ' UNION ALL '

    SET @counter = @counter + 1
END

-- Remove the trailing 'UNION ALL'
SET @sqlQuery = LEFT(@sqlQuery, LEN(@sqlQuery) - LEN('UNION ALL'))

-- Execute the dynamic SQL
EXEC sp_executesql @sqlQuery
