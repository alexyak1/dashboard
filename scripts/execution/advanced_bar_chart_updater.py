import tile
import json

def update_tile(advanced_chart_id, params, include_ongoing = False):
    maas_url = 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com'
    url = '/aggregated-summary?'.join((maas_url, params))
   
    extractedData = tile.bar_chart_fetch_data(url, include_ongoing)
    passed_series = []
    failed_series = []


    for index,(passed, total) in enumerate(zip(extractedData["passed"], extractedData["total"])):
        passed_persent = round(float(passed) / total * 100, 2)
        if passed == total:
            passed_series.append([index+1, passed_persent])
            failed_series.append([index+1, 0])
        else:

            failed_series.append([index+1, passed_persent])
            passed_series.append([index+1, 0])

    #success_rate = round(extractedData["series"][len(extractedData["series"])-1][1], 2)
    percentage = round(float(extractedData['passed'][-1]) / total * 100, 2) 
    line_chart_content = {
        'title': str(percentage) + '%',
        'description': str(extractedData['passed'][-1]) + '/' + str(total),
        'subdescription': str(extractedData["rstate"]),
        'plot_data': [passed_series, failed_series]
    }
    data_json = json.dumps(line_chart_content)
    tile.update_tile('advanced_plot1', advanced_chart_id, data_json)

    total = extractedData['undone'][-1] + extractedData['passed'][-1]
    
    

    if percentage > 99.5:
        tile.default_advanced_config(advanced_chart_id, params)
    else:
        tile.advanced_config_alert(advanced_chart_id, params)