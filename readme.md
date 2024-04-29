Project Title:
 -----
 Automating JIRA Ticket Creation from GitHub Comments

Problem Statement:-
--------
In the organizational workflow,When QE spot bugs during testing, they report them on 
GitHub. The development team verifies the issues and creates JIRA tickets for genuine ones, typically
a manual task. To improve efficiency, the DevOps team automates this process.
This automation facilitates automatic ticket creation on JIRA when comments are made on GitHub.

 
Project Flow:
 ---
 
 When a developer comments "/jira" in the project's GitHub repository.GitHub triggers a webhook,
 interact with API of python application(Developed using Flask) which is deployed on an EC2 instance, 
 receives the webhook payload in json format. Then it communicates with the Jira API.
 Finally, Jira ticket is created in the Jira dashboard.

 Execution:
-----
1. Write a Python Script to create jira issue
2. Now convert the Script into API using Flask Framework
3. Deploy the Python Application to server
4. Configure the Webhook in Github to interact with api of Python application
5. Now, comment "/jira" in github so that it create jira ticket.

For best Pratices:
-------
Parsing api token using envorinorment variables
 
 In Code:

 import os

 os.getenv("api_token")
 
 In CLI:

 export api_token="ATATT3xFf........"

 For References:
 -------
 Jira Api Docs:

 https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/