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
- 增加第一个地址
```bash
git remote add origin <url1>
```
- 然后增加第二个地址
```bash
git remote set-url --add origin <url2>
```
- 增加第三个地址
```bash
git remote set-url --add origin <url3>
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
	ad = remote set-url --add origin
[credential]
	helper=store
```
# fatal
## fatal: remote origin already exists.
```
$ git remote rm origin
$ git remote add origin https://github.com/z54/Operating-system-exploration.git
```
