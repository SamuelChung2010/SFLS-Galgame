## 来源：story/chapter1/1.3.2.md
## 帮忙后午休；未帮忙则停在被锁阳台，F 的救场留待第二章。
label chapter1_3_2:

    scene chapter1 arrival_walkway with fade
    "又一个周二，12点45分。我和倒霉熊刚从食堂出来，正往宿舍走。"
    p "今天去的时候，想吃的那几个菜又没了。"
    a "前面的人跑得太快了。等我们到了，就剩菜汤。"
    p "下次换个窗口试试吧。"
    a "行，总得找个能吃饱的。"
    scene chapter1 bathroom with fade
    "回到寝室，我先去洗了把脸。镜子里的自己看着还有点没睡醒，下巴上又冒了颗痘。"
    "还好，下午上课前能躺一会儿。"
    roommate_e "……等一下，我没带纸！"
    roommate_e "有人吗？李哥？"
    "隔间上方伸出一只手。我还没来得及走，他就听见了水声。"
    roommate_e "刚回来的是你吧？帮我拿点纸呗，在我桌上。必有重谢！"
    "纸就在寝室里，倒是不远。只是这味道……我默默往门口退了一步。"
    menu:
        "帮，给王力豪拿纸":
            $ helped_e = True
            p "等一下，我去拿。"
            roommate_e "好兄弟，靠你了！"
            "我回寝室找到纸巾，又走到隔间外。"
            p "拿来了。放门口？"
            roommate_e "从上面递一下，我接着。"
            scene chapter1 paper with dissolve
            "我把纸从隔板上方递过去，他赶紧接住。"
            roommate_e "收到了，谢了啊。"
            p "下次进来之前先看一眼。"
            roommate_e "记住了，这回是真记住了。"
            scene chapter1 e_saved with dissolve
            "过了一会儿，王力豪洗完手回到寝室，从柜子里拿出一瓶补水啦递给我。"
            roommate_e "说好的重谢，拿着。"
            p "递个纸而已，不用吧。"
            roommate_e "刚才可不只是递个纸而已。拿着拿着。"
            "我没再推辞，接过来放在桌上。"
            p "那谢了。"
            $ e_affection += 1
            $ paper_reward_received = True
        "不帮，假装没听到":
            $ helped_e = False
            $ paper_reward_received = False
            scene chapter1 paper_ignored with dissolve
            "我在门口犹豫了一下，还是没出声，轻手轻脚地回了寝室。"
            roommate_e "诶，别走啊！我听见脚步声了！"
            "李哥在床边应了一声，起身去找纸。我低头翻了翻桌上的东西，没再接话。"
            scene chapter1 dorm_f_think with dissolve
            "过了一会儿，洗手间那边安静下来。我想起晾在阳台上的毛巾，便出去收。"
            "手刚碰到毛巾，身后就传来玻璃门合上的声音。我回头推了推，没推动。"
            scene chapter1 balcony_locked with dissolve
            "王力豪站在门另一边，手还搭在门锁上。"
            p "……王力豪？开一下门。"
            roommate_e "这回听得见啦？刚才怎么叫都没反应。"
            "我握着门把手，一时有点尴尬。原来他早就听出来了。"
            p "……先让我进去吧。"
            scene chapter1 balcony_teasing with dissolve
            "他偏过头去，嘴角却没忍住。看样子，一时半会儿还不打算开门。"
            p "李哥？你在吗？帮我开一下门……"
            "我又推了一下门，还是没开。"
            $ e_affection -= 1
            stop music fadeout 1.5
            # 停在求助，不提前演出第二章 F 来救场的后续。
            return
    scene chapter1 dorm_f_think with fade
    "折腾完这一阵，午休的时间也剩得不多了。我爬上床，定好闹钟。"
    "刚闭上眼，就听见有人轻手轻脚地挪开椅子。寝室里渐渐安静下来。"
    stop music fadeout 1.5
    scene chapter1 campus_nap with fade
    "至于下午会发生什么，等睡醒再说吧。"
    scene black with fade

    return
