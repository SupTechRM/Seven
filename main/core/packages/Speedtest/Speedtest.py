################################
# Speedtest Access Reach Internet
################################

# Import Package Speedtest
import Speedtest
import speedtest

from main.bridges import utils

def InternetSpeedTest(wifi):
    download = wifi.download()
    upload = wifi.upload()
    return utils.translate("Download Speed: ", download/1000000 + " Mbps", "Upload Speed: ", upload/1000000 + " Mbps")
