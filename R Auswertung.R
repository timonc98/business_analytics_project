install.packages(c('RPostgres',"DBI","RODBC","odbc","dplyr","dbplyr"))

library (RPostgres)
library (DBI)
library (RODBC)
library (odbc)
library (dplyr)
library (dbplyr)

con1 <- dbConnect (RPostgres::Postgres(),
                     dbname = "postgres" ,
                     host = "127.0.0.1" , 
                     port = 5432,
                     user = "postgres", 
                     password = "timon1998" 
)
con1


ahlete_df <- dbGetQuery(con1, "SELECT * FROM athlete")
ahlete_df