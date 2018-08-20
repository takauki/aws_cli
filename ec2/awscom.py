import subprocess
import re
import sys
import glob


args = glob.glob('idList')

with open('idList') as LIST:
    word = LIST.readline().rstrip('\r\n')
 
    for i in word:
        print(word)
        word = LIST.readline().rstrip('\r\n')


        ## の削除保護解除
        #subprocess.call( ["./ec2ModifyInstanceAttribute.sh" , word])

        ## ec2の削除
        #subprocess.call( ["./ec2Terminal.sh" , word])
        

