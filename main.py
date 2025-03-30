from scanner import Scanner
from ai_classifier import VulnerabilityClassifier
import json

def main():
    scanner = Scanner(zap_api_key='lpv5os7flkcbha05es0shcnjr3')
    classifier = VulnerabilityClassifier()

    print("Vulnerability Scanner")
    choice = input("Scan [1] Network [2] Host [3] Web Application: ")

    if choice == "1":
        subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
        if '/' not in subnet:
            print("Error: Subnet mask required.")
            return
        results = scanner.network_scan(subnet)
    
    elif choice == "2":
        host = input("Enter specific host IP address: ")
        results = scanner.host_scan(host)

    elif choice == "3":
        url = input("Enter web application URL (include http/https): ")
        results = scanner.web_scan(url)
    
    else:
        print("Invalid choice!")
        return

    print("\nSending results to AI for vulnerability classification...")
    classified_data = classifier.classify(json.dumps(results, indent=2))
    
    with open('scan_report.json', 'w') as report:
        report.write(classified_data)

    print("\nScan Completed Successfully!")
    print("Report saved as scan_report.json")

if __name__ == "__main__":
    main()
