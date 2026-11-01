# 网页体验版构建与部署

网页版沿用 Ren’Py 8.5.3，官网保持 HTML / CSS / JavaScript 静态网站，不需要游戏服务器或数据库。

## 构建

在项目根目录运行，替换 SDK 和输出目录路径：

```powershell
python tools/build_web_site.py --sdk D:/renpy-8.5.3-sdk --output D:/SFLS_Dear_Moments-web-build
```

SDK 需要安装对应版本的官方 Web 组件。构建会重新生成输出目录中的 `sflsgal-site/play/game/`，因此请使用专门的构建目录，不要在这个生成目录里保存手工修改。

输出：

- `sflsgal-site/`：可部署的完整官网，包含在线试玩。
- `sflsgal-site.zip`：完整网站压缩包，根目录为官网 `index.html`。
- `SFLS_Dear_Moments-web.zip`：独立的 Ren’Py 网页游戏包，可用于其他静态游戏托管。

修改官网请编辑 `website/`，修改游戏仍编辑 `game/`。生成的游戏运行资源不提交 Git。`progressive_download.txt` 使剧情图片与音乐按需加载，菜单图片保留在初始游戏包中。

## 本地预览

```powershell
python -m http.server 4174 --directory D:/SFLS_Dear_Moments-web-build/sflsgal-site
```

打开 `http://127.0.0.1:4174/play/`。不能通过双击 HTML 文件启动 WebAssembly 游戏。

## Cloudflare

继续更新现有绑定 `sflsgal.top` 的静态站点，上传完整 `sflsgal-site/` 内容。当前账户实际使用 Workers 静态资源上传入口。不要把独立的 `SFLS_Dear_Moments-web.zip` 放入站点目录：它是分发用的压缩包，超过静态资源单文件 25 MiB 限制；运行所需资源已在 `play/game/` 中拆开。

构建脚本检查每个部署文件不超过 25 MiB、文件数不超过 20,000。`_headers` 为 WASM 提供正确 MIME 类型，并让网页版资源重新验证缓存。游戏 Service Worker 的作用范围仅为 `/play/game/`。

## 触屏、音频和存档

- iPhone / iPad 使用较新的 Safari，建议横屏。Ren’Py 会检测移动设备并启用现有 touch / small 界面。
- 设备全屏 API 可用时显示“全屏”按钮；不支持时隐藏。
- 浏览器通常要求先点击游戏画面才能播放声音。
- 存档保存在当前设备和浏览器中，不会自动跨设备同步。通过游戏左上角菜单导出或导入存档，清理网站数据之前先备份。
- 当前音乐同时包含 MP3 和 OGG，保留引擎默认音频能力检测与回退，不强制 Safari 使用不支持的音频格式。

参考：[Ren’Py Web 官方文档](https://www.renpy.org/doc/html/web.html)、[Cloudflare 静态资源限制](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/)。
