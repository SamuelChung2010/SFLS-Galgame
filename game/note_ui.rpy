## 「课间笔记」游戏内界面：米白笔记纸、角色色姓名贴、挂在纸边的索引标签、荧光笔选项。
## 只有 say / choice / quick_menu 使用 note_* 样式；主菜单、设置等界面保持原样。
## 文字全部为 Ren'Py 原生文本，gui/note/ 中的 SVG 只负责形状与颜色。
##
## 尺寸以 1920×1080 虚拟画布为准：
##   桌面  对话纸宽 1240（约 65%），正文 32，下方索引标签高 46。
##   touch 标签高 74、按钮宽 ≥112；small 对话纸宽 1680，正文 42。

## 精简版思源黑体有全部 ASCII，但缺 Latin-1 补充（如“·”）和 ★☆♪ 等符号。
## 只把这两段交给引擎自带的 DejaVu Sans，其余字符仍用项目字体。
define note_text_font = FontGroup().add("DejaVuSans.ttf", 0x00A0, 0x024F).add("DejaVuSans.ttf", 0x2600, 0x26FF).add(gui.text_font, None, None)
define note_name_font = FontGroup().add("DejaVuSans.ttf", 0x00A0, 0x024F).add("DejaVuSans.ttf", 0x2600, 0x26FF).add(gui.name_text_font, None, None)

init python:

    def note_speaker_colors(who):
        """
        用 Character(color=...) 里已有的角色色给姓名贴上色，不改动角色定义。
        找不到对应角色（例如 Python 直接调用 renpy.say）时用默认浅蓝。
        返回 (底色, 文字色)。
        """

        color = None

        try:
            speaker = renpy.eval_who(store._last_say_who)
            if renpy.substitute(speaker.name) == who:
                color = speaker.who_args.get("color")
        except Exception:
            color = None

        color = Color(color or "#D6E6FF")
        r, g, b = color.rgb

        # 角色色都是浅色，配深蓝字；以后若有深色角色色，自动改用白字。
        if 0.299 * r + 0.587 * g + 0.114 * b > 0.55:
            return color, "#18355C"
        else:
            return color, "#FFFFFF"

    def note_plate(color):
        """姓名贴：着色的底 + 不着色的深蓝描边与错位阴影。"""

        return Fixed(
            # 在图像层着色，软件渲染也能显示角色颜色；描边保持深蓝。
            Frame(im.MatrixColor("gui/note/plate_fill.svg", im.matrix.tint(*Color(color).rgb)), 22, 0, 22, 0),
            Frame("gui/note/plate_line.svg", 22, 0, 22, 0),
        )

    def note_choice_area(with_say):
        """
        选项区底边贴近对话纸上方，少量选项靠近视线，过多时向上展开并滚动。
        若提问台词与选项同时显示，底边再上移，给最多四行的对话纸留位置。
        返回 viewport 的 (x, y, 宽, 高)；宽度含右侧 20 px 滚动条，按钮仍在画面正中。
        """

        if renpy.variant("small"):
            width, top, bottom = 1564, 64, (620 if with_say else 900)
        else:
            width, top, bottom = 1008, 96, (700 if with_say else 880)

        return ((1920 - width) // 2, top, width + 20, bottom - top)


## 继续提示：纸张右下角的小箭头轻轻浮动。
transform note_next_bob(dx=-26, dy=-18):
    xalign 1.0
    yalign 1.0
    xoffset dx
    yoffset dy
    block:
        easein 0.5 yoffset (dy + 4)
        easeout 0.5 yoffset dy
        repeat

## 选项悬停时向右轻推，呼应主菜单丝带的移动。
transform note_choice_nudge:
    subpixel True
    on hover:
        ease 0.12 xoffset 8
    on idle:
        ease 0.12 xoffset 0
    on insensitive:
        xoffset 0


## 快捷栏：贴在对话纸下缘右侧，像笔记本的索引标签。
## 没有对话纸时（选项、window hide）在原位置独立显示，位置不跳。
screen note_quickbar(attached=True):
    frame:
        id "note_tabs"
        style "note_tabs"
        background Frame(("gui/note/tabs_attached.svg" if attached else "gui/note/tabs_floating.svg"), 14, 2, 14, 14)

        hbox:
            style_prefix "note_tab"
            textbutton _("回退") id "qm_back" action Rollback()
            textbutton _("历史") id "qm_history" action ShowMenu("history")
            textbutton _("自动") id "qm_auto" action Preference("auto-forward", "toggle")
            textbutton _("快进") id "qm_skip" action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("保存") id "qm_save" action ShowMenu("save")
            textbutton _("读取") id "qm_load" action ShowMenu("load")
            textbutton _("更多") id "qm_more" action ToggleScreen("note_more")

## 次要操作收进“更多”。点击面板外、右键或 Esc 关闭。
screen note_more():
    modal True
    zorder 110
    key "game_menu" action Hide("note_more")

    button:
        id "note_more_scrim"
        style "note_more_scrim"
        action Hide("note_more")

    frame:
        id "note_more_panel"
        style "note_more_panel"

        vbox:
            style_prefix "note_more"
            textbutton _("快速保存") id "qm_qsave" action [Hide("note_more"), QuickSave()]
            textbutton _("快速读取") id "qm_qload" action [Hide("note_more"), QuickLoad()]
            textbutton _("设置") id "qm_prefs" action [Hide("note_more"), ShowMenu("preferences")]
            textbutton _("隐藏界面") id "qm_hide" action [Hide("note_more"), HideInterface()]
            textbutton _("返回标题") id "qm_title" action [Hide("note_more"), MainMenu()]


## 对话纸 ######################################################################

style note_window is default:
    xalign 0.5
    yalign 1.0
    yoffset -56
    xsize 1240
    xfill False
    yfill False
    padding (0, 0)
    background Frame("gui/note/card.svg", 36, 28, 36, 12)

## 高度由正文决定：一行约 112 px，四行约 274 px；底部不为按钮预留空白。
style note_body is default:
    xsize 1240
    padding (52, 40, 52, 26)
    background None

## 旁白没有姓名贴，顶部留白收窄。
style note_body_narration is note_body:
    top_padding 28

style note_dialogue is say_dialogue:
    font note_text_font
    xpos 0
    ypos 0
    xsize 1136
    size 32
    line_spacing 8
    color "#1E3350"
    outlines []

## 姓名贴跨在纸张上缘左侧，宽度随名字伸缩。
style note_namebox is default:
    pos (30, -26)
    ysize 54
    xminimum 140
    xmaximum 1100
    padding (28, 1, 32, 5)

style note_name is say_label:
    font note_name_font
    size 27
    bold True
    xalign 0.0
    yalign 0.5
    outlines []


## 索引标签快捷栏 #################################################################

## 对话纸右缘 x=1580，向内 24；上缘与纸张底边重叠 2 px，盖住边线形成一体。
style note_tabs is frame:
    xanchor 1.0
    xpos 1556
    yanchor 1.0
    ypos 1070
    ysize 48
    padding (12, 2, 12, 4)

style note_tab_hbox is hbox:
    spacing 0

style note_tab_button is button:
    xminimum 74
    yfill True
    padding (14, 0, 14, 0)
    background None
    hover_background Frame("gui/note/tab_hover.svg", 10, 10)
    selected_background Frame("gui/note/tab_on.svg", 10, 10)
    selected_hover_background Frame("gui/note/tab_hover.svg", 10, 10)

style note_tab_button_text is button_text:
    font note_text_font
    size 22
    xalign 0.5
    yalign 0.5
    color "#4F6987"
    hover_color "#18355C"
    selected_color "#0B6E44"
    selected_hover_color "#18355C"
    insensitive_color "#97A6B6"
    outlines []

style note_more_scrim is button:
    xfill True
    yfill True
    padding (0, 0)
    background Solid("#0B1F3826")
    hover_background Solid("#0B1F3826")

## 面板右缘与快捷栏对齐，底边在快捷栏上方。
style note_more_panel is frame:
    xanchor 1.0
    xpos 1561
    yanchor 1.0
    ypos 1014
    padding (14, 14, 19, 19)
    background Frame("gui/note/panel.svg", 30, 30, 30, 30)

style note_more_vbox is vbox:
    spacing 4

style note_more_button is button:
    xsize 232
    ysize 58
    padding (20, 0, 20, 0)
    background None
    hover_background Frame("gui/note/tab_hover.svg", 10, 10)

style note_more_button_text is note_tab_button_text:
    size 26
    xalign 0.0


## 选项 ########################################################################

style note_choice_viewport is viewport

style note_choice_side is side:
    spacing 12

style note_choice_vscrollbar is vscrollbar:
    xsize 8
    unscrollable "hide"
    base_bar Solid("#FFFDF8B3")
    thumb Solid("#2F72E6")

style note_choice_vbox is vbox:
    xfill True
    box_align 1.0
    spacing 16

## 左侧 46 留给蓝色标记条，右下 4 px 是悬停阴影。
style note_choice_button is button:
    xalign 0.5
    xsize 984
    yminimum 84
    padding (46, 16, 44, 20)
    background Frame("gui/note/choice_idle.svg", 24, 24, 28, 28)
    hover_background Frame("gui/note/choice_hover.svg", 24, 24, 28, 28)
    insensitive_background Frame("gui/note/choice_insensitive.svg", 24, 24, 28, 28)

style note_choice_button_text is button_text:
    font note_text_font
    size 31
    xalign 0.0
    textalign 0.0
    color "#1E3350"
    hover_color "#18355C"
    insensitive_color "#8C99A7"
    outlines []


## 触摸与小屏 ####################################################################
## touch：标签与“更多”按钮加高加宽；small：对话纸、文字和选项整体放大。

style note_window:
    variant "touch"
    yoffset -84

style note_tabs:
    variant "touch"
    ysize 76
    padding (12, 2, 12, 6)

style note_tab_button:
    variant "touch"
    xminimum 112

style note_tab_button_text:
    variant "touch"
    size 28

style note_more_panel:
    variant "touch"
    ypos 986

style note_more_button:
    variant "touch"
    xsize 300
    ysize 86

style note_more_button_text:
    variant "touch"
    size 32

style note_window:
    variant "small"
    xsize 1680

style note_body:
    variant "small"
    xsize 1680
    padding (64, 50, 64, 34)

style note_body_narration:
    variant "small"
    top_padding 36

style note_dialogue:
    variant "small"
    xsize 1552
    size 42
    line_spacing 10

style note_namebox:
    variant "small"
    pos (36, -34)
    ysize 68
    padding (34, 1, 40, 7)

style note_name:
    variant "small"
    size 35

style note_tabs:
    variant "small"
    xpos 1776

style note_tab_button_text:
    variant "small"
    size 30

style note_more_panel:
    variant "small"
    xpos 1781

style note_choice_vbox:
    variant "small"
    spacing 20

style note_choice_button:
    variant "small"
    xsize 1540
    yminimum 108
    padding (58, 22, 54, 26)

style note_choice_button_text:
    variant "small"
    size 42
