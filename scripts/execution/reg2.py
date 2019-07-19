import line_tile_updater as updater


def main():
    line_chart_id = 'line_chart_reg2'
    percentage_chart_id = 'precentage_chart_reg2'
    params = 'ciOfficial=true&program=ML66&createdTimestamp=-3&testLoopType=REG2&aggregated=&column=testLoop&column2=rstate&row=hardware'
    updater.update_tile(line_chart_id, percentage_chart_id, params)

if __name__ == "__main__":
    main()