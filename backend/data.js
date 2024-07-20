const safe_ips = [
  "192.168.1.100",
  "10.0.0.2",
  "172.16.0.10",
  "10.10.10.10",
  "192.168.0.1",
  "192.168.2.5",
  "10.1.1.1",
  "172.16.1.100",
  "192.168.10.5",
  "10.0.0.100",
];
const safe_destination_ips = [
  "192.168.0.2",
  "10.0.0.3",
  "172.16.0.20",
  "10.10.10.20",
  "192.168.0.3",
  "192.168.2.6",
  "10.1.1.2",
  "172.16.1.101",
  "192.168.10.6",
  "10.0.0.101",
];
const users = ["user123", "anonymous", "admin", "guest"];
const device = ["DeviceXYZ", "ServerABC", "Workstation123"];
const event_description_templates = {
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
};

const event_types = [
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
];

const event_severity = [
  "informational",
  "informational",
  "warning",
  "warning",
  "warning",
  "error",
  "error",
  "critical",
];

const campLocation = ["Delhi", "Bangalore", "Mumbai"];
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
};

ip_threat = {
  malicious: 0.9,
  safe: 0.1,
};
let action = [
  "wire-transfer-large",
  "card-suspicious-activity",
  "identity-theft-alert",
  "phishing-report",
  "insider-trading-suspicion",
  "money-laundering-suspicion",
];

module.exports = {
  action,
  campLocation,
  event_severity,
  event_types,
  event_description_templates,
  device,
  users,
  safe_destination_ips,
  safe_ips,
  event_type_threat,
  ip_threat,
};
