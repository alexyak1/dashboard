#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests as req
import json
import random
import time


API_KEY = '755c3de7f9b94afdbc003349c2d4ba3a'
API_URL = 'http://localhost:7272/api/v0.1/{}'.format(API_KEY)
API_PUSH_URL = '/'.join((API_URL, 'push'))
API_TITLECONFIG_URL = '/'.join((API_URL, 'tileconfig'))
done = {
    True : 'Finished',
    False : 'Ongoing'
} 
def update_tile_config(tileId, value):       
    data_to_push = {
        'value': value
    }
    print(tileId, data_to_push)
    resp = req.post('/'.join((API_TITLECONFIG_URL, tileId)), data=data_to_push)
    if resp.status_code != 200:
        print(resp.status_code, resp.text)

def update_tile(tileName, tileId, content):
    param = {
        'tile': tileName, 
        'key': tileId, 
        'data': content
    }

    resp = req.post(API_PUSH_URL, data=param)
    if resp.status_code != 200:
        print(resp.status_code, resp.text)

 
def conf_line_chart(tileId):
    tile_config = {
        'axesDefaults': {
            'show': False,
            #'min': 0,
            #'max': 100,
        },
        'axes': {
            'y2axis': {
                #'ticks':[0,25,50,75,100] 
            } 
        },

        'seriesDefaults': {
            'label': 'Test',
            'yaxis': 'y2axis',
            'lineWidth': 2,
            'trendline': {
                'show': False
            },
            'rendererOptions':{
                'smooth': True
            },
            'markerOptions': {
                'show': True,
                'style': 'filledCircle',
                'size': 5
            }  
        },
        'legend': {
            'show': False,
            'location': 'sw'
        },
        'grid': {
            'drawGridLines': False,
        }
    }      
    data_json = json.dumps(tile_config)   
    update_tile_config(tileId, data_json)

def ML66_REG1_line_chart(tileId, url):
    response = req.get(url)
    series = []
    passed = None
    total = None
    finished = None
    exluded = None
    for item in reversed(response.json()):
        passed = item["passed"]
        total = item["total"]
        exluded = item["excluded"]
        finished = done[item["finished"]]
        series.append(passed*1.0/(total-exluded)*100)
    
    success_rate = round(series[len(series)-1], 2)
    content = {
        'subtitle': str(success_rate) + '%',
        'description': finished + ' ' + str(passed) + '/' + str(total-exluded),
        'series_list': [[list((i+1, int(series[i]))) for i in range(len(series))]]}
    data_json = json.dumps(content) 
    update_tile('line_chart', tileId, data_json)
    simple_perc_chart(tileId, success_rate, finished)

def simple_perc_chart(tileId, success_rate, finished):
    color_value(tileId+'_1', success_rate)
    content = {
        'title': finished,
        'subtitle': '',
        'big_value': str(success_rate) + '%',
        'left_value': '',
        'right_value': '',
        'left_label': '',
        'right_label': ''
    }
    data_json = json.dumps(content)
    update_tile('simple_percentage', tileId+'_1', data_json)

def create_cumulative_flow_data():
    tileName = 'cumulative_flow'
    tileId = 'id_4'
    data ={
        'title': "Test",
        'series_list' :[] 
    } 
    for i in range(0,5):
        series = random.sample(xrange(0,11), 10)

        label = {'label' : 'Label ' + str(i), 'series': series}
        data["series_list"].append(label)
    print(data) 
    data_json = json.dumps(data)
    update_tile(tileName, tileId, data_json)

def color_value(tileId, data):
    print(data)
    value = {
        'big_value_color': ''
    }
    if int(data) > 98:
        value['big_value_color'] = '#27ae60'
        value['fading_background'] = False
    elif int(data) <= 98:
        value['big_value_color'] = '#c0392b'
        value['fading_background'] = True

    color_value_json = json.dumps(value)
    update_tile_config(tileId, color_value_json)



def main():
    
    #create_cumulative_flow_data()
    
    urls = { 
        'id_1': 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com/aggregated-summary?ciOfficial=true&program=ML66&createdTimestamp=-3&testLoopType=REG1&aggregated=&column=testLoop&column2=rstate&row=hardware',
        'id_2': 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com/aggregated-summary?ciOfficial=true&program=ML66&createdTimestamp=-3&testLoopType=REG2&aggregated=&column=testLoop&column2=rstate&row=hardware',
        'id_3': 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com/aggregated-summary?ciOfficial=true&program=AOD&createdTimestamp=-3&testLoopType=HOURLY&aggregated=&column=testLoop&column2=rstate&row=hardware',
        'id_5': 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com/aggregated-summary?ciOfficial=true&program=AOD&createdTimestamp=-3&testLoopType=DAILY&aggregated=&column=testLoop&column2=rstate&row=hardware',
        'id_6': 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com/aggregated-summary?ciOfficial=true&program=ML66&createdTimestamp=-3&testLoopType=DAILY&aggregated=&column=testLoop&column2=rstate&row=hardware',
        'id_7': 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com/aggregated-summary?ciOfficial=true&program=SWAT&createdTimestamp=-3&testLoopType=REGRESSION_VERSION_TRIAL&aggregated=&column=testLoop&column2=rstate&row=hardware'
    }
    
    while True:
        for key, value in urls.iteritems():
            #conf_line_chart(key)
            conf_line_chart(key)
            ML66_REG1_line_chart(key, value)
        time.sleep(30)
    
    

if __name__ == '__main__':
    main()