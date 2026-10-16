# 保留原有角色变量；第一章使用下面的校园角色。
define e = Character("艾琳")

define p = Character("我", color="#8DD5FF")
define a = Character("A", color="#FFE680")
define b = Character("B", color="#B5D8EC")
define roommate_e = Character("E", color="#A4E5AE")
define roommate_f = Character("F", color="#C9B6FF")

# 记录 1.1.1 的选择，随存档保存：None / "roommates" / "a"。
default arrival_companion = None

# 关系变化随存档保存；目前只记录剧本指定的增加。
default a_affection = 0
default b_affection = 0


# 主菜单的“开始游戏”从这里进入剧情。
label start:
    call chapter1_1_1
    call chapter1_1_2
    call chapter1_2_1
    return
