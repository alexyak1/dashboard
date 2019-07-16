import requests as req
import tile 
import json
import line_tile_updater as updater

def main():
    line_chart_id = 'line_chart_aod'
    percentage_chart_id = 'precentage_chart_aod'
    params = 'ciOfficial=true&program=AOD&createdTimestamp=-3&testLoopType=HOURLY&aggregated=&column=testLoop&column2=rstate&row=hardware'
    updater.update_tile(line_chart_id, percentage_chart_id, params)

if __name__ == "__main__":
    main()