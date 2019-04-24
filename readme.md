# Elevator Judger  v3.0			

注：**无需更改路径**，按照下述操作可直接运行

## **操作流程**

示例：(下载到本地后执行这段操作即可看到现象)

![Image text]https://github.com/Sonicsss/Elevator_Judger-v3.0/blob/master/image.png

测试自己的程序：

1.将自己的src文件夹替换掉这里的src

2.bomber/mode下选择需要的弹夹运行数据生成脚本

3.在当前目录下运行build.py将java文件编译成class文件

4.在当前目录下运行run.py，根据提示输入即可

5.result目录下存放测评结果，其中abstract中存放评测摘要，如果有WA的话，WA_details中将会分析错误详情

## **目前实现的功能：**

1.逻辑检查：IN，OUT，OPEN，CLOSE，ARRIVE行为是否符合逻辑

2.功能检查：电梯能且仅能完成所有请求

3.自定义弹夹：只需在bomber/mode目录下新建一个文件夹即可，可在新建文件夹里存放构造的测试点

4.混合攻击：执行mix弹夹中的copy脚本可将各弹夹中的测试点随机抽取作为混合弹夹

5.附加工具：

（1）tools目录下存放的rename.py可将同目录下所有txt文件转为子弹测试点的命名格式

（2）各弹夹目录下存放着对应的随机数据生成脚本



###### 																		by Sonic 

Contact me：1711284972@qq.com
