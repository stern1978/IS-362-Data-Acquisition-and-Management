import pandas as pd
import sqlite3
import sqlalchemy as sqla


sql = '''SELECT c.LastName, c.FirstName, t.Name, a.Title
         FROM Customer as c
         LEFT JOIN Invoice as i
         ON c.CustomerId = i.CustomerId
         LEFT JOIN InvoiceLine as il
         ON i.InvoiceId = il.InvoiceId
         LEFT JOIN Track as t
         ON il.TrackId = t.TrackId
         LEFT JOIN Album as a
         ON t.AlbumId = a.AlbumId
         ORDER BY c.LastName, c.FirstName'''

con = sqlite3.connect('Chinook_Sqlite.sqlite')
db = pd.read_sql_query(sql, con=con)
con.close()

print(db)
