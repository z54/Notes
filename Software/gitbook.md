# gitbook

## 依赖
Node.js

## 安装
`npm install gitbook-cli -g`
## 管理
更新 GitBook命令：`npm update gitbook-cli -g`

## 使用
1. 新建并进入库目录
2. 执行 `gitbook init` 得到文件 `README.md` 和 `SUMMARY.md`
3. 按以下格式以目录结构编辑 `SUMMARY.md`
    ``` 
        # Summary

        * [项目简介](README.md)
        * [快速开始](docs/快速开始.md)
            * [环境搭建](docs/环境搭建.md)
            * [简单使用](docs/简单使用.md)
        * [学入学习](docs/深入学习)  
    ```
4. 执行`gitbook init`，则没有的目录和文件都会被创建，编辑对应文件填充。
5. 执行`gitbook serve`启动服务，打开浏览器 http://localhost:4000/ 或 http://127.0.0.1:4000/ 查看显示书籍的效果。