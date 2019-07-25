import tile
import json

def update_tile(advanced_chart_id, params, include_ongoing = False):
    maas_url = 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com'
    url = '/aggregated-summary?'.join((maas_url, params))
   
    extractedData = tile.bar_chart_fetch_data(url, include_ongoing)
    passed_series = []
    failed_series = []


    for index,(passed, total) in enumerate(zip(extractedData["passed"], extractedData["total"])):
        if passed == total:
            passed_series.append([index+1, passed])
            failed_series.append([index+1, 0])
        else:
            failed_series.append([index+1, passed])
            passed_series.append([index+1, 0])

    #success_rate = round(extractedData["series"][len(extractedData["series"])-1][1], 2)
    percentage = round(float(extractedData['passed'][-1]) / total * 100, 2) 
    line_chart_content = {
        'title': str(percentage) + '% ' + str(extractedData["rstate"]),
        'description': str(extractedData['passed'][-1]) + '/' + str(total),
        'plot_data': [passed_series, failed_series]
    }
    data_json = json.dumps(line_chart_content)
    tile.update_tile('advanced_plot1', advanced_chart_id, data_json)

    total = extractedData['undone'][-1] + extractedData['passed'][-1]
    
    

    if percentage > 99.5:
        tile.default_advanced_config(advanced_chart_id)
    else:
        tile.advanced_config_alert(advanced_chart_id)