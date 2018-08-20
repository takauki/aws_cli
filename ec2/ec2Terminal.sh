#!/bin/bash

instanceId=$1

aws ec2 terminate-instances \
     --instance-ids $instanceId
