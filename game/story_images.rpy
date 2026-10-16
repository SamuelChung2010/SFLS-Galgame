## 实拍剧情镜头：人物和场景放在同一张照片中，使用 scene 切换整张图。
## 拍摄前使用纯色占位，不要将图片路径写成空字符串。
## 照片准备好后，直接替换对应定义，剧情中的 scene 名称不用改。

# TODO：行李箱上楼镜头；照片就绪后改为：
# image arrival stairs = "images/arrival_stairs.jpg"
image arrival stairs = Solid("#334B60")

# TODO：楼梯间遇见 A 的镜头（人物与背景同框）；照片就绪后改为：
# image arrival meet_a = "images/arrival_meet_a.jpg"
image arrival meet_a = Solid("#52604B")

# TODO：进入寝室，遇见 E、F 的镜头；照片就绪后改为：
# image arrival dorm = "images/arrival_dorm.jpg"
image arrival dorm = Solid("#604B52")

# TODO：开门后 A 递补水啦的镜头；照片就绪后改为：
# image arrival door_a = "images/arrival_door_a.jpg"
image arrival door_a = Solid("#4B6060")

# TODO：A 走回隔壁房间的镜头；照片就绪后改为：
# image arrival a_leaving = "images/arrival_a_leaving.jpg"
image arrival a_leaving = Solid("#4D5268")

# TODO：主角与 E、F 边走边聊的镜头；照片就绪后改为：
# image arrival roommates_walk = "images/arrival_roommates_walk.jpg"
image arrival roommates_walk = Solid("#605D43")

## 在剧情 label 中使用，例如：
##     scene arrival stairs with fade
##     "我拖着行李箱爬上楼梯。"
##     scene arrival meet_a with dissolve

# TODO：主角与 A 一起下楼的完整实拍镜头；照片就绪后改为：
# image arrival with_a_walk = "images/arrival_with_a_walk.jpg"
image arrival with_a_walk = Solid("#435565")


## 1.1.2 / 1.2.1 的完整实拍镜头；拍摄前沿用纯色占位。
# TODO：早晨教室，与 B 初次交谈（人物与背景同框）。
# image chapter1 classroom_morning = "images/chapter1_classroom_morning.jpg"
image chapter1 classroom_morning = Solid("#566774")

# TODO：中午教室，与 B 寻找校园卡。
# image chapter1 classroom_noon = "images/chapter1_classroom_noon.jpg"
image chapter1 classroom_noon = Solid("#716957")

# TODO：中餐厅靠窗座位，与 B 吃饭聊天。
# image chapter1 chinese_restaurant = "images/chapter1_chinese_restaurant.jpg"
image chapter1 chinese_restaurant = Solid("#6C5B51")
