# business_analytics_project
Business Athletics Read me:

This Software conatains:
- Graphical User Interface (GUI)
    - Features:
        - Create Athletes
        - Create Training
        - Enter Training Data
        - Training Schedule

- Analysis via tables for training data of all athletes or a specific athlete (including: average training duration, median, standard deviation)
	- Features:
	   - Identify target group age of a specific training/ all trainings
	   - Gender distribution for all trainings/ specific training
	   - Barchart with number of athletes for each training and the age distribution

You can clone the Github with the following link:
https://github.com/timonc98/business_analytics_project.git

Notice for the correct working of the code:
Change the database connection with your database data for 
	dbname = "..." ,
      host = "..." , 
      port = ...,
      user = "...", 
      password = "..." 
Python: Line 62
R: Line 17-21

For executing the code install the packages below, if not installed.

Python package versions and installs:
tkinter    8.6
Python     3.10.4
asgiref    3.6.0
Babel      2.11.0
Django     4.1.5
django-db  0.0.7
Pillow     9.3.0
pip        22.0.4
psycopg2   2.9.5
PyMySQL    1.0.2
pytz       2022.7
setuptools 58.1.0
sqlparse   0.4.3
tkcalendar 1.6.1
tzdata     2022.7

R package versions and installs:
knitr		1.39      
ggplot2	3.3.6   
dplyr		1.0.8     
odbc		1.3.3      
RODBC		1.3-19    
DBI		1.1.3      
RPostgres	1.4.3
