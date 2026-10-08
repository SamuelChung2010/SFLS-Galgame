## 青春校园：米白纸张、蓝绿姓名签、斜切箭头。背景与原生中文文字分离。
## 只定制 campus_* 样式，主菜单与其他游戏菜单不继承这些改动。
## 精简中文字体未必包含 Latin-1 标点；拉丁字符使用引擎自带字体。
define campus_text_font = FontGroup().add("DejaVuSans.ttf", 0x0000, 0x024F).add(gui.text_font, None, None)
define campus_name_font = FontGroup().add("DejaVuSans.ttf", 0x0000, 0x024F).add(gui.name_text_font, None, None)

transform campus_choice_motion:
    subpixel True
    on hover:
        ease 0.12 xoffset 8
    on idle:
        ease 0.12 xoffset 0
    on insensitive:
        xoffset 0

screen gameplay_quickbar(touch=False, in_dialogue=False):
    frame:
        id "campus_toolbar"
        style "campus_toolbar_frame"
        background (None if in_dialogue else Solid("#FCFBF4F2"))
        hbox:
            xalign 1.0
            spacing 0
            style_prefix "campus_tool"
            textbutton _("回退") action Rollback() id "play_rollback"
            if not touch:
                textbutton _("历史") action ShowMenu("history") id "play_history"
            textbutton _("自动") action Preference("auto-forward", "toggle") id "play_auto"
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True) id "play_skip"
            if not touch:
                textbutton _("保存") action ShowMenu("save") id "play_save"
                textbutton _("读取") action ShowMenu("load") id "play_load"
                textbutton _("设置") action ShowMenu("preferences") id "play_settings"
            else:
                textbutton _("菜单") action ShowMenu() id "play_menu"
            textbutton _("更多") action ToggleScreen("gameplay_tools") id "play_more"

screen gameplay_tools():
    modal True
    zorder 110
    key "game_menu" action Hide("gameplay_tools")
    button:
        xfill True
        yfill True
        background Solid("#24495938")
        action Hide("gameplay_tools")
    frame:
        style "campus_tools_popup"
        vbox:
            spacing 8
            style_prefix "campus_popup"
            textbutton _("快速保存") action [Hide("gameplay_tools"), QuickSave()] id "play_quicksave"
            textbutton _("快速读取") action [Hide("gameplay_tools"), QuickLoad()] id "play_quickload"
            textbutton _("隐藏界面") action [Hide("gameplay_tools"), HideInterface()] id "play_hide"
            textbutton _("标题菜单") action [Hide("gameplay_tools"), MainMenu()] id "play_title"
            textbutton _("关闭") action Hide("gameplay_tools") id "play_tools_close"

style campus_dialogue_window is default:
    xalign 0.5
    yalign 1.0
    yoffset -20
    xfill False
    yfill False
    xsize 1480
    yminimum 176
    padding (0, 0)
    background Frame("gui/campus/textbox.svg", 32, 24, 48, 24)

# 底部为框内快捷操作预留空间；正文自身决定卡片高度。
style campus_dialogue_content is default:
    xsize 1480
    yminimum 176
    xfill False
    yfill False
    padding (44, 40, 44, 52)
    background None

style campus_namebox is default:
    pos (36, -22)
    xminimum 160
    xmaximum 1040
    yminimum 52
    padding (24, 8, 36, 8)
    background Frame("gui/campus/namebox.svg", 28, 12, 48, 12)

style campus_speaker is say_label:
    font campus_name_font
    size 26
    xalign 0.0
    yalign 0.5
    color "#FFFFFF"
    outlines [(1, "#174D69", 0, 1)]

style campus_dialogue_text is say_dialogue:
    font campus_text_font
    xpos 0
    ypos 0
    xsize 1392
    size 32
    line_spacing 6
    color "#244959"
    outlines []

style campus_toolbar_frame is frame:
    xalign 0.5
    yalign 1.0
    yoffset -30
    xsize 1480
    padding (44, 0, 64, 0)
    background None

style campus_tool_button is button:
    xminimum 84
    yminimum 32
    padding (12, 4)
    background None
    hover_background Solid("#DFEDE5")
    selected_background Solid("#DFEDE5")
    selected_hover_background Solid("#CDE3D7")
style campus_tool_button_text is button_text:
    font gui.interface_text_font
    size 22
    color "#456477"
    hover_color "#205F63"
    selected_color "#205F63"
    selected_hover_color "#174E52"
    insensitive_color "#899795"
    outlines []

style campus_tools_popup is frame:
    xalign 0.75
    yalign 1.0
    yoffset -76
    padding (20, 20)
    background Frame("gui/campus/textbox.svg", 32, 24, 48, 24)
style campus_popup_button is campus_tool_button:
    xsize 240
    yminimum 56
style campus_popup_button_text is campus_tool_button_text:
    size 26

style campus_choice_viewport is viewport
style campus_choice_side is side:
    spacing 16
style campus_choice_vscrollbar is vscrollbar:
    unscrollable "hide"
    xsize 8
    base_bar Solid("#FCFBF4B8")
    thumb Solid("#589C8C")
style campus_choice_vbox is vbox:
    xfill True
    yminimum 584
    box_align 0.5
    spacing 18
style campus_choice_button is button:
    xalign 0.5
    xsize 1200
    yminimum 88
    padding (56, 22, 88, 22)
    background Frame("gui/campus/choice_idle.svg", 56, 20, 88, 20)
    hover_background Frame("gui/campus/choice_hover.svg", 56, 20, 88, 20)
    insensitive_background Frame("gui/campus/choice_insensitive.svg", 56, 20, 88, 20)
style campus_choice_button_text is button_text:
    font campus_text_font
    size 32
    xalign 0.0
    textalign 0.0
    color "#2C5669"
    hover_color "#174F52"
    insensitive_color "#778681"
    outlines []

## Ren'Py 按 1920×1080 虚拟画布等比缩放；small/touch 单独扩大文字与触摸区域。
style campus_dialogue_window:
    variant "small"
    xsize 1640
    yminimum 208
style campus_dialogue_content:
    variant "small"
    xsize 1640
    yminimum 208
    padding (44, 42, 44, 68)
style campus_dialogue_text:
    variant "small"
    xsize 1552
    size 38
    line_spacing 8
style campus_namebox:
    variant "small"
    xpos 36
style campus_speaker:
    variant "small"
    size 32
style campus_tool_button:
    variant "touch"
    xminimum 132
    yminimum 56
style campus_toolbar_frame:
    variant "small"
    xsize 1640
style campus_tool_button_text:
    variant "small"
    size 26
style campus_popup_button:
    variant "touch"
    xsize 300
    yminimum 76
style campus_popup_button_text:
    variant "small"
    size 32
style campus_choice_button:
    variant "small"
    xsize 1664
    yminimum 104
style campus_choice_vbox:
    variant "small"
    yminimum 520
style campus_choice_button_text:
    variant "small"
    size 40
