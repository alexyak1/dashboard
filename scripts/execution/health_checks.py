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
    converter_color = {True: "#27ae60", False: "#c0392b"}

    health_jobs = {
        "ML66 REG1": [
            "https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/ml66_hourly/lastBuild/api/json?depth=0"],
        "ML66 REG2": [
            "https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/ml66_reg2/lastBuild/api/json?depth=0"],
        "AOD HOURLY": [
            "https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/aod_hourly/lastBuild/api/json?depth=0"]
    }

    data = []
    config_data = {}
    for index, (title, urls) in enumerate(health_jobs.iteritems()):
        health_status = get_health_status(urls)
        data.append({"label": title})
        config_data[index + 1] = {"label_color": converter_color[health_status], "center": True}

    json_data = json.dumps(data)
    tile.update_tile('fancy_listing_1', tileId, json_data)

    json_data_config = json.dumps(config_data)
    tile.update_tile_config(tileId, json_data_config)


if __name__ == "__main__":
    main()
