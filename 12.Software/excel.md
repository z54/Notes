# excel

## 快捷键

| 快捷键        | 功能         |
| ------------- | ------------ |
| Alt+Enter     | 单元格内换行 |
| Ctrl+;| 当前日期 |
| Ctrl+Pageup   | 上一个工作表 |
| Ctrl+PageDown | 下一个工作表 |

## 公式

- if `=if(c3>60,"合格","不合格")`

## 扩展公式

- QQ联系

```excel
=HYPERLINK("tencent://Message/?websiteName=qzone.qq.com&Menu=yes&Uin="&A3,"点击联系我")
```

- 迷你位图

```excel
=REPT（text，number_times)
=REPT("▍",B2/10)
```

- 自动翻译

```excel
=FILTERXML(WEBSERVICE("http://fanyi.youdao.com/translate?&i="&A2&"&doctype=xml&version"),"//translation")
```

## fatal

[EXCEL每次打开文件都会出现一个空白sheet1窗口-CSDN论坛](https://bbs.csdn.net/topics/392258511?page=1)

## Reference
- [你见过哪些惊为天人的Excel公式？](https://www.toutiao.com/i6535451547000635907/)