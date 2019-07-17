import requests as req
import tile 
import json

def get_health_status(urls):

    for url in urls:
        status = tile.jenkins_running_check(url)
        if not status:
            return False

    return True


def multi_value_list_color_config(tileId):
    value = {
        "vertical_center": True,
        "1": {"label_color": "#27ae60", "center": True},
        "2": {"label_color": "#27ae60", "center": True},
        "3": {"label_color": "#27ae60", "center": True},
        "4": {"label_color": "#27ae60", "center": True},
        "5": {"label_color": "#27ae60", "center": True},
        "6": {"label_color": "#27ae60", "center": True},
        "7": {"label_color": "#27ae60", "center": True}
    }
    conigurationData = json.dumps(value)
    tile.update_tile_config(tileId, conigurationData)