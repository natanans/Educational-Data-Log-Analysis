from sqlalchemy import create_engine
from sqlalchemy import create_engine
import pandas as pd    
import matplotlib.pyplot as plt






class db_con:
 def open_local_db(self,**kwargs):
       
    # Postgres username, password, and database name
    POSTGRES_ADDRESS = '127.0.0.1' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
    POSTGRES_PORT = '5432'
    POSTGRES_USERNAME = kwargs.get('POSTGRES_USERNAME') ## CHANGE THIS TO YOUR PANOPLY/POSTGRES USERNAME
    POSTGRES_PASSWORD =kwargs.get('POSTGRES_PASSWORD')## CHANGE THIS TO YOUR PANOPLY/POSTGRES PASSWORD
    POSTGRES_DBNAME = kwargs.get('POSTGRES_DBNAME') ## CHANGE THIS TO YOUR DATABASE NAME
    # A long string that contains the necessary Postgres login information
    postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(username=POSTGRES_USERNAME,password=POSTGRES_PASSWORD,ipaddress=POSTGRES_ADDRESS,port=POSTGRES_PORT,dbname=POSTGRES_DBNAME))
    # Create the connection
    cnx = create_engine(postgres_str)
    return cnx
