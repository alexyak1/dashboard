import requests as req
import json
API_KEY = '755c3de7f9b94afdbc003349c2d4ba3a'
API_URL = 'http://localhost:7272/api/v0.1/{}'.format(API_KEY)
API_PUSH_URL = '/'.join((API_URL, 'push'))
API_TITLECONFIG_URL = '/'.join((API_URL, 'tileconfig'))

def default_line_config(tileId):
    tile_config = {
        'seriesDefaults': {
            'trendline': {
                'show': True,
                'color': '#ffffff',
                'lineWidth': 0.9
            },
            'rendererOptions':{
                'smooth': True
            }
        }
    }       
    data_json = json.dumps(tile_config)   
    update_tile_config(tileId, data_json)

def update_tile(tileName, tileId, content):
    API_TITLECONFIG_URL = '/'.join((API_URL, 'tileconfig'))
    params = {
        'tile': tileName, 
        'key': tileId, 
        'data': content
    }

    respons = req.post(API_PUSH_URL, data=params)
    if respons.status_code != 200:
        print(respons.status_code, respons.text)

def update_tile_config(tileId, value):       
    data_to_push = {
        'value': value
    }
    print(tileId, data_to_push)
    resp = req.post('/'.join((API_TITLECONFIG_URL, tileId)), data=data_to_push)
    if resp.status_code != 200:
        print(resp.status_code, resp.text)

def percentage_chart_color_config(success_rate):

    value = {}
    if int(success_rate) > 98:
        value['big_value_color'] = '#27ae60'
        value['fading_background'] = False
    elif int(success_rate) <= 98:
        value['big_value_color'] = '#c0392b'
        value['fading_background'] = True

    color_value_json = json.dumps(value)
    return color_value_json

def health_check_color_config(health_check):

    value = {}
    if health_check:
        value["just-value-color"] = "#27ae60"
        value['fading_background'] = False
    else:
        value["just-value-color"] = "#c0392b"
        value['fading_background'] = True

    return json.dumps(value)


def line_chart_fetch_data(url, include_finished=True):
    rawData = req.get(url)

    testCases = rawData.json()
    testCases.reverse()    

    extractedData = {
        "series": [] 
    }
    
    for index, testCase in enumerate((testCases)):
        if not testCase["finished"] and not include_finished:
            continue 
        extractedData["passed"] = testCase["passed"]
        extractedData["total"] = testCase["total"]
        extractedData["excluded"] = testCase["excluded"]
        extractedData["rstate"] = testCase["rstateStats"][0]["rstate"] 
        extractedData["series"].append([index, float(extractedData["passed"])/(extractedData["total"]-extractedData["excluded"])*100])
        extractedData["finished"] = testCase["finished"]
    
    return extractedData

def jenkins_running_check(url):
    rawData = req.get(url)

    data = rawData.json()

    if data["result"] == None:
        return True
    else:
        return False