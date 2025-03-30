import nmap
from zapv2 import ZAPv2
import time

class Scanner:
    def __init__(self, zap_api_key='lpv5os7flkcbha05es0shcnjr3', zap_host='localhost', zap_port='8080'):
        self.nm = nmap.PortScanner()
        self.zap = ZAPv2(apikey=zap_api_key, proxies={'http': f'http://{zap_host}:{zap_port}', 'https': f'http://{zap_host}:{zap_port}'})

    def network_scan(self, subnet):
        scan_arguments = "-sV --script=vuln"
        print(f"Running Nmap command: nmap {scan_arguments} {subnet}")
        result = self.nm.scan(hosts=subnet, arguments=scan_arguments)
        print("Nmap Scan Output:", result)
        return result

    def host_scan(self, host):
        scan_arguments = "-sV --script=vuln"
        print(f"Running Nmap command: nmap {scan_arguments} {host}")
        result = self.nm.scan(hosts=host, arguments=scan_arguments)
        print("Nmap Scan Output:", result)
        return result

    def web_scan(self, url):
        print(f"Starting OWASP ZAP scan on {url}...")
        scan_id = self.zap.spider.scan(url)
        while int(self.zap.spider.status(scan_id)) < 100:
            print(f"Spider progress: {self.zap.spider.status(scan_id)}%")
            time.sleep(2)

        ascan_id = self.zap.ascan.scan(url)
        while int(self.zap.ascan.status(ascan_id)) < 100:
            print(f"Active Scan progress: {self.zap.ascan.status(ascan_id)}%")
            time.sleep(5)

        alerts = self.zap.core.alerts(baseurl=url)
        print("OWASP ZAP Scan Alerts:", alerts)
        return alerts
