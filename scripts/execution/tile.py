import requests as req
import json
from datetime import datetime
API_KEY = '755c3de7f9b94afdbc003349c2d4ba3a'
API_URL = 'http://localhost:7272/api/v0.1/{}'.format(API_KEY)
API_PUSH_URL = '/'.join((API_URL, 'push'))
API_TITLECONFIG_URL = '/'.join((API_URL, 'tileconfig'))

def advanced_chart_config(tileId, grid, param):
    url = 'https://mwn-maoni.seln.wh.rnd.internal.ericsson.com/test-run-matrix?'

    tile_config = {
        'seriesColors' : [ "#0FC373", "#FF3232 "],
        'stackSeries': True,
        'seriesDefaults': {
            'trendline': {
                'show': False 
            }, 
            'renderer': 'BarRenderer', 
            'pointLabels': {
                'show': False, 
                'edgeTolerance': -15
            }, 
            'shadowAngle': 135, 
            'rendererOptions': {
                'barDirection': 'vertical'
            }
        },
        'axesDefaults' : {
            'tickOptions': {
                'textColor': 'white',
                'fontSize': '2rem'
            }
        },
        'urlForLink': url + param,
        'grid': grid,
        'axes': {
            'xaxis': { 
                'renderer': 'CategoryAxisRenderer'
            },
            'yaxis': {
                'min': 0,
                'max': 100
            }
        }
    }
    data_json = json.dumps(tile_config)   
    update_tile_config(tileId, data_json)

def advanced_config_alert(tileId, param):
    grid = {
        'tileColor': '#c0392b',
        'background': '#39110c',
        'gridLineColor': '#25282D',
        'borderColor': '#25282D'
    }

    advanced_chart_config(tileId, grid, param)

def default_advanced_config(tileId, param):
    grid = {
        #'tileColor': '#25282D',
        'background': '#25282D',
        'gridLineColor': '#25282D',
        'borderColor': '#25282D'
    }

    advanced_chart_config(tileId, grid, param)

def line_config_green(tileId, param):
    grid = {
        'tileColor': '#0FC373',
        'background': '#092d1a',
        'gridLineColor': 'black',
    }

    line_config(tileId, grid, param)

def line_config_alert(tileId, param):
    grid = {
        'tileColor': '#FF3232 ',
        'background': '#FF3232 ',
        'gridLineColor': '#FF3232 ',
        'borderColor': 'red',
        'borderWidth': 4.0
    }

    line_config(tileId, grid, param)

def line_config_warning(tileId, param):
    grid = {
        'background': '#272700',
        'gridLineColor': 'black',
        'tileColor': '#7b7b00'
    }

    line_config(tileId, grid, param)


def line_config(tileId, grid, param):
    url = 'https://mwn-maoni.seln.wh.rnd.internal.ericsson.com/test-run-matrix?'

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
        },
        'urlForLink': url + param,
        'grid': grid,
        'axesDefaults' : {
            'tickOptions': {
                'showMark' : False,
                'textColor': 'white',
                'fontSize': '2rem'
            },
            'pad': 1.5,
            'showTicksMarks': True
        }
    }
    data_json = json.dumps(tile_config)
    update_tile_config(tileId, data_json)

def update_tile(tileName, tileId, content):

    params = {
        'tile': tileName, 
        'key': tileId, 
        'data': content
    }

    respons = req.post(API_PUSH_URL, data=params)
    if respons.status_code != 200:
        print(respons.status_code, respons.text)
    else:
        print(tileId + " updated")

def update_tile_config(tileId, value):       
    data_to_push = {
        'value': value
    }
    
    resp = req.post('/'.join((API_TITLECONFIG_URL, tileId)), data=data_to_push)
    if resp.status_code != 200:
        print(resp.status_code, resp.text)
    else:
        print(tileId + " config updated")

def health_check_color_config(health_check):

    value = {}
    if health_check:
        value["just-value-color"] = "#0FC373"
        value['fading_background'] = False
    else:
        value["just-value-color"] = "#c0392b"
        value['fading_background'] = True

    return json.dumps(value)

def bar_chart_fetch_data(url,include_finished=False):
    rawData = req.get(url)

    testCases = rawData.json()
    testCases.reverse()    

    extractedData = {
        "passed": [],
        "undone": [],
        "total": []
    }
    for testCase in testCases:
        if not testCase["finished"] and not include_finished:
            continue 
        extractedData["passed"].append(testCase["passed"])
        extractedData["undone"].append(testCase["total"] - testCase["passed"])
        extractedData["rstate"] = testCase["rstateStats"][0]["rstate"]
        extractedData["total"].append(testCase["total"])


    return extractedData

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
        
        date_object = datetime.strptime(testCase["beginTimestamp"], '%Y-%m-%dT%H:%M:%S.%fZ')
        date = date_object.strftime("%d/%m")
        extractedData["passed"] = testCase["passed"]
        extractedData["total"] = testCase["total"]
        extractedData["excluded"] = testCase["excluded"]
        extractedData["rstate"] = testCase["rstateStats"][0]["rstate"] 
        extractedData["series"].append([date, float(extractedData["passed"])/(extractedData["total"]-extractedData["excluded"])*100])
        extractedData["finished"] = testCase["finished"]
    
    return extractedData

def jenkins_running_check(url, resultParam = None):
    rawData = req.get(url)
    data = rawData.json()

    if data["result"] == resultParam:
        return True
    else:
        return False