import requests as req
import tile 
import json
import health_check_updater as updater

def main():
    url = 'https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/aod_hourly/lastBuild/api/json?depth=0'
    tileId = 'health_check_aod'    
    title = 'AOD HOURLY'
    updater.update_tile(url, tileId, title)
    updater.multi_value_list('health_checks')
    

if __name__ == "__main__":
    main()