import requests as req
import tile 
import json
import line_tile_updater as updater

maas_url = 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com'
line_chart_id = 'line_chart_ml66_daily'
percentage_chart_id = 'precentage_chart_ml66_daily'
params = 'ciOfficial=true&program=ML66&createdTimestamp=-20&testLoopType=DAILY&aggregated=&column=testLoop&column2=rstate&row=hardware'

def main():
    updater.update_tile(maas_url, line_chart_id, percentage_chart_id, params, True)

if __name__ == "__main__":
    main()