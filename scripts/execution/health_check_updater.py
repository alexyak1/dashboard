import requests as req
import tile 
import json


def update_tile(url, tileId, title):
    running = tile.jenkins_running_check(url)

    health_status = "DOWN"
    if running:
        health_status = "RUNNING"
    
    data = {
        "title": title,
        "description": '',
        "just-value": health_status 
    }
    
    json_data = json.dumps(data)
    tile.update_tile('just_value',tileId, json_data)

    coniguration_data = tile.health_check_color_config(running)
    tile.update_tile_config(tileId, coniguration_data)