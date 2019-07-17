import requests as req
import tile 
import json

def get_health_status(urls):

    for url in urls:
        status = tile.jenkins_running_check(url, 'SUCCESS')
        if not status:
            return False

    return True

def main():
    tileId = "health_checks_triggers"
    converter_color = {True : "#27ae60", False: "#c0392b"}

    healthJobs = {
        "POOLAREN-SUPERVISOR": ["http://eselnvlx2635.mo.sw.ericsson.se:8080/job/poolaren-supervisor/lastCompletedBuild/api/json?depth=0"],
        "LN LAB INSTRUMENTS HEALTH CHECK": [        
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_ECA_servers/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_ETA_servers/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_PDH_SDH_testers/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_PDUs/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_Serial_servers/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_ftp_tftp_servers/lastCompletedBuild/api/json?depth=0'
        ],
        "SLAVE TEST EXECUTOR CONFIGURATION (!!!)": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/aod_hourly/lastBuild/api/json?depth=0"],
        "LN 6609B BENCHES IN MAINTENANCE (!!!)": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/aod_hourly/lastBuild/api/json?depth=0"]
    }

    data = []
    config_data = []
    
    for title, urls in healthJobs.iteritems():
        healthStatus = get_health_status(urls)
        data.append({"label" : title})
        config_data.append({"label_color": converter_color[healthStatus], "center": True})

    json_data = json.dumps(data)
    tile.update_tile('fancy_listing_1', tileId, json_data)
    
    ready_config_data = {}
    for index, value in enumerate(config_data):
        ready_config_data[index+1] = value

    json_data_config = json.dumps(ready_config_data)
    tile.update_tile_config(tileId, json_data_config)
main()