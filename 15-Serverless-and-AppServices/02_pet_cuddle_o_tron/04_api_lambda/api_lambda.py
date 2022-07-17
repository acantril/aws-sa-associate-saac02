# This code is a bit ...messy and includes some workarounds
# It functions fine, but needs some cleanup
# Checked the DecimalEncoder and Checks workarounds 20200402 and no progression towards fix

import decimal
import json

import boto3

SM_ARN = "YOUR_STATEMACHINE_ARN"

sm = boto3.client("stepfunctions")


def lambda_handler(event, context):
    # Print event data to logs ..
    print("Received event: " + json.dumps(event))

    # Load data coming from APIGateway
    data = json.loads(event["body"])
    data["waitSeconds"] = int(data["waitSeconds"])

    # Sanity check that all the parameters we need have come through from API gateway
    # Mixture of optional and mandatory ones
    checks = [
        "waitSeconds" in data,
        type(data["waitSeconds"]) == int,
        "preference" in data,
        "message" in data,
    ]
    if data.get("preference") == "sms":
        checks.append("phone" in data)
    if data.get("preference") == "email":
        checks.append("email" in data)

    # if any checks fail, return error to API Gateway to return to client
    if False in checks:
        response = {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps(
                {"Status": "Success", "Reason": "Input failed validation"},
                cls=DecimalEncoder,
            ),
        }
    # If none, start the state machine execution and inform client of 2XX success :)
    else:
        sm.start_execution(
            stateMachineArn=SM_ARN, input=json.dumps(data, cls=DecimalEncoder)
        )
        response = {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"Status": "Success"}, cls=DecimalEncoder),
        }
    return response


# This is a workaround for: http://bugs.python.org/issue16535
# Solution discussed on this thread:
# https://stackoverflow.com/questions/11942364/typeerror-integer-is-not-json-serializable-when-serializing-json-in-python
# https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object
# Credit goes to the group :)
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)
