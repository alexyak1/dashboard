import tile
import json

def update_tile(line_chart_id, percentage_chart_id, params, include_ongoing = False):
    maas_url = 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com'
    url = '/aggregated-summary?'.join((maas_url, params))
    extractedData = tile.line_chart_fetch_data(url, include_ongoing)
    
    success_rate = round(extractedData["series"][len(extractedData["series"])-1][1], 2)
    line_chart_content = {
        'subtitle': str(success_rate) + '%',
        'description': str(extractedData["passed"]) + '/' + str(extractedData["total"] - extractedData["excluded"]),
        'series_list': [extractedData["series"]] 
    }
    data_json = json.dumps(line_chart_content)
    tile.update_tile('line_chart', line_chart_id, data_json)

    if int(success_rate) > 98:
        tile.default_line_config(line_chart_id)
    elif int(success_rate) <= 98:
        tile.line_config_alert(line_chart_id)