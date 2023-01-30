# 防ak



广受好评的送分题



ida打开

![image-20221207140539396](C:\Users\47652\AppData\Roaming\Typora\typora-user-images\image-20221207140539396.png)

一开始进入汇编界面，于是按F5

![image-20221207140614736](C:\Users\47652\AppData\Roaming\Typora\typora-user-images\image-20221207140614736.png)

发现如果是让![image-20221207140629821](C:\Users\47652\AppData\Roaming\Typora\typora-user-images\image-20221207140629821.png)都为真，则str就是flag

我们进入sub_401530和sub_4015A7观察函数，

![image-20221207140737588](C:\Users\47652\AppData\Roaming\Typora\typora-user-images\image-20221207140737588.png)

第一个i=0，是正着来，

![image-20221207140803804](C:\Users\47652\AppData\Roaming\Typora\typora-user-images\image-20221207140803804.png)

第一个v4=str-1，发现是倒着来，

把str拼起来，答案即为NUAACTF{We1c0me_t0_the_reverse_w0r1d}