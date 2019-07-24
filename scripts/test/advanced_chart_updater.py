import tile
import json

def update_tile(advanced_chart_id, params, include_ongoing = False):
    maas_url = 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com'
    url = '/aggregated-summary?'.join((maas_url, params))
   
    extractedData = tile.bar_chart_fetch_data(url, include_ongoing)
    data = [
        [[1, 1, '', {'background':'green','border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [1, 2, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [1, 3, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [1, 4, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [1, 5, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [1, 6, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [1, 7, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [1, 8, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [1, 9, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [1, 10, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [1, 11, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[2, 1, '', {'background':'red','border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [2, 2, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [2, 3, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [2, 4, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [2, 5, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [2, 6, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [2, 7, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [2, 8, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [2, 9, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]], 
        
        [[3, 1, '', {'background':'green','border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [3, 2, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [3, 3, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [3, 4, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [3, 5, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [3, 6, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [3, 7, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [3, 8, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [3, 9, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [3, 10, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[4, 1, '', {'background':'red','border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [4, 2, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [4, 3, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [4, 4, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [4, 5, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [4, 6, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [4, 7, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[5, 1, '', {'background':'red','border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [5, 2, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [5, 3, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [5, 4, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [5, 5, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [5, 6, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [5, 7, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [5, 8, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [5, 9, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [5, 10, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[6, 1, '', {'background':'green','border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [6, 2, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [6, 3, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [6, 4, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [6, 5, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [6, 6, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [6, 7, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [6, 8, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [6, 9, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[7, 1, '', {'background':'green','border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [7, 2, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}], 
        [7, 3, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [7, 4, '',{'background':'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [7, 5, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [7, 6, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [7, 7, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [7, 8, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [7, 9, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [7, 10, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
        [7, 11, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]]
        
        
              ]
    #data.append(extractedData["passed"])
    #data.append(extractedData["undone"])

    success_rate = round(float(extractedData["passed"][-1][1]) / (extractedData["passed"][-1][1] + extractedData["undone"][-1][1]) * 100,2)
    line_chart_content = {
        'title': extractedData["rstate"],
        'description': str(success_rate) + '%',
        'plot_data': data 
    }
    data_json = json.dumps(line_chart_content)
    tile.update_tile('advanced_plot', advanced_chart_id, data_json)
    tile.block_config(advanced_chart_id)
    #tile.default_advanced_config(advanced_chart_id)