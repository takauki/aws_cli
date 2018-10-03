#################################################################################
#
# ファイル名　：　awscom.py
# 処理名　　　：　awsのインスタンス削除
# 処理概要　　：　idListファイルに記載されているインスタンスの削除保護を外し
#                 インスタンスを削除する
# 引数　　　　：　
# 使い方（例）：　python awscom.py
#
#################################################################################

import subprocess
import re
import sys
import glob

with open('idList') as LIST:
    getId = LIST.readline().rstrip('\r\n')
 
    while getId:
        if not getId:
            break

        print(getId)
        getId = LIST.readline().rstrip('\r\n')

        ## ec2のインスタンス表示
        #subprocess.call( ["./ec2Describe-filterID.sh" , loopId])

        ## ec2の削除保護解除
        #subprocess.call( ["./ec2ModifyInstanceAttribute.sh" , loopId])

        ## ec2の削除
        #subprocess.call( ["./ec2Terminal.sh" , loopId])
        

