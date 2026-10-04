# 保留原有角色变量；第一章使用下面的校园角色。
define e = Character("艾琳")

define p = Character("我", color="#8DD5FF")
define a = Character("A", color="#FFE680")
define roommate_e = Character("E", color="#A4E5AE")
define roommate_f = Character("F", color="#C9B6FF")

# 记录 1.1.1 的选择，随存档保存：None / "roommates" / "a"。
default arrival_companion = None


# 主菜单的“开始游戏”从这里进入剧情。
label start:
    call chapter1_1_1
    return
