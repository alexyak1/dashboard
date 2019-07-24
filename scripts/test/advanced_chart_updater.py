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
        [7, 11, '',{'background':'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[8, 1, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [8, 2, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [8, 3, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [8, 4, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [8, 5, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [8, 6, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [8, 7, '', {'background': 'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [8, 8, '', {'background': 'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [8, 9, '', {'background': 'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[9, 1, '', {'background': 'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [9, 2, '', {'background': 'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [9, 3, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [9, 4, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [9, 5, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [9, 6, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [9, 7, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [9, 8, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[10, 1, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [10, 2, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [10, 3, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [10, 4, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [10, 5, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [10, 6, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [10, 7, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [10, 8, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [10, 9, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[11, 1, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [11, 2, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [11, 3, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [11, 4, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [11, 5, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [11, 6, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [11, 7, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [11, 8, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [11, 9, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [11, 10, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[12, 1, '', {'background': 'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [12, 2, '', {'background': 'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [12, 3, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [12, 4, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [12, 5, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [12, 6, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [12, 7, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [12, 8, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[13, 1, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [13, 2, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [13, 3, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [13, 4, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [13, 5, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [13, 6, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [13, 7, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [13, 8, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],

        [[14, 1, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [14, 2, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [14, 3, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [14, 4, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [14, 5, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [14, 6, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [14, 7, '', {'background': 'green', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [14, 7, '', {'background': 'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}],
         [14, 8, '', {'background': 'red', 'border-width': '2px', 'border-color': 'black', 'padding': '7px'}]],
    
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