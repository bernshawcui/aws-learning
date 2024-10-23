# Exam Topic Questions

## Question: 1.png

<img src="1.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- 2) Use the Trusted Advisor recommendations in the management account
- 5) Review the Trusted Advisor checks for Amazon RDS Reserved Instance Optimization

Notes:

- 

</details>







## Question: 2.png

<img src="2.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- 1) Host the visualization tool in the same AWS Region as the data warehouse and access it over a Direct Connect conncetion at a location in the same Region

Notes:

- 

</details>






## Question: 3.jpeg

<img src="3.jpeg" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Implement a target tracking action triggered at a lower CPU threshold, and decrease the cooldown period

Notes:

- Target Tracking Scaling Policy: With a target tracking scaling policy, you can set a target value for a specific metric, such as CPU utilization. The Auto Scaling group then adjusts the capacity to maintain that target.

- Lower CPU Threshold: By triggering the target tracking action at a lower CPU threshold, the Auto Scaling group can proactively add instances when the workload increases, helping to address the slowness at the beginning of the day.

- Decrease Cooldown Period: Reducing the cooldown period allows the Auto Scaling group to scale in and out more rapidly, making adjustments quicker in response to changing demand.

</details>





## Question: 4.png

<img src="4.png" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Configure AWS WAF

Notes:

- WAF helps with layer 7 attacks like SQL injection and Cross-Site Scripting. Shield is helpful for DDOS attacks.

</details>




## Question: 5.jpeg

<img src="5.jpeg" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Request strongly consistent reads for the table

Notes:

- DynamoDB by default provides eventual consistency for read operations, which means that a query may not reflect the most recent data changes immediately after an update. Instead, it may take some time for the data to propagate across all replicas in the DynamoDB global table.

- To ensure that read operations return the latest data and address the issue of stale data being returned to users, the solutions architect should recommend switching the read consistency level from eventually consistent reads to strongly consistent reads.

</details>



## Question: 6.jpeg

<img src="6.jpeg" alt="Question" width="800">

<details>
<summary>Click to reveal the correct answer</summary>

- Add a resource-based policy to the function with lambda:InvokeFunction as the action and Service: events.amazonaws.com as the principal

Notes:

- 

</details>

