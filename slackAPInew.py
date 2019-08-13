def getCustomMessageBodyFields(customFields):
    customMessageBodyFields = []
    for fieldValue, fieldType in customMessageBodyFields.items():
        customMessageBodyFields.append(
            {
                "type": fieldType,
                "text": accountName,
            }
        )
    return customMessageBodyFields

def getMessageTopPost( # make these a dict? see template below
        serviceName, 
        messageHeadline, 
        accountName, 
        resourceID, 
        statusMessage, 
        timeStamp, 
        callToAction="", 
        buttonText="",
        buttonTarget="",
        customFields = [] # dict in the form of { fieldValue : fieldType, ... }
        ):

    generalTemplate = [
        {
            # Header
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "{} {}".format(serviceName, messageHeadline)
            }
        },
        {
            "type": "divider"
        },
        {
            # Message Body
            "type": "section",
            "fields": messageBodyFields if ! customMessageBodyFields else messageBodyFields + getCustomMessageBodyFields(customFields)
        },
        {
            "type": "divider"
        },
        {
            # Footer (timestamp)
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": timeStamp
                }
            ]
        }
    ]

    messageBodyFields = [
        {
            "type": "plain_text",
            "text": accountName,
        },
        {
            "type": "plain_text",
            "text": resourceID,
        },
        {
            "type": "plain_text",
            "text": statusMessage,
            "emoji": true
        },
    ]

    callToAction = 
        {
            # Call to action and button
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": callToAction
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": buttonText,
                    "emoji": true
                },
                "value": buttonTarget
            }
        }

    return messageToPost


# Define which service is the origin
resourceParserPattern = [
    {
        "MessageSourceID" : { # must have at least one of these
            "condition" : (True), # some condition about multiple keys/values etc
            "messageContent" : "valueToLookFor"
        }
        "MessageSourceParseKey" : "exampleKey", # Unique value to identify message source, if in "message" (new pattern) NOTE: Optional, of not present, other uses
        "MessageSourceParserFunction" : function, # function to apply to properly parameter source NOTE: EVAL
        "MessageSourceParseSubKeys" : {
            "SubKey": "value", # optional ( if template has it, iterate)
        } 
        "MessageSourceAWSService" : "serviceName" # Resolve to human readable service name
        "MessageTemplateSourceValues" : { # set values here
            "serviceName" : pass, 
            "messageHeadline" : pass, 
            "accountName": pass, 
            "resourceID": pass, 
            "statusMessage": pass, 
            "timeStamp": pass, 
            "callToAction": pass, 
            "buttonText": pass, # optional
            "buttonTarget": pass, # optional 
            "customFields" = {} # optional dict { fieldValue : fieldType, ...}
        }
    }
]
# cast template with these values
