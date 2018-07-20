# Git

## initial

```bash
echo "# Operating-system-exploration" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/z54/Operating-system-exploration.git
git push -u origin master
```

### config

```bash
[user]
	email = xxx@xxx.com
	name = xxx
[alias]
	st = status
	ci = commit
	co = checkout
	br = branch
	ps = push -u origin master
[credential]
	helper=store
```

## usage

| /                | /                            |
| ---------------- | ---------------------------- |
| 取消某文件的修改 | `git checkout -- readme.txt` |
| 回滚到上一版本   | `git reset --hard HEAD~1  `  |

### add
| /                | /                            |
| ---------------- | ---------------------------- |
| 添加指定文件到暂存区 |`git add [file1] [file2] ...`|
| 添加指定目录到暂存区，包括子目录 | `git add [dir]`|
| 添加当前目录的所有文件到暂存区 | `git add .`|

### rm

| /                | /                            |
| ---------------- | ---------------------------- |
| 删除工作区文件，并且将这次删除放入暂存区 | `git rm [file1] [file2] ...`|
| 停止追踪指定文件，但该文件会保留在工作区 | `git rm --cached [file]` |
| 添加指定目录到暂存区，包括子目录 | `git add [dir]` |

### multi remote

#### 方法1: 使用命令修改

- 增加
	- 增加第一个地址`git remote add origin <url1>`
	- 增加第二个地址`git remote set-url --add origin <url2>`
- 删除`git remote rm <主机名>`
- 查询`git remote -v`
#### 方法2: 使用配置修改

```
[remote "origin"]
	url = https://github.com/z54/Notes.git
	fetch = +refs/heads/*:refs/remotes/origin/*
	url = http://cs3.swfu.edu.cn/~20141156047/Notes.git
```

### 强制覆盖云

`git push --force`

### 强制覆盖本地

```git
git fetch --all
git reset --hard origin/master
git pull
```

### ignore 忽略文件（指定文件/文件夹 不同步）

添加.gitignore 文件
内容如

```
# 文件（*为通配符）

*.exe

# 目录

video
music

# 排除忽略

!abc.mp3
```

## commit

- message formation

```bash
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

-  type: commit 的类型

	- feat: 新特性
	- fix: 修改问题
	- refactor: 代码重构
	- docs: 文档修改
	- style: 代码格式修改, 注意不是 css 修改
	- test: 测试用例修改
	- chore: 其他修改, 比如构建流程, 依赖管理.

- scope: commit 影响的范围, 比如: route, component, utils, build...

- subject: commit 的概述, 建议符合  50/72 formatting

	- body: commit 具体修改内容, 可以分为多行, 建议符合 50/72 formatting
	- footer: 一些备注, 通常是 BREAKING CHANGE 或修复的 bug 的链接.

## fatal

- fatal: remote origin already exists.

```
$ git remote rm origin
$ git remote add origin https://github.com/z54/Operating-system-exploration.git
```
