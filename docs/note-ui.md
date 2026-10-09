# 课间笔记 UI：独立比较方案

本方案接续 Claude 留在本地的 `game/note_ui.rpy` 与 12 个 SVG，补齐 `say`、`choice`、桌面/触摸 `quick_menu` 的接入。保留米白笔记纸、角色色姓名贴、索引标签快捷栏与黄色荧光笔选项；修正姓名贴着色，使软件与 GPU 渲染使用相同角色色。

![实际引擎对话预览](note-preview/dialogue.jpg)
![普通与悬停选项](note-preview/choices.jpg)

照片与台词和原校园 UI 的测试预览一致，便于比较。正式剧情、主菜单、设置页、角色定义及原 `campus_*` 文件均未改动。截图中的照片是测试场景，正式第一章仍使用既有占位背景。

## 布局

桌面对话纸宽 1240，约占虚拟画布宽度 65%；正文 32，姓名 27。纸张随文字行数扩展，旁白减少顶部留白。姓名贴颜色取自已有 Character 的角色色，并根据明暗选择文字颜色。索引标签挂在纸张下缘右侧；设置、快速保存/读取、隐藏和返回标题收在“更多”，可点击面板外或按 Esc 关闭。

small 对话纸宽 1680、正文 42、姓名 35；touch 快捷标签高 76，保留完整七个入口。选择区从纸张上方向上排列，多选项可滚动；提问台词同时显示时，选项区域上移，为四行正文预留空间。

文本保持 Ren’Py 原生控件；SVG 只负责背景与装饰。测试样例和标签仅在 `tests/note_ui_qa.rpy`，不进入正式剧情。超过四行的长提问仍应拆段，避免选项区与正文同时占用过大空间。

## 运行和比较

切换 `feature/claude-campus-ui` 并在 Ren’Py 启动器启动现有项目，即可从“开始游戏”查看。切回 `main` 可比较另一套已合并的校园 UI。不要将测试脚本留在发布目录。

## 隔离测试

在单独测试副本里，将 `tests/note_ui_qa.rpy` 临时复制到 `game/zz_note_qa.rpy`，运行：

```sh
/path/to/renpy-sdk/renpy.sh "$PWD" test note_ui_qa --overwrite-screenshots --savedir "$PWD/test-saves"
```

无显示器环境可使用 `SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy RENPY_RENDERER=sw`。测试脚本包含此前 QA 使用的周期刷新与独立 RGBA 软件捕获缓冲适配，SDK 和正式游戏代码不含测试适配。设置 `SFLS_UI_QA_OUTPUT` 可指定截图目录；`RENPY_SCALE_FACTOR=0.666666667` 检查 1280×720，`RENPY_VARIANT="small touch mobile"` 与 `RENPY_SCALE_FACTOR=0.5` 检查 960×540。

测试结束后删除临时 `.rpy` 及对应 `.rpyc`。测试存档独立于正式游戏。使用 Ren’Py 8.5.3 验证，尚未验证硬件 GPU、Windows 和真实 Android/iOS 设备。

## 验证结果

Ren’Py 8.5.3 lint 与差异空白检查通过。桌面 1920×1080、缩放 1280×720、small/touch 960×540 均通过五个运行用例，共 15 个用例、65 个引擎断言；另通过角色色、短/长正文几何、选项与四行提问不重叠检查。桌面短台词卡高 115、四行正文高 262；small/touch 对应为 146 与 332。

覆盖原剧情两条选择分支、快速保存/读取、保存/设置/历史页、自动模式、隐藏并恢复界面、长姓名、长选项与八项滚动。预览使用实际引擎的软件渲染，未宣称硬件 GPU 或真实移动设备验证。
