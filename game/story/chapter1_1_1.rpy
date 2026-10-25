## 来源：story/chapter1/1.1.1.md

label chapter1_1_1:

    scene chapter1 arrival_walkway with fade
    play music "audio/bgm/焉知晴雨.mp3" fadein 1.5 volume 0.6
    "以前听人说‘等你上了高中’，总觉得还早。"
    "现在连住校的行李都带来了，倒还有点不习惯。"
    "新的班级，新的舍友……也不知道大家好不好相处。"
    scene chapter1 arrival_cat with dissolve
    "连廊边，一只猫正靠着墙休息。我拖着箱子从它旁边走过，继续往宿舍楼走。"
    "8月31日下午，我把行李箱抬上最后几级台阶，靠着墙喘了口气。"
    "前些天一直请假在家，今天才第一次搬进宿舍。正式住校要带的东西，比我想象中多得多。"
    scene chapter1 a_door with dissolve
    a "诶，你也住这层？"
    "是倒霉熊，初中时和我同年级。以前没怎么聊过，没想到在这里又碰见了。"
    p "是啊，今天才搬来。我爸妈今天都忙，只能自己来了。"
    p "六楼啊……我现在算是知道这箱子有多重了。"
    a "先歇会儿。我正好下去买水，顺便给你带瓶补水啦？"
    p "好啊，等一下，我拿下校园卡。"
    a "不用拿了，算我请你。"
    p "那谢啦，下次我请你。"
    a "行。你住这间吧？我一会给你送过来，我就在隔壁。"
    "我点点头，等呼吸缓下来，才把箱子拖进寝室。"
    scene chapter1 dorm_f with fade
    "房间里已经有两个人。我还没见过他们，一时不知道该先打招呼，还是先把卡在门口的箱子挪开。"
    scene chapter1 dorm_e with dissolve
    roommate_e "来啦？先进去，门口这袋是我的，我挪一下。"
    "他把袋子拎到床边，给我让出一条路。"
    scene chapter1 dorm_e with dissolve
    roommate_e "我叫王力豪，那边那个，我们都叫他李哥。你怎么称呼？"
    "我也报了自己的名字。"
    p "今天才搬进来，以后多关照。"
    scene chapter1 dorm_f_think with dissolve
    roommate_f "你好。你的床在这边，床头贴着名字。"
    p "好，谢谢。你们都收拾完了？"
    scene chapter1 dorm_e_folded with dissolve
    roommate_e "差不多了。你先铺床，一会儿还要回班集合，别的东西回来再慢慢弄。"
    "我看了眼时间，先从箱子里翻出床单。东西堆在一块儿，越想快点，越找不着。"
    "刚把床单展开，门口就响起了敲门声。"
    p "来了来了。"
    scene chapter1 a_standing with dissolve
    "我拉开门。倒霉熊站在外面，把一瓶补水啦递过来。"
    a "呐，你的水。"
    p "谢了，正好渴了。"
    a "一会回班，你要不要跟我一起走？收拾好了来隔壁找我就行。"
    menu:
        "跟舍友一起去":
            $ arrival_companion = "roommates"
            p "我还有点东西没弄好，一会和舍友过去，你先走吧。"
            a "行，那我先跟他们走。班里见。"
            "倒霉熊回隔壁拿了东西，和他的舍友先下了楼。"
            scene chapter1 dorm_e_folded with dissolve
            "我把床铺好，把暂时用不到的东西塞回箱子里。王力豪和李哥也准备出门了。"
            roommate_e "好了？那一块走吧。"
            p "好。"
            scene chapter1 class_route with fade
            roommate_e "刚才那位，你以前就认识啊？"
            p "嗯，初中同年级，不过以前没怎么聊过。"
            roommate_e "挺巧。你今天第一次来，路还不熟的话就跟着我们。"
            roommate_f "从这边下楼，近一点。"
            p "行，谢谢。"
            roommate_e "没事，顺路。"
            "话还不算多，但一起走出宿舍时，刚进门那会儿的生疏已经少了一点。"
        "和倒霉熊一起去":
            $ arrival_companion = "a"
            p "好，我先把床铺上，弄好就去找你。"
            a "行，我就在隔壁。"
            "倒霉熊回了房间。我把水放在桌边，继续整理床铺。"
            scene chapter1 dorm_e_folded with dissolve
            p "我一会跟隔壁的倒霉熊过去，你们不用等我。"
            roommate_e "行，那我们先走了。"
            scene chapter1 dorm_f_think with dissolve
            roommate_f "走的时候带上钥匙，别落屋里。"
            p "好，谢了。"
            "铺好床，我把钥匙装进口袋，去隔壁敲了敲门。"
            scene chapter1 a_talk with dissolve
            a "好了？走吧。"
            scene chapter1 class_route with fade
            p "刚才还觉得行李少带了什么，现在只想下次少带一点。"
            a "你先住两天再说，说不定到时候又想往学校搬了。"
            "我笑了笑，跟着他下楼。新宿舍里还有不少东西没收拾，不过总算安顿下来了。"

    return
