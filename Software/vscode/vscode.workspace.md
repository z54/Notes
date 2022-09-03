# 工作区配置

.code-workspace

## 空

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

## tex

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

    }
}
```

## Markdown

```
	"extensions": {
		"recommendations": [
			"mathiassoeholm.markdown-link-updater",
			"csholmq.excel-to-markdown-table",
			"geeklearningio.graphviz-markdown-preview",
			"cipchk.vscode-markdown-compact-table-formatter",
			"tchayen.markdown-links",
			"kortina.vscode-markdown-notes",
			"qiqiworld.vscode-markdown-tinymind",
			"mushan.vscode-paste-image"
		]
	}
```

## math

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