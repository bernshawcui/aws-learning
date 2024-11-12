# Exam Prepper Questions

## Question: 1.png

<img src="1.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Create an AWS Global Accelerator standard accelerator. Specify the ALB as the accelerator's endpoint. Provide the accelerator's IP addresses to the customer

Notes:

- **Global Accelerator provides two global static public IPs** that act as a fixed entry point to your application endpoints, such as Application Load Balancers, Network Load Balancers, Amazon Elastic Compute Cloud (EC2) instances, and elastic IPs.

</details>












## Question: 2.png

<img src="2.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Create a CloudFront origin group that has two origins. Set the ALB endpoint as the primary origin. For the secondary origin, set an S3 bucket that is configured to host a static website. Set up origin failover for the CloudFront distribution. Update the S3 static website to incorporate the custom error page.

Notes:

- 

</details>











## Question: 3.png

<img src="3.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Create a separate service in the ECS cluster for the waiting room. Use a separate scaling configuration. Create a CloudFront function that inspects the JWT information and appropriately forwards requests to the ticketing service or the waiting room service.

Notes:

- 

</details>










## Question: 4.png

<img src="4.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Create an AWS Transfer Family server. Configure an internet-facing VPC endpoint for the Transfer Family server. Specify an Elastic IP address for each subnet. COnfigure the Transfer Family server to place files into an Amazon Elastic File System (Amazon EFS) file system that is deployed across multiple Availability Zones. Modify the configuration on the downstream applications that access the existing NFS share to mount the EFS endpoint instead.

Notes:

- AWS Transfer Family eliminates SFTP server management

</details>










## Question: 5.png

<img src="5.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- AWS Migration Hub, AWS Application Discovery Service, AWS Cloud Adoption Readiness Tool (CART)

Notes:

- AWS Application Discovery Service helps gather information about on-premises data centers to plan migrations to AWS.
- Helps understand existing infrastructure, identifies dependencies between applications and estimate AWS costs

</details>







## Question: 6.png

<img src="6.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Deploy a Lambda@Edge function to sort parameters by name and force them to be lowercase. Select the CloudFront viewer request trigger to invoke the function

Notes:

- Amazon CloudFront considers **the case of parameter names and values when caching based on query string parameters**, thus inconsistent query strings may cause CloudFront to forward mixed-cased/misordered requests to the origin.

</details>






## Question: 7.png

<img src="7.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Create an Amazon RDS DB instance to host the product data. Configure a read replica for the DB instance in another Region. Create an Amazon DynamoDB global table to host the user session data

Notes:

- 

</details>





## Question: 8.png

<img src="8.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Create one VPC peering connection for each VPC in us-east-2 to the VPC in eu-west-1. Create the necessary route entries in each VPC so that the traffic is routed through the VPC peering connection

Notes:

- 

</details>




## Question: 9.png

<img src="9.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Create an Amazon EventBridge (Amazon CloudWatch Events) rule. Define a pattern with the detail-type value set to AWS API Call via CloudTrail and an eventName of CreateUser.
- Invoke an AWS Step Functions state machine to remove access
- Use Amazon Simple Notifcation Service (Amazon SNS) to notify the security team

Notes:

- 

</details>



## Question: 10.png

<img src="10.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Update ALB Security group ingress to allow access only from the com.amazonaws.global.cloudfront.origin-facing CloudFront managed prefix list

Notes:

- 

</details>

