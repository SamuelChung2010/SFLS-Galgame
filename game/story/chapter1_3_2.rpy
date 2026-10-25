## 来源：story/chapter1/1.3.2.md
## 来源正文只有递纸与离开；本 demo 不使用旧版锁阳台镜头。
label chapter1_3_2:

    scene chapter1 campus with fade
    "又一个周二，12点45分。我和倒霉熊刚从食堂出来，正往宿舍走。"
    p "这帮学长学姐也太爽了吧，比我们吃饭还早。隔壁班那些人也是，跑那么快，害得所有人都得一起卷。"
    a "是啊，我们就剩点菜汤了，根本吃不饱嘛。没事，等明年就好了。"
    scene chapter1 bathroom with fade
    "好不容易回到寝室，我先去了一趟洗手间。"
    p "唉，这几天脸上的痘越来越多了，也不知道是累的还是没有好好洗脸。"
    roommate_e "啊——舒服了。等一下，我靠，我没带纸啊！"
    roommate_e "有人吗？李哥！有人吗？救命啊！刚才是不是你回来了？帮我拿点纸来呗，必有重谢！"
    "好臭啊……我要不要帮他呢？"
    menu:
        "帮，给王力豪拿纸":
            $ helped_e = True
            p "你小子也有今天？快叫两声爸爸。"
            roommate_e "别废话了，人命关天啊！"
            p "好好好，马上来。"
            "我回寝室拿了纸，又走到厕所门口。"
            p "拿到了，我怎么给你拿进去啊？"
            roommate_e "从上面递进来就行！搞快啊——"
            scene chapter1 paper with dissolve
            p "知道了儿子，稍安勿躁。"
            "我把纸从隔板上方递了进去。"
            scene chapter1 e_saved with dissolve
            "过了一会儿，王力豪从里面出来，先去洗了手。"
            roommate_e "谁是你儿子……不过还是谢了。这个给你吧，希望好人有好运。"
            "王力豪从柜子里拿出一瓶补水啦递给我。"
            p "嘿，翻脸不认爹。"
            $ e_affection += 1
            $ paper_reward_received = True
        "不帮，假装没听到":
            $ helped_e = False
            "我装作没听见，悄悄往寝室里走。"
            roommate_e "别装没听见！我知道你听得到！我不会放过你的！"
            "没走出几步，我就听见李哥应了一声，随后是翻找纸巾的声音。"
            $ e_affection -= 1
    scene chapter1 dorm_f_think with fade
    "折腾完这一阵，午休的时间也剩得不多了。我爬上床，定好闹钟。"
    "刚来时还不太习惯的寝室，好像已经没那么陌生了。"
    stop music fadeout 1.5
    scene black with fade
    "至于下午会发生什么，等睡醒再说吧。"

    return
