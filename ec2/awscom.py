import subprocess
import re
import sys
import glob


args = glob.glob('idList')

with open('idList') as LIST:
    #getId = LIST.readline().rstrip('\r\n')
    getId = LIST.readlines()
 
    for loopId in getId:
        print(loopId, end='')
        #loopId = LIST.readline().rstrip('\r\n')

        ## ec2のインスタンス表示
        #subprocess.call( ["./ec2Describe-filterID.sh" , loopId])

        ## ec2の削除保護解除
        #subprocess.call( ["./ec2ModifyInstanceAttribute.sh" , loopId])

        ## ec2の削除
        #subprocess.call( ["./ec2Terminal.sh" , loopId])
        

