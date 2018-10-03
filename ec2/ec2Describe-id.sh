#!/bin/bash

## 出力結果の絞り込み
fId=$1
fName="tag:Name"
fVale="test*"
## 表示項目の絞り込み
qParam="Reservations[].Instances[].InstanceId[]"

aws ec2 describe-instances |jq .Reservations[].Instances[].InstanceId

#aws ec2 describe-instances \
#    --instance-ids $fId \
#    --filters "Name=$fName,Values=$fVale" \
#    --query $qParam
