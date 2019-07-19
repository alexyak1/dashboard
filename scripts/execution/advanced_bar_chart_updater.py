import requests as req
import tile 
import json

def update_tile(advanced_chart_id, params, include_ongoing = False):
    maas_url = 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com'
    url = '/aggregated-summary?'.join((maas_url, params))
   
    extractedData = tile.bar_chart_fetch_data(url, include_ongoing)
    data = []
    data.append(extractedData["passed"])
    data.append(extractedData["failed"])


    #success_rate = round(extractedData["series"][len(extractedData["series"])-1][1], 2)
    line_chart_content = {
        'title': extractedData["rstate"],
        'description': '',
        'plot_data': data 
    }
    data_json = json.dumps(line_chart_content)
    tile.update_tile('advanced_plot', advanced_chart_id, data_json)

    tile.default_advanced_config(advanced_chart_id)