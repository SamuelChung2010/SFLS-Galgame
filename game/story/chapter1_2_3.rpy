## 来源：story/chapter1/1.2.3.md

label chapter1_2_3:

    scene chapter1 field_entry with fade
    play music "audio/bgm/Background music(1).ogg" fadein 1.0 volume 0.6
    "第二天晚饭后，离晚自习还有一段时间。"
    scene chapter1 track_approach with dissolve
    "我暂时没有什么事情，便一个人在操场上散步。"
    scene chapter1 field with dissolve
    "旁边的足球场上，几名学生正在踢球。我并没有太在意，只是沿着跑道慢慢向前走。"
    "这时，足球场上传来一阵喊声。"
    teammate "这边！传过来！"
    "我下意识朝足球场看了一眼。"
    "一个男生接到了球。从他的动作来看，似乎准备来一脚长传。"
    "姿势看起来倒还挺像那么回事。"
    "他起脚。"
    "足球划过一个十分微妙的弧线，并没有飞向他的队友，而是直奔跑道而来。"
    p "……？"
    "下一秒——"
    scene chapter1 ball
    with hpunch
    "砰！"
    "足球擦着我的头侧砸了过来，我踉跄了一下。"
    p "我靠……"
    "足球滚到一旁。"
    scene chapter1 g_hand with dissolve
    "足球场上的男生愣了两秒，随后立刻朝我跑来。"
    g "卧槽！同学！你没事吧？！"
    scene chapter1 g_hand with dissolve
    "他跑到我旁边，伸手扶住了我。"
    g "对不起啊，今天锁头忘关了。"
    p "……"
    p "锁头？"
    g "……"
    g "等一下。"
    scene chapter1 g_think with dissolve
    "他的表情突然认真起来。"
    g "不是，真对不起啊同学。"
    g "我刚刚那句是胡话，你别往心里去。"
    g "你头没事吧？要不要去校医室看看？"
    p "应该没什么事。"
    g "真没事？"
    p "嗯。"
    "他松了一口气。"
    g "那就好。"
    "短暂沉默。"
    g "我刚才本来是想传中的。"
    p "……"
    p "所以为什么球会飞到跑道上？"
    scene chapter1 g_think with dissolve
    "他低头思考了几秒。"
    g "这个问题……"
    g "可能足球有自己的想法。"
    "远处传来队友的声音。"
    teammate "你那叫传中？？？"
    "他立刻转过头。"
    g "你闭嘴！"
    g "至少方向是往中间去的！"
    teammate "你都踢出场了！"
    g "过程有一点小偏差而已！"
    scene chapter1 g_talk with dissolve
    "他再次转过身，像是什么都没有发生一样。"
    scene chapter1 g_sorry with dissolve
    g "不过确实是我的问题。"
    g "下次我会注意的。"
    "道歉和嘴硬之间，切换得倒是很流畅。"
    p "你也是高一？"
    g "对啊。"
    g "国际书院的。"
    p "国际书院？"
    g "嗯。"
    "他看了我一眼。"
    g "你哪个书院的？"
    p "文理书院。"
    "他突然站直，神情严肃。"
    g "久仰。"
    p "？"
    "几秒后。"
    g "虽然其实也没有很久。"
    p "……"
    scene chapter1 g_talk with dissolve
    p "说了半天，还不知道你叫什么呢。"
    g "哦对，忘了自我介绍。"
    g "我叫何云泽，英文名 Alexios。"
    p "Alexios？这不是《刺客信条：奥德赛》里的那个吗？"
    g "对啊，就是从那儿取的。"
    g "怎么样，很有气势吧？"
    p "确实。尤其是刚才一脚把球踢我头上的时候。"
    scene chapter1 g_think with dissolve
    g "……"
    scene chapter1 g_sorry with dissolve
    g "哈哈，英雄也有失手的时候。"
    "笑过之后，我也报了自己的名字。"
    "Alexios用脚踩住足球。"
    g "要不要来踢两脚？"
    g "我保证这次不开锁。"
    menu:
        "算了，我还是散步吧":
            $ football_choice = "walk"
            p "算了，我还是继续散步吧。"
            g "合理。"
            g "毕竟你已经体验过我们的远程打击能力了。"
            p "“我们的”？"
            g "……"
            g "我的。"
            g "这锅不能让国际书院一起背。"
            "我们又聊了两句。"
            g "那行，下次见。"
            g "我先回去接受队友的审判了。"
            scene chapter1 g_leaving with dissolve
            "Alexios抱着球跑回足球场。"
            "跑了两步，又回头。"
            g "同学！你头要是晚上疼，记得去校医室！"
            g "——不是锁头，是头！"
            p "……"
            "Alexios 跑远。"
            teammate "你还知道回来啊！"
            g "刚才发生了一点外交事故！"
            "……奇怪的人。"
        "那就踢一会儿":
            $ football_choice = "play"
            p "行吧。"
            g "好。欢迎你租借加盟我们国院足球队。"
            p "……"
            scene chapter1 g_play with dissolve
            "我跟着Alexios来到足球场。"
            "几分钟后。"
            g "传我传我传我！"
            scene chapter1 g_chase with dissolve
            "队友把球传给Alexios。"
            scene chapter1 g_kick with dissolve
            "Alexios抬脚。"
            scene chapter1 g_wide with dissolve
            "足球直接飞出边线。"
            "全场沉默。"
            g "……"
            scene chapter1 g_think with dissolve
            "Alexios看了一眼脚下。"
            g "草皮的问题。"
            teammate "这里是人工草！"
            "Alexios 思考两秒。"
            g "那就是人工的问题。"
            "我原本以为刚才砸到我的那一脚只是意外。现在看来……好像并不是。"
            g "……不对。"
            scene chapter1 g_sorry with dissolve
            "Alexios突然认真起来。"
            g "是我脚的问题。"
            g "真抱歉，我再找找感觉。"
            "几秒后。"
            g "这次我不开锁。"
            teammate "你先把锁装上！"
            "……"
            $ g_affection += 1
    scene chapter1 field_overview with fade
    "晚自习前，我沿着跑道慢慢往回走。今天倒是又认识了一个人。"

    return
