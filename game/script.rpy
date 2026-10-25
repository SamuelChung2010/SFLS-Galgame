# 第一章 demo：角色、可存档状态与完整流程。
define e = Character("艾琳")
define p = Character("我", color="#8DD5FF")
define a = Character("倒霉熊", color="#FFE680")
define b = Character("齐文昌", color="#B5D8EC")
define d = Character("小邓", color="#FFC99D")
define roommate_e = Character("王力豪", color="#A4E5AE")
define roommate_f = Character("李哥", color="#C9B6FF")
define g = Character("G", color="#9EDFD4")
define teacher = Character("老师", color="#E7D6B7")
define teammate = Character("队友", color="#D5E0E9")

default arrival_companion = None
default football_choice = None
default helped_e = None
default paper_reward_received = False
default a_affection = 0
default b_affection = 0
default d_affection = 0
default e_affection = 0
default g_affection = 0
default chapter1_demo_completed = False

label start:
    call chapter1_1_1
    call chapter1_1_2
    call chapter1_2_1
    call chapter1_2_2
    call chapter1_2_3
    call chapter1_3_1
    call chapter1_3_2
    $ chapter1_demo_completed = True
    $ quick_menu = False
    window hide
    play music "audio/bgm/Title Bgm.ogg" fadein 1.0 volume 0.6
    call screen chapter1_demo_end
    return
