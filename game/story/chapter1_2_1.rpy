## 来源：story/chapter1/1.2.1.md
## 走廊相识后约傍晚探索，不再用黑场承载校医室或聚餐对白。
label chapter1_2_1:

    scene chapter1 corridor with fade
    "开学第一天的课间，下课铃一响，我便走出教室，想认一认周围的路。"
    scene chapter1 d_running with dissolve
    d "借过借过——！"
    scene chapter1 d_near with dissolve
    scene chapter1 collision
    with hpunch
    pause 0.15
    scene chapter1 d_hand with dissolve
    p "哎哟！"
    "我被撞得坐在地上。面前的男生连忙停下，伸手把我扶了起来。"
    d "对不起对不起！你没事吧？"
    "我站稳了，拍了拍裤子上的灰。"
    p "没事……你慢一点啊。"
    d "真不好意思。有没有撞疼？要不要去校医室看看？"
    p "不用，没撞到哪里。"
    "见我走了两步也没什么异样，他才松了口气。"
    d "那就好。我叫小邓，也是高一的，你呢？"
    "我也报了自己的名字。"
    p "你刚才跑那么急，是快上课了吗？"
    d "没有，我绕错路了，正赶着回班呢。"
    "他有些不好意思地摊开手里折着的校园平面图。上面已经画了几处记号。"
    p "你还带了地图？"
    d "学校这么大，总得先认认路。我还想去2栋看看，听说以前国际书院在那边上课。"
    p "那边现在不用了？"
    d "好像有些教室空着。你傍晚有空吗？一起去逛一圈？"
    p "怎么突然叫上我了？"
    d "一个人逛没意思嘛。刚才还撞了你，就当给你带个路。"
    "我看了一眼他手上的地图。反正自己也不熟悉学校，多认一条路也好。"
    p "行，不过别又跑起来了。"
    d "放心，这次慢慢走。吃完晚饭，在这边碰头？"
    p "好。"
    "我们说好碰头的位置，便各自回班上课。"
    scene chapter1 class_route with fade
    "傍晚吃过饭，我按约来到连廊。小邓已经等在那里，见到我便收起地图，领着我往2栋走。"
    play music "audio/bgm/薄雾弥时.mp3" fadeout 1.0 fadein 1.5 volume 0.6
    scene chapter1 oldbuilding with fade
    "我们来到 2 栋。相比其他教学楼，这里显得安静许多。"
    d "就这儿了，今天的寻宝地点。"
    p "感觉也没什么特别的啊。"
    scene chapter1 oldbuilding_walk with dissolve
    "我们沿着开放的走廊逛了一圈。"
    scene chapter1 oldbuilding_room with dissolve
    "往里面望去，除了空着的教室和几张旧海报，似乎什么也没有。"
    p "所以宝藏呢？"
    d "急什么，才刚来。"
    scene chapter1 props with dissolve
    "小邓四处张望，突然注意到走廊一角放着几个装旧杂物的纸箱。"
    d "诶，那边是什么？"
    scene chapter1 sword with dissolve
    "他在杂物旁发现了一把像素造型的道具剑。"
    d "我去，这不是钻石剑吗？"
    p "还真是。"
    "小邓翻来覆去地看了看，忍不住笑了起来。"
    d "谁把这玩意儿留这儿了？"
    p "估计是以前什么活动用的吧。"
    d "还挺新的。"
    scene chapter1 d_pose with dissolve
    "小邓突然摆出一个十分中二的姿势。"
    d "勇者，传说中的武器已经出现了！"
    scene chapter1 d_sword with dissolve
    "小邓又换了个夸张的姿势。"
    p "你差不多得了……"
    scene chapter1 d_hero with dissolve
    "小邓把道具剑高高举起。"
    d "从今天起，我们的冒险正式开始！"
    d "哈哈哈，没想到还真有收获。"
    p "你一开始不会真觉得能找到宝藏吧？"
    d "当然没有，我就随口一说。"
    p "那你还拉着我过来？"
    d "谁知道运气这么好呢。"
    "小邓拿着道具剑比划了两下，又看了看时间。"
    d "哎，不早了，我得回家了。"
    p "你是走读生？"
    d "对啊。不然我也不用每天赶着回家。"
    p "那今天就到这儿？"
    d "行，下次再带你去别的地方逛逛。"
    "小邓把地图塞回口袋，又看了看手里的钻石剑。"
    d "这玩意儿还挺值，今天没白来。"
    p "你开心就好。"
    d "行，那我先走了。下次见！"
    p "下次见。"
    scene chapter1 d_leaving with dissolve
    "小邓抱着道具剑，朝校门的方向走去。"
    scene chapter1 d_leaving_far with dissolve
    "原本只想认一认路，结果跟着他逛了一趟空教学楼。"
    "不过，这家伙倒还挺有意思的。"
    $ d_affection += 1
    scene chapter1 teaching_square with fade
    "我也往教室走去。晚自习还没开始，正好能把今天的笔记理一理。"

    return
