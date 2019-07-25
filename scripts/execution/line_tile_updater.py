import tile
import json

def update_tile(line_chart_id, params, include_ongoing = False):
    maas_url = 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com'
    url = '/aggregated-summary?'.join((maas_url, params))
    extractedData = tile.line_chart_fetch_data(url, include_ongoing)
    
    success_rate = round(extractedData["series"][len(extractedData["series"])-1][1], 2)
    line_chart_content = {
        'subtitle': str(success_rate) + '%',
        'description': str(extractedData["passed"]) + '/' + str(extractedData["total"] - extractedData["excluded"]),
        'subdescription': extractedData["rstate"],
        'series_list': [extractedData["series"]] 
    }
    data_json = json.dumps(line_chart_content)
    tile.update_tile('line_chart1', line_chart_id, data_json)
    
    if success_rate > 99.5:
        tile.line_config_green(line_chart_id, params)
    elif success_rate <= 99.5 and include_ongoing:
        tile.line_config_warning(line_chart_id, params)
    else:
        tile.line_config_alert(line_chart_id, params)