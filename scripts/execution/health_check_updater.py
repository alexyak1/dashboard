import tile
import json

def update_tile(url, tileId, title):
    running = tile.jenkins_running_check(url)

    health_status = "DOWN"
    if running:
        health_status = "RUNNING"

    send_tile_data(title, tileId, health_status, running)

def update_tile_multiple_url(urls, tileId, title):

    health_status = "RUNNING"
    for url in urls:
        running = tile.jenkins_running_check(url, "SUCCESS")
        if not running:
            health_status = "DOWN"
            break

    send_tile_data(title, tileId, health_status, running)

def send_tile_data(title, tileId, health_status, running):
    data = {
        "title": title,
        "description": '',
        "just-value": health_status
    }
    
    json_data = json.dumps(data)
    tile.update_tile('just_value',tileId, json_data)

    conigurationData = tile.health_check_color_config(running)
    tile.update_tile_config(tileId, conigurationData)
