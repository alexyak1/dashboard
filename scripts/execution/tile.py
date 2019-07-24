import requests as req
import json
API_KEY = '755c3de7f9b94afdbc003349c2d4ba3a'
API_URL = 'http://localhost:7272/api/v0.1/{}'.format(API_KEY)
API_PUSH_URL = '/'.join((API_URL, 'push'))
API_TITLECONFIG_URL = '/'.join((API_URL, 'tileconfig'))

def default_advanced_config(tileId):
    tile_config = {
        'seriesColors' : [ "rgba(39,174,96,1)", "rgba(192,57,43,1)"],
        'stackSeries': True,
        'seriesDefaults': {
            'trendline': {
                'show': False 
            }, 
            'renderer': 'BarRenderer', 
            'pointLabels': {
                'show': True, 
                'edgeTolerance': -15
            }, 
            'shadowAngle': 135, 
            'rendererOptions': {
                'barDirection': 'vertical'
            }
        }, 
        'grid': {
            'gridLineColor' : '#25282D',
            'background' : '#25282D',
            'borderColor' : '#25282D'
        },
        'axes': {
            'xaxis': { 
                'renderer': 'CategoryAxisRenderer'
            }
        }
    }
    data_json = json.dumps(tile_config)   
    update_tile_config(tileId, data_json)

def line_config_green(tileId):
    grid = {
        'tileColor': '#27ae60',
        'background': '#092d1a',
        'gridLineColor': 'black',
    }

    line_config(tileId, grid)

def line_config_alert(tileId):
    grid = {
        'tileColor': 'rgba(192,57,43,0.3)',
        'background': 'rgba(192,57,43,0.3)',
        'gridLineColor': 'rgba(192,57,43,0.3)',
        'borderColor': 'red',
        'borderWidth': 4.0
    }

    line_config(tileId, grid)

def line_config_warning(tileId):
    grid = {
        'background': '#272700',
        'gridLineColor': 'black',
        'tileColor': '#7b7b00'
    }

    line_config(tileId, grid)


def line_config(tileId, grid):
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

        'grid': grid,
        'axesDefaults' : {
            'tickOptions': {
                'showMark' : False
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
        value["just-value-color"] = "#27ae60"
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
    }
    for index, testCase in enumerate((testCases)):
        if not testCase["finished"] and not include_finished:
            continue 
        extractedData["passed"].append([index+1, testCase["passed"]])
        extractedData["undone"].append([index+1, testCase["total"] - testCase["passed"]])
        extractedData["rstate"] = testCase["rstateStats"][0]["rstate"] 

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
        extractedData["passed"] = testCase["passed"]
        extractedData["total"] = testCase["total"]
        extractedData["excluded"] = testCase["excluded"]
        extractedData["rstate"] = testCase["rstateStats"][0]["rstate"] 
        extractedData["series"].append([index, float(extractedData["passed"])/(extractedData["total"]-extractedData["excluded"])*100])
        extractedData["finished"] = testCase["finished"]
    
    return extractedData

def jenkins_running_check(url, resultParam = None):
    rawData = req.get(url)
    data = rawData.json()

    if data["result"] == resultParam:
        return True
    else:
        return False