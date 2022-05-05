from datetime import datetime

def today():
    today = datetime.now()
    return today

def verify_date(date):
    try:
        date_format = datetime.strptime(date, "%d-%m-%Y")
        return date_format
    except:
        raise Exception ("Verifique o formato, Ex.: 00-00-0000")

def verify_due(date_refer):
    due_date = verify_date(date=date_refer)
    if today() > due_date:
        return "Expirado...."
    else:
        return "Válido"