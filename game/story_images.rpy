## 完整实拍镜头，以人物/关键动作优先选取 16:9 裁切框，再铺满 1920×1080。
## 裁切只在 Ren'Py 显示时执行，原始照片和游戏副本不改动。
## 4:3 人物近景优先保留头顶；接笔镜头优先保留手与笔。

image chapter1 campus = Transform("pictures/demo/campus.jpg", crop=(0.0, 0, 1920.0, 1080), crop_relative=False, xysize=(1920, 1080))
image chapter1 a_door = Transform("pictures/demo/1.1.1/dorm1.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 a_standing = Transform("pictures/demo/1.1.1/dorm6.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 a_talk = Transform("pictures/demo/standby/A/329.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 a_tired = Transform("pictures/demo/standby/A/328.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 dorm_f = Transform("pictures/demo/1.1.1/dorm2.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 dorm_f_think = Transform("pictures/demo/1.1.1/dorm3.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 dorm_f_folded = Transform("pictures/demo/1.1.1/355.JPG", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 dorm_f_pondering = Transform("pictures/demo/1.1.1/372.JPG", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 dorm_e = Transform("pictures/demo/1.1.1/dorm4.jpg", crop=(0.0, 0, 1280.0, 720), crop_relative=False, xysize=(1920, 1080))
image chapter1 dorm_e_folded = Transform("pictures/demo/1.1.1/dorm5.jpg", crop=(0.0, 0, 1280.0, 720), crop_relative=False, xysize=(1920, 1080))
## 重新拍摄的教室照：站立、落座和交谈的不同视角。
## 捡笔与递笔暂无对应动作特写，先使用落座镜头承接对白。
image chapter1 b_enter = Transform("pictures/demo/1.1.2/Weixin Image_20261030183131_350_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_enter_near = Transform("pictures/demo/1.1.2/Weixin Image_20261030183131_342_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_seated = Transform("pictures/demo/1.1.2/Weixin Image_20261030183131_339_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_side = Transform("pictures/demo/1.1.2/Weixin Image_20261030183131_332_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_pen_reach = Transform("pictures/demo/1.1.2/Weixin Image_20261030183131_334_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_pen_return = Transform("pictures/demo/1.1.2/Weixin Image_20261030183131_341_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 corridor = Transform("pictures/demo/1.2.1/corridor1.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 d_running = Transform("pictures/demo/1.2.1/corridor2.jpg", crop=(0, 1.312, 1702, 957.375), crop_relative=False, xysize=(1920, 1080))
image chapter1 d_near = Transform("pictures/demo/1.2.1/corridor3.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 d_hand = Transform("pictures/demo/1.2.1/corridor5.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 oldbuilding = Transform("pictures/demo/1.2.1/oldbuilding1.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 oldbuilding_walk = Transform("pictures/demo/1.2.1/oldbuilding2.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 oldbuilding_room = Transform("pictures/demo/1.2.1/oldbuilding3.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 props = Transform("pictures/demo/1.2.1/ob5.jpg", crop=(0, 1.312, 1702, 957.375), crop_relative=False, xysize=(1920, 1080))
image chapter1 sword = Transform("pictures/demo/1.2.1/ob6.jpg", crop=(0, 1.312, 1702, 957.375), crop_relative=False, xysize=(1920, 1080))
image chapter1 d_pose = Transform("pictures/demo/1.2.1/ob7.jpg", crop=(0, 1.312, 1702, 957.375), crop_relative=False, xysize=(1920, 1080))
image chapter1 d_sword = Transform("pictures/demo/1.2.1/ob8.jpg", crop=(0, 1.312, 1702, 957.375), crop_relative=False, xysize=(1920, 1080))
image chapter1 d_hero = Transform("pictures/demo/1.2.1/ob9.jpg", crop=(0, 1.312, 1702, 957.375), crop_relative=False, xysize=(1920, 1080))
image chapter1 d_leaving = Transform("pictures/demo/1.2.1/ob10.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 night_f = Transform("pictures/demo/1.2.2/dorm1.jpg", crop=(0, 27.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 night_e = Transform("pictures/demo/1.2.2/dorm2.jpg", crop=(0, 0.25, 1672, 940.5), crop_relative=False, xysize=(1920, 1080))
image chapter1 night_f_think = Transform("pictures/demo/1.2.2/dorm3.jpg", crop=(0, 27.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 night_e_point = Transform("pictures/demo/1.2.2/dorm4.jpg", crop=(0, 0.25, 1672, 940.5), crop_relative=False, xysize=(1920, 1080))
image chapter1 night_f_smile = Transform("pictures/demo/1.2.2/dorm5.jpg", crop=(0, 67.5, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 field = Transform("pictures/demo/1.2.3/footballfield1.jpg", crop=(0, 135.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 ball = Transform("pictures/demo/1.2.3/footballfield2.jpg", crop=(0, 135.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 g_hand = Transform("pictures/demo/1.2.3/footballfield3.jpg", crop=(0, 81.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 g_think = Transform("pictures/demo/1.2.3/footballfield4.jpg", crop=(0, 94.5, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 g_talk = Transform("pictures/demo/1.2.3/footballfield5.jpg", crop=(0, 94.5, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 g_sorry = Transform("pictures/demo/1.2.3/footballfield6.jpg", crop=(0, 94.5, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 g_play = Transform("pictures/demo/1.2.3/footballfield7.jpg", crop=(0, 135.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 g_chase = Transform("pictures/demo/1.2.3/footballfield8.jpg", crop=(0, 135.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 g_kick = Transform("pictures/demo/1.2.3/footballfield9.jpg", crop=(0, 135.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 g_wide = Transform("pictures/demo/1.2.3/footballfield10.jpg", crop=(0, 81.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 g_leaving = Transform("pictures/demo/1.2.3/footballfield11.jpg", crop=(0, 162.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
## 重新拍摄的找校卡镜头：翻找、外套口袋、取卡与反应。
image chapter1 b_search = Transform("pictures/demo/1.3.1/Weixin Image_20261030183131_331_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_search_worried = Transform("pictures/demo/1.3.1/Weixin Image_20261030183131_324_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_search_desk = Transform("pictures/demo/1.3.1/Weixin Image_20261030183131_319_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_search_floor = Transform("pictures/demo/1.3.1/Weixin Image_20261030183131_316_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_pocket = Transform("pictures/demo/1.3.1/Weixin Image_20261030183131_315_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_card_reveal = Transform("pictures/demo/1.3.1/Weixin Image_20261030183131_314_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_card_held = Transform("pictures/demo/1.3.1/Weixin Image_20261030183131_313_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_card_apology = Transform("pictures/demo/1.3.1/Weixin Image_20261030183131_312_24.jpg", crop=(0, 0, 4000, 2250), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_restaurant = Transform("pictures/demo/1.3.1/western_restaurant1.jpg", crop=(0, 0.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_restaurant_laugh = Transform("pictures/demo/1.3.1/western_restaurant2.jpg", crop=(0, 0.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 b_restaurant_talk = Transform("pictures/demo/1.3.1/western_restaurant3.jpg", crop=(0, 0.0, 1440, 810.0), crop_relative=False, xysize=(1920, 1080))
image chapter1 bathroom = Transform("pictures/demo/1.3.2/helping/bathroom1.jpg", crop=(0.0, 0, 1280.0, 720), crop_relative=False, xysize=(1920, 1080))
image chapter1 paper = Transform("pictures/demo/1.3.2/helping/bathroom2.jpg", crop=(0.0, 0, 1280.0, 720), crop_relative=False, xysize=(1920, 1080))
image chapter1 e_saved = Transform("pictures/demo/1.3.2/be saved.jpg", crop=(0, 1.406, 1915, 1077.188), crop_relative=False, xysize=(1920, 1080))
image chapter1 collision = Transform("pictures/demo/1.2.1/corridor4.jpg", crop=(0.222, 0.0, 579.556, 326), crop_relative=False, xysize=(1920, 1080))
image chapter1 d_leaving_far = Transform("pictures/demo/1.2.1/ob11.jpg", crop=(0.0, 1.312, 1702, 957.375), crop_relative=False, xysize=(1920, 1080))
image arrival stairs = "chapter1 campus"
image arrival meet_a = "chapter1 a_door"
image arrival dorm = "chapter1 dorm_e"
image arrival door_a = "chapter1 a_standing"
image arrival a_leaving = "chapter1 a_standing"
image arrival roommates_walk = "chapter1 campus"
image arrival with_a_walk = "chapter1 campus"
image chapter1 classroom_morning = "chapter1 b_enter"
image chapter1 classroom_noon = "chapter1 b_search"
image chapter1 chinese_restaurant = "chapter1 b_restaurant"
image chapter1 campus_evening = Transform("chapter1 teaching_square", matrixcolor=BrightnessMatrix(-0.3))

## 新增校园建立镜头：按各节 start/end 顺序连接入场与收尾。
image chapter1 arrival_walkway = Transform("pictures/demo/1.1.1/start1.jpg", crop=(0, 175.134, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 arrival_cat = Transform("pictures/demo/1.1.1/start2.jpg", crop=(0, 255.966, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 class_route = Transform("pictures/demo/1.1.2/start1.jpg", crop=(0, 121.247, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 class_courts = Transform("pictures/demo/1.1.2/start2.jpg", crop=(0, 148.191, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 class_field_view = Transform("pictures/demo/1.1.2/start3.jpg", crop=(0, 215.55, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 class_building = Transform("pictures/demo/1.1.2/start4.jpg", crop=(0, 40.416, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 teaching_square = Transform("pictures/demo/1.2.1/end.jpg", crop=(0, 229.022, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 field_entry = Transform("pictures/demo/1.2.3/start1.jpg", crop=(0, 269.438, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 track_approach = Transform("pictures/demo/1.2.3/start2.jpg", crop=(0, 94.303, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 campus_nap = Transform("pictures/demo/campus/quiet_cat.jpg", crop=(0, 255.966, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))
image chapter1 field_overview = Transform("pictures/demo/campus/field_overview.jpg", crop=(0, 148.191, 1441, 810.562), crop_relative=False, xysize=(1920, 1080))

## 1.3.2 未帮忙后的阳台分支。原图为 16:9，整幅铺满。
image chapter1 paper_ignored = Transform("pictures/demo/1.3.2/not helping/bathroom1.jpg", crop=(0, 0, 1280, 720), crop_relative=False, xysize=(1920, 1080))
image chapter1 balcony_locked = Transform("pictures/demo/1.3.2/not helping/dorm1.jpg", crop=(0, 0, 1280, 720), crop_relative=False, xysize=(1920, 1080))
image chapter1 balcony_teasing = Transform("pictures/demo/1.3.2/not helping/dorm2.jpg", crop=(0, 0, 1280, 720), crop_relative=False, xysize=(1920, 1080))
