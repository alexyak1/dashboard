import tile
import json

def update_tile(url, tileId, title):
    running = tile.jenkins_running_check(url)

    healthStatus = "DOWN"
    if running:
        healthStatus = "RUNNING"

    send_tile_data(title, tileId, healthStatus, running)

def update_tile_multiple_url(urls, tileId, title):

    healthStatus = "RUNNING"
    for url in urls:
        running = tile.jenkins_running_check(url, "SUCCESS")
        if not running:
            healthStatus = "DOWN"
            break

    send_tile_data(title, tileId, healthStatus, running)

def send_tile_data(title, tileId, healthStatus, running):
    data = {
        "title": title,
        "description": '',
        "just-value": healthStatus 
    }
    
    json_data = json.dumps(data)
    tile.update_tile('just_value',tileId, json_data)

    conigurationData = tile.health_check_color_config(running)
    tile.update_tile_config(tileId, conigurationData)
