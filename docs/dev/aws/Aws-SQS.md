## Local Development

### ElasticMQ

Docker config: https://github.com/softwaremill/elasticmq#elasticmq-via-docker


https://github.com/softwaremill/elasticmq/issues/149

Log
```
    <configuration>
      <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
          <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
              <level>INFO</level>
          </filter>
          <encoder>
              <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
          </encoder>
      </appender>

      <root level="INFO">
          <appender-ref ref="STDOUT" />
      </root>
    </configuration>
```


### Local Development with SQS and Elastic Beanstalk SQSD

Complete example with Docker Compose: https://github.com/addictivedev/sqs_sqsd

ssh -i ~/.ssh/nb-docker-keypair.pem ubuntu@ec2-18-192-69-238.eu-central-1.compute.amazonaws.com

ElasticMQ
https://blog.linkme.it/mocking-sqs-with-elasticmq-and-docker-compose-2eee960fe15

sqsd is the elastic beanstalk deamon

https://github.com/mogadanez/sqsd


WARNING la URL delle code deve finire con /queue
https://github.com/softwaremill/elasticmq/issues/207


https://github.com/jwilder/dockerize


#### Debug

SQSD uses https://www.npmjs.com/package/debug


# SQS Configuration

## Delay

Ref: https://cloudaffaire.com/how-to-configure-delay-queue-in-sqs/

If delivery delay is defined for a queue, any new message will not be visible to the consumer for the duration of delay.

Delay queues are similar to visibility timeouts because both features make messages unavailable to consumers for a specific period of time. The difference between the two is that:
* for delay queues, a message is hidden when it is first added to queue,
* whereas for visibility timeouts a message is hidden only after it is consumed from the queue.

To set delay seconds on **individual messages**, rather than on an entire queue, use message timers to allow Amazon SQS to use the message timer’s DelaySeconds value instead of the delay queue’s DelaySeconds value.


# SQS API

## List Queues
http://localhost:9324?Action=ListQueues&QueueNamePrefix=*

## Queue stats

https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue/
?Action=GetQueueAttributes
&AttributeName.1=All
&Expires=2020-10-18T22%3A52%3A43PST
&Version=2012-11-05
&AUTHPARAMS


DOC: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html

## Receive Message

* https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue/?Action=ReceiveMessage&MaxNumberOfMessages=5&VisibilityTimeout=15&AttributeName=All&Version=2012-11-05&AUTHPARAMS

* Doc: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html#API_ReceiveMessage_Examples


