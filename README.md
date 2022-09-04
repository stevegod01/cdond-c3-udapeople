
## Building a CI/CD Pipeline coupled with monitoring and Logging

# Continuous Delivery

Continuous delivery is a software development practice where code changes are automatically prepared for a release to production. A pillar of modern application development, continuous delivery expands upon continuous integration by deploying all code changes to a testing environment and/or a production environment after the build stage. When properly implemented, developers will always have a deployment-ready build artifact that has passed through a standardized test process. 

Continuous delivery lets developers automate testing beyond just unit tests so they can verify application updates across multiple dimensions before deploying to customers. These tests may include UI testing, load testing, integration testing, API reliability testing, etc. This helps developers more thoroughly validate updates and pre-emptively discover issues. With the cloud, it is easy and cost-effective to automate the creation and replication of multiple environments for testing, which was previously difficult to do on-premises.
![image](https://user-images.githubusercontent.com/48868321/184530337-35f25dab-3be0-4e77-8b03-33c029556db8.png)

In this project Continuous Delivery was achieved using  [Ansible](https://www.ansible.com/) - Configuration management tool, [Circle CI](www.circleci.com) - Cloud-based CI/CD service, and [CloudFormation](https://aws.amazon.com/cloudformation/) - Infrastrcuture as code.

## Monitoring 
As a DevOps engineer, during an outage, you should be able to know where to look to find the source of the problem. You should be able to see through a haystack of monitoring data and zero in on the issue at hand.

Before any outage, you should be thinking about where failures might occur and ensure those areas have proper monitoring. Some common areas where you might need monitoring are:

* Database Stats
* Application Logs
* Docker Logs
* Firewall
* Load Balancer
* GPU
* Operating System
* Router
* Cable Modem
* Message Bus
* AWS Services
* Mail Server
* Other 3rd Party Services
* Other Monitoring Systems.

In this project, monitoring was achieved using [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/)

### Log Management

Log management is the practice of continuously gathering, storing, processing, synthesizing and analyzing data from disparate programs and applications in order to optimize system performance, identify technical issues, better manage resources, strengthen security and improve compliance.

A log is a computer-generated file that captures activity within the operating system or software applications. The log file automatically documents any information designed by the system administrators, including: messages, error reports, file requests and file transfers. The activity is also timestamped, which helps IT professionals and developers understand what occurred as well as when it happened.



### Built With

- [Circle CI](www.circleci.com) - Cloud-based CI/CD service
- [Amazon AWS](https://aws.amazon.com/) - Cloud services
- [AWS CLI](https://aws.amazon.com/cli/) - Command-line tool for AWS
- [CloudFormation](https://aws.amazon.com/cloudformation/) - Infrastrcuture as code
- [Ansible](https://www.ansible.com/) - Configuration management tool
- [Prometheus](https://prometheus.io/) - Monitoring tool

### License

[License](LICENSE.md)
