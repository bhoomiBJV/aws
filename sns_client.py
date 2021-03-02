import boto3

aws_access_key_id = input('Enter your AWS Key : ')
aws_secret_access_key = input('Enter your AWS Secret Key : ')

sns = boto3.client("sns",
                   region_name='us-east-1',
                   aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key,
                   )
# Create Topics
response = sns.create_topic(Name="topic_name")
topic_arn = response["TopicArn"]

# List topics
response = sns.list_topics()
topics = response["Topics"]

print('Topics :', topics)

# Topics Attributes
for topic in topics:
    print('TopicArn : ', topic['TopicArn'])
    print('Topic Attributes : ', sns.get_topic_attributes(TopicArn=topic['TopicArn']))

# Delete Topic
topic_arn = input('Enter topic ARN : ')
sns.delete_topic(TopicArn=topic_arn)

# Create SMS subscription
protocol = input('Choose any one for subscription \n 1. SMS \n 2. Email :')
if protocol == 'sms':
    endpoint = input('Enter Mobile number : ')
elif protocol == 'email':
    endpoint = input('Enter email address : ')

response = sns.subscribe(TopicArn=topic_arn,
                        Protocol=protocol,
                        Endpoint=endpoint,
                        )
print('Subscription ARN : ', response['SubscriptionArn'])

# List all Subscriptions
response = sns.list_subscriptions()
print ('Subscription : \n', response['Subscriptions'])

# List subscriptions by topic
response = sns.list_subscriptions_by_topic(TopicArn=topic_arn)
subscriptions = response["Subscriptions"]
print ('Subscription : \n', subscriptions)

# Delete subscription
subscription_arn = input('Enter Subscription Arn for Unsubscribe: ')
sns.unsubscribe(SubscriptionArn=subscription_arn)

# Publish to topic
sns.publish(TopicArn=topic_arn,
            Message="Here is Message Body",
            Subject="Email Subject")

# Send a single SMS (no topic, no subscription needed)
phone_number = input('Enter Phone number : ')
sns.publish(PhoneNumber=phone_number,
            Message="Hello Love How are you?")
