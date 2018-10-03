#!/bin/bash

instanceId=$1

aws ec2 modify-instance-attribute \
    --instance-id $instanceId \
    --no-disable-api-termination
