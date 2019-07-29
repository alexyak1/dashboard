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
    converter_color = {True : "#0FC373", False: "#c0392b"}
    hyper_links = ['https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/slaveVerificationMultiJob/',
         'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se/view/ln_lab_instruments_health_check/', 
         'http://eselnvlx2635.mo.sw.ericsson.se:8080/view/Poolaren/job/poolaren-supervisor/',
         'https://tp-mwn-pt-webui.mo.sw.ericsson.se/ptvaadinui/benches?property=Maintenance&lab=LN_6609B'
    ] 
    health_jobs = {
        "POOLAREN-SUPERVISOR": ["http://eselnvlx2635.mo.sw.ericsson.se:8080/job/poolaren-supervisor/lastCompletedBuild/api/json?depth=0"],
        "LN LAB INSTRUMENTS HEALTH CHECK": [        
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_ECA_servers/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_ETA_servers/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_PDH_SDH_testers/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_PDUs/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_Serial_servers/lastCompletedBuild/api/json?depth=0',
            'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_ftp_tftp_servers/lastCompletedBuild/api/json?depth=0'],
        "SLAVE TEST EXECUTOR CONFIGURATION": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/slaveVerificationMultiJob/lastCompletedBuild/api/json?depth=0"]
    }

    tile_data = []
    tile_config_data = {}
    
    for index, (title, urls) in enumerate(health_jobs.iteritems()):
        health_status = get_health_status(urls)
        tile_data.append({"label" : title})
        tile_config_data[index+1] = {
            "label_color": converter_color[health_status], 
            "center": True,
            "urlForLink":hyper_links[index]
        }

    color, current, benches_with_jira = get_test_benches()
    tile_data.append({"label": "LN 6609B - BENCHES IN MAINTENANCE: " + str(current) + benches_with_jira})
    tile_config_data[len(tile_config_data)+1] = {
        "label_color": converter_color[color], 
        "center": True, 
        "urlForLink": hyper_links[3]
        }
    tile_data_json = json.dumps(tile_data)
    tile.update_tile('fancy_listing_1', tileId, tile_data_json)

    config_data_json = json.dumps(tile_config_data)
    tile.update_tile_config(tileId, config_data_json)

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

    curr = len(benchesInMaintenanceWithoutJira)
    if len(benchesInMaintenanceWithoutJira) == 0:
        is_green_tile = True    
    else:
        is_green_tile = False
    
    benches_with_jira = " benches with jira: " + str(len(benchesInMaintenanceWithJira))
    return is_green_tile, curr, benches_with_jira

            
if __name__ == "__main__":
    main()
