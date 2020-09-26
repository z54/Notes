# 7.3 java

# 7.3.1 env

## Install

[Java SE - Downloads | Oracle Technology Network | Oracle](http://www.oracle.com/technetwork/java/javase/downloads/index.html)

下载JDK并安装

## PATH
计算机 - 属性 - 高级系统设置 - 环境变量

- JAVA_HOME
先设置这个系统变量名称，变量值为JDK在你电脑上的安装路径：`C:\Program Files\Java\jdk1.8.0_20`。创建好后则可以利用`%JAVA_HOME%`作为JDK安装目录的统一引用路径。
 
- Path
PATH属性已存在，可直接编辑，在原来变量后追加：`;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin`。
 
- CLASSPATH 
新建系统变量：CLASSPATH  变量值为：`.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar` 。
> 注意变量值字符串前面有一个"."表示当前目录，设置CLASSPATH 的目的，在于告诉Java执行环境，在哪些目录下可以找到您所要执行的Java程序所需要的类或者包。

## 输入

```java
import java.util.Scanner;

public class t1000 {
	public static void main() {
		int a, b, s;
		Scanner sc = new Scanner(System.in);
		a = sc.nextInt();
		b = sc.nextInt();
		s = a + b;
		System.out.println(s);
	}
}
```

## 字符串截取
	L=N.substring(0,i).trim();  

	来自 <http://heisetoufa.iteye.com/blog/227238>

## java截取字符串，截串，substring和split，分割字母和数字，正则缝隙
	博客分类： 
	• java
	Java正则表达式 
	需求，把"01:大汽车"，分成01和大汽车
	有两种做法：一是substring
	Java代码  
```java
package test;  

public class substringTest  
{  
    public static void main(String args[])   
    {   
        String N = "01:大汽车";   
        String L="";   
        String R="";   
        int k= N.length();   
        for (int i = 0; i < N.length(); i++)   
        {   
            if (N.substring(i, i + 1).equals("|"))   
            {     
                L=N.substring(0,i).trim();   
                R=N.substring(i+1,k).trim();   
            }   
            else   
            {   
            
            }   
            System.out.println(L);   
            System.out.println(R);   
        }  
    }  
}   
```

另外一种方法

```java

public class splitTest  
{  
    public static void main(String[] args)  
    {  
        String s = new String("01:大汽车");   
        String a[] = s.split(":");  
  
        System.out.println(a[0]);  
        System.out.println(a[1]);  
    }  
}  
```
## split分割字母和数字，简单正则缝隙
```java
public class Test01 {  
    public static void main(String[] args) {  
        String str = "one123";  
        String regex = "(?<=one)(?=123)";  
        String[] strs = str.split(regex);  
        for(int i = 0; i < strs.length; i++) {  
            System.out.printf("strs[%d] = %s%n", i, strs[i]);  
        }  
    }  
}  
```

### substring讲解：
 
s＝s.substring(int begin);截取掉s从首字母起长度为begin的字符串，将剩余字符串赋值给s；
s＝s.substring(int begin，int end);截取s中从begin开始至end结束时的字符串，并将其赋值给s;
split讲解：
java.lang.string.split
split 方法
将一个字符串分割为子字符串，然后将结果作为字符串数组返回。
stringObj.split([separator，[limit]])
参数
stringObj 
必选项。要被分解的 String 对象或文字。该对象不会被 split 方法修改。
separator 
可选项。字符串或 正则表达式 对象，它标识了分隔字符串时使用的是一个还是多个字符。如果忽
略该选项，返回包含整个字符串的单一元素数组。 
limit
可选项。该值用来限制返回数组中的元素个数。
说明
split 方法的结果是一个字符串数组，在 stingObj 中每个出现 separator 的位置都要进行分解
。separator 不作为任何数组元素的部分返回。
split 的实现直接调用的 matcher 类的 split 的方法。“ . ”在正则表达式中有特殊的含义，因此我们使用的时候必须进行转义。
Java代码  

```java
public static void main(string[] args) {  
    string value = "192.168.128.33";  
    string[] names = value.split("\\.");  
    for (int i = 0; i < names.length; i++) {  
        system.out.println(names[i]);  
    }
}  
```
	 如果用竖线“|”分隔的话，将出现不可得到的结果，必须改为“\\|”  

[java截取字符串，截串，substring和split，分割字母和数字，正则缝隙 - 黑色头发 - ITeye博客](http://heisetoufa.iteye.com/blog/227238)

## java用substring函数截取string中一段字符串

在String中有两个substring()函数，如下：

一：String.substring(int start)

参数：

    start：要截取位置的索引

返回：

   从start开始到结束的字符串

例如：
```java
String str = "hello word!";
System.out.println(str.substring(1));
System.out.println(str.substring(3));
System.out.println(str.substring(6));
```
将得到结果为：
```
ello word!
lo word!
ord!
```
如果start大于字符串的长度将会抛出越界异常；

二：String.substring(int beginIndex, int endIndex)

参数：

`beginIndex 开始位置索引`
`endIndex    结束位置索引`

返回：

      从beginIndex位置到endIndex位置内的字符串

例如：

```java
String str = "hello word!";
System.out.println(str.substring(1,4));
System.out.println(str.substring(3,5));
System.out.println(str.substring(0,4));
```

将得到结果为：
```
ell
lo
hell
```
如果startIndex和endIndex其中有越界的将会抛出越界异常。

[java用substring函数截取string中一段字符串 - 阿曚 - 博客园](http://www.cnblogs.com/laiweili/archive/2012/11/26/2789503.html)

## Java中字符(串)和数值类型的转换

```java
String string="123";
int x=Integer.parseInt(string);
System.out.println("1:字符串转数值 "+x);
  
char c='5';
int x1=c-'0';
System.out.println("2:字符转数值 "+x1);
  
int v=123;
String s1=String.valueOf(v);
String s2=Integer.toString(v);
System.out.println("3:数值转字符串/字符 "+s1+" "+s2);
  
String str="abc123";
StringBuffer buf=new StringBuffer();
char[] ch=str.toCharArray();

for(int i=0;i<ch.length;i++){
    if(ch[i]>'0' && ch[i]<'9'){
            buf.append(ch[i]);
    }
}

int b=Integer.valueOf(buf.toString());
int b2=Integer.parseInt(buf.toString());
System.out.println("提取的int值为 "+b+" "+b2);
 
int index=buf.indexOf("2");
System.out.println("字符串\"2\"在串中的位置"+index);
int index1=str.indexOf("123");
System.out.println("字符串\"123\"在串中的位置"+index1); 
```

输出:
   1:字符串转数值 123
   2:字符转数值 5
   3:数值转字符串/字符 123 123
   4:提取的int值为 123 123
      字符串"2"在串中的位置1
      字符串"123"在串中的位置3


[Java中字符(串)和数值类型的转换-就像以往-51CTO博客](http://blog.51cto.com/dongdong1314/79385)
