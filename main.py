#test.txt 	
#11/7/2022, 1:17:41 PM
#11/7/2022, 1:28:32 PM
from datetime import datetime
from azure.storage.blob.changefeed import ChangeFeedClient
import json

def main():

    cf_client = ChangeFeedClient("https://{}.blob.core.windows.net".format("lugutcf"),
                             credential="KnWAj3KcuMLeFKe/bnVMHza3DmiN4+i/CiXN4FR25chxCG4reXUbeqaHA5ZaSfV5WQxC/I94xs0J+AStfwFRuw==")
    start_time = datetime(2022, 11, 1)
    end_time = datetime(2022, 11, 10)
    change_feed = cf_client.list_changes(start_time=start_time, end_time=end_time)
    for change in change_feed:
        if change['data']['previousInfo'] and change['eventType'] == 'BlobCreated':
            print('Change Detected. URI: ' + change['data']['url'])
            print('Previous timestamp ' + change['data']['previousInfo']['SoftDeleteSnapshot'])
            print('')

if __name__ == '__main__':
    main()