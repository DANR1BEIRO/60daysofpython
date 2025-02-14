from datetime import datetime
import pytz


def displays_current_date_hour(): 
    
    fuso = pytz.timezone("america/Sao_Paulo")
    date_hour = datetime.now(fuso)
    date_format = date_hour.strftime("%d/%m/%Y %H:%M:%S")
    
    print(f"Current date and hour: {date_format}")

if __name__=="__main__":
    displays_current_date_hour()
