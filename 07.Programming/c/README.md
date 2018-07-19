# 7.1 c

# env

> 输入以%s型放入数组时，若输入小于数组长度，输入将从数组0位置开始放

`strlen()` 计算数组内已有元素位数；// #include <string.h>

int 整型

% 余数


## 数组已有元素位数
```c
#include <stdio.h>
#include <string.h>


int main(int argc, char const *argv[])
{
	char s[100];
	scanf ("%s", s);
	printf("%d\n", strlen(s));
	return 0;
}
```
## Coin toss 硬币投掷N次问题
```c
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
	int i, t=0;
	srand((unsigned)time(NULL));

	//get the true values and count them
	for(i=0;i<100000;i++){
		if(rand()%2)
			t++;
	}
	printf("硬币经过10000次投掷，其中");
	printf("正面向上次数为：%d，反面向上次数为：%d\n",t,100000-t);
	printf("正面向上概率为：%.2f%\n",t/100000.0*100);
	return 0;
}
```

## 三目运算符

`a?b:c` 三目运算符
对a作判断 如果值为真就执行b，否则执行c

[C程序中a?b:c是什么意思_百度知道](https://zhidao.baidu.com/question/494768749.html)

条件运算符为`?`和`：`，它是一个三目运算符，即有三个参与运算的量。由条件运算符组成条件表达式的一般形式为：
`表达式1？表达式2：表达式3 `
其求值规则为：如果表达式1的值为真，则以表达式2 的值作为条件表达式的值，否则以表达式2的值作为整个条件表达式的值。 

[Ｃ语言的三目运算符 - CSDN博客](https://blog.csdn.net/yuanzhuohang/article/details/5176303)

## 循环
`Do while`
do...while 循环是 while 循环的变体。在检查while()条件是否为真之前，该循环首先会执行一次do{}之内的语句，然后在while()内检查条件是否为真，如果条件为真的话，就会重复do...while这个循环,直至while()为假。

[do while_百度百科](https://baike.baidu.com/item/do%20while/2814046?fr=aladdin)
