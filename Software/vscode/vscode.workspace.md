### 工作区配置

.code-workspace

#### 空

```json
{
	"folders": [
		{
			"path": "."
		}
    ],
    "settings": {}
}
```

#### Root

```json
{
// extensions.json
    "recommendations": [
        "mushan.vscode-paste-image",
        "yzhang.markdown-all-in-one",
        "wayou.vscode-todo-highlight",
        "qiqiworld.vscode-markdown-tinymind",
        "kortina.vscode-markdown-notes",
        "mathiassoeholm.markdown-link-updater",
        "formulahendry.terminal",
        "cipchk.vscode-markdown-compact-table-formatter",
        "csholmq.excel-to-markdown-table",
        "sandcastle.vscode-open",
    ]
}
```

#### markdown

```json
{
	"folders": [
		{
			"path": "."
		}
	],
	"settings": {
		"files.exclude": {
			"**/.aux": true,
			"**/.bbl": true,
			"**/.blg": true,
			"**/.synctex.**": true
		}
    },
    "extensions": {
        "recommendations": [
			"cipchk.vscode-markdown-compact-table-formatter",
            "yzhang.markdown-all-in-one",
		]
    }
}
```

#### dendron

```json
{
  "folders": [
    {
      "path": "vault"
    }
  ],
  "settings": {},
  "extensions": {
    "recommendations": [
      "dendron.dendron-paste-image",
      "dendron.dendron-markdown-shortcuts",
      "redhat.vscode-yaml"
    ]
  }
}
```

#### math

> tex, markdown

```json
// math.code-workspace
```

```json
// extensions.json
{
    "recommendations": [
        "mathpix.vscode-mathpix-markdown",
        "yzhang.markdown-all-in-one",
        "qiqiworld.vscode-markdown-tinymind"
    ]
}
```