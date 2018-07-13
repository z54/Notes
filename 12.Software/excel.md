# 基础操作

## 单元格内换行

在单元格中输入数据时，只要按下“Alt+Enter”组合键即可直接在单元格光标所在处换行。

# 扩展公式

## QQ联系
```excel
=HYPERLINK("tencent://Message/?websiteName=qzone.qq.com&Menu=yes&Uin="&A3,"点击联系我")
```

## 迷你位图
```excel
=REPT（text，number_times)
=REPT("▍",B2/10)
```

## 自动翻译
```excel
=FILTERXML(WEBSERVICE("http://fanyi.youdao.com/translate?&i="&A2&"&doctype=xml&version"),"//translation")
```

# Reference
- [你见过哪些惊为天人的Excel公式？](https://www.toutiao.com/i6535451547000635907/)