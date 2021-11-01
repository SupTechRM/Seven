################################
# Speedtest Access Reach Internet
################################

# Import Package Speedtest
import Speedtest
import speedtest

def InternetSpeedTest(wifi):
    download = wifi.download()
    upload = wifi.upload()
    print("Download Speed: ", download/1000000 + " Mbps")
    print("Upload Speed: ", upload/1000000 + " Mbps")
    return download, upload

# Define Wifi 
Wifi = speedtest.Speedtest()

InternetSpeedTest(Wifi)
