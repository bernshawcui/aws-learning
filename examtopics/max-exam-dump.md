- Q214
- Q217
- Q218
- Q219
- Q222
- Q224
- Q230
- Q232
- Q233
- Q235


### Q308
A company has multiple AWS accounts that use consolidated billing. The company runs several active high performance Amazon RDS for Oracle On-Demand DB instances for 90 days. The company’s finance team has access to AWS Trusted Advisor in the consolidated billing account and all other AWS accounts.

The finance team needs to use the appropriate AWS account to access the Trusted Advisor check recommendations for RDS. The finance team must review the appropriate Trusted Advisor check to reduce RDS costs.

Which combination of steps should the finance team take to meet these requirements? (Choose two.)


A. Use the Trusted Advisor recommendations from the account where the RDS instances are running. <br>
B. Use the Trusted Advisor recommendations from the consolidated billing account to see all RDS instance checks at the same time. <br>
C. Review the Trusted Advisor check for Amazon RDS Reserved Instance Optimization. <br>
D. Review the Trusted Advisor check for Amazon RDS Idle DB Instances <br>
E. Review the Trusted Advisor check for Amazon Redshift Reserved Node Optimization. <br>

<details>
  <summary>Click to show the answer</summary>
  Answer: B & D
</details>


### Q312
A company has an application that runs on several Amazon EC2 instances. Each EC2 instance has multiple Amazon Elastic Block Store (Amazon EBS) data volumes attached to it. The application’s EC2 instance configuration and data need to be backed up nightly. The application also needs to be recoverable in a different AWS Region.

Which solution will meet these requirements in the MOST operationally efficient way?

A. Write an AWS Lambda function that schedules nightly snapshots of the application’s EBS volumes and copies the snapshots to a different Region. <br>
B. Create a backup plan by using AWS Backup to perform nightly backups. Copy the backups to another Region. Add the application’s EC2 instances as resources. <br>
C. Create a backup plan by using AWS Backup to perform nightly backups. Copy the backups to another Region. Add the application’s EBS volumes as resources. <br>
D. Write an AWS Lambda function that schedules nightly snapshots of the application's EBS volumes and copies the snapshots to a different Availability Zone. <br>
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>

### Q322
A solutions architect is designing a multi-tier application for a company. The application's users upload images from a mobile device. The application generates a thumbnail of each image and returns a message to the user to confirm that the image was uploaded successfully.

The thumbnail generation can take up to 60 seconds, but the company wants to provide a faster response time to its users to notify them that the original image was received. The solutions architect must design the application to asynchronously dispatch requests to the different application tiers.

What should the solutions architect do to meet these requirements?

A. Write a custom AWS Lambda function to generate the thumbnail and alert the user. Use the image upload process as an event source to invoke the Lambda function. <br>
B. Create an AWS Step Functions workflow. Configure Step Functions to handle the orchestration between the application tiers and alert the user when thumbnail generation is complete.<br>
C. Create an Amazon Simple Queue Service (Amazon SQS) message queue. As images are uploaded, place a message on the SQS queue for thumbnail generation. Alert the user through an application message that the image was received.<br>
D. Create Amazon Simple Notification Service (Amazon SNS) notification topics and subscriptions. Use one subscription with the application to generate the thumbnail after the image upload is complete. Use a second subscription to message the user's mobile app by way of a push notification after thumbnail generation is complete.<br>
<details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


### Q324
A company wants to implement a disaster recovery plan for its primary on-premises file storage volume. The file storage volume is mounted from an Internet Small Computer Systems Interface (iSCSI) device on a local storage server. The file storage volume holds hundreds of terabytes (TB) of data.

The company wants to ensure that end users retain immediate access to all file types from the on-premises systems without experiencing latency.

Which solution will meet these requirements with the LEAST amount of change to the company's existing infrastructure?

A. Provision an Amazon S3 File Gateway as a virtual machine (VM) that is hosted on premises. Set the local cache to 10 TB. Modify existing applications to access the files through the NFS protocol. To recover from a disaster, provision an Amazon EC2 instance and mount the S3 bucket that contains the files.
B. Provision an AWS Storage Gateway tape gateway. Use a data backup solution to back up all existing data to a virtual tape library. Configure the data backup solution to run nightly after the initial backup is complete. To recover from a disaster, provision an Amazon EC2 instance and restore the data to an Amazon Elastic Block Store (Amazon EBS) volume from the volumes in the virtual tape library.
C. Provision an AWS Storage Gateway Volume Gateway cached volume. Set the local cache to 10 TB. Mount the Volume Gateway cached volume to the existing file server by using iSCSI, and copy all files to the storage volume. Configure scheduled snapshots of the storage volume. To recover from a disaster, restore a snapshot to an Amazon Elastic Block Store (Amazon EBS) volume and attach the EBS volume to an Amazon EC2 instance.
D. Provision an AWS Storage Gateway Volume Gateway stored volume with the same amount of disk space as the existing file storage volume. Mount the Volume Gateway stored volume to the existing file server by using iSCSI, and copy all files to the storage volume. Configure scheduled snapshots of the storage volume. To recover from a disaster, restore a snapshot to an Amazon Elastic Block Store (Amazon EBS) volume and attach the EBS volume to an Amazon EC2 instance.
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


### 327
A solutions architect must secure a VPC network that hosts Amazon EC2 instances. The EC2 instances contain highly sensitive data and run in a private subnet. According to company policy, the EC2 instances that run in the VPC can access only approved third-party software repositories on the internet for software product updates that use the third party’s URL. Other internet traffic must be blocked.

Which solution meets these requirements?

A. Update the route table for the private subnet to route the outbound traffic to an AWS Network Firewall firewall. Configure domain list rule groups.
B. Set up an AWS WAF web ACL. Create a custom set of rules that filter traffic requests based on source and destination IP address range sets.
C. Implement strict inbound security group rules. Configure an outbound rule that allows traffic only to the authorized software repositories on the internet by specifying the URLs.
D. Configure an Application Load Balancer (ALB) in front of the EC2 instances. Direct all outbound traffic to the ALB. Use a URL-based rule listener in the ALB’s target group for outbound access to the internet.
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 329
A security audit reveals that Amazon EC2 instances are not being patched regularly. A solutions architect needs to provide a solution that will run regular security scans across a large fleet of EC2 instances. The solution should also patch the EC2 instances on a regular schedule and provide a report of each instance’s patch status.

Which solution will meet these requirements?

A. Set up Amazon Macie to scan the EC2 instances for software vulnerabilities. Set up a cron job on each EC2 instance to patch the instance on a regular schedule.
B. Turn on Amazon GuardDuty in the account. Configure GuardDuty to scan the EC2 instances for software vulnerabilities. Set up AWS Systems Manager Session Manager to patch the EC2 instances on a regular schedule.
C. Set up Amazon Detective to scan the EC2 instances for software vulnerabilities. Set up an Amazon EventBridge scheduled rule to patch the EC2 instances on a regular schedule.
D. Turn on Amazon Inspector in the account. Configure Amazon Inspector to scan the EC2 instances for software vulnerabilities. Set up AWS Systems Manager Patch Manager to patch the EC2 instances on a regular schedule.
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>

### 338
A solutions architect must create a disaster recovery (DR) plan for a high-volume software as a service (SaaS) platform. All data for the platform is stored in an Amazon Aurora MySQL DB cluster.

The DR plan must replicate data to a secondary AWS Region.

Which solution will meet these requirements MOST cost-effectively?

A. Use MySQL binary log replication to an Aurora cluster in the secondary Region. Provision one DB instance for the Aurora cluster in the secondary Region.
B. Set up an Aurora global database for the DB cluster. When setup is complete, remove the DB instance from the secondary Region.
C. Use AWS Database Migration Service (AWS DMS) to continuously replicate data to an Aurora cluster in the secondary Region. Remove the DB instance from the secondary Region.
D. Set up an Aurora global database for the DB cluster. Specify a minimum of one DB instance in the secondary Region.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### Q340
A media company hosts its website on AWS. The website application’s architecture includes a fleet of Amazon EC2 instances behind an Application Load Balancer (ALB) and a database that is hosted on Amazon Aurora. The company’s cybersecurity team reports that the application is vulnerable to SQL injection.

How should the company resolve this issue?

A. Use AWS WAF in front of the ALB. Associate the appropriate web ACLs with AWS WAF.
B. Create an ALB listener rule to reply to SQL injections with a fixed response.
C. Subscribe to AWS Shield Advanced to block all SQL injection attempts automatically.
D. Set up Amazon Inspector to block all SQL injection attempts automatically.
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### Q347
A company has an application that is running on Amazon EC2 instances. A solutions architect has standardized the company on a particular instance family and various instance sizes based on the current needs of the company.

The company wants to maximize cost savings for the application over the next 3 years. The company needs to be able to change the instance family and sizes in the next 6 months based on application popularity and usage.

Which solution will meet these requirements MOST cost-effectively?

A. Compute Savings Plan
B. EC2 Instance Savings Plan
C. Zonal Reserved Instances
D. Standard Reserved Instances
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 353
A company hosts a three-tier web application on Amazon EC2 instances in a single Availability Zone. The web application uses a self-managed MySQL database that is hosted on an EC2 instance to store data in an Amazon Elastic Block Store (Amazon EBS) volume. The MySQL database currently uses a 1 TB Provisioned IOPS SSD (io2) EBS volume. The company expects traffic of 1,000 IOPS for both reads and writes at peak traffic.

The company wants to minimize any disruptions, stabilize performance, and reduce costs while retaining the capacity for double the IOPS. The company wants to move the database tier to a fully managed solution that is highly available and fault tolerant.

Which solution will meet these requirements MOST cost-effectively?

A. Use a Multi-AZ deployment of an Amazon RDS for MySQL DB instance with an io2 Block Express EBS volume.
B. Use a Multi-AZ deployment of an Amazon RDS for MySQL DB instance with a General Purpose SSD (gp2) EBS volume.
C. Use Amazon S3 Intelligent-Tiering access tiers.
D. Use two large EC2 instances to host the database in active-passive mode.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 363
A company is building a game system that needs to send unique events to separate leaderboard, matchmaking, and authentication services concurrently. The company needs an AWS event-driven system that guarantees the order of the events.

Which solution will meet these requirements?

A. Amazon EventBridge event bus
B. Amazon Simple Notification Service (Amazon SNS) FIFO topics
C. Amazon Simple Notification Service (Amazon SNS) standard topics
D. Amazon Simple Queue Service (Amazon SQS) FIFO queues
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>

### 364
A hospital is designing a new application that gathers symptoms from patients. The hospital has decided to use Amazon Simple Queue Service (Amazon SQS) and Amazon Simple Notification Service (Amazon SNS) in the architecture.

A solutions architect is reviewing the infrastructure design. Data must be encrypted at rest and in transit. Only authorized personnel of the hospital should be able to access the data.

Which combination of steps should the solutions architect take to meet these requirements? (Choose two.)

A. Turn on server-side encryption on the SQS components. Update the default key policy to restrict key usage to a set of authorized principals.
B. Turn on server-side encryption on the SNS components by using an AWS Key Management Service (AWS KMS) customer managed key. Apply a key policy to restrict key usage to a set of authorized principals.
C. Turn on encryption on the SNS components. Update the default key policy to restrict key usage to a set of authorized principals. Set a condition in the topic policy to allow only encrypted connections over TLS.
D. Turn on server-side encryption on the SQS components by using an AWS Key Management Service (AWS KMS) customer managed key. Apply a key policy to restrict key usage to a set of authorized principals. Set a condition in the queue policy to allow only encrypted connections over TLS.
E. Turn on server-side encryption on the SQS components by using an AWS Key Management Service (AWS KMS) customer managed key. Apply an IAM policy to restrict key usage to a set of authorized principals. Set a condition in the queue policy to allow only encrypted connections over TLS.

<details>
  <summary>Click to show the answer</summary>
  Answer: BD
</details>


### 390
A company hosts a three-tier ecommerce application on a fleet of Amazon EC2 instances. The instances run in an Auto Scaling group behind an Application Load Balancer (ALB). All ecommerce data is stored in an Amazon RDS for MariaDB Multi-AZ DB instance.

The company wants to optimize customer session management during transactions. The application must store session data durably.

Which solutions will meet these requirements? (Choose two.)

A. Turn on the sticky sessions feature (session affinity) on the ALB. <br>
B. Use an Amazon DynamoDB table to store customer session information. <br>
C. Deploy an Amazon Cognito user pool to manage user session information. <br>
D. Deploy an Amazon ElastiCache for Redis cluster to store customer session information. <br>
E. Use AWS Systems Manager Application Manager in the application to manage user session information. <br>

<details>
  <summary>Click to show the answer</summary>
  Answer: AD or BD, debatable
  Note: ALB sticky session isn't persisted.
</details>



### 394
A company is running a multi-tier ecommerce web application in the AWS Cloud. The application runs on Amazon EC2 instances with an Amazon RDS for MySQL Multi-AZ DB instance. Amazon RDS is configured with the latest generation DB instance with 2,000 GB of storage in a General Purpose SSD (gp3) Amazon Elastic Block Store (Amazon EBS) volume. The database performance affects the application during periods of high demand.

A database administrator analyzes the logs in Amazon CloudWatch Logs and discovers that the application performance always degrades when the number of read and write IOPS is higher than 20,000.

What should a solutions architect do to improve the application performance?

A. Replace the volume with a magnetic volume. <br>
B. Increase the number of IOPS on the gp3 volume. <br>
C. Replace the volume with a Provisioned IOPS SSD (io2) volume. <br>
D. Replace the 2,000 GB gp3 volume with two 1,000 GB gp3 volumes. <br>
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


### 406
A solutions architect is designing a two-tiered architecture that includes a public subnet and a database subnet. The web servers in the public subnet must be open to the internet on port 443. The Amazon RDS for MySQL DB instance in the database subnet must be accessible only to the web servers on port 3306.

Which combination of steps should the solutions architect take to meet these requirements? (Choose two.)

A. Create a network ACL for the public subnet. Add a rule to deny outbound traffic to 0.0.0.0/0 on port 3306.
B. Create a security group for the DB instance. Add a rule to allow traffic from the public subnet CIDR block on port 3306.
C. Create a security group for the web servers in the public subnet. Add a rule to allow traffic from 0.0.0.0/0 on port 443.
D. Create a security group for the DB instance. Add a rule to allow traffic from the web servers’ security group on port 3306.
E. Create a security group for the DB instance. Add a rule to deny all traffic except traffic from the web servers’ security group on port 3306.
<details>
  <summary>Click to show the answer</summary>
  Answer: C & D
</details>

### 420
A company wants to use an Amazon RDS for PostgreSQL DB cluster to simplify time-consuming database administrative tasks for production database workloads. The company wants to ensure that its database is highly available and will provide automatic failover support in most scenarios in less than 40 seconds. The company wants to offload reads off of the primary instance and keep costs as low as possible.

Which solution will meet these requirements?

A. Use an Amazon RDS Multi-AZ DB instance deployment. Create one read replica and point the read workload to the read replica.
B. Use an Amazon RDS Multi-AZ DB duster deployment Create two read replicas and point the read workload to the read replicas.
C. Use an Amazon RDS Multi-AZ DB instance deployment. Point the read workload to the secondary instances in the Multi-AZ pair.
D. Use an Amazon RDS Multi-AZ DB cluster deployment Point the read workload to the reader endpoint.
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


### 426
A company needs to store data from its healthcare application. The application’s data frequently changes. A new regulation requires audit access at all levels of the stored data.

The company hosts the application on an on-premises infrastructure that is running out of storage capacity. A solutions architect must securely migrate the existing data to AWS while satisfying the new regulation.

Which solution will meet these requirements?

A. Use AWS DataSync to move the existing data to Amazon S3. Use AWS CloudTrail to log data events.
B. Use AWS Snowcone to move the existing data to Amazon S3. Use AWS CloudTrail to log management events.
C. Use Amazon S3 Transfer Acceleration to move the existing data to Amazon S3. Use AWS CloudTrail to log data events.
D. Use AWS Storage Gateway to move the existing data to Amazon S3. Use AWS CloudTrail to log management events.
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 430
A manufacturing company has machine sensors that upload .csv files to an Amazon S3 bucket. These .csv files must be converted into images and must be made available as soon as possible for the automatic generation of graphical reports.

The images become irrelevant after 1 month, but the .csv files must be kept to train machine learning (ML) models twice a year. The ML trainings and audits are planned weeks in advance.

Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

A. Launch an Amazon EC2 Spot Instance that downloads the .csv files every hour, generates the image files, and uploads the images to the S3 bucket.
B. Design an AWS Lambda function that converts the .csv files into images and stores the images in the S3 bucket. Invoke the Lambda function when a .csv file is uploaded.
C. Create S3 Lifecycle rules for .csv files and image files in the S3 bucket. Transition the .csv files from S3 Standard to S3 Glacier 1 day after they are uploaded. Expire the image files after 30 days.
D. Create S3 Lifecycle rules for .csv files and image files in the S3 bucket. Transition the .csv files from S3 Standard to S3 One Zone-Infrequent Access (S3 One Zone-IA) 1 day after they are uploaded. Expire the image files after 30 days.
E. Create S3 Lifecycle rules for .csv files and image files in the S3 bucket. Transition the .csv files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 1 day after they are uploaded. Keep the image files in Reduced Redundancy Storage (RRS).
<details>
  <summary>Click to show the answer</summary>
  Answer: B&C
</details>


### 447
A company has a stateless web application that runs on AWS Lambda functions that are invoked by Amazon API Gateway. The company wants to deploy the application across multiple AWS Regions to provide Regional failover capabilities.

What should a solutions architect do to route traffic to multiple Regions?

A. Create Amazon Route 53 health checks for each Region. Use an active-active failover configuration.
B. Create an Amazon CloudFront distribution with an origin for each Region. Use CloudFront health checks to route traffic.
C. Create a transit gateway. Attach the transit gateway to the API Gateway endpoint in each Region. Configure the transit gateway to route requests.
D. Create an Application Load Balancer in the primary Region. Set the target group to point to the API Gateway endpoint hostnames in each Region.
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 450
A company has a three-tier web application that is in a single server. The company wants to migrate the application to the AWS Cloud. The company also wants the application to align with the AWS Well-Architected Framework and to be consistent with AWS recommended best practices for security, scalability, and resiliency.

Which combination of solutions will meet these requirements? (Choose three.)

A. Create a VPC across two Availability Zones with the application's existing architecture. Host the application with existing architecture on an Amazon EC2 instance in a private subnet in each Availability Zone with EC2 Auto Scaling groups. Secure the EC2 instance with security groups and network access control lists (network ACLs).
B. Set up security groups and network access control lists (network ACLs) to control access to the database layer. Set up a single Amazon RDS database in a private subnet.
C. Create a VPC across two Availability Zones. Refactor the application to host the web tier, application tier, and database tier. Host each tier on its own private subnet with Auto Scaling groups for the web tier and application tier.
D. Use a single Amazon RDS database. Allow database access only from the application tier security group.
E. Use Elastic Load Balancers in front of the web tier. Control access by using security groups containing references to each layer's security groups.
F. Use an Amazon RDS database Multi-AZ cluster deployment in private subnets. Allow database access only from application tier security groups.
<details>
  <summary>Click to show the answer</summary>
  Answer: C, E, F
</details>


### 451
A company is migrating its applications and databases to the AWS Cloud. The company will use Amazon Elastic Container Service (Amazon ECS), AWS Direct Connect, and Amazon RDS.

Which activities will be managed by the company's operational team? (Choose three.)

A. Management of the Amazon RDS infrastructure layer, operating system, and platforms
B. Creation of an Amazon RDS DB instance and configuring the scheduled maintenance window
C. Configuration of additional software components on Amazon ECS for monitoring, patch management, log management, and host intrusion detection
D. Installation of patches for all minor and major database versions for Amazon RDS
E. Ensure the physical security of the Amazon RDS infrastructure in the data center
F. Encryption of the data that moves in transit through Direct Connect
<details>
  <summary>Click to show the answer</summary>
  Answer: B, C, F
</details>

### 454
A company has resources across multiple AWS Regions and accounts. A newly hired solutions architect discovers a previous employee did not provide details about the resources inventory. The solutions architect needs to build and map the relationship details of the various workloads across all accounts.

Which solution will meet these requirements in the MOST operationally efficient way?

A. Use AWS Systems Manager Inventory to generate a map view from the detailed view report.
B. Use AWS Step Functions to collect workload details. Build architecture diagrams of the workloads manually.
C. Use Workload Discovery on AWS to generate architecture diagrams of the workloads.
D. Use AWS X-Ray to view the workload details. Build architecture diagrams with relationships.
<details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


### 455
A company uses AWS Organizations. The company wants to operate some of its AWS accounts with different budgets. The company wants to receive alerts and automatically prevent provisioning of additional resources on AWS accounts when the allocated budget threshold is met during a specific period.

Which combination of solutions will meet these requirements? (Choose three.)

A. Use AWS Budgets to create a budget. Set the budget amount under the Cost and Usage Reports section of the required AWS accounts.
B. Use AWS Budgets to create a budget. Set the budget amount under the Billing dashboards of the required AWS accounts.
C. Create an IAM user for AWS Budgets to run budget actions with the required permissions.
D. Create an IAM role for AWS Budgets to run budget actions with the required permissions.
E. Add an alert to notify the company when each account meets its budget threshold. Add a budget action that selects the IAM identity created with the appropriate config rule to prevent provisioning of additional resources.
F. Add an alert to notify the company when each account meets its budget threshold. Add a budget action that selects the IAM identity created with the appropriate service control policy (SCP) to prevent provisioning of additional resources.
<details>
  <summary>Click to show the answer</summary>
  Answer: B, D, F
</details>


### 457
A company that uses AWS is building an application to transfer data to a product manufacturer. The company has its own identity provider (IdP). The company wants the IdP to authenticate application users while the users use the application to transfer data. The company must use Applicability Statement 2 (AS2) protocol.

Which solution will meet these requirements?

A. Use AWS DataSync to transfer the data. Create an AWS Lambda function for IdP authentication.
B. Use Amazon AppFlow flows to transfer the data. Create an Amazon Elastic Container Service (Amazon ECS) task for IdP authentication.
C. Use AWS Transfer Family to transfer the data. Create an AWS Lambda function for IdP authentication.
D. Use AWS Storage Gateway to transfer the data. Create an Amazon Cognito identity pool for IdP authentication.
<details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


### 467
A company uses AWS Organizations. A member account has purchased a Compute Savings Plan. Because of changes in the workloads inside the member account, the account no longer receives the full benefit of the Compute Savings Plan commitment. The company uses less than 50% of its purchased compute power.

A. Turn on discount sharing from the Billing Preferences section of the account console in the member account that purchased the Compute Savings Plan.
B. Turn on discount sharing from the Billing Preferences section of the account console in the company's Organizations management account.
C. Migrate additional compute workloads from another AWS account to the account that has the Compute Savings Plan.
D. Sell the excess Savings Plan commitment in the Reserved Instance Marketplace.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 468
A company is developing a microservices application that will provide a search catalog for customers. The company must use REST APIs to present the frontend of the application to users. The REST APIs must access the backend services that the company hosts in containers in private VPC subnets.

Which solution will meet these requirements?

A. Design a WebSocket API by using Amazon API Gateway. Host the application in Amazon Elastic Container Service (Amazon ECS) in a private subnet. Create a private VPC link for API Gateway to access Amazon ECS.
B. Design a REST API by using Amazon API Gateway. Host the application in Amazon Elastic Container Service (Amazon ECS) in a private subnet. Create a private VPC link for API Gateway to access Amazon ECS.
C. Design a WebSocket API by using Amazon API Gateway. Host the application in Amazon Elastic Container Service (Amazon ECS) in a private subnet. Create a security group for API Gateway to access Amazon ECS.
D. Design a REST API by using Amazon API Gateway. Host the application in Amazon Elastic Container Service (Amazon ECS) in a private subnet. Create a security group for API Gateway to access Amazon ECS.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 470
A company has applications hosted on Amazon EC2 instances with IPv6 addresses. The applications must initiate communications with other external applications using the internet. However the company’s security policy states that any external service cannot initiate a connection to the EC2 instances.

What should a solutions architect recommend to resolve this issue?

A. Create a NAT gateway and make it the destination of the subnet's route table
B. Create an internet gateway and make it the destination of the subnet's route table
C. Create a virtual private gateway and make it the destination of the subnet's route table
D. Create an egress-only internet gateway and make it the destination of the subnet's route table

<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


### 475
A company is designing a containerized application that will use Amazon Elastic Container Service (Amazon ECS). The application needs to access a shared file system that is highly durable and can recover data to another AWS Region with a recovery point objective (RPO) of 8 hours. The file system needs to provide a mount target m each Availability Zone within a Region.

A solutions architect wants to use AWS Backup to manage the replication to another Region.

Which solution will meet these requirements?

A. Amazon FSx for Windows File Server with a Multi-AZ deployment
B. Amazon FSx for NetApp ONTAP with a Multi-AZ deployment
C. Amazon Elastic File System (Amazon EFS) with the Standard storage class
D. Amazon FSx for OpenZFS

<details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


# 486
A company is looking for a solution that can store video archives in AWS from old news footage. The company needs to minimize costs and will rarely need to restore these files. When the files are needed, they must be available in a maximum of five minutes.

What is the MOST cost-effective solution?

A. Store the video archives in Amazon S3 Glacier and use Expedited retrievals.
B. Store the video archives in Amazon S3 Glacier and use Standard retrievals.
C. Store the video archives in Amazon S3 Standard-Infrequent Access (S3 Standard-IA).
D. Store the video archives in Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA).
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 496
A company uses on-premises servers to host its applications. The company is running out of storage capacity. The applications use both block storage and NFS storage. The company needs a high-performing solution that supports local caching without re-architecting its existing applications.

Which combination of actions should a solutions architect take to meet these requirements? (Choose two.)

A. Mount Amazon S3 as a file system to the on-premises servers.
B. Deploy an AWS Storage Gateway file gateway to replace NFS storage.
C. Deploy AWS Snowball Edge to provision NFS mounts to on-premises servers.
D. Deploy an AWS Storage Gateway volume gateway to replace the block storage.
E. Deploy Amazon Elastic File System (Amazon EFS) volumes and mount them to on-premises servers.
<details>
  <summary>Click to show the answer</summary>
  Answer: B, D
</details>


### 498
A company uses Amazon S3 to store high-resolution pictures in an S3 bucket. To minimize application changes, the company stores the pictures as the latest version of an S3 object. The company needs to retain only the two most recent versions of the pictures.

The company wants to reduce costs. The company has identified the S3 bucket as a large expense.

Which solution will reduce the S3 costs with the LEAST operational overhead?

A. Use S3 Lifecycle to delete expired object versions and retain the two most recent versions.
B. Use an AWS Lambda function to check for older versions and delete all but the two most recent versions.
C. Use S3 Batch Operations to delete noncurrent object versions and retain only the two most recent versions.
D. Deactivate versioning on the S3 bucket and retain the two most recent versions.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>

### 500
A company has multiple Windows file servers on premises. The company wants to migrate and consolidate its files into an Amazon FSx for Windows File Server file system. File permissions must be preserved to ensure that access rights do not change.

Which solutions will meet these requirements? (Choose two.)

A. Deploy AWS DataSync agents on premises. Schedule DataSync tasks to transfer the data to the FSx for Windows File Server file system.
B. Copy the shares on each file server into Amazon S3 buckets by using the AWS CLI. Schedule AWS DataSync tasks to transfer the data to the FSx for Windows File Server file system.
C. Remove the drives from each file server. Ship the drives to AWS for import into Amazon S3. Schedule AWS DataSync tasks to transfer the data to the FSx for Windows File Server file system.
D. Order an AWS Snowcone device. Connect the device to the on-premises network. Launch AWS DataSync agents on the device. Schedule DataSync tasks to transfer the data to the FSx for Windows File Server file system.
E. Order an AWS Snowball Edge Storage Optimized device. Connect the device to the on-premises network. Copy data to the device by using the AWS CLI. Ship the device back to AWS for import into Amazon S3. Schedule AWS DataSync tasks to transfer the data to the FSx for Windows File Server file system.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A, D
</details>


### 503
A company runs an infrastructure monitoring service. The company is building a new feature that will enable the service to monitor data in customer AWS accounts. The new feature will call AWS APIs in customer accounts to describe Amazon EC2 instances and read Amazon CloudWatch metrics.

What should the company do to obtain access to customer accounts in the MOST secure way?

A. Ensure that the customers create an IAM role in their account with read-only EC2 and CloudWatch permissions and a trust policy to the company’s account.
B. Create a serverless API that implements a token vending machine to provide temporary AWS credentials for a role with read-only EC2 and CloudWatch permissions.
C. Ensure that the customers create an IAM user in their account with read-only EC2 and CloudWatch permissions. Encrypt and store customer access and secret keys in a secrets management system.
D. Ensure that the customers create an Amazon Cognito user in their account to use an IAM role with read-only EC2 and CloudWatch permissions. Encrypt and store the Amazon Cognito user and password in a secrets management system.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 510
Topic 1
A global marketing company has applications that run in the ap-southeast-2 Region and the eu-west-1 Region. Applications that run in a VPC in eu-west-1 need to communicate securely with databases that run in a VPC in ap-southeast-2.

Which network design will meet these requirements?

A. Create a VPC peering connection between the eu-west-1 VPC and the ap-southeast-2 VPC. Create an inbound rule in the eu-west-1 application security group that allows traffic from the database server IP addresses in the ap-southeast-2 security group.
B. Configure a VPC peering connection between the ap-southeast-2 VPC and the eu-west-1 VPC. Update the subnet route tables. Create an inbound rule in the ap-southeast-2 database security group that references the security group ID of the application servers in eu-west-1.
C. Configure a VPC peering connection between the ap-southeast-2 VPC and the eu-west-1 VPUpdate the subnet route tables. Create an inbound rule in the ap-southeast-2 database security group that allows traffic from the eu-west-1 application server IP addresses.
D. Create a transit gateway with a peering attachment between the eu-west-1 VPC and the ap-southeast-2 VPC. After the transit gateways are properly peered and routing is configured, create an inbound rule in the database security group that references the security group ID of the application servers in eu-west-1.
 <details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


### 514
A company is running a microservices application on Amazon EC2 instances. The company wants to migrate the application to an Amazon Elastic Kubernetes Service (Amazon EKS) cluster for scalability. The company must configure the Amazon EKS control plane with endpoint private access set to true and endpoint public access set to false to maintain security compliance. The company must also put the data plane in private subnets. However, the company has received error notifications because the node cannot join the cluster.

Which solution will allow the node to join the cluster?

A. Grant the required permission in AWS Identity and Access Management (IAM) to the AmazonEKSNodeRole IAM role.
B. Create interface VPC endpoints to allow nodes to access the control plane.
C. Recreate nodes in the public subnet. Restrict security groups for EC2 nodes.
D. Allow outbound traffic in the security group of the nodes.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A or B
</details>


### 515
A company is migrating an on-premises application to AWS. The company wants to use Amazon Redshift as a solution.

Which use cases are suitable for Amazon Redshift in this scenario? (Choose three.)

A. Supporting data APIs to access data with traditional, containerized, and event-driven applications
B. Supporting client-side and server-side encryption
C. Building analytics workloads during specified hours and when the application is not active
D. Caching data to reduce the pressure on the backend database
E. Scaling globally to support petabytes of data and tens of millions of requests per minute
F. Creating a secondary replica of the cluster by using the AWS Management Console
<details>
  <summary>Click to show the answer</summary>
  Answer: B, C, E
</details>


### 517
A company wants to send all AWS Systems Manager Session Manager logs to an Amazon S3 bucket for archival purposes.

Which solution will meet this requirement with the MOST operational efficiency?

A. Enable S3 logging in the Systems Manager console. Choose an S3 bucket to send the session data to.
B. Install the Amazon CloudWatch agent. Push all logs to a CloudWatch log group. Export the logs to an S3 bucket from the group for archival purposes.
C. Create a Systems Manager document to upload all server logs to a central S3 bucket. Use Amazon EventBridge to run the Systems Manager document against all servers that are in the account daily.
D. Install an Amazon CloudWatch agent. Push all logs to a CloudWatch log group. Create a CloudWatch logs subscription that pushes any incoming log events to an Amazon Kinesis Data Firehose delivery stream. Set Amazon S3 as the destination.
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 523
A company runs a microservice-based serverless web application. The application must be able to retrieve data from multiple Amazon DynamoDB tables A solutions architect needs to give the application the ability to retrieve the data with no impact on the baseline performance of the application.

Which solution will meet these requirements in the MOST operationally efficient way?

A. AWS AppSync pipeline resolvers
B. Amazon CloudFront with Lambda@Edge functions
C. Edge-optimized Amazon API Gateway with AWS Lambda functions
D. Amazon Athena Federated Query with a DynamoDB connector
<details>
  <summary>Click to show the answer</summary>
  Answer: D or A
</details>


### 526
A solutions architect is reviewing the resilience of an application. The solutions architect notices that a database administrator recently failed over the application's Amazon Aurora PostgreSQL database writer instance as part of a scaling exercise. The failover resulted in 3 minutes of downtime for the application.

Which solution will reduce the downtime for scaling exercises with the LEAST operational overhead?

A. Create more Aurora PostgreSQL read replicas in the cluster to handle the load during failover.
B. Set up a secondary Aurora PostgreSQL cluster in the same AWS Region. During failover, update the application to use the secondary cluster's writer endpoint.
C. Create an Amazon ElastiCache for Memcached cluster to handle the load during failover.
D. Set up an Amazon RDS proxy for the database. Update the application to use the proxy endpoint.
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


### 527
A company has a regional subscription-based streaming service that runs in a single AWS Region. The architecture consists of web servers and application servers on Amazon EC2 instances. The EC2 instances are in Auto Scaling groups behind Elastic Load Balancers. The architecture includes an Amazon Aurora global database cluster that extends across multiple Availability Zones.

The company wants to expand globally and to ensure that its application has minimal downtime.

Which solution will provide the MOST fault tolerance?

A. Extend the Auto Scaling groups for the web tier and the application tier to deploy instances in Availability Zones in a second Region. Use an Aurora global database to deploy the database in the primary Region and the second Region. Use Amazon Route 53 health checks with a failover routing policy to the second Region. <br>
B. Deploy the web tier and the application tier to a second Region. Add an Aurora PostgreSQL cross-Region Aurora Replica in the second Region. Use Amazon Route 53 health checks with a failover routing policy to the second Region. Promote the secondary to primary as needed. <br>
C. Deploy the web tier and the application tier to a second Region. Create an Aurora PostgreSQL database in the second Region. Use AWS Database Migration Service (AWS DMS) to replicate the primary database to the second Region. Use Amazon Route 53 health checks with a failover routing policy to the second Region. <br>
D. Deploy the web tier and the application tier to a second Region. Use an Amazon Aurora global database to deploy the database in the primary Region and the second Region. Use Amazon Route 53 health checks with a failover routing policy to the second Region. Promote the secondary to primary as needed. <br>
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


###c 535
A company is building an Amazon Elastic Kubernetes Service (Amazon EKS) cluster for its workloads. All secrets that are stored in Amazon EKS must be encrypted in the Kubernetes etcd key-value store.

Which solution will meet these requirements?

A. Create a new AWS Key Management Service (AWS KMS) key. Use AWS Secrets Manager to manage, rotate, and store all secrets in Amazon EKS.
B. Create a new AWS Key Management Service (AWS KMS) key. Enable Amazon EKS KMS secrets encryption on the Amazon EKS cluster.
C. Create the Amazon EKS cluster with default options. Use the Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver as an add-on.
D. Create a new AWS Key Management Service (AWS KMS) key with the alias/aws/ebs alias. Enable default Amazon Elastic Block Store (Amazon EBS) volume encryption for the account.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 536
A company wants to provide data scientists with near real-time read-only access to the company's production Amazon RDS for PostgreSQL database. The database is currently configured as a Single-AZ database. The data scientists use complex queries that will not affect the production database. The company needs a solution that is highly available.

Which solution will meet these requirements MOST cost-effectively?

A. Scale the existing production database in a maintenance window to provide enough power for the data scientists.
B. Change the setup from a Single-AZ to a Multi-AZ instance deployment with a larger secondary standby instance. Provide the data scientists access to the secondary instance.
C. Change the setup from a Single-AZ to a Multi-AZ instance deployment. Provide two additional read replicas for the data scientists.
D. Change the setup from a Single-AZ to a Multi-AZ cluster deployment with two readable standby instances. Provide read endpoints to the data scientists.
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


### 539
A company wants to use the AWS Cloud to improve its on-premises disaster recovery (DR) configuration. The company's core production business application uses Microsoft SQL Server Standard, which runs on a virtual machine (VM). The application has a recovery point objective (RPO) of 30 seconds or fewer and a recovery time objective (RTO) of 60 minutes. The DR solution needs to minimize costs wherever possible.

Which solution will meet these requirements?

A. Configure a multi-site active/active setup between the on-premises server and AWS by using Microsoft SQL Server Enterprise with Always On availability groups.

B. Configure a warm standby Amazon RDS for SQL Server database on AWS. Configure AWS Database Migration Service (AWS DMS) to use change data capture (CDC).

C. Use AWS Elastic Disaster Recovery configured to replicate disk changes to AWS as a pilot light.

D. Use third-party backup software to capture backups every night. Store a secondary set of backups in Amazon S3.
<details>
  <summary>Click to show the answer</summary>
  Answer: B or C
</details>


### 540
A company has an on-premises server that uses an Oracle database to process and store customer information. The company wants to use an AWS database service to achieve higher availability and to improve application performance. The company also wants to offload reporting from its primary database system.

Which solution will meet these requirements in the MOST operationally efficient way?

A. Use AWS Database Migration Service (AWS DMS) to create an Amazon RDS DB instance in multiple AWS Regions. Point the reporting functions toward a separate DB instance from the primary DB instance.

B. Use Amazon RDS in a Single-AZ deployment to create an Oracle database. Create a read replica in the same zone as the primary DB instance. Direct the reporting functions to the read replica.

C. Use Amazon RDS deployed in a Multi-AZ cluster deployment to create an Oracle database. Direct the reporting functions to use the reader instance in the cluster deployment.

D. Use Amazon RDS deployed in a Multi-AZ instance deployment to create an Amazon Aurora database. Direct the reporting functions to the reader instances.
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


### 543
A company runs Amazon EC2 instances in multiple AWS accounts that are individually bled. The company recently purchased a Savings Pian. Because of changes in the company’s business requirements, the company has decommissioned a large number of EC2 instances. The company wants to use its Savings Plan discounts on its other AWS accounts.

Which combination of steps will meet these requirements? (Choose two.)

A. From the AWS Account Management Console of the management account, turn on discount sharing from the billing preferences section.
B. From the AWS Account Management Console of the account that purchased the existing Savings Plan, turn on discount sharing from the billing preferences section. Include all accounts.
C. From the AWS Organizations management account, use AWS Resource Access Manager (AWS RAM) to share the Savings Plan with other accounts.
D. Create an organization in AWS Organizations in a new payer account. Invite the other AWS accounts to join the organization from the management account.
E. Create an organization in AWS Organizations in the existing AWS account with the existing EC2 instances and Savings Plan. Invite the other AWS accounts to join the organization from the management account.
<details>
  <summary>Click to show the answer</summary>
  Answer: A, D
</details>


### 563
A company runs its applications on both Amazon Elastic Kubernetes Service (Amazon EKS) clusters and on-premises Kubernetes clusters. The company wants to view all clusters and workloads from a central location.

Which solution will meet these requirements with the LEAST operational overhead?

A. Use Amazon CloudWatch Container Insights to collect and group the cluster information.
B. Use Amazon EKS Connector to register and connect all Kubernetes clusters.
C. Use AWS Systems Manager to collect and view the cluster information.
D. Use Amazon EKS Anywhere as the primary cluster to view the other clusters with native Kubernetes commands.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 591
A company runs a container application by using Amazon Elastic Kubernetes Service (Amazon EKS). The application includes microservices that manage customers and place orders. The company needs to route incoming requests to the appropriate microservices.

Which solution will meet this requirement MOST cost-effectively?

A. Use the AWS Load Balancer Controller to provision a Network Load Balancer.
B. Use the AWS Load Balancer Controller to provision an Application Load Balancer.
C. Use an AWS Lambda function to connect the requests to Amazon EKS.
D. Use Amazon API Gateway to connect the requests to Amazon EKS.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 593
A solutions architect is designing a highly available Amazon ElastiCache for Redis based solution. The solutions architect needs to ensure that failures do not result in performance degradation or loss of data locally and within an AWS Region. The solution needs to provide high availability at the node level and at the Region level.

Which solution will meet these requirements?

A. Use Multi-AZ Redis replication groups with shards that contain multiple nodes.
B. Use Redis shards that contain multiple nodes with Redis append only files (AOF) turned on.
C. Use a Multi-AZ Redis cluster with more than one read replica in the replication group.
D. Use Redis shards that contain multiple nodes with Auto Scaling turned on.
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 598
A research company uses on-premises devices to generate data for analysis. The company wants to use the AWS Cloud to analyze the data. The devices generate .csv files and support writing the data to an SMB file share. Company analysts must be able to use SQL commands to query the data. The analysts will run queries periodically throughout the day.

Which combination of steps will meet these requirements MOST cost-effectively? (Choose three.)

A. Deploy an AWS Storage Gateway on premises in Amazon S3 File Gateway mode.
B. Deploy an AWS Storage Gateway on premises in Amazon FSx File Gateway made.
C. Set up an AWS Glue crawler to create a table based on the data that is in Amazon S3.
D. Set up an Amazon EMR cluster with EMR File System (EMRFS) to query the data that is in Amazon S3. Provide access to analysts.
E. Set up an Amazon Redshift cluster to query the data that is in Amazon S3. Provide access to analysts.
F. Setup Amazon Athena to query the data that is in Amazon S3. Provide access to analysts.
<details>
  <summary>Click to show the answer</summary>
  Answer: A, C, F
</details>


### 601
A company runs its critical database on an Amazon RDS for PostgreSQL DB instance. The company wants to migrate to Amazon Aurora PostgreSQL with minimal downtime and data loss.

Which solution will meet these requirements with the LEAST operational overhead?

A. Create a DB snapshot of the RDS for PostgreSQL DB instance to populate a new Aurora PostgreSQL DB cluster.
B. Create an Aurora read replica of the RDS for PostgreSQL DB instance. Promote the Aurora read replicate to a new Aurora PostgreSQL DB cluster.
C. Use data import from Amazon S3 to migrate the database to an Aurora PostgreSQL DB cluster.
D. Use the pg_dump utility to back up the RDS for PostgreSQL database. Restore the backup to a new Aurora PostgreSQL DB cluster.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 606
A solutions architect is designing an application that will allow business users to upload objects to Amazon S3. The solution needs to maximize object durability. Objects also must be readily available at any time and for any length of time. Users will access objects frequently within the first 30 days after the objects are uploaded, but users are much less likely to access objects that are older than 30 days.

Which solution meets these requirements MOST cost-effectively?

A. Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Glacier after 30 days.
B. Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.
C. Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 One Zone-Infrequent Access (S3 One Zone-IA) after 30 days.
D. Store all the objects in S3 Intelligent-Tiering with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 622
A company is creating a new web application for its subscribers. The application will consist of a static single page and a persistent database layer. The application will have millions of users for 4 hours in the morning, but the application will have only a few thousand users during the rest of the day. The company's data architects have requested the ability to rapidly evolve their schema.

Which solutions will meet these requirements and provide the MOST scalability? (Choose two.)

A. Deploy Amazon DynamoDB as the database solution. Provision on-demand capacity.
B. Deploy Amazon Aurora as the database solution. Choose the serverless DB engine mode.
C. Deploy Amazon DynamoDB as the database solution. Ensure that DynamoDB auto scaling is enabled.
D. Deploy the static content into an Amazon S3 bucket. Provision an Amazon CloudFront distribution with the S3 bucket as the origin.
E. Deploy the web servers for static content across a fleet of Amazon EC2 instances in Auto Scaling groups. Configure the instances to periodically refresh the content from an Amazon Elastic File System (Amazon EFS) volume.
<details>
  <summary>Click to show the answer</summary>
  Answer: A/C, D
</details>


### 638
A company collects and shares research data with the company's employees all over the world. The company wants to collect and store the data in an Amazon S3 bucket and process the data in the AWS Cloud. The company will share the data with the company's employees. The company needs a secure solution in the AWS Cloud that minimizes operational overhead.

Which solution will meet these requirements?

A. Use an AWS Lambda function to create an S3 presigned URL. Instruct employees to use the URL.
B. Create an IAM user for each employee. Create an IAM policy for each employee to allow S3 access. Instruct employees to use the AWS Management Console.
C. Create an S3 File Gateway. Create a share for uploading and a share for downloading. Allow employees to mount shares on their local computers to use S3 File Gateway.
D. Configure AWS Transfer Family SFTP endpoints. Select the custom identity provider options. Use AWS Secrets Manager to manage the user credentials Instruct employees to use Transfer Family.

<details>
  <summary>Click to show the answer</summary>
  Answer: D or A
</details>

### 640
A company has an application workflow that uses an AWS Lambda function to download and decrypt files from Amazon S3. These files are encrypted using AWS Key Management Service (AWS KMS) keys. A solutions architect needs to design a solution that will ensure the required permissions are set correctly.

Which combination of actions accomplish this? (Choose two.)

A. Attach the kms:decrypt permission to the Lambda function’s resource policy
B. Grant the decrypt permission for the Lambda IAM role in the KMS key's policy
C. Grant the decrypt permission for the Lambda resource policy in the KMS key's policy.
D. Create a new IAM policy with the kms:decrypt permission and attach the policy to the Lambda function.
E. Create a new IAM role with the kms:decrypt permission and attach the execution role to the Lambda function.
<details>
  <summary>Click to show the answer</summary>
  Answer: B, E
</details>


### 644
An international company has a subdomain for each country that the company operates in. The subdomains are formatted as example.com, country1.example.com, and country2.example.com. The company's workloads are behind an Application Load Balancer. The company wants to encrypt the website data that is in transit.

Which combination of steps will meet these requirements? (Choose two.)

A. Use the AWS Certificate Manager (ACM) console to request a public certificate for the apex top domain example com and a wildcard certificate for *.example.com.
B. Use the AWS Certificate Manager (ACM) console to request a private certificate for the apex top domain example.com and a wildcard certificate for *.example.com.
C. Use the AWS Certificate Manager (ACM) console to request a public and private certificate for the apex top domain example.com.
D. Validate domain ownership by email address. Switch to DNS validation by adding the required DNS records to the DNS provider.
E. Validate domain ownership for the domain by adding the required DNS records to the DNS provider.
<details>
  <summary>Click to show the answer</summary>
  Answer: A, E
</details>


### 653
A company maintains an Amazon RDS database that maps users to cost centers. The company has accounts in an organization in AWS Organizations. The company needs a solution that will tag all resources that are created in a specific AWS account in the organization. The solution must tag each resource with the cost center ID of the user who created the resource.

Which solution will meet these requirements?

A. Move the specific AWS account to a new organizational unit (OU) in Organizations from the management account. Create a service control policy (SCP) that requires all existing resources to have the correct cost center tag before the resources are created. Apply the SCP to the new OU.
B. Create an AWS Lambda function to tag the resources after the Lambda function looks up the appropriate cost center from the RDS database. Configure an Amazon EventBridge rule that reacts to AWS CloudTrail events to invoke the Lambda function.
C. Create an AWS CloudFormation stack to deploy an AWS Lambda function. Configure the Lambda function to look up the appropriate cost center from the RDS database and to tag resources. Create an Amazon EventBridge scheduled rule to invoke the CloudFormation stack.
D. Create an AWS Lambda function to tag the resources with a default value. Configure an Amazon EventBridge rule that reacts to AWS CloudTrail events to invoke the Lambda function when a resource is missing the cost center tag.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A OR B
</details>

### 657
A company has multiple AWS accounts in an organization in AWS Organizations that different business units use. The company has multiple offices around the world. The company needs to update security group rules to allow new office CIDR ranges or to remove old CIDR ranges across the organization. The company wants to centralize the management of security group rules to minimize the administrative overhead that updating CIDR ranges requires.

Which solution will meet these requirements MOST cost-effectively?

A. Create VPC security groups in the organization's management account. Update the security groups when a CIDR range update is necessary.
B. Create a VPC customer managed prefix list that contains the list of CIDRs. Use AWS Resource Access Manager (AWS RAM) to share the prefix list across the organization. Use the prefix list in the security groups across the organization.
C. Create an AWS managed prefix list. Use an AWS Security Hub policy to enforce the security group update across the organization. Use an AWS Lambda function to update the prefix list automatically when the CIDR ranges change.
D. Create security groups in a central administrative AWS account. Create an AWS Firewall Manager common security group policy for the whole organization. Select the previously created security groups as primary groups in the policy.
 <details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 664
A company has a web application that runs on premises. The application experiences latency issues during peak hours. The latency issues occur twice each month. At the start of a latency issue, the application's CPU utilization immediately increases to 10 times its normal amount.

The company wants to migrate the application to AWS to improve latency. The company also wants to scale the application automatically when application demand increases. The company will use AWS Elastic Beanstalk for application deployment.

Which solution will meet these requirements?

A. Configure an Elastic Beanstalk environment to use burstable performance instances in unlimited mode. Configure the environment to scale based on requests.
B. Configure an Elastic Beanstalk environment to use compute optimized instances. Configure the environment to scale based on requests.
C. Configure an Elastic Beanstalk environment to use compute optimized instances. Configure the environment to scale on a schedule.
D. Configure an Elastic Beanstalk environment to use burstable performance instances in unlimited mode. Configure the environment to scale on predictive metrics.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 667
A company is moving its data and applications to AWS during a multiyear migration project. The company wants to securely access data on Amazon S3 from the company's AWS Region and from the company's on-premises location. The data must not traverse the internet. The company has established an AWS Direct Connect connection between its Region and its on-premises location.

Which solution will meet these requirements?

A. Create gateway endpoints for Amazon S3. Use the gateway endpoints to securely access the data from the Region and the on-premises location.
B. Create a gateway in AWS Transit Gateway to access Amazon S3 securely from the Region and the on-premises location.
C. Create interface endpoints for Amazon S3. Use the interface endpoints to securely access the data from the Region and the on-premises location.
D. Use an AWS Key Management Service (AWS KMS) key to access the data securely from the Region and the on-premises location.
 <details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


### 670
A company performs tests on an application that uses an Amazon DynamoDB table. The tests run for 4 hours once a week. The company knows how many read and write operations the application performs to the table each second during the tests. The company does not currently use DynamoDB for any other use case. A solutions architect needs to optimize the costs for the table.

Which solution will meet these requirements?

A. Choose on-demand mode. Update the read and write capacity units appropriately.
B. Choose provisioned mode. Update the read and write capacity units appropriately.
C. Purchase DynamoDB reserved capacity for a 1-year term.
D. Purchase DynamoDB reserved capacity for a 3-year term.
 <details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 675
A company uses Amazon EC2 instances and Amazon Elastic Block Store (Amazon EBS) volumes to run an application. The company creates one snapshot of each EBS volume every day to meet compliance requirements. The company wants to implement an architecture that prevents the accidental deletion of EBS volume snapshots. The solution must not change the administrative rights of the storage administrator user.

Which solution will meet these requirements with the LEAST administrative effort?

A. Create an IAM role that has permission to delete snapshots. Attach the role to a new EC2 instance. Use the AWS CLI from the new EC2 instance to delete snapshots.
B. Create an IAM policy that denies snapshot deletion. Attach the policy to the storage administrator user.
C. Add tags to the snapshots. Create retention rules in Recycle Bin for EBS snapshots that have the tags.
D. Lock the EBS snapshots to prevent deletion.
 <details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


### 677
A company is developing an application that will run on a production Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The EKS cluster has managed node groups that are provisioned with On-Demand Instances.

The company needs a dedicated EKS cluster for development work. The company will use the development cluster infrequently to test the resiliency of the application. The EKS cluster must manage all the nodes.

Which solution will meet these requirements MOST cost-effectively?

A. Create a managed node group that contains only Spot Instances.
B. Create two managed node groups. Provision one node group with On-Demand Instances. Provision the second node group with Spot Instances.
C. Create an Auto Scaling group that has a launch configuration that uses Spot Instances. Configure the user data to add the nodes to the EKS cluster.
D. Create a managed node group that contains only On-Demand Instances.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A or B
</details>


### 679
A company wants to back up its on-premises virtual machines (VMs) to AWS. The company's backup solution exports on-premises backups to an Amazon S3 bucket as objects. The S3 backups must be retained for 30 days and must be automatically deleted after 30 days.

Which combination of steps will meet these requirements? (Choose three.)

A. Create an S3 bucket that has S3 Object Lock enabled.
B. Create an S3 bucket that has object versioning enabled.
C. Configure a default retention period of 30 days for the objects.
D. Configure an S3 Lifecycle policy to protect the objects for 30 days.
E. Configure an S3 Lifecycle policy to expire the objects after 30 days.
F. Configure the backup solution to tag the objects with a 30-day retention period
 <details>
  <summary>Click to show the answer</summary>
  Answer: A, C, E
</details>



### 682
A company needs a solution to enforce data encryption at rest on Amazon EC2 instances. The solution must automatically identify noncompliant resources and enforce compliance policies on findings.

Which solution will meet these requirements with the LEAST administrative overhead?

A. Use an IAM policy that allows users to create only encrypted Amazon Elastic Block Store (Amazon EBS) volumes. Use AWS Config and AWS Systems Manager to automate the detection and remediation of unencrypted EBS volumes.
B. Use AWS Key Management Service (AWS KMS) to manage access to encrypted Amazon Elastic Block Store (Amazon EBS) volumes. Use AWS Lambda and Amazon EventBridge to automate the detection and remediation of unencrypted EBS volumes.
C. Use Amazon Macie to detect unencrypted Amazon Elastic Block Store (Amazon EBS) volumes. Use AWS Systems Manager Automation rules to automatically encrypt existing and new EBS volumes.
D. Use Amazon inspector to detect unencrypted Amazon Elastic Block Store (Amazon EBS) volumes. Use AWS Systems Manager Automation rules to automatically encrypt existing and new EBS volumes.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 705
A company runs a three-tier application in a VPC. The database tier uses an Amazon RDS for MySQL DB instance.

The company plans to migrate the RDS for MySQL DB instance to an Amazon Aurora PostgreSQL DB cluster. The company needs a solution that replicates the data changes that happen during the migration to the new database.

Which combination of steps will meet these requirements? (Choose two.)

A. Use AWS Database Migration Service (AWS DMS) Schema Conversion to transform the database objects.
B. Use AWS Database Migration Service (AWS DMS) Schema Conversion to create an Aurora PostgreSQL read replica on the RDS for MySQL DB instance.
C. Configure an Aurora MySQL read replica for the RDS for MySQL DB instance.
D. Define an AWS Database Migration Service (AWS DMS) task with change data capture (CDC) to migrate the data.
E. Promote the Aurora PostgreSQL read replica to a standalone Aurora PostgreSQL DB cluster when the replica lag is zero.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A, D
</details>


### 709
A company has an organization in AWS Organizations. The company runs Amazon EC2 instances across four AWS accounts in the root organizational unit (OU). There are three nonproduction accounts and one production account. The company wants to prohibit users from launching EC2 instances of a certain size in the nonproduction accounts. The company has created a service control policy (SCP) to deny access to launch instances that use the prohibited types.

Which solutions to deploy the SCP will meet these requirements? (Choose two.)

A. Attach the SCP to the root OU for the organization.
B. Attach the SCP to the three nonproduction Organizations member accounts.
C. Attach the SCP to the Organizations management account.
D. Create an OU for the production account. Attach the SCP to the OU. Move the production member account into the new OU.
E. Create an OU for the required accounts. Attach the SCP to the OU. Move the nonproduction member accounts into the new OU.
 <details>
  <summary>Click to show the answer</summary>
  Answer: B, E
</details>


### 719
A company is designing a web application on AWS. The application will use a VPN connection between the company’s existing data centers and the company's VPCs.

The company uses Amazon Route 53 as its DNS service. The application must use private DNS records to communicate with the on-premises services from a VPC.

Which solution will meet these requirements in the MOST secure manner?

A. Create a Route 53 Resolver outbound endpoint. Create a resolver rule. Associate the resolver rule with the VPC.
B. Create a Route 53 Resolver inbound endpoint. Create a resolver rule. Associate the resolver rule with the VPC.
C. Create a Route 53 private hosted zone. Associate the private hosted zone with the VPC.
D. Create a Route 53 public hosted zone. Create a record for each service to allow service communication
 <details>
  <summary>Click to show the answer</summary>
  Answer: B, E
</details>


### 724
A company runs container applications by using Amazon Elastic Kubernetes Service (Amazon EKS) and the Kubernetes Horizontal Pod Autoscaler. The workload is not consistent throughout the day. A solutions architect notices that the number of nodes does not automatically scale out when the existing nodes have reached maximum capacity in the cluster, which causes performance issues.

Which solution will resolve this issue with the LEAST administrative overhead?

A. Scale out the nodes by tracking the memory usage.
B. Use the Kubernetes Cluster Autoscaler to manage the number of nodes in the cluster.
C. Use an AWS Lambda function to resize the EKS cluster automatically.
D. Use an Amazon EC2 Auto Scaling group to distribute the workload.
 <details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 737
A company has an application that delivers on-demand training videos to students around the world. The application also allows authorized content developers to upload videos. The data is stored in an Amazon S3 bucket in the us-east-2 Region.

The company has created an S3 bucket in the eu-west-2 Region and an S3 bucket in the ap-southeast-1 Region. The company wants to replicate the data to the new S3 buckets. The company needs to minimize latency for developers who upload videos and students who stream videos near eu-west-2 and ap-southeast-1.

Which combination of steps will meet these requirements with the FEWEST changes to the application? (Choose two.)

A. Configure one-way replication from the us-east-2 S3 bucket to the eu-west-2 S3 bucket. Configure one-way replication from the us-east-2 S3 bucket to the ap-southeast-1 S3 bucket.
B. Configure one-way replication from the us-east-2 S3 bucket to the eu-west-2 S3 bucket. Configure one-way replication from the eu-west-2 S3 bucket to the ap-southeast-1 S3 bucket.
C. Configure two-way (bidirectional) replication among the S3 buckets that are in all three Regions.
D. Create an S3 Multi-Region Access Point. Modify the application to use the Amazon Resource Name (ARN) of the Multi-Region Access Point for video streaming. Do not modify the application for video uploads.
E. Create an S3 Multi-Region Access Point. Modify the application to use the Amazon Resource Name (ARN) of the Multi-Region Access Point for video streaming and uploads.
 <details>
  <summary>Click to show the answer</summary>
  Answer: AE or CE
</details>


### 738
A company has a new mobile app. Anywhere in the world, users can see local news on topics they choose. Users also can post photos and videos from inside the app.

Users access content often in the first minutes after the content is posted. New content quickly replaces older content, and then the older content disappears. The local nature of the news means that users consume 90% of the content within the AWS Region where it is uploaded.

Which solution will optimize the user experience by providing the LOWEST latency for content uploads?

A. Upload and store content in Amazon S3. Use Amazon CloudFront for the uploads.
B. Upload and store content in Amazon S3. Use S3 Transfer Acceleration for the uploads.
C. Upload content to Amazon EC2 instances in the Region that is closest to the user. Copy the data to Amazon S3.
D. Upload and store content in Amazon S3 in the Region that is closest to the user. Use multiple distributions of Amazon CloudFront.
 <details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 754
A company has users all around the world accessing its HTTP-based application deployed on Amazon EC2 instances in multiple AWS Regions. The company wants to improve the availability and performance of the application. The company also wants to protect the application against common web exploits that may affect availability, compromise security, or consume excessive resources. Static IP addresses are required.

What should a solutions architect recommend to accomplish this?

A. Put the EC2 instances behind Network Load Balancers (NLBs) in each Region. Deploy AWS WAF on the NLBs. Create an accelerator using AWS Global Accelerator and register the NLBs as endpoints.
B. Put the EC2 instances behind Application Load Balancers (ALBs) in each Region. Deploy AWS WAF on the ALBs. Create an accelerator using AWS Global Accelerator and register the ALBs as endpoints.
C. Put the EC2 instances behind Network Load Balancers (NLBs) in each Region. Deploy AWS WAF on the NLBs. Create an Amazon CloudFront distribution with an origin that uses Amazon Route 53 latency-based routing to route requests to the NLBs.
D. Put the EC2 instances behind Application Load Balancers (ALBs) in each Region. Create an Amazon CloudFront distribution with an origin that uses Amazon Route 53 latency-based routing to route requests to the ALBs. Deploy AWS WAF on the CloudFront distribution.

 <details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 757
A company is running a legacy system on an Amazon EC2 instance. The application code cannot be modified, and the system cannot run on more than one instance. A solutions architect must design a resilient solution that can improve the recovery time for the system.

What should the solutions architect recommend to meet these requirements?

A. Enable termination protection for the EC2 instance.
B. Configure the EC2 instance for Multi-AZ deployment.
C. Create an Amazon CloudWatch alarm to recover the EC2 instance in case of failure.
D. Launch the EC2 instance with two Amazon Elastic Block Store (Amazon EBS) volumes that use RAID configurations for storage redundancy.
 <details>
  <summary>Click to show the answer</summary>
  Answer: C?
</details>


### 762
A company stores multiple Amazon Machine Images (AMIs) in an AWS account to launch its Amazon EC2 instances. The AMIs contain critical data and configurations that are necessary for the company’s operations. The company wants to implement a solution that will recover accidentally deleted AMIs quickly and efficiently.

Which solution will meet these requirements with the LEAST operational overhead?

A. Create Amazon Elastic Block Store (Amazon EBS) snapshots of the AMIs. Store the snapshots in a separate AWS account.
B. Copy all AMIs to another AWS account periodically.
C. Create a retention rule in Recycle Bin.
D. Upload the AMIs to an Amazon S3 bucket that has Cross-Region Replication.
 <details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>

### 775
Use Amazon Elastic Kubernetes Service (Amazon EKS) with Amazon EC2 worker nodes.

A company has deployed an application in an AWS account. The application consists of microservices that run on AWS Lambda and Amazon Elastic Kubernetes Service (Amazon EKS). A separate team supports each microservice. The company has multiple AWS accounts and wants to give each team its own account for its microservices.

A solutions architect needs to design a solution that will provide service-to-service communication over HTTPS (port 443). The solution also must provide a service registry for service discovery.

Which solution will meet these requirements with the LEAST administrative overhead?

A. Create an inspection VPC. Deploy an AWS Network Firewall firewall to the inspection VPC. Attach the inspection VPC to a new transit gateway. Route VPC-to-VPC traffic to the inspection VPC. Apply firewall rules to allow only HTTPS communication.
B. Create a VPC Lattice service network. Associate the microservices with the service network. Define HTTPS listeners for each service. Register microservice compute resources as targets. Identify VPCs that need to communicate with the services. Associate those VPCs with the service network.
C. Create a Network Load Balancer (NLB) with an HTTPS listener and target groups for each microservice. Create an AWS PrivateLink endpoint service for each microservice. Create an interface VPC endpoint in each VPC that needs to consume that microservice.
D. Create peering connections between VPCs that contain microservices. Create a prefix list for each service that requires a connection to a client. Create route tables to route traffic to the appropriate VPC. Create security groups to allow only HTTPS communication.
 <details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 777
A company uses AWS Organizations for its multi-account AWS setup. The security organizational unit (OU) of the company needs to share approved Amazon Machine Images (AMIs) with the development OU. The AMIs are created by using AWS Key Management Service (AWS KMS) encrypted snapshots.

Which solution will meet these requirements? (Choose two.)

A. Add the development team's OU Amazon Resource Name (ARN) to the launch permission list for the AMIs.

B. Add the Organizations root Amazon Resource Name (ARN) to the launch permission list for the AMIs.

C. Update the key policy to allow the development team's OU to use the AWS KMS keys that are used to decrypt the snapshots.

D. Add the development team’s account Amazon Resource Name (ARN) to the launch permission list for the AMIs.

E. Recreate the AWS KMS key. Add a key policy to allow the Organizations root Amazon Resource Name (ARN) to use the AWS KMS key.
 <details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 778
A data analytics company has 80 offices that are distributed globally. Each office hosts 1 PB of data and has between 1 and 2 Gbps of internet bandwidth.

The company needs to perform a one-time migration of a large amount of data from its offices to Amazon S3. The company must complete the migration within 4 weeks.

Which solution will meet these requirements MOST cost-effectively?

A. Establish a new 10 Gbps AWS Direct Connect connection to each office. Transfer the data to Amazon S3.

B. Use multiple AWS Snowball Edge storage-optimized devices to store and transfer the data to Amazon S3.

C. Use an AWS Snowmobile to store and transfer the data to Amazon S3.

D. Set up an AWS Storage Gateway Volume Gateway to transfer the data to Amazon S3.
 <details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 789
A company needs a solution to prevent AWS CloudFormation stacks from deploying AWS Identity and Access Management (IAM) resources that include an inline policy or “*” in the statement. The solution must also prohibit deployment of Amazon EC2 instances with public IP addresses. The company has AWS Control Tower enabled in its organization in AWS Organizations.

Which solution will meet these requirements?

A. Use AWS Control Tower proactive controls to block deployment of EC2 instances with public IP addresses and inline policies with elevated access or “*”.

B. Use AWS Control Tower detective controls to block deployment of EC2 instances with public IP addresses and inline policies with elevated access or “*”.

C. Use AWS Config to create rules for EC2 and IAM compliance. Configure the rules to run an AWS Systems Manager Session Manager automation to delete a resource when it is not compliant.

D. Use a service control policy (SCP) to block actions for the EC2 instances and IAM resources if the actions lead to noncompliance.
<details>
  <summary>Click to show the answer</summary>
  Answer: A or D
</details>


### 807
A company uses high concurrency AWS Lambda functions to process a constantly increasing number of messages in a message queue during marketing events. The Lambda functions use CPU intensive code to process the messages. The company wants to reduce the compute costs and to maintain service latency for its customers.

Which solution will meet these requirements?

A. Configure reserved concurrency for the Lambda functions. Decrease the memory allocated to the Lambda functions.

B. Configure reserved concurrency for the Lambda functions. Increase the memory according to AWS Compute Optimizer recommendations.

C. Configure provisioned concurrency for the Lambda functions. Decrease the memory allocated to the Lambda functions.

D. Configure provisioned concurrency for the Lambda functions. Increase the memory according to AWS Compute Optimizer recommendations.

<details>
  <summary>Click to show the answer</summary>
  Answer: B or D
</details>

### 813
A solutions architect runs a web application on multiple Amazon EC2 instances that are in individual target groups behind an Application Load Balancer (ALB). Users can reach the application through a public website.

The solutions architect wants to allow engineers to use a development version of the website to access one specific development EC2 instance to test new features for the application. The solutions architect wants to use an Amazon Route 53 hosted zone to give the engineers access to the development instance. The solution must automatically route to the development instance even if the development instance is replaced.

Which solution will meet these requirements?

A. Create an A Record for the development website that has the value set to the ALB. Create a listener rule on the ALB that forwards requests for the development website to the target group that contains the development instance.

B. Recreate the development instance with a public IP address. Create an A Record for the development website that has the value set to the public IP address of the development instance.

C. Create an A Record for the development website that has the value set to the ALB. Create a listener rule on the ALB to redirect requests for the development website to the public IP address of the development instance.

D. Place all the instances in the same target group. Create an A Record for the development website. Set the value to the ALB. Create a listener rule on the ALB that forwards requests for the development website to the target group.
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 827
A company is planning to deploy its application on an Amazon Aurora PostgreSQL Serverless v2 cluster. The application will receive large amounts of traffic. The company wants to optimize the storage performance of the cluster as the load on the application increases.

Which solution will meet these requirements MOST cost-effectively?

A. Configure the cluster to use the Aurora Standard storage configuration.

B. Configure the cluster storage type as Provisioned IOPS.

C. Configure the cluster storage type as General Purpose.

D. Configure the cluster to use the Aurora I/O-Optimized storage configuration.
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>



### 841
A company uses Amazon EC2 instances and Amazon Elastic Block Store (Amazon EBS) to run its self-managed database. The company has 350 TB of data spread across all EBS volumes. The company takes daily EBS snapshots and keeps the snapshots for 1 month. The daily change rate is 5% of the EBS volumes.

Because of new regulations, the company needs to keep the monthly snapshots for 7 years. The company needs to change its backup strategy to comply with the new regulations and to ensure that data is available with minimal administrative effort.

Which solution will meet these requirements MOST cost-effectively?

A. Keep the daily snapshot in the EBS snapshot standard tier for 1 month. Copy the monthly snapshot to Amazon S3 Glacier Deep Archive with a 7-year retention period.

B. Continue with the current EBS snapshot policy. Add a new policy to move the monthly snapshot to Amazon EBS Snapshots Archive with a 7-year retention period.

C. Keep the daily snapshot in the EBS snapshot standard tier for 1 month. Keep the monthly snapshot in the standard tier for 7 years. Use incremental snapshots.

D. Keep the daily snapshot in the EBS snapshot standard tier. Use EBS direct APIs to take snapshots of all the EBS volumes every month. Store the snapshots in an Amazon S3 bucket in the Infrequent Access tier for 7 years.

<details>
  <summary>Click to show the answer</summary>
  Answer: A or B?
</details>


### 844
A company has an on-premises business application that generates hundreds of files each day. These files are stored on an SMB file share and require a low-latency connection to the application servers. A new company policy states all application-generated files must be copied to AWS. There is already a VPN connection to AWS.

The application development team does not have time to make the necessary code modifications to move the application to AWS.

Which service should a solutions architect recommend to allow the application to copy files to AWS?

A. Amazon Elastic File System (Amazon EFS)

B. Amazon FSx for Windows File Server

C. AWS Snowball

D. AWS Storage Gateway

<details>
  <summary>Click to show the answer</summary>
  Answer: B or D?
</details>


### 859
A company runs several Amazon RDS for Oracle On-Demand DB instances that have high utilization. The RDS DB instances run in member accounts that are in an organization in AWS Organizations.

The company's finance team has access to the organization's management account and member accounts. The finance team wants to find ways to optimize costs by using AWS Trusted Advisor.

Which combination of steps will meet these requirements? (Choose two.)

A. Use the Trusted Advisor recommendations in the management account.

B. Use the Trusted Advisor recommendations in the member accounts where the RDS DB instances are running.

C. Review the Trusted Advisor checks for Amazon RDS Reserved Instance Optimization.

D. Review the Trusted Advisor checks for Amazon RDS Idle DB Instances.

E. Review the Trusted Advisor checks for compute optimization. Crosscheck the results by using AWS Compute Optimizer.

<details>
  <summary>Click to show the answer</summary>
  Answer: A, C
</details>


### 870
A company has two AWS accounts: Production and Development. The company needs to push code changes in the Development account to the Production account. In the alpha phase, only two senior developers on the development team need access to the Production account. In the beta phase, more developers will need access to perform testing.

Which solution will meet these requirements?

A. Create two policy documents by using the AWS Management Console in each account. Assign the policy to developers who need access.

B. Create an IAM role in the Development account. Grant the IAM role access to the Production account. Allow developers to assume the role.

C. Create an IAM role in the Production account. Define a trust policy that specifies the Development account. Allow developers to assume the role.

D. Create an IAM group in the Production account. Add the group as a principal in a trust policy that specifies the Production account. Add developers to the group.
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 878
A company creates dedicated AWS accounts in AWS Organizations for its business units. Recently, an important notification was sent to the root user email address of a business unit account instead of the assigned account owner. The company wants to ensure that all future notifications can be sent to different employees based on the notification categories of billing, operations, or security.

Which solution will meet these requirements MOST securely?

A. Configure each AWS account to use a single email address that the company manages. Ensure that all account owners can access the email account to receive notifications. Configure alternate contacts for each AWS account with corresponding distribution lists for the billing team, the security team, and the operations team for each business unit.

B. Configure each AWS account to use a different email distribution list for each business unit that the company manages. Configure each distribution list with administrator email addresses that can respond to alerts. Configure alternate contacts for each AWS account with corresponding distribution lists for the billing team, the security team, and the operations team for each business unit.

C. Configure each AWS account root user email address to be the individual company managed email address of one person from each business unit. Configure alternate contacts for each AWS account with corresponding distribution lists for the billing team, the security team, and the operations team for each business unit.

D. Configure each AWS account root user to use email aliases that go to a centralized mailbox. Configure alternate contacts for each account by using a single business managed email distribution list each for the billing team, the security team, and the operations team.
<details>
  <summary>Click to show the answer</summary>
  Answer: D
</details>


### 879
A company runs an ecommerce application on AWS. Amazon EC2 instances process purchases and store the purchase details in an Amazon Aurora PostgreSQL DB cluster.

Customers are experiencing application timeouts during times of peak usage. A solutions architect needs to rearchitect the application so that the application can scale to meet peak usage demands.

Which combination of actions will meet these requirements MOST cost-effectively? (Choose two.)

A. Configure an Auto Scaling group of new EC2 instances to retry the purchases until the processing is complete. Update the applications to connect to the DB cluster by using Amazon RDS Proxy.

B. Configure the application to use an Amazon ElastiCache cluster in front of the Aurora PostgreSQL DB cluster.

C. Update the application to send the purchase requests to an Amazon Simple Queue Service (Amazon SQS) queue. Configure an Auto Scaling group of new EC2 instances that read from the SQS queue.

D. Configure an AWS Lambda function to retry the ticket purchases until the processing is complete.

E. Configure an Amazon AP! Gateway REST API with a usage plan.
<details>
  <summary>Click to show the answer</summary>
  Answer: AC or BC
</details>


### 881
A company is hosting a high-traffic static website on Amazon S3 with an Amazon CloudFront distribution that has a default TTL of 0 seconds. The company wants to implement caching to improve performance for the website. However, the company also wants to ensure that stale content is not served for more than a few minutes after a deployment.

Which combination of caching methods should a solutions architect implement to meet these requirements? (Choose two.)

A. Set the CloudFront default TTL to 2 minutes.

B. Set a default TTL of 2 minutes on the S3 bucket.

C. Add a Cache-Control private directive to the objects in Amazon S3.

D. Create an AWS Lambda@Edge function to add an Expires header to HTTP responses. Configure the function to run on viewer response.

E. Add a Cache-Control max-age directive of 24 hours to the objects in Amazon S3. On deployment, create a CloudFront invalidation to clear any changed files from edge caches.
<details>
  <summary>Click to show the answer</summary>
  Answer: AC or AE
</details>


### 887
A solutions architect must design a solution to ensure that all newly created Amazon EBS volumes are encrypted by default. The solution must also prevent the creation of unencrypted EBS volumes.

Which solution will meet these requirements?

A. Configure the EC2 account attributes to always encrypt new EBS volumes. <br>
B. Use AWS Config. Configure the encrypted-volumes identifier. Apply the default AWS Key Management Service (AWS KMS) key. <br>
C. Configure AWS Systems Manager to create encrypted copies of the EBS volumes. Reconfigure the EC2 instances to use the encrypted volumes. <br>
D. Create a customer managed key in AWS Key Management Service (AWS KMS). Configure AWS Migration Hub to use the key when the company migrates workloads. <br>
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>



### 890
A company needs to optimize its Amazon S3 storage costs for an application that generates many files that cannot be recreated. Each file is approximately 5 MB and is stored in Amazon S3 Standard storage.

The company must store the files for 4 years before the files can be deleted. The files must be immediately accessible. The files are frequently accessed in the first 30 days of object creation, but they are rarely accessed after the first 30 days.

Which solution will meet these requirements MOST cost-effectively?

A. Create an S3 Lifecycle policy to move the files to S3 Glacier Instant Retrieval 30 days after object creation. Delete the files 4 years after object creation. <br> 
B. Create an S3 Lifecycle policy to move the files to S3 One Zone-Infrequent Access (S3 One Zone-IA) 30 days after object creation. Delete the files 4 years after object creation. <br>
C. Create an S3 Lifecycle policy to move the files to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days after object creation. Delete the files 4 years after object creation. <br>
D. Create an S3 Lifecycle policy to move the files to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days after object creation. Move the files to S3 Glacier Flexible Retrieval 4 years after object creation. <br>

<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>

### 890
A company is migrating a data center from its on-premises location to AWS. The company has several legacy applications that are hosted on individual virtual servers. Changes to the application designs cannot be made.

Each individual virtual server currently runs as its own EC2 instance. A solutions architect needs to ensure that the applications are reliable and fault tolerant after migration to AWS. The applications will run on Amazon EC2 instances.

Which solution will meet these requirements?

A. Create an Auto Scaling group that has a minimum of one and a maximum of one. Create an Amazon Machine Image (AMI) of each application instance. Use the AMI to create EC2 instances in the Auto Scaling group Configure an Application Load Balancer in front of the Auto Scaling group. <br>
B. Use AWS Backup to create an hourly backup of the EC2 instance that hosts each application. Store the backup in Amazon S3 in a separate Availability Zone. Configure a disaster recovery process to restore the EC2 instance for each application from its most recent backup. <br>
C. Create an Amazon Machine Image (AMI) of each application instance. Launch two new EC2 instances from the AMI. Place each EC2 instance in a separate Availability Zone. Configure a Network Load Balancer that has the EC2 instances as targets. <br>
D. Use AWS Mitigation Hub Refactor Spaces to migrate each application off the EC2 instance. Break down functionality from each application into individual components. Host each application on Amazon Elastic Container Service (Amazon ECS) with an AWS Fargate launch type. <br>
<details>
  <summary>Click to show the answer</summary>
  Answer: A or C
</details>


### 893
A company wants to isolate its workloads by creating an AWS account for each workload. The company needs a solution that centrally manages networking components for the workloads. The solution also must create accounts with automatic security controls (guardrails).

Which solution will meet these requirements with the LEAST operational overhead?

A. Use AWS Control Tower to deploy accounts. Create a networking account that has a VPC with private subnets and public subnets. Use AWS Resource Access Manager (AWS RAM) to share the subnets with the workload accounts.
B. Use AWS Organizations to deploy accounts. Create a networking account that has a VPC with private subnets and public subnets. Use AWS Resource Access Manager (AWS RAM) to share the subnets with the workload accounts.
C. Use AWS Control Tower to deploy accounts. Deploy a VPC in each workload account. Configure each VPC to route through an inspection VPC by using a transit gateway attachment.
D. Use AWS Organizations to deploy accounts. Deploy a VPC in each workload account. Configure each VPC to route through an inspection VPC by using a transit gateway attachment.
<details>
  <summary>Click to show the answer</summary>
  Answer: A
</details>


### 896
A company is designing its production application's disaster recovery (DR) strategy. The application is backed by a MySQL database on an Amazon Aurora cluster in the us-east-1 Region. The company has chosen the us-west-1 Region as its DR Region.

The company's target recovery point objective (RPO) is 5 minutes and the target recovery time objective (RTO) is 20 minutes. The company wants to minimize configuration changes.

Which solution will meet these requirements with the MOST operational efficiency?

A. Create an Aurora read replica in us-west-1 similar in size to the production application's Aurora MySQL cluster writer instance.
B. Convert the Aurora cluster to an Aurora global database. Configure managed failover.
C. Create a new Aurora cluster in us-west-1 that has Cross-Region Replication.
D. Create a new Aurora cluster in us-west-1. Use AWS Database Migration Service (AWS DMS) to sync both clusters.

<details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


### 905
A company wants to improve the availability and performance of its hybrid application. The application consists of a stateful TCP-based workload hosted on Amazon EC2 instances in different AWS Regions and a stateless UDP-based workload hosted on premises.

Which combination of actions should a solutions architect take to improve availability and performance? (Choose two.)

A. Create an accelerator using AWS Global Accelerator. Add the load balancers as endpoints.
B. Create an Amazon CloudFront distribution with an origin that uses Amazon Route 53 latency-based routing to route requests to the load balancers.
C. Configure two Application Load Balancers in each Region. The first will route to the EC2 endpoints, and the second will route to the on-premises endpoints.
D. Configure a Network Load Balancer in each Region to address the EC2 endpoints. Configure a Network Load Balancer in each Region that routes to the on-premises endpoints.
E. Configure a Network Load Balancer in each Region to address the EC2 endpoints. Configure an Application Load Balancer in each Region that routes to the on-premises endpoints.

<details>
  <summary>Click to show the answer</summary>
  Answer: A, D
</details>


 
### 923
A company hosts a monolithic web application on an Amazon EC2 instance. Application users have recently reported poor performance at specific times. Analysis of Amazon CloudWatch metrics shows that CPU utilization is 100% during the periods of poor performance.

The company wants to resolve this performance issue and improve application availability.

Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

A. Use AWS Compute Optimizer to obtain a recommendation for an instance type to scale vertically.
B. Create an Amazon Machine Image (AMI) from the web server. Reference the AMI in a new launch template.
C. Create an Auto Scaling group and an Application Load Balancer to scale vertically.
D. Use AWS Compute Optimizer to obtain a recommendation for an instance type to scale horizontally.
E. Create an Auto Scaling group and an Application Load Balancer to scale horizontally.

<details>
  <summary>Click to show the answer</summary>
  Answer: AE or BE
</details>




### 928
A company hosts a video streaming web application in a VPC. The company uses a Network Load Balancer (NLB) to handle TCP traffic for real-time data processing. There have been unauthorized attempts to access the application.

The company wants to improve application security with minimal architectural change to prevent unauthorized attempts to access the application.

Which solution will meet these requirements?

A. Implement a series of AWS WAF rules directly on the NLB to filter out unauthorized traffic.
B. Recreate the NLB with a security group to allow only trusted IP addresses.
C. Deploy a second NLB in parallel with the existing NLB configured with a strict IP address allow list.
D. Use AWS Shield Advanced to provide enhanced DDoS protection and prevent unauthorized access attempts.
 
<details>
  <summary>Click to show the answer</summary>
  Answer: B
</details>


### 931
A. Create an IAM resource policy for the Lambda function that allows Amazon SNS to invoke the function. <br> 
B. Implement an Amazon Simple Queue Service (Amazon SQS) queue in the administrator account to buffer messages from the SNS topic that is in the production account. Configure the SQS queue to invoke the Lambda function. <br>
C. Create an IAM policy for the SNS topic that allows the Lambda function to subscribe to the topic. <br>
D. Use an Amazon EventBridge rule in the production account to capture the SNS topic notifications. Configure the EventBridge rule to forward notifications to the Lambda function that is in the administrator account. <br>
E. Store performance metrics in an Amazon S3 bucket in the production account. Use Amazon Athena to analyze the metrics from the administrator account. <br>
<details>
  <summary>Click to show the answer</summary>
  Answer: A, C
</details>


### 935
A software company needs to upgrade a critical web application. The application currently runs on a single Amazon EC2 instance that the company hosts in a public subnet. The EC2 instance runs a MySQL database. The application's DNS records are published in an Amazon Route 53 zone.

A solutions architect must reconfigure the application to be scalable and highly available. The solutions architect must also reduce MySQL read latency.

Which combination of solutions will meet these requirements? (Choose two.)

A. Launch a second EC2 instance in a second AWS Region. Use a Route 53 failover routing policy to redirect the traffic to the second EC2 instance. <br>
B. Create and configure an Auto Scaling group to launch private EC2 instances in multiple Availability Zones. Add the instances to a target group behind a new Application Load Balancer. <br>
C. Migrate the database to an Amazon Aurora MySQL cluster. Create the primary DB instance and reader DB instance in separate Availability Zones. <br>
D. Create and configure an Auto Scaling group to launch private EC2 instances in multiple AWS Regions. Add the instances to a target group behind a new Application Load Balancer.
E. Migrate the database to an Amazon Aurora MySQL cluster with cross-Region read replicas. <br>
<details>
  <summary>Click to show the answer</summary>
  Answer: B, C
</details>


### 941
A company is using an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The company must ensure that Kubernetes service accounts in the EKS cluster have secure and granular access to specific AWS resources by using IAM roles for service accounts (IRSA).

Which combination of solutions will meet these requirements? (Choose two.)

A. Create an IAM policy that defines the required permissions Attach the policy directly to the IAM role of the EKS nodes.
B. Implement network policies within the EKS cluster to prevent Kubernetes service accounts from accessing specific AWS services.
C. Modify the EKS cluster's IAM role to include permissions for each Kubernetes service account. Ensure a one-to-one mapping between IAM roles and Kubernetes roles.
D. Define an IAM role that includes the necessary permissions. Annotate the Kubernetes service accounts with the Amazon ResourceName (ARN) of the IAM role.
E. Set up a trust relationship between the IAM roles for the service accounts and an OpenID Connect (OIDC) identity provider.
<details>
  <summary>Click to show the answer</summary>
  Answer: D, E
</details>


### 942
A company regularly uploads confidential data to Amazon S3 buckets for analysis.

The company's security policies mandate that the objects must be encrypted at rest. The company must automatically rotate the encryption key every year. The company must be able to track key rotation by using AWS CloudTrail. The company also must minimize costs for the encryption key.

Which solution will meet these requirements?

A. Use server-side encryption with customer-provided keys (SSE-C)
B. Use server-side encryption with Amazon S3 managed keys (SSE-S3)
C. Use server-side encryption with AWS KMS keys (SSE-KMS)
D. Use server-side encryption with customer managed AWS KMS keys

<details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


### 973
A company is designing a web application with an internet-facing Application Load Balancer (ALB).

The company needs the ALB to receive HTTPS web traffic from the public internet. The ALB must send only HTTPS traffic to the web application servers hosted on the Amazon EC2 instances on port 443. The ALB must perform a health check of the web application servers over HTTPS on port 8443.

Which combination of configurations of the security group that is associated with the ALB will meet these requirements? (Choose three.)

A. Allow HTTPS inbound traffic from 0.0.0.0/0 for port 443.
B. Allow all outbound traffic to 0.0.0.0/0 for port 443.
C. Allow HTTPS outbound traffic to the web application instances for port 443.
D. Allow HTTPS inbound traffic from the web application instances for port 443.
E. Allow HTTPS outbound traffic to the web application instances for the health check on port 8443.
F. Allow HTTPS inbound traffic from the web application instances for the health check on port 8443.

<details>
  <summary>Click to show the answer</summary>
  Answer: A, C, E
</details>


### 993
A solutions architect is creating an application that will handle batch processing of large amounts of data. The input data will be held in Amazon S3 and the output data will be stored in a different S3 bucket. For processing, the application will transfer the data over the network between multiple Amazon EC2 instances.

What should the solutions architect do to reduce the overall data transfer costs?

A. Place all the EC2 instances in an Auto Scaling group.
B. Place all the EC2 instances in the same AWS Region.
C. Place all the EC2 instances in the same Availability Zone.
D. Place all the EC2 instances in private subnets in multiple Availability Zones.
<details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


### 1017
A company has an application that runs on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster on Amazon EC2 instances. The application has a UI that uses Amazon DynamoDB and data services that use Amazon S3 as part of the application deployment.

The company must ensure that the EKS Pods for the UI can access only Amazon DynamoDB and that the EKS Pods for the data services can access only Amazon S3. The company uses AWS Identity and Access Management (IAM).

Which solution meals these requirements?

A. Create separate IAM policies for Amazon S3 and DynamoDB access with the required permissions. Attach both IAM policies to the EC2 instance profile. Use role-based access control (RBAC) to control access to Amazon S3 or DynamoDB for the respective EKS Pods.
B. Create separate IAM policies for Amazon S3 and DynamoDB access with the required permissions. Attach the Amazon S3 IAM policy directly to the EKS Pods for the data services and the DynamoDB policy to the EKS Pods for the UI.
C. Create separate Kubernetes service accounts for the UI and data services to assume an IAM role. Attach the AmazonS3FullAccess policy to the data services account and the AmazonDynamoDBFullAccess policy to the UI service account.
D. Create separate Kubernetes service accounts for the UI and data services to assume an IAM role. Use IAM Role for Service Accounts (IRSA) to provide access to the EKS Pods for the UI to Amazon S3 and the EKS Pods for the data services to DynamoDB.
<details>
  <summary>Click to show the answer</summary>
  Answer: C
</details>


### 1019
A company is developing an application in the AWS Cloud. The application's HTTP API contains critical information that is published in Amazon API Gateway. The critical information must be accessible from only a limited set of trusted IP addresses that belong to the company's internal network.

Which solution will meet these requirements?

A. Set up an API Gateway private integration to restrict access to a predefined set of IP addresses.
B. Create a resource policy for the API that denies access to any IP address that is not specifically allowed.
C. Directly deploy the API in a private subnet. Create a network ACL. Set up rules to allow the traffic from specific IP addresses.
D. Modify the security group that is attached to API Gateway to allow inbound traffic from only the trusted IP addresses.
<details>
  <summary>Click to show the answer</summary>
  Answer: b
</details>