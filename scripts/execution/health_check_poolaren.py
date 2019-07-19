import health_check_updater as updater

def main():
    url = ['http://eselnvlx2635.mo.sw.ericsson.se:8080/job/poolaren-supervisor/lastCompletedBuild/api/json?depth=0']
    tileId = 'health_check_poolaren'    
    title = 'POOLAREN-SUPERVISOR'

    updater.update_tile_multiple_url(url, tileId, title)
    

if __name__ == "__main__":
    main()