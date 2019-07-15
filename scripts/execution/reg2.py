import requests as req
import tile 
import json
import line_tile_updater as updater


maas_url = 'https://mwn-maas.seln.wh.rnd.internal.ericsson.com'
line_chart_id = 'line_chart_reg2'
percentage_chart_id = 'precentage_chart_reg2'
params = 'ciOfficial=true&program=ML66&createdTimestamp=-3&testLoopType=REG2&aggregated=&column=testLoop&column2=rstate&row=hardware'

def main():
    updater.update_tile(maas_url, line_chart_id, percentage_chart_id, params)

if __name__ == "__main__":
    main()