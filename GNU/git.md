# initial

```
echo "# Operating-system-exploration" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/z54/Operating-system-exploration.git
git push -u origin master
```

## multi remote

### 方法1: 使用命令修改

- 增加
	- 增加第一个地址`git remote add origin <url1>`
	- 增加第二个地址`git remote set-url --add origin <url2>`
- 删除`git remote rm <主机名>`

### 方法2: 使用配置修改

```
[remote "origin"]
	url = https://github.com/z54/Notes.git
	fetch = +refs/heads/*:refs/remotes/origin/*
	url = http://cs3.swfu.edu.cn/~20141156047/Notes.git
```

## 强制覆盖云

`git push --force`

## 强制覆盖本地

```git
git fetch --all
git reset --hard origin/master 
git pull
```

## config

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
	ad = remote set-url --add origin <url>
[credential]
	helper=store
```

## usage

| /                | /                            |
| ---------------- | ---------------------------- |
| 取消某文件的修改 | `git checkout -- readme.txt` |
| 回滚到上一版本   | `git reset --hard HEAD~1  `  |

# fatal

## fatal: remote origin already exists.

```
$ git remote rm origin
$ git remote add origin https://github.com/z54/Operating-system-exploration.git
```
