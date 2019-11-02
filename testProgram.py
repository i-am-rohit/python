fs=open('test1.txt','w')
strHash=40*'#'
strCommand="Testcase ReadSignBoard commad.".center(40)
fs.write(strHash+'\n')
fs.write(strCommand+'\n')
fs.write(strHash+'\n')
fs.close()