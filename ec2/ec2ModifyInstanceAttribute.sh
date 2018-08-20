#!/bin/bash

id=$1

aws ec2 modify-instance-attribute \
    --instance-id $id \
    --no-disable-api-termination
