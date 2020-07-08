from random import *
#seed(100)
num=randint(0,20)
count=0
while 1:
       try :
              usernum=eval(input("请输入您猜测的数字："))
              count+=1
              if usernum > num:
                     print("遗憾！太大了")
              elif usernum <num:
                     print("遗憾！太小了")
              elif usernum==num:
                     print("预测{}次，你猜中了！".format(count))
                     break
       except:
              print("输入有误！")

