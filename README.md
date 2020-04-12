# CSV exporter from sqlite db
 A Python package for exporting sqlite.db to set of csv files.
* Install the package
    ```
    pip install sqlite3
    pip install pandas
    pip install git+https://github.com/kaskou/Sqllite_to_CSV.git
    ```

* It has two methods , `alltables` - which exports all the table to csv files by taking dbname and `singletable`- which takes the dbname and tablename for generating specific .csv file.
* Sample code for exporting csv files
```
from sqlitetocsv.sqlitetocsv import *
dbname = "ENTER your local db name"
value=exporttoCSV(dbname)
value.alltables()
```
