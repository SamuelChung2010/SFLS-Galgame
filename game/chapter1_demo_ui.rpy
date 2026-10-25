## 第一章 demo 结束页。
screen chapter1_demo_end():
    modal True
    add "chapter1 campus"
    add Solid("#081B2CCB")
    vbox:
        align (0.5, 0.48)
        spacing 26
        text "第一章 · 初入高中":
            font note_text_font
            size 56
            color "#FFFFFF"
            xalign 0.5
        text "Demo · 未完待续":
            font note_text_font
            size 30
            color "#D2E0ED"
            xalign 0.5
        null height 35
        textbutton "返回标题":
            id "demo_title"
            style "note_more_button"
            text_style "note_more_button_text"
            background Solid("#F3F7FA")
            xalign 0.5
            text_xalign 0.5
            action MainMenu(confirm=False)
