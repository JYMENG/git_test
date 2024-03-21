SELECT
  b.c AS c_value
FROM
  xml_table,
  XMLTable('/a/b' PASSING xml_data
           COLUMNS c NUMBER PATH '@c') b;