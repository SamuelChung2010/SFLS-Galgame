## 主菜单的三个图层各自响应焦点，移出时立即打断正在播放的动画。
transform title_blue_motion:
    alpha 1.0
    on hover:
        pause 0.20
        ease 0.10 alpha 0.0
    on idle:
        ease 0.12 alpha 1.0
    on insensitive:
        alpha 1.0

transform title_yellow_motion:
    alpha 0.0
    xoffset -240
    on hover:
        parallel:
            easeout 0.20 xoffset 0
        parallel:
            linear 0.06 alpha 1.0
    on idle:
        ease 0.16 xoffset -240 alpha 0.0
    on insensitive:
        alpha 0.0
        xoffset -240

transform title_caption_motion:
    subpixel True
    anchor (0.0, 0.5)
    pos (103, 69)
    zoom 1.0
    on hover:
        easeout 0.20 xoffset 22 zoom 1.12
    on idle:
        ease 0.16 xoffset 0 zoom 1.0
    on insensitive:
        xoffset 0
        zoom 1.0

screen title_ribbon(caption, ribbon_action, button_id):
    button:
        id button_id
        style "title_ribbon_button"
        action ribbon_action

        fixed:
            xysize (830, 110)

            if ribbon_action.get_sensitive():
                add "gui/main_menu/menu_idle.png":
                    xysize (698, 116)
                    ypos -22
                    at title_blue_motion
                # 裁掉透明外边距，使黄条的左端与蓝条同样抵达屏幕边缘。
                add Transform("gui/main_menu/menu_hover.png", crop=(8, 13, 902, 143), xysize=(810, 128)):
                    ypos -32
                    at title_yellow_motion
            else:
                add "gui/main_menu/menu_insensitive.png":
                    xysize (698, 116)
                    ypos -22

            text caption:
                style "title_ribbon_text"
                at title_caption_motion

style title_ribbon_button is button:
    xsize 830
    ysize 110
    padding (0, 0)
    background None
    hover_background None
    insensitive_background None

style title_ribbon_text is button_text:
    font gui.interface_text_font
    size 34
    color "#FFFFFF"
    hover_color "#632B16"
    insensitive_color "#AAB8C2"
    outlines [(2, "#183F68", 0, 0)]
    hover_outlines [(1, "#FFF9BC", 0, 0)]

## 设置、关于和帮助共享顶部导航与内容面板。
screen settings_page(active):
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    add Solid("#061C32B8")

    frame:
        pos (80, 88)
        xysize (1760, 900)
        padding (0, 0)
        background Solid("#EDF5FAF5")

        fixed:
            add Solid("#153B54") xysize (1760, 198)
            add Solid("#FFE66A") pos (0, 198) xysize (1760, 4)

            textbutton _("返回"):
                id "settings_return"
                pos (36, 28)
                style "settings_header_button"
                action Return()

            text _("设置"):
                pos (48, 98)
                size 44
                color "#FFFFFF"

            hbox:
                pos (365, 26)
                spacing 24

                for section, asset, caption in [("system", "System", _("系统")), ("sound", "Sound", _("声音")), ("text", "Text", _("文本"))]:
                    vbox:
                        spacing 6
                        $ idle_height = {"System": 292, "Sound": 252, "Text": 270}[asset]
                        $ hover_height = {"System": 305, "Sound": 265, "Text": 283}[asset]
                        $ idle_icon = Fixed(Transform("gui/settings/Config_" + asset + "_0.png", crop=(0, 0, 501, idle_height), zoom=180.0 / 501, yalign=1.0), xysize=(180, 110))
                        $ hover_icon = Fixed(Transform("gui/settings/Config_" + asset + "_1.png", crop=(0, 7, 501, hover_height), zoom=180.0 / 501, yalign=1.0), xysize=(180, 110))
                        imagebutton:
                            id ("settings_" + section)
                            style "settings_icon_button"
                            idle idle_icon
                            hover hover_icon
                            selected_idle hover_icon
                            selected_hover hover_icon
                            selected active == section
                            action ShowMenu("preferences", section=section, _transition=None)
                            alt caption
                        text caption:
                            xalign 0.5
                            size 24
                            color ("#FFE66A" if active == section else "#C4D7E3")

                textbutton _("关于"):
                    id "settings_about"
                    style "settings_tab_button"
                    selected active == "about"
                    action ShowMenu("about", _transition=None)
                textbutton _("帮助"):
                    id "settings_help"
                    style "settings_tab_button"
                    selected active == "help"
                    action ShowMenu("help", _transition=None)

            viewport:
                id "settings_content"
                style_prefix "settings_page"
                pos (64, 242)
                xysize (1632, 600)
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True
                vbox:
                    spacing 24
                    transclude

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style settings_page_viewport is viewport
style settings_page_side is side:
    spacing 24
style settings_page_vscrollbar is vscrollbar:
    unscrollable "hide"
    xsize 8
    base_bar Solid("#D3DFE7")
    thumb Solid("#5A93AC")

style settings_header_button is button:
    background None
    hover_background None
    padding (12, 8)
style settings_header_button_text is button_text:
    size 26
    color "#D7E7EF"
    hover_color "#FFE66A"

style settings_tab_button is settings_header_button:
    xsize 160
    ysize 150
    selected_background Solid("#244F69")
    hover_background Solid("#244F69")
style settings_tab_button_text is settings_header_button_text:
    size 32
    align (0.5, 0.5)
    selected_color "#FFE66A"

style settings_icon_button is button:
    padding (0, 0)
    background None
    hover_background Solid("#244F69")

style settings_content_label is label
style settings_content_label_text is text:
    font gui.interface_text_font
    size 36
    color "#17455E"
style settings_content_text is text:
    font gui.interface_text_font
    size 26
    color "#526E80"
style settings_content_button is button:
    background Solid("#D9E7EF")
    hover_background Solid("#C4DDEB")
    selected_background Solid("#225B79")
    selected_hover_background Solid("#2B708E")
    padding (26, 14)
style settings_content_button_text is button_text:
    font gui.interface_text_font
    size 30
    color "#254D65"
    hover_color "#103950"
    selected_color "#FFF3A5"
    selected_hover_color "#FFF7CD"
style settings_content_vbox is vbox:
    spacing 22
style settings_content_hbox is hbox:
    spacing 22
style settings_slider is bar:
    xsize 1060
    ysize 24
    left_bar Solid("#328DA8")
    right_bar Solid("#CBDDE8")
    thumb Solid("#E8BC44", xsize=18, ysize=32)
    thumb_shadow None
    left_gutter 9
    right_gutter 9

## 关于、帮助的内容使用浅色面板上的深色文字。
style about_label_text:
    color "#17455E"
style about_text:
    color "#36576B"
    size 27
style help_text:
    color "#36576B"
    size 27
style help_label_text:
    color "#17455E"
    size 27
style help_button:
    background Solid("#D9E7EF")
    hover_background Solid("#C4DDEB")
    selected_background Solid("#225B79")
    padding (24, 12)
style help_button_text:
    color "#254D65"
    hover_color "#103950"
    selected_color "#FFF3A5"
