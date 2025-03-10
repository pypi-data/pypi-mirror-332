This script was created to import data from excel sheets in a workbook into multiple tables that have been created in a postgresql database.


- The part that states `postgres` should be `your database username`. (it mostly is `postgres` as most people don't change that).
- The part that states `password` should be `your database password`.
- The default `localhost_no` is your PostgreSQL port number which is usually `5432`. This isn't the default, so please confirm yours from postgresql.
- The part that states `database_name` should be the `name of your database` with the empty tables.
- Input `your file path` where it states `excelfile_path`. Also, please make sure to save your Excel workbook as an Excel file and not csv.
- The `if_exists='replace'` parameter is the default and will replace the table if it already exists. You can change it to `‘append'` if you want to add data to an existing table.