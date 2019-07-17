import requests as req
import tile 
import json
import line_tile_updater as updater


def main():
    line_chart_id = 'line_chart_swat'
    percentage_chart_id = 'precentage_chart_swat'
    params = 'ciOfficial=true&program=SWAT&createdTimestamp=-20&testLoopType=REGRESSION_VERSION_TRIAL&aggregated=&column=testLoop&column2=rstate&row=hardware'
    updater.update_tile(line_chart_id, percentage_chart_id, params, True)

if __name__ == "__main__":
    main()