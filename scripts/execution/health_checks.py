import tile
import json


def get_health_status(urls):
    for url in urls:
        status = tile.jenkins_running_check(url)
        if not status:
            return False
    return True


def main():
    tileId = "health_checks"
    converter_color = {True: "#0FC373", False: "#c0392b"}

    health_jobs = {
        "ML66 REG1": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/ml66_hourly/lastBuild/api/json?depth=0"],
        "ML66 REG2": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/ml66_reg2/lastBuild/api/json?depth=0"],
        "AOD HOURLY": ["https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/aod_hourly/lastBuild/api/json?depth=0"]
    }

    tile_data = []
    tile_config_data = {}
    for index, (title, urls) in enumerate(health_jobs.iteritems()):
        health_status = get_health_status(urls)
        tile_data.append({"label": title})
        
        tile_config_data[index + 1] = {
            "label_color": converter_color[health_status],
            "center": True,
            "urlForLink": urls[0].replace('/lastBuild/api/json?depth=0', '')
        }

    tile_data_json = json.dumps(tile_data)
    tile.update_tile('fancy_listing_1', tileId, tile_data_json)

    config_data_json = json.dumps(tile_config_data)
    tile.update_tile_config(tileId, config_data_json)


if __name__ == "__main__":
    main()
