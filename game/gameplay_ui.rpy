## 对话、选项与快捷工具使用统一的原生文字样式，避免不同图片字号混排。
screen gameplay_quickbar(touch=False):
    frame:
        style "campus_toolbar_frame"
        hbox:
            spacing 8
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
        background Solid("#00000040")
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
    xsize 1792
    ysize 290
    padding (0, 0)
    background Solid("#0C1722E8")

style campus_namebox is default:
    pos (64, 24)
    padding (0, 0)
    background None

style campus_speaker is say_label:
    size 28
    xalign 0.0
    yalign 0.0
    outlines []

style campus_dialogue_text is say_dialogue:
    xpos 64
    ypos 72
    xsize 1664
    size 32
    line_spacing 9
    color "#F4F7FA"
    outlines []

style campus_toolbar_frame is frame:
    xalign 0.5
    yalign 1.0
    yoffset -12
    padding (12, 4)
    background Solid("#07111C88")

style campus_tool_button is button:
    padding (18, 8)
    background None
    hover_background Solid("#315369")
    selected_background Solid("#244659")
    selected_hover_background Solid("#315369")
style campus_tool_button_text is button_text:
    font gui.interface_text_font
    size 22
    color "#B7C9D6"
    hover_color "#FFFFFF"
    selected_color "#FFE68A"
    selected_hover_color "#FFE68A"
    insensitive_color "#536575"
    outlines []

style campus_tools_popup is frame:
    xalign 0.75
    yalign 1.0
    yoffset -78
    padding (16, 16)
    background Solid("#102536F5")
style campus_popup_button is campus_tool_button:
    xsize 220
    ysize 48
style campus_popup_button_text is campus_tool_button_text:
    size 24

style campus_choice_vbox is vbox:
    xalign 0.5
    ypos 420
    yanchor 0.5
    spacing 18
style campus_choice_button is button:
    xsize 1120
    padding (32, 20)
    background Solid("#102536EB")
    hover_background Solid("#2C637EFA")
    insensitive_background Solid("#10253688")
style campus_choice_button_text is button_text:
    font gui.interface_text_font
    size 30
    xalign 0.5
    textalign 0.5
    color "#E5EEF4"
    hover_color "#FFE68A"
    insensitive_color "#738A98"
    outlines []

style campus_dialogue_window:
    variant "small"
    xsize 1840
    ysize 340
style campus_dialogue_text:
    variant "small"
    xpos 48
    xsize 1744
    size 38
style campus_namebox:
    variant "small"
    xpos 48
style campus_tool_button_text:
    variant "small"
    size 28
