import line_tile_updater as updater

def main():
    line_chart_id = 'line_chart_aod_daily'
    params = 'ciOfficial=true&program=AOD&createdTimestamp=-20&testLoopType=DAILY&aggregated=&column=testLoop&column2=rstate&row=hardware'
    updater.update_tile(line_chart_id, params, True)

if __name__ == "__main__":
    main()