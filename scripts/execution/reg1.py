import requests as req
import tile 
import json


MAAS_URL = 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com'
line_chart_id = 'line_chart_reg1'
percentage_chart_id = 'precentage_chart_reg1'



def main():
    params = 'ciOfficial=true&program=ML66&createdTimestamp=-3&testLoopType=REG1&aggregated=&column=testLoop&column2=rstate&row=hardware'
    url = '/aggregated-summary?'.join((MAAS_URL, params))
    tile.default_line_config(line_chart_id)
    extractedData = tile.fetch_data(url)
    
    success_rate = round(extractedData["series"][len(extractedData["series"])-1][1], 2)
    line_chart_content = {
        'subtitle': str(success_rate) + '%',
        'description': str(extractedData["passed"]) + '/' + str(extractedData["total"]-extractedData["excluded"]),
        'series_list': [extractedData["series"]] 
    }
    data_json = json.dumps(line_chart_content)
    tile.update_tile('line_chart', line_chart_id, data_json)

    percentage_chart_content = {
        'title': extractedData["rstate"],
        'subtitle': 'Finshed',
        'big_value': str(success_rate) + '%',
        'left_value': extractedData["passed"],
        'right_value': extractedData["total"] - extractedData["excluded"],
        'left_label': 'Passed',
        'right_label': 'Total'
    } 
    data_json = json.dumps(percentage_chart_content)
    tile.update_tile('simple_percentage', percentage_chart_id, data_json)
    color_config_json = tile.percentage_chart_color_config(success_rate)
    tile.update_tile_config(percentage_chart_id, color_config_json)
     


if __name__ == "__main__":
    main()