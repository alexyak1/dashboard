import health_check_updater as updater

def main():
    urls = [ 
        'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_ECA_servers/lastCompletedBuild/api/json?depth=0',
        'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_ETA_servers/lastCompletedBuild/api/json?depth=0',
        'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_PDH_SDH_testers/lastCompletedBuild/api/json?depth=0',
        'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_PDUs/lastCompletedBuild/api/json?depth=0',
        'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_Serial_servers/lastCompletedBuild/api/json?depth=0',
        'https://pdutp-mwn-jenkins02.mo.sw.ericsson.se//job/LN_ftp_tftp_servers/lastCompletedBuild/api/json?depth=0'
    ] 
    tileId = 'ln_lab_health_check'    
    title = 'LN LAB INSTRUMENTS HEALTH CHECK'
            
    updater.update_tile_multiple_url(urls, tileId, title)
    

if __name__ == "__main__":
    main()