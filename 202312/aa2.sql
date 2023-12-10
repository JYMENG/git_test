DECLARE @sqlQuery NVARCHAR(MAX);

-- Assuming both tables have a common ID column named 'ID'

-- Generate dynamic SQL for Table1
SET @sqlQuery = 
    'SELECT ID, ' +
    STRING_AGG('' AS ' + QUOTENAME(ColumnName), ', ') +
    ' FROM Table1';

-- Append UNION ALL and dynamic SQL for Table2
SET @sqlQuery = @sqlQuery + 
    ' UNION ALL ' +
    'SELECT ID, ' +
    STRING_AGG('' AS ' + QUOTENAME(ColumnName), ', ') +
    ' FROM Table2';

-- Execute the dynamic SQL
EXEC sp_executesql @sqlQuery;
