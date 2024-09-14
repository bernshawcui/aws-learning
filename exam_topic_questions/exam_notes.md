# Exam Topic Questions

## Question: 5.png

<img src="5.png" alt="Question" width="800">

### Notes:

- 































## Question: 6.png

<img src="6.png" alt="Question" width="800">

### Notes:

- 































## Question: 12.png

<img src="12.png" alt="Question" width="800">

### Notes:

- 































## Question: 19.png

<img src="19.png" alt="Question" width="800">

### Notes:

- 































## Question: 20.png

<img src="20.png" alt="Question" width="800">

### Notes:

- 































## Question: 24.png

<img src="24.png" alt="Question" width="800">

### Notes:

- 
































## Question: 25.jpeg

<img src="25.jpeg" alt="Question" width="800">

### Notes:

- 






























## Question: 27.png

<img src="27.png" alt="Question" width="800">

### Notes:

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.html  
- Share a single dashboard and designate specific email addresses of the people who can view the dashboard. Each of these users creates their own password that they must enter to view the dashboard.































## Question: 29.jpeg

<img src="29.jpeg" alt="Question" width="800">

### Notes:

- Global Accelerator has automatic failover 
- CloudFront is designed to handle HTTP protocol meanwhile Global Accelerator is best used for both HTTP and non-HTTP protocols such as TCP and UDP. 
- Amazon Application Load Balancer: Ideal for load balancing HTTP and HTTPS traffic
- Amazon Network Load Balancer: Ideal for load balancing TCP and UDP traffic






























## Question: 30.png

<img src="30.png" alt="Question" width="800">

### Notes:

- Still pay for storage when an RDS database is stopped -> Not A





























## Question: 39.png

<img src="39.png" alt="Question" width="800">

### Notes:

- Provisioned IOPS SSD: This storage type is designed to deliver fast, predictable, and consistent I/O performance, which is crucial for databases with high transaction rates and frequent updates.

- Option C (changing the DB instance to a burstable performance instance class) is suitable for workloads with varying usage patterns and burstable performance needs, but it may not provide consistent and predictable performance for heavy write workloads.




























## Question: 41.png

<img src="41.png" alt="Question" width="800">

### Notes:

- Amazon AppFlow is a fully managed integration service that helps you securely transfer data between software as a service (SaaS) applications such as Salesforce, SAP, Google Analytics, Facebook Ads, and ServiceNow, and AWS services such as Amazon Simple Storage Service (S3) and Amazon Redshift in just a few clicks. 



























## Question: 47.jpeg

<img src="47.jpeg" alt="Question" width="800">

### Notes:

- With an On-Demand Capacity Reservation, you can specify the Region and Availability Zones where you want to reserve capacity, and the number of EC2 instances you want to reserve. This allows you to guarantee capacity in specific Availability Zones in a specific Region.

- Reserved instances are for long term


























## Question: 60.png

<img src="60.png" alt="Question" width="800">

### Notes:

- ALB listener rules allow you to redirect traffic from one listener port (e.g. 80 for HTTP) to another (e.g. 443 for HTTPS). This achieves the goal to forward all requests over HTTPS.
- Network ACLs control traffic at the subnet level and cannot distinguish between HTTP and HTTPS requests to implement a redirect (option A incorrect). 
- Replacing HTTP with HTTPS in the URL happens at the client side. It does not redirect at the ALB (option B incorrect).

























## Question: 67.png

<img src="67.png" alt="Question" width="800">

### Notes:

- The visibility timeout determines the amount of time that a message received from an SQS queue is hidden from other consumers while the message is being processed. 

- If the processing of a message takes longer than the visibility timeout, the message will become visible to other consumers and may be processed again. 
























## Question: 68.png

<img src="68.png" alt="Question" width="800">

### Notes:

- 























## Question: 73.png

<img src="73.png" alt="Question" width="800">

### Notes:

- on-prem -----> bastion host (we use internet, means that we need external IPs of the company) 
- bastion host -----> private subnet (we use private IP since we are in the same VPC, as bastion can communicate to EC2 via its private IP address)






















## Question: 76.png

<img src="76.png" alt="Question" width="800">

### Notes:

- DMS is for databases, while the question refers to JSON files





















## Question: 79.png

<img src="79.png" alt="Question" width="800">

### Notes:

- Provisioned capacity is recommended for known patterns. On-demand mode is recommended for unpredictable application traffic




















## Question: 83.png

<img src="83.png" alt="Question" width="800">

### Notes:

- 



















## Question: 93.png

<img src="93.png" alt="Question" width="800">

### Notes:

- Aurora cloning is especially useful for quickly setting up test environments using your production data, without risking data corruption































## Question: 95.png

<img src="95.png" alt="Question" width="800">

### Notes:

- 































## Question: 98.png

<img src="98.png" alt="Question" width="800">

### Notes:

- By increasing the visibility timeout to a value greater than the total of the function timeout and the batch window timeout, we ensure that the message remains invisible long enough for the Lambda function to complete its processing. This prevents duplicate processing of the same message.

- FIFO queues guarantee that messages are processed in the exact order they are sent.































## Question: 101.png

<img src="101.png" alt="Question" width="800">

### Notes:

- NAT gateways allow private instances to initiate outbound traffic to the Internet but do not allow inbound traffic from the Internet to reach the private instances.
- NAT gateways must be created in public subnets
- NAT gateways are availability zone specific, if you need HA you will need a NAT gateway in each availability zone.






























## Question: 104.png

<img src="104.png" alt="Question" width="800">

### Notes:

- 































## Question: 107.png

<img src="107.png" alt="Question" width="800">

### Notes:

- Integration with analytics: Lambda functions can be designed to store the data in a format that's easily consumable by the company's existing analytics platform.




























## Question: 108.png

<img src="108.png" alt="Question" width="800">

### Notes:

- RDS Event Notifications: This allows you to capture database changes efficiently.

- Amazon SNS Topic: This provides a pub/sub messaging service that can fan out to multiple endpoints.

- Multiple SQS Queues: Each target system can have its own queue, allowing for decoupled and independent processing.

- Options A and B are less suitable because they don't provide the fan-out capability to multiple targets as efficiently.































## Question: 109.png

<img src="109.png" alt="Question" width="800">

### Notes:

- The Object Lock legal hold operation enables you to place a legal hold on an object version.
- A legal hold prevents an object version from being overwritten or deleted. 
- However, a legal hold doesn't have an associated retention period and remains in effect until removed.


















## Question: 117.png

<img src="117.png" alt="Question" width="800">

### Notes:

- You can configure a CloudWatch Logs log group to stream data it receives to your Amazon OpenSearch Service cluster in NEAR REAL-TIME through a CloudWatch Logs subscription































## Question: 119.png

<img src="119.png" alt="Question" width="800">

### Notes:

- 































## Question: 120.png

<img src="120.png" alt="Question" width="800">

### Notes:

- 

















## Question: 121.png

<img src="121.png" alt="Question" width="800">

### Notes:

- You can enable encryption for an Amazon RDS DB instance when you create it, but not after it's created. 
- However, you can add encryption to an unencrypted DB instance by creating a snapshot of your DB instance, and then creating an encrypted copy of that snapshot. 
- You can then restore a DB instance from the encrypted snapshot to get an encrypted copy of your original DB instance































## Question: 124.png

<img src="124.png" alt="Question" width="800">

### Notes:

- 































## Question: 125.png

<img src="125.png" alt="Question" width="800">

### Notes:

- NAT gateways must be created in public subnets
- NAT gateways are availability zone specific, if you need HA you will need a NAT gateway in each availability zone.































## Question: 127.png

<img src="127.png" alt="Question" width="800">

### Notes:

- 
















## Question: 128.png

<img src="128.png" alt="Question" width="800">

### Notes:

- Containers: The company wants to run applications in containers, which EKS supports natively.
- Stateless applications: The applications are stateless and can tolerate disruptions, making them ideal candidates for Spot Instances.
- Spot Instances offer significant cost savings compared to On-Demand Instances, often up to 90% cheaper.





























## Question: 131.png

<img src="131.png" alt="Question" width="800">

### Notes:

- An OAI provides secure access between CloudFront and S3 without exposing the S3 bucket publicly.
- The OAI is associated with the CloudFront distribution.
- The S3 bucket policy limits access only to that OAI.






























## Question: 132.png

<img src="132.png" alt="Question" width="800">

### Notes:

- Historical reports imply static content















## Question: 133.png

<img src="133.png" alt="Question" width="800">

### Notes:

- Maintain access to the underlying OS: RDS Custom provides access to the underlying operating system, which is a specific requirement mentioned in the question.














## Question: 134.png

<img src="134.png" alt="Question" width="800">

### Notes:

- Server-side encryption with SSE-S3: This provides encryption with the least operational overhead. SSE-S3 is fully managed by AWS, requiring no key management from the user.

- Amazon Athena: This is a serverless query service that can directly analyze data in S3, which aligns with the company's desire for a serverless solution and the need to analyze data using SQL.












## Question: 135.png

<img src="135.png" alt="Question" width="800">

### Notes:

- AWS PrivateLink provides private connectivity between VPCs, AWS services, and your on-premises networks, without exposing your traffic to the public internet
- Option A VPC peering connection may not meet security requirement as it can allow communication between all resources in both VPCs.
- Option C, creating a NAT gateway in a public subnet of the company’s VPC can expose the target service to the internet, which would not meet the security requirements.












## Question: 138.jpeg

<img src="138.jpeg" alt="Question" width="800">

### Notes:

- Migrating to Amazon MQ reduces the overhead on the queue management. Amazon MQ provides a managed, highly available RabbitMQ cluster














## Question: 139.jpeg

<img src="139.jpeg" alt="Question" width="800">

### Notes:

- S3 event notifications can only send to SNS, SQS and lambda, but not to Sagemaker. Eventbridge can send to Sagemaker


























## Question: 140.png

<img src="140.png" alt="Question" width="800">

### Notes:

- 































## Question: 141.png

<img src="141.png" alt="Question" width="800">

### Notes:

- Caching: CloudFront can cache both static and dynamic content, reducing the load on your origin and improving response times.































## Question: 142.png

<img src="142.png" alt="Question" width="800">

### Notes:

- Among the given options, only Network Load Balancer (NLB) supports UDP traffic. Application Load Balancer (ALB) and API Gateway do not support UDP.

- Global Accelerator provides static IP addresses that act as a fixed entry point to your application endpoints. This meets the requirement for static IP addresses for entry into the application.

- Since the application runs on a modified Linux kernel, it needs to run on EC2 instances rather than serverless options like Lambda.

- A and B: Lambda doesn't support custom Linux kernels, and Application Load Balancer doesn't support UDP.

- D: API Gateway and Application Load Balancer don't support UDP traffic.











## Question: 145.png

<img src="145.png" alt="Question" width="800">

### Notes:

- Auto Scaling: Using an Auto Scaling group allows the application to scale seamlessly based on demand, addressing the performance degradation and 5xx errors during busy times.

- Database Migration: Moving the database to Amazon Aurora MySQL provides better performance and scalability compared to a single EC2 instance running MySQL.

- Spot Fleet: Using Spot Instances in the Auto Scaling group can significantly reduce costs compared to On-Demand Instances, making this the most cost-effective option.































## Question: 150.png

<img src="150.png" alt="Question" width="800">

### Notes:

- By creating composite alarms in CloudWatch, the solutions architect can combine multiple metrics, such as CPU utilization and read IOPS, into a single alarm. This allows the company to take action only when both conditions are met, reducing false alarms and focusing on meaningful alerts.































## Question: 152.png

<img src="152.png" alt="Question" width="800">

### Notes:

- 









## Question: 154.png

<img src="154.png" alt="Question" width="800">

### Notes:

- Governance mode: Only users with special permissions can overwrite, delete, or alter object lock settings

- Compliance mode: No user, including the root user in an AWS account, can overwrite, delete, or alter object lock settings









## Question: 157.jpeg

<img src="157.jpeg" alt="Question" width="800">

### Notes:

- The maximum retention period for automated backups configured directly in Amazon Aurora is 35 days.

- AWS Backup can be used to extend the backup retention beyond the 35-day limit of Aurora's native automated backups. It allows you to store backups for up to 5 years, which meets the company's requirement.




























## Question: 158.jpeg

<img src="158.jpeg" alt="Question" width="800">

### Notes:

- 







## Question: 165.jpeg

<img src="165.jpeg" alt="Question" width="800">

### Notes:

- 






























## Question: 168.png

<img src="168.png" alt="Question" width="800">

### Notes:

- 































## Question: 172.png

<img src="172.png" alt="Question" width="800">

### Notes:

- With Amazon CloudFront, you can enforce secure end-to-end connections to origin servers by using HTTPS. Field-level encryption adds an additional layer of security that lets you protect specific data throughout system processing so that only certain applications can see it.































## Question: 175.png

<img src="175.png" alt="Question" width="800">

### Notes:

- Many applications, including those built on modern serverless architectures, can have a large number of open connections to the database server and may open and close database connections at a high rate, exhausting database memory and compute resources. 

- Amazon RDS Proxy allows applications to pool and share connections established with the database, improving database efficiency and application scalability.































## Question: 178.png

<img src="178.png" alt="Question" width="800">

### Notes:

- 































## Question: 183.jpeg

<img src="183.jpeg" alt="Question" width="800">

### Notes:

- DynamoDB with on-demand capacity automatically scales read and write capacity to accommodate traffic spikes without the need for manual intervention.

- Aurora requires more management than DynamoDB and may not scale as quickly for write operations.






























## Question: 184.jpeg

<img src="184.jpeg" alt="Question" width="800">

### Notes:

- To access private resources, the Lambda function needs to be configured to run within your VPC.

- Once in your VPC, the Lambda function can use the existing Direct Connect connection to reach the on-premises data center.






## Question: 188.jpeg

<img src="188.jpeg" alt="Question" width="800">

### Notes:

- SFTP support: AWS Transfer Family natively supports SFTP, which is the required protocol for the new partner.






























## Question: 190.png

<img src="190.png" alt="Question" width="800">

### Notes:

- Easy feature testing: With Elastic Beanstalk, you can create multiple environments (e.g., production, staging, development). The URL swapping feature allows you to easily switch between these environments, facilitating frequent testing of new site features.































## Question: 193.png

<img src="193.png" alt="Question" width="800">

### Notes:

- Reduces database reads: By storing frequently accessed data in Redis, the application can retrieve this data from the cache instead of querying the RDS databases, thus reducing the number of database reads.

- Add Amazon RDS read replicas: While this could help distribute read operations, it doesn't reduce the total number of database reads. It just spreads them across more instances.





## Question: 194.png

<img src="194.png" alt="Question" width="800">

### Notes:

- C: While this provides high availability across regions, it's typically more complex and expensive than necessary. Cross-region replication often has higher latency and doesn't provide automatic failover without additional configuration.

- Automatic Failover: Configuring the EC2 instances as a cluster with database replication allows for automatic failover if one instance or AZ experiences issues.






























## Question: 199.png

<img src="199.png" alt="Question" width="800">

### Notes:

- Multiple speaker recognition: Amazon Transcribe offers a feature called speaker diarization, which can identify and label different speakers in an audio file. This meets the requirement for multiple speaker recognition.
































## Question: 201.png

<img src="201.png" alt="Question" width="800">

### Notes:

- SMS Messaging: Amazon Pinpoint is designed for customer engagement and supports sending SMS messages at scale. It's ideal for marketing communications and can handle both outbound and inbound SMS.





## Question: 202.png

<img src="202.png" alt="Question" width="800">

### Notes:

- Server-side encryption: SSE-S3 provides automatic encryption of data at rest in S3 buckets.

- Automatic key rotation: With SSE-S3, AWS automatically handles key management and rotation. The keys are rotated on a regular basis, which meets the requirement of annual key rotation.































## Question: 207.png

<img src="207.png" alt="Question" width="800">

### Notes:

- 































## Question: 208.png

<img src="208.png" alt="Question" width="800">

### Notes:

- Security groups cannot be attached to gateway VPC endpoints



























## Question: 213.png

<img src="213.png" alt="Question" width="800">

### Notes:

- 































## Question: 215.png

<img src="215.png" alt="Question" width="800">

### Notes:

- Transferring 700 TB over a 500 Mbps connection would take longer than the 1-month requirement.

- Snowball can transfer 700 TB within the 1-month timeframe.

- S3 Glacier Deep Archive is the most cost-effective storage for long-term, infrequently accessed data.





























## Question: 217.png

<img src="217.png" alt="Question" width="800">

### Notes:

- Allowing for up to 30 minutes of downtime (active-passive failover)

- Minimizing potential data loss (Aurora Replica)

- Not requiring the solution to handle the full load during normal operations (active-passive setup)































## Question: 219.png

<img src="219.png" alt="Question" width="800">

### Notes:

- R5 instances are memory-optimized, which is suitable for the stateful, in-memory tasks required by the application.

- However, CloudWatch doesn't provide built-in memory metrics for EC2 instances.

- The CloudWatch agent can collect custom metrics, including memory usage and application latency, which are not available as built-in metrics.































## Question: 222.png

<img src="222.png" alt="Question" width="800">

### Notes:

- IAM roles for cross-account access, which is a standard and secure method for allowing access between AWS accounts.

- Not C: IAM users and groups are confined to a single AWS account. You can't add users from other AWS accounts to your IAM groups.




## Question: 224.png

<img src="224.png" alt="Question" width="800">

### Notes:

- Multivalue answer routing allows you to configure Amazon Route 53 to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

- Having two instances in each AZ ensures that the application can handle the load even if one instance or an entire AZ fails.





























## Question: 225.png

<img src="225.png" alt="Question" width="800">

### Notes:

- 































## Question: 226.png

<img src="226.png" alt="Question" width="800">

### Notes:

- 



## Question: 235.png

<img src="235.png" alt="Question" width="800">

### Notes:

- AWS Schema Conversion Tool (SCT): This is necessary to convert the schema from Oracle to PostgreSQL, as these are different database engines.

- AWS Database Migration Service (AWS DMS): This service is ideal for migrating databases to AWS, especially when you need to keep the source and target databases in sync during migration.

- Table mapping to select all tables: Since the applications write to the same tables and the data must be kept in sync across both databases, it's important to include all tables in the migration.





























## Question: 237.png

<img src="237.png" alt="Question" width="800">

### Notes:

- You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account. Peering within the same AZ is free of charge.

## Question: 239.png

<img src="239.png" alt="Question" width="800">

### Notes:

- 




























































