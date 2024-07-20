import random
import pandas as pd
from datetime import datetime

def random_zero_or_one():
    return random.choice([0,0,0,0,1])


event_types = [
  "auth-failed",
  "auth-success",
  "auth-lockout",
  "transaction-large",
  "transaction-frequent",
  "transaction-unusual-location",
  "payee-added",
  "customer-info-change",
  "credit-limit-change",
  "account-closure",
  "wire-transfer-large",
  "card-suspicious-activity",
  "identity-theft-alert",
  "phishing-report",
  "insider-trading-suspicion",
  "money-laundering-suspicion",
]
event_severity = ["low",
  "low",
  "medium",
  "medium",
  "medium",
  "high",
  "high",
  "critical"]
event_type_threat = {
   "auth-failed": 0.3,
  "auth-success": 0.1,
  "auth-lockout": 0.7,
  "transaction-large": 0.6,
  "transaction-frequent": 0.5,
  "transaction-unusual-location": 0.8,
  "payee-added": 0.4,
  "customer-info-change": 0.3,
  "credit-limit-change": 0.5,
  "account-closure": 0.6,
  "wire-transfer-large": 0.9,
  "card-suspicious-activity": 0.8,
  "identity-theft-alert": 0.9,
  "phishing-report": 0.7,
  "insider-trading-suspicion": 0.8,
  "money-laundering-suspicion": 0.9,
}

ip_threat = {
    "malicious": 0.9,
    "safe": 0.1
}


# Predefined templates for event descriptions
event_description_templates = {
    "auth-failed":
    "Failed login attempt for user '{username}' from account {source_ip}",
  "auth-success":
    "Successful login for user '{username}' from account {source_ip}",
  "auth-lockout":
    "User '{username}' locked out after multiple failed login attempts from account {source_ip}",
  "transaction-large":
    "Large transaction detected: {amount} for account {source_ip}",
  "transaction-frequent":
    "Frequent transactions detected for account {source_ip}",
  "transaction-unusual-location":
    "Transaction from unusual location for account {source_ip}",
  "payee-added": "New payee added to account {source_ip}",
  "customer-info-change":
    "Customer information changed for account {source_ip}",
  "credit-limit-change":
    "Credit limit change requested for account {source_ip}",
  "account-closure": "Account closure requested for {source_ip}",
  "wire-transfer-large":
    "Large wire transfer: {amount} from account {source_ip} to {destination_ip}",
  "card-suspicious-activity":
    "Suspicious activity detected on card linked to account {source_ip}",
  "identity-theft-alert":
    "Potential identity theft detected for account {source_ip}",
  "phishing-report": "Phishing attempt reported by user of account {source_ip}",
  "insider-trading-suspicion":
    "Potential insider trading flagged for account {source_ip}",
  "money-laundering-suspicion":
    "Potential money laundering activity detected for account {source_ip}",
}
safe_ips = [
    "192.168.1.100", "10.0.0.2", "172.16.0.10", "10.10.10.10",
    "192.168.0.1", "192.168.2.5", "10.1.1.1", "172.16.1.100",
    "192.168.10.5", "10.0.0.100"
]  # Example safe IPs
safe_destination_ips = [
    "192.168.0.2", "10.0.0.3", "172.16.0.20", "10.10.10.20",
    "192.168.0.3", "192.168.2.6", "10.1.1.2", "172.16.1.101",
    "192.168.10.6", "10.0.0.101"
]  # Example safe IPs

# Function to generate a fake log entry with realistic event descriptions
def generate_fake_log_entry():
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    res = random_zero_or_one()
    source_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}" if res else random.choice(safe_ips)
    source_port =  random.randint(1024, 65535);
    source_ip_port = f"{source_ip}:{source_port}" if res else source_ip
    res = random_zero_or_one()

    destination_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}" if res else random.choice(safe_destination_ips)
    destination_port = random.randint(80, 8080)  # Adjust the port range as needed
    destination_ip_port = f"{destination_ip}:{destination_port}" if res else destination_ip

    user_info = random.choice(["user123", "anonymous", "admin", "guest"])
    device_info = random.choice(["DeviceXYZ", "ServerABC", "Workstation123"])
    event_type = random.choice(event_types)

    event_description_template = event_description_templates[event_type]
    if "{source_ip}" in event_description_template:
        source_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    event_description = event_description_template.format(
        username=user_info,
        source_ip=source_ip,
        device=device_info,
        port=random.randint(1, 65535),
        domain=f"example{random.randint(1, 1000)}.com",
        filename=f"file{random.randint(1, 1000)}.txt",
        reason=f"Reason{random.randint(1, 10)}",
        error_message=f"Error message: {random.randint(1, 100)}",
        app_name=f"App{random.randint(1, 10)}",
        api_name=f"API{random.randint(1, 5)}",
        access_type=random.choice(["Read", "Write", "Delete"]),
        file_path=f"/path/to/file{random.randint(1, 1000)}.txt",
        software_name=f"Software{random.randint(1, 10)}",
        version=f"v{random.randint(1, 5)}",
        amount=random.randint(100, 1000000),
        destination_ip=destination_ip
    )

    event_sev = random.choice(event_severity)

    # Classify source IPs as either safe or potentially malicious
    source_ip_class = "safe" if source_ip in safe_ips else "malicious"
    dest_ip_class = "safe" if destination_ip_port in safe_destination_ips else "malicious"

    event_type_threat_score = event_type_threat.get(event_type, 0.5)
    source_ip_threat_score = ip_threat.get(source_ip_class, 0.5)
    dest_ip_threat_score = ip_threat.get(dest_ip_class, 0.5)

    ml_risk_score = round((event_type_threat_score + source_ip_threat_score + dest_ip_threat_score) / 3, 2)

    log_entry = [timestamp, source_ip_port,source_ip_class,destination_ip,dest_ip_class, user_info, device_info, event_type, event_description, event_sev, ml_risk_score]
    return log_entry

# Generate a sample dataset with 100 log entries
sample_dataset = []
for _ in range(500):
    log_entry = generate_fake_log_entry()
    sample_dataset.append(log_entry)

# Create a DataFrame with appropriate column names
df = pd.DataFrame(sample_dataset, columns=["Timestamp", "Source","SourceClass","Destination","DestinationClass", "User", "Device", "EventType", "Description", "Severity", "MLRiskScore"])

# Save the dataset to a CSV file
df.to_csv('sample_log_dataset.csv', index=False)

print("Sample dataset with realistic event descriptions generated and saved to 'sample_log_dataset.csv'")