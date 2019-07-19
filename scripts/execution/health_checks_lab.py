import requests as req
import tile 
import json
import re

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
        "SLAVE TEST EXECUTOR CONFIGURATION (!!!)": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/aod_hourly/lastBuild/api/json?depth=0"]
    }

    data = []
    config_data = {}
    
    for index, (title, urls) in enumerate(healthJobs.iteritems()):
        healthStatus = get_health_status(urls)
        data.append({"label" : title})
        config_data[index+1] = {"label_color": converter_color[healthStatus], "center": True}

    color, current, benches_with_jira = get_test_benches()
    data.append({"label": "LN 6609B - BENCHES IN MAINTENANCE: " + str(current) + benches_with_jira})
    config_data[len(config_data)+1] = {"label_color": converter_color[color], "center": True}
    json_data = json.dumps(data)
    tile.update_tile('fancy_listing_1', tileId, json_data)

    json_data_config = json.dumps(config_data)
    tile.update_tile_config(tileId, json_data_config)

def get_test_benches():
    url = 'http://eselnvlx2918.mo.sw.ericsson.se:8090/rest/public/evaluate-expression'
    headers = {"content-type": "application/json"}
    data = {
        "expression": "bench.isInLab(\"" + "LN_6609B" + "\") && bench.isMaintenance()"
    }
    json_data = json.dumps(data)
    resp = req.post(url, data=json_data, headers=headers)
    body = resp.json()
    listOfBenchesInfo = body["matchedTestBenches"]
    

    benchesInMaintenanceWithJira = []
    benchesInMaintenanceWithoutJira = []

    for bench in listOfBenchesInfo:
        
        reg = re.search("NODECIEX-[0-9]+", bench["comment"], re.IGNORECASE)
        if reg:
            benchesInMaintenanceWithJira.append(bench['name'])
        else:
            benchesInMaintenanceWithoutJira.append(bench['name'])



    curr =len(benchesInMaintenanceWithoutJira)
    if len(benchesInMaintenanceWithoutJira) == 0:
        is_green_tile = True    
    else:
        is_green_tile = False


    benches_with_jira = " benches with jira: " + str(len(benchesInMaintenanceWithJira))
    return is_green_tile, curr, benches_with_jira

            
if __name__ == "__main__":
    main()
