# excel

## 快捷键

| 快捷键        | 功能         |
| ------------- | ------------ |
| Alt+Enter     | 单元格内换行 |
| Ctrl+; | 当前日期 |
| Ctrl+Shift+; | 当前时间 |
| Ctrl+Shift+l | 筛选|
| Ctrl+Shift+{ ↑ | ↓ | ← | → } | 快速选中表格内容 |
| Ctrl+d | 向下填充 |
| Ctrl+r | 向右填充 |
| Ctrl+Pageup   | 上一个工作表 |
| Ctrl+PageDown | 下一个工作表 |

[你绝对不知道的6个Excel快捷键，实用性超强！](https://baijiahao.baidu.com/s?id=1608132713959148188&wfr=spider&for=pc)

## 公式

```excel
<!-- if  -->
=if(c3>60,"合格","不合格")

<!-- vlookup -->
=vlookup(key,range,1,1)

<!-- text  -->
A1 2022/3/22 
="今天是"&TEXT(A1,"YYYY/M/D")

<!-- REPT -->
=REPT(text，number_times)
=REPT("*-", 3) 显示星号和短划线 (*-) 3 次 *-*-*-
=REPT("-",10) 显示短划线 (-) 10 次 ----------
```

- [REPT 函数](https://support.microsoft.com/zh-cn/office/rept-%e5%87%bd%e6%95%b0-04c4d778-e712-43b4-9c15-d656582bb061?ui=zh-cn&rs=zh-cn&ad=cn)
- [TEXT 函数](https://support.microsoft.com/zh-cn/office/text-%E5%87%BD%E6%95%B0-20d5ac4d-7b94-49fd-bb38-93d29371225c)

## 外链扩展公式

- QQ联系

```excel
=HYPERLINK("tencent://Message/?websiteName=qzone.qq.com&Menu=yes&Uin="&A3,"点击联系我")
```

- 翻译

```excel
=FILTERXML(WEBSERVICE("http://fanyi.youdao.com/translate?&i="&A2&"&doctype=xml&version"),"//translation")
=IFERROR(FILTERXML(WEBSERVICE("http://fanyi.youdao.com/translate?&i="&A2&"&doctype=xml&version"),"//translation"),"")
```

=OFFSET($A$1,MOD(COLUMN(A1)+7,8)+ROW(A1)*8-7,)
=OFFSET($A$1,INT(COLUMN(C1)/3)+ROW(A1)*3-3,MOD(COLUMN(C1),3))

## fatal

[EXCEL每次打开文件都会出现一个空白sheet1窗口-CSDN论坛](https://bbs.csdn.net/topics/392258511?page=1)

[Excel 怎样在一行或一列快速输入ABCD_百度知道](https://zhidao.baidu.com/question/2016975136004804828.html)

=CHAR(ROW(A65))

## Reference

- [你见过哪些惊为天人的Excel公式？](https://www.toutiao.com/i6535451547000635907/)