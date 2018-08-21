#!/bin/bash

## 出力結果の絞り込み
fId=$1

## 表示項目の絞り込み
qParam="Reservations[].Instances[].Tags[].Value[]"


aws ec2 describe-instances \
    --instance-ids $fId \
    --query $qParam
