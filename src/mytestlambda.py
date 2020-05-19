import json


def myfunction_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'This is a successful message'
    }