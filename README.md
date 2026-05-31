# github-weekly-feishu

把 GitHub/AI 周报 Markdown 转成适合飞书导入和 Word 编辑的 `.docx` 文件。

这个项目适合中文技术内容创作者、开源学习社群和课程整理者：先用 Markdown 写周报、项目推荐或学习笔记，再一键生成排版更稳定的文档，用于飞书、Word 或后续发布流程。

## 功能

- 支持 Markdown 标题、段落、引用、无序列表、有序列表、链接、表格和图片。
- 链接会转换为 `标题（URL）`，方便在文档平台里保留来源。
- 图片按相对路径读取；缺失图片会跳过，不中断生成。
- 提供命令行工具和 Python API。

## 安装

开发环境推荐直接从仓库安装：

```bash
python -m pip install -e .
```

## 命令行使用

```bash
github-weekly-feishu examples/weekly.md --output dist/weekly.docx
```

如果 Markdown 里的图片路径相对某个资源目录，可以指定 `--assets-root`：

```bash
github-weekly-feishu examples/weekly.md \
  --output dist/weekly.docx \
  --assets-root .
```

不传 `--output` 时，默认在源文件旁生成同名 `.docx`。

## Python API

```python
from pathlib import Path

from github_weekly_feishu import build_doc

build_doc(
    source=Path("examples/weekly.md"),
    output=Path("dist/weekly.docx"),
    assets_root=Path("."),
)
```

## Markdown 支持范围

当前版本专注于周报类内容的常见结构：

- `#` 到 `######` 标题
- `>` 引用
- `-`、`*`、`+` 无序列表
- `1.` 有序列表
- Markdown 表格
- Markdown 链接
- Markdown 图片

它不是完整 Markdown 渲染器，而是一个轻量的发布工作流工具。复杂排版建议先在 Markdown 中保持结构简单，再生成 `.docx`。

## 开发与测试

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

也可以直接用标准库测试运行器执行：

```bash
python -m unittest
```

## 维护计划

- 改进 Markdown 表格和列表转换质量。
- 增加更多中文周报模板。
- 增加发布前检查，例如链接格式、缺失图片提示和字数统计。
- 用 Codex 辅助维护 issue、测试、文档和 release note。

## 贡献

欢迎提交 issue 和 pull request，尤其是：

- 飞书导入后的格式问题。
- 中文技术周报的真实样例。
- Markdown 结构兼容性改进。
- 自动化发布工作流建议。

## License

MIT
