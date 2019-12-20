from django.contrib.sites import requests
from bin.models import stat_count
import datetime

def _get_dustbin_json():
    url = 'http://127.0.0.1:8080/update_status/'
    
  
    r = requests.get(url)

    try:
        r.raise_for_status()
        return r.json()
    except:
        return None

      
def update_dusbin_stat():
    json = _get_dustbin_json()
    if json is not None:
        try:
            new_status = stat_count()
            
            # open weather map gives temps in Kelvin. We want celsius.              
            

            new_status.full_bin = json['full']
            new_status.half_bin = json['half']
            new_status.empty_bin = json['empty']
            new_status.date_time = datetime.datetime.now()
            new_status.save()
            print("saving...\n" + new_status)
        except:
            pass