#
# All or portions of this file Copyright (c) Amazon.com, Inc. or its affiliates or
# its licensors.
#
# For complete copyright and license terms please see the LICENSE at the root of this
# distribution (the "License"). All use of this software is governed by the License,
# or, if provided, by the license below or the license accompanying this file. Do not
# remove or modify any license notices. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# $Revision: #1 $

import boto3
import CloudCanvas

# These settings come from the Settings property of the lambda function's configuration
# resource definition in the feature's feature-template.json file. Some of those values
# are taken from the template's parameters. Template parameter default values can be 
# overriden using the project settings file (project-settings.json).
messages_table_name = CloudCanvas.get_setting('MessagesTable')
greeting = CloudCanvas.get_setting('Greeting')

messages_table = boto3.resource('dynamodb').Table(messages_table_name)

def say_hello(event, context):
    
    print 'event: {}'.format(event)
    print 'context {}'.format(context)
    print 'messages_table_name: "{}"'.format(messages_table_name)
    print 'greeting: "{}"'.format(greeting)

    target = event['Target']

    message = greeting + ' ' + target

    response = messages_table.put_item(
        Item={
            'PlayerId': context.identity.cognito_identity_id,
            'Message': message
        })

    return message
