# Ecosystem
 
## OpenSearch VS Elastic Search

AWS forked the version 7.10 of ES to create OpenSearch and created a consortium of [partners](https://opensearch.org/partners/). 
Elastic.co is the company that owns Elastic Search.

[OpenSearch](https://opensearch.org) is an opensource fork of Elastic Search version 7.10 ( see [here](https://pureinsights.com/blog/2021/elasticsearch-vs-opensearch-user-point-of-view-part-1-of-3/) for details of the reason behind the fork)


from the OpenSearch a list of FAQ for people used to the ES ecosystem:

* [1.10 Do Elasticsearch clients like Logstash and Beats work with OpenSearch?](https://opensearch.org/faq/#q1.10)
* [1.11 Does OpenSearch include forks of Logstash and Beats?](https://opensearch.org/faq/#q1.11)
* [1.15 Will you be making contributions back to Elasticsearch open-source?](https://opensearch.org/faq/#q1.11) No
* 1.18 [GOVERNANCE] What will your governance model be? Are you looking at any foundations?

At this time, there is not a plan to move OpenSearch in to a foundation. As we work together in the open, we expect to uncover the best ways to collaborate and empower all interested stakeholders to share in decision making. Cultivating the right governance approach for an open source project requires thoughtful deliberation with the community. We’re confident that we can find the best approach together over time. For now, `AWS is the steward of OpenSearch`. The principles of development define the guidelines for how decisions about the project are made. These principles will continue to be iterated and refined based on feedback.

* 1.20 What tools do you recommend for log and metrics collection?

OpenSearch is supported by a range of tools like Beats, Fluentd, Fluent Bit, and OpenTelemetry Collector. Moving forward, we will focus effort on improving Data Prepper, Fluentd, and FluentBit. Users who are using Beats <= 7.12.x as an agent tool, and considering open source alternatives, should migrate to Fluent Bit >= 1.9 or Open Telemetry Collector. Beats version >= 7.13 does not support OpenSearch.

* 1.21 What tools do you recommend for log aggregation?

OpenSearch is supported by a range of tools like Data Prepper, Fluentd, Logstash, and Kafka. OpenSearch believes in multiple open source options and will focus on improving the Data Prepper, Fluentd, and Kafka support going forward.

## What is Amazon OpenSearch Service?

https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html

`Amazon OpenSearch Service` provides a managed version of OpenSearch and legacy version of Elasticsearch OSS (up to 7.10, the final open source version of the software)
 
Domains are clusters with the settings, instance types, instance counts, and storage resources that you specify.


## Elastic Search Alternatives Hosting solutions

All this company offers a managed solution that can be deployed on AWS or other clouds: 
* Elastic.co
* Bonsai https://bonsai.io/pricing
*  Instacluster
https://www.instaclustr.com/pricing/?_bt=605198283008&_bk=hosted%20opensearch&_bm=b&_bn=g&_bg=139580640442






# Creating and managing Amazon OpenSearch Service domains

10 min video tutorial: https://www.youtube.com/watch?v=XqQJmV2yoks&t=602s

https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html


Security for public access: For the quick start of building opensearch, we can put the opensearch in public network and control access by using basic authentication and domain access policy from Fine-grain access controller. But this is a Critical alert from AWS security standard.

https://dev.to/aws-builders/access-control-and-opensearch-service-security-2lkn

> WARNING OpenSearch domains should be in a VPC



NIK TEST:
* For a Viblio Staging public access instance I've used "Only use fine-grained access control"



# Security

## Fine-grained access control in Amazon OpenSearch Service

https://docs.amazonaws.cn/en_us/opensearch-service/latest/developerguide/fgac.html


If you get this error `{"Message":"User: anonymous is not authorized to perform: es:ESHttpGet with an explicit deny in a resource-based policy"}` : 
https://stackoverflow.com/questions/62738960/on-aws-elastic-search-messageuser-anonymous-is-not-authorized-to-perform
 