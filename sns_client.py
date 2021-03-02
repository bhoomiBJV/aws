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
