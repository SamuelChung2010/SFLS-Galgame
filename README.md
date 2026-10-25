# SFLS～我挚爱的时光～

**SFLS ~Dear Moments~**

以深圳外国语学校高中部为背景的校园实拍视觉小说，由 **SFLS 计算机科学社**成员合作开发，是 2026–2027 学年社团项目。

[官方网站](https://sflsgal.top/) · [第一章 Demo 下载与说明](https://github.com/SamuelChung2010/SFLS-Galgame/releases/tag/v0.1.0-demo) · [问题反馈](https://github.com/SamuelChung2010/SFLS-Galgame/issues)

![项目中的 SFLS 校园照片](game/gui/main_menu.jpg)

## 第一章 Demo 已发布

**当前体验版：v0.1.0-demo · 2026 年 10 月 25 日发布**

第一章「初入高中」Demo 现已提供下载。本版本在 GitHub Releases 中标记为 **Pre-release**；完整游戏仍在开发，剧情、画面和界面会继续调整。

| 平台 | 游戏包 | 大小 |
| --- | --- | --- |
| Windows / Linux | [Windows / Linux 体验版](https://github.com/SamuelChung2010/SFLS-Galgame/releases/download/v0.1.0-demo/SFLS_Beloved_Days-demo-Win.Linux.zip) | 约 94.9 MiB |
| macOS | [macOS 体验版](https://github.com/SamuelChung2010/SFLS-Galgame/releases/download/v0.1.0-demo/SFLS_Beloved_Days-demo-Mac.zip) | 约 89.3 MiB |

### 如何游玩

1. 下载上表中对应系统的游戏 ZIP 压缩包。
2. **完整解压**到一个文件夹，保留其中所有文件和目录。
3. 运行解压目录中对应系统的游戏启动程序。Windows 使用游戏 `.exe`，其他平台使用包内对应启动文件。

游玩发行包无需另外安装 Ren’Py。Releases 页面自动生成的 **Source code (zip / tar.gz)** 是项目源码；直接游玩请下载上表中的游戏包。

## 关于游戏

你将扮演一名刚进入 SFLS 的高一新生。从搬进宿舍、认识同学，到逐渐熟悉校园，在一段段对话和小小的选择中经历高中生活。

作品以**校园日常、轻喜剧、角色互动、玩梗与亚文化、人物成长**为主要风格，是一部非恋爱向校园视觉小说。

### 本次 Demo 内容

- 第一章现有剧情与选项分支。
- 校园实拍场景、角色互动和背景音乐。
- 自定义主菜单、设置与对话界面。

具体版本内容以 [Release 说明](https://github.com/SamuelChung2010/SFLS-Galgame/releases/tag/v0.1.0-demo)为准。

## 后续开发规划

| 章节 | 主题 | 当前状态 |
| --- | --- | --- |
| 第一章 | 初入高中 | Demo v0.1.0 已发布，后续继续完善 |
| 第二章 | 计算机科学社 | 剧情规划中 |
| 第三章 | 期中考试 | 剧情规划中 |
| 第四章 | 运动会 | 剧情规划中 |

整体叙事暂定采用「共通主线 + 人物关系支线 + 校园事件短支线 + 多结局」。以上为开发规划，不代表本次 Demo 已包含全部内容；后续安排以项目更新为准。

## 英文名称

项目英文名统一为 **SFLS ~Dear Moments~**，打包标识使用 `SFLS_Dear_Moments`。

## 开发与项目结构

- 引擎：Ren’Py 8
- 语言：Ren’Py Script + Python
- 编辑器：Visual Studio Code
- 版本管理：Git + GitHub

```text
game/                   游戏程序与运行资源
├── script.rpy          角色、游戏状态与第一章流程入口
├── story/              已实现的剧情脚本
├── pictures/           剧情画面
├── audio/              音乐与音效
├── gui/                界面素材
├── screens.rpy         界面定义
└── options.rpy         游戏配置
story/                  剧情原稿、人物设定与大纲
PNG/                    界面设计素材
docs/                   界面实现说明与预览
tests/                  测试与验证脚本
```

开发者可下载或克隆仓库源码，在 Ren’Py 8 Launcher 中添加项目所在目录，再启动项目。修改剧情前可先阅读 [项目协作说明](AGENTS.md)、[人物设定](story/characters.md)和[剧情大纲](story/outline.md)。

## 问题反馈

欢迎通过 [Issues](https://github.com/SamuelChung2010/SFLS-Galgame/issues)报告问题或提出建议。反馈时请附上游戏版本、操作系统、出现问题的场景、复现步骤，以及方便提供的截图或报错信息。

---

开发：**SFLS 计算机科学社** · [sflsgal.top](https://sflsgal.top/)

学生创作作品，非学校官方出品。

