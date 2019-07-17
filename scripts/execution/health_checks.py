import requests as req
import tile 
import json
import update_health_check_list as updater


def main():
    tileId = "health_checks"
    converter = {True : "RUNNING", False: "DOWN"}
    converter_color = {True : "#27ae60", False: "#c0392b"}

    healthJobs = {
        "MLG66 REG1": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/ml66_hourly/lastBuild/api/json?depth=0"],
        "MLG66 REG2": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/ml66_reg2/lastBuild/api/json?depth=0"],
        "AOD HOURLY": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/aod_hourly/lastBuild/api/json?depth=0"]
    }

    data = []
    config_data = []
    
    for title, urls in healthJobs.iteritems():
        healthStatus = updater.get_health_status(urls)
        data.append({"label" : converter[healthStatus], "text": title})
        config_data.append({"label_color": converter_color[healthStatus], "center": True})

    json_data = json.dumps(data)
    tile.update_tile('fancy_listing', tileId, json_data)
    
    ready_config_data = {}
    for index, value in enumerate(config_data):
        ready_config_data[index+1] = value

    json_data_config = json.dumps(ready_config_data)
    tile.update_tile_config(tileId, json_data_config)
main()