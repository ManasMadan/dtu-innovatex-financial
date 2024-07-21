# Financial Log Analyzer Backend

This is the backend repository of the Financial Log Analysis System, responsible for managing financial transaction data, performing fraud detection analysis, and providing APIs for the frontend interface. The backend system plays a crucial role in centralizing financial log data, implementing machine learning-based fraud detection algorithms, and facilitating real-time monitoring of financial activities.


### Tasks Completed

- [x] InterPlanetary File System (IPFS) implemented
- [x] Diamante Blockchain Implemented

## Tech Stack

- [Ganache](https://trufflesuite.com/ganache/)
- [Truffle](https://trufflesuite.com/)
- [Node JS](https://nodejs.org/en)
- [Express JS](https://expressjs.com/)
- [Moralis IPFS](https://moralis.io/)
- [Luxon](https://www.npmjs.com/package/luxon)
- [Diamante Blockchain](https://diamanteblockchain.com/)

### Financial Log Collection and Management
- *Log Data Storage:* Financial transaction logs are collected, securely stored using IPFS, and organized for efficient retrieval and analysis.
- *Data Ingestion:* The backend provides mechanisms for ingesting financial log data from diverse sources, ensuring compatibility and data integrity.
- *Data Retention:* Define data retention policies to manage the storage of financial log data, ensuring compliance with financial regulations and data protection laws.

### Real-time Fraud Detection Analysis
- *Machine Learning Models:* Implement advanced machine learning algorithms (XGBoost, CatBoost, LightGBM, and MLPRegressor) to detect anomalies and identify fraud patterns in real-time.
- *Risk Assessment:* Utilize the ML model to predict risk percentages for entered logs, providing a continuous output from 0 to 1 (1 being most risky, 0 being least risky).
- *Alerting System:* Create an alerting system that triggers notifications when potential fraudulent activities or policy violations are detected.

### API and Data Access
- *RESTful APIs:* Provide secure RESTful APIs for the frontend to access financial log data, fraud detection results, and system configuration settings.
- *User Authentication:* Implement robust user authentication and authorization mechanisms for API access, ensuring data privacy and security.
- *Data Visualization:* Offer APIs for data visualization tools to fetch real-time financial insights and generate reports for monitoring and investigation purposes.

### Security Measures
- *Encryption:* Implement strong encryption for sensitive data both at rest and in transit.
- *Access Control:* Utilize smart contracts for executing access control logic, ensuring only authorized parties can retrieve or modify specific data stored on IPFS.
- *Network Security:* Implement firewalls, network segmentation, and strict access controls to protect the private network from external threats.

This backend system ensures a secure, reliable, and efficient approach to detecting and managing fraudulent activities in financial environments, leveraging the benefits of blockchain, IPFS, and advanced machine learning techniques.
