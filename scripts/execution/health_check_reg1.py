import health_check_updater as updater

def main():
    url = 'https://fem203-eiffel024.mo.sw.ericsson.se:8443/jenkins/job/ml66_hourly/lastBuild/api/json?depth=0'
    tileId = 'health_check_ml66_reg1'    
    title = 'ML66 REG1'

    updater.update_tile(url, tileId, title)
    

if __name__ == "__main__":
    main()