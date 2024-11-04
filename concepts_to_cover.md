**Amazon Athena**

Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. 

Helps to analyze unstructured, semi-structured and structured data stored in S3. (eg csv, json, or columnar data formats such as Apache PArquet and Apache ORC)

Ideal for running ad-hoc queries using ANSI SQL

**Amazon CloudFront**

**Amazon Quicksight:**

<ins>Business intelligence (BI) service built for the cloud.</ins> Create and publish interactive dashboards, perform ad-hoc analysis, and quickly get insights from their data.

**Amazon Network Firewall:**

Managed firewall service that provides filtering for both inbound and outbound network traffic. <ins>Allows creation of rules for traffic insepction and filtering</ins>

**Amazon Guard Duty:**

<ins>Threat detection service</ins> that monitors for malicious activity and anomalous behaviour to protect AWS accounts, workloads and data.
For <ins>account monitoring</ns> for suspicious activity

**Amazon Shield:**

A managed <ins>Distributed Denial of Service (DDoS)</ins> protection service that safeguards applications running on AWS


**Amazon Application Load Balancer:**

Ideal for load balancing HTTP and HTTPS traffic

**Amazon Network Load Balancer:**

Ideal for load balancing TCP and UDP traffic

**Amazon Gateway Load Balancer:**

Easily deploy, scale and manage <ins>third-party virtual appliances.</ins> One gateway for distributing traffic across multiple virtual appliances


**Amazon Aurora:**

Amazon RDS database engine ideal for <ins>high-traffic web applications, real-time analytics and applications demanding high throughput and resilience.</ins>

- Aurora cloning


**Amazon Elastic Block Store:**

- Provides scalable, high-performance block storage resources that can be used with Amazon EC2 instances.
- EBS volumes attached to EC2 instances
- EBS snapshots: Point-in-time incremental backups of EBS volumes that persist independently from volume itself
- EBS fast snapshot restore feature on the EBS snapshots


**Amazon S3:**
- S3 Intelligent Tiering
- Hosting static resources such as HTML, CSS, client-side JavaScript, and images.
- MFA Delete: security feature for S3 that adds an additional layer of <ins>protection against accidental or malicious deletion of data</ins>, requiring multi-factor authentication (MFA) for certain operations to be performed.



**Amazon Simple Queue Service (SQS):**

Fully managed message queuing service, enabling the decoupling and scaling of microservices, distributed systems, and serverless applications

**Amazon Simple Notification Service (SNS):**


**Amazon Config**

Enables you to assess, audit, and evaluate the <ins>configurations of your AWS resources</ins>

**AWS Cloud Trail:**

Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail.
Events include actions taken in AWS Management Console, AWS CLI, AWS SDK and APIs


**Amazon Kinesis Data Streams**

Serverless streaming data service that makes it easy to capture, process and store data streams at any scale

**Amazon AppFlow:**

Fully managed integration service that helps to securely transfer data <ins>between AWS services and various software-as-a-service (SaaS) applications</ins> such as Salesforce, SAP, Google Analytics, Facebook Ads, and ServiceNow

**AWS Direct Connect:**

A cloud service solution that makes it easy to establish a <ins>dedicated network connection from your premises to AWS. Ideal for organizations that need to transfer large volumes of data to and from AWS</ins>, require consistent network performance, or need to ensure data privacy and security for sensitive workloads.

**AWS Data Sync:**

A secure, online service that automates and accelerates moving data between <ins>on premises and AWS Storage services</ins>
During a transfer, AWS DataSync always checks the integrity of your data.

**AWS Backup:**

A cost-effective, fully managed, policy-based service that simplifies data protection at scale.

**Amazon Macie:**

Fully managed data security and data privacy service. Continuously monitors and <ins>evaluates data in S3 buckets to identify and classify sensitive data, such as personally identifiable information (PII), financial data, and intellectual property.</ins>

**AWS Elasticache:**

Fully managed, Redis and Memcached compatible service. Useful for storing <ins>session data</ins> (real-time session stores) and storing frequently used data in memory (real-time application data caching)

**Amazon S3 Transfer Acceleration:**

Speed up content transfers to and from Amazon S3 by as much as 50-500% for long-distance transfer of larger objects.


**Amazon Neptune**

A fully managed graph database service, designed to store and query highly connected data in the form of graphs.
*Neptune Streams is a change data capture (CDC)* feature for Amazon Neptune that provides a near real-time stream of changes made to the graph database


**Amazon Cognito User Pools**

- Handles user authentication
- User management and authentication
- Output: Provides JSON Web Tokens (JWT) upon successful authentication


**Amazon Cognito Identity Pools**

- Handles user authorization to *AWS services*
- Provide temporary AWS credentials for accessing AWS services
- Maps users to IAM roles
- Output: Provides temporary AWS credentials (Access Key ID, Secret Access Key, and Session Token)



**Amazon Lambda Concurrency**

*Reserved:* 
- Sets an upper limit on the number of concurrent executions for a function.
- Use case: Ensuring function does not scale beyond a certain point, often for cost control or to manage downstream resources

*Provisioned:*
- Initializes a requested number of execution environments so that they are prepared to respond immediately to function invocations, eliminating cold starts
- Use case: Ensuring consistently low latency for function, especially for user-facing applications or high-volume event processing



**Amazon Outpost**



**Amazon Control Tower**



**Misc**

- <font color="red">**NAT gateways are availability zone specific, and must be created in public subnets**</font>
- S3 event notifications: only to SNS, SQS and Lambda
- <font color="red">**Composite alarms in CloudWatch combines**</font> multiple metrics into a single alarm
- S3 Object Lock Governance/Compliance mode
- Maximum retention period for <font color="red">**automated backups configured directly in Amazon Aurora is 35 days**</font>
- <font color="red">**Amazon Cloudfront field level encryption**</font> protects specific data throughout system processing so that only certain applications can see it
- <font color="red">**AWS Transfer Family natively supports SFTP**</font>
- <font color="red">**AWS Elastic Beanstalk**</font> allows creation of multiple environments (eg production, staging, development). The URL swapping feature enables easy switching between the environments
- <font color="red">**Amazon Pinpoint**</font> is designed for customer engagement and supports sending SMS messages at scale
- <font color="red">**IAM roles for cross-account access**</font>, which is a standard and secure method for allowing access between AWS accounts.
- <font color="red">**AWS Database Migration Service (AWS DMS)**</font> to keep the source and target databases in sync during migration.
- <font color="red">**AWS Schema Conversion Tool (SCT)**</font> to convert the schema from Oracle to PostgreSQL
- <font color="red">**Kinesis Data Streams default data retention period is 24 hours**</font>
- <font color="red">**An egress-only internet gateway is for use with IPv6 traffic only.**</font> To enable outbound-only internet communication over IPv4, use a NAT gateway instead.
- <font color="red">**API Gateway canary release development**</font> allows incremental rollout of the new API version to a percentage of traffic.
- <font color="red">**Lambda SnapStart**</font> is specifically designed to reduce cold start times for Java functions

- <font color="red">**Instance Scheduler**</font> on AWS solution automates the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances.

- <font color="red">**Amazon FSx for Lustre**</font> is specifically designed for <font color="red">**high-performance workloads like HPC**</font>. It provides extremely low latency and high throughput, which aligns with the requirement for access latency within 1 ms.
