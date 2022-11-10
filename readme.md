# Code
Code is to attempt to create an application that can listen for changes in an Azure storage account and validate if a blob has been overwritten.

By design, adding and appending a file to blob appears as a Create event. This code takes advantage of changefeed to provide a link to the softblob delete url. In order for this code to work two things need to happen:

1. Change feed needs to be enabled.
2. Soft blob delete needs to be enabled.

both of these features are only features of Storage account v2


## Sample output:
Change Detected. URI: https://lugutcf.blob.core.windows.net/changefeedtest/test.txt
Previous timestamp 2022-11-07T21:28:32.8672212Z

Change Detected. URI: https://lugutcf.blob.core.windows.net/changefeedtest/test.txt
Previous timestamp 2022-11-09T01:26:37.3039434Z