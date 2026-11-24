## 来源：story/chapter1/1.2.2.md

label chapter1_2_2:

    scene chapter1 campus_evening with fade
    "晚自习结束的铃声响过，教室门已经被推开了。"
    "话说我是不是走慢了，怎么一抬头教室人少一半。"
    "这学校不愧是国际生态学校，这灯下全是飞虫。"
    "开学第一天，就这么过了。"
    "早上还担心同学关系，结果同桌齐文昌只是话少，并不是不好相处。中午食堂的人倒是真的多，放学后又被小邓拉着逛了一趟校园。"
    "不知道王力豪和李哥在干什么，他们应该先回宿舍了？"
    "想到这里，脚步不自觉快了一些。"
    play music "audio/bgm/happy background music by Wu.ogg" fadeout 1.0 fadein 1.5 volume 0.6
    scene chapter1 night_f with fade
    "晚上回到宿舍，我刚把书包放下，就听见王力豪在一本正经地宣布。李哥在旁边整理东西，头也不抬一下。"
    scene chapter1 night_e with dissolve
    roommate_e "各位，今天我决定了，我要带领我们寝室的生活水平再上一个台阶。"
    scene chapter1 night_f_think with dissolve
    roommate_f "先把你堆在阳台扶手下的袜子收起来，寝室卫生已经下一个台阶了。"
    scene chapter1 night_e with dissolve
    roommate_e "格局小了。真正生活，不在于眼前的整洁，而在于精神上的富足。"
    scene chapter1 night_f_think with dissolve
    roommate_f "那你的精神富足能不能先把你的箱子盖好？已经没地方走路了。"
    scene chapter1 night_e with dissolve
    roommate_e "还真是..."
    "王力豪立刻扣上行李箱，把它挪回柜子旁，总算腾出一条路。"
    roommate_e "从今天开始，寝室里的事都包在我身上！洗衣、打水只要你们开口，我——"
    scene chapter1 night_f_think with dissolve
    roommate_f "你就负责开口是吧？"
    scene chapter1 night_e_point with dissolve
    roommate_e "我负责统筹全局。比如洗衣房，我已经帮大家研究过了。"
    scene chapter1 night_f_smile with dissolve
    roommate_f "研究出什么了？"
    scene chapter1 night_e_point with dissolve
    roommate_e "要提个桶过去，还要刷校卡。"
    scene chapter1 night_f_smile with dissolve
    roommate_f "厉害，下一步准备研究阳台门吗？"
    menu:
        "格局打开，寝室确实需要一位战略家。":
            p "我站王力豪这边。干大事的人都在统筹全局，哪有空管区区一双袜子？"
            scene chapter1 night_e_point with dissolve
            roommate_e "听听！什么叫知音！终于有人懂我的大局观了！"
            scene chapter1 night_f_think with dissolve
            roommate_f "懂了，那今天的值日你们俩战略家一起统筹一下？"
            scene chapter1 night_e with dissolve
            roommate_e "咳……战略家只负责画蓝图，落地执行得靠团队协作。"
            scene chapter1 night_f_smile with dissolve
            roommate_f "果然。"
            scene chapter1 night_e_point with dissolve
            roommate_e "算了算了，不说这些扫兴的。难得遇上知音，今晚我请大家喝“补水啦”！"
            $ e_affection += 1
        "我站李哥这边，先把值日做好。":
            p "我站李哥这边。你说要提升生活水平，先把值日做好咋样？顺便把阳台那几双袜子从“生态系统”里移除。"
            roommate_f "终于来个正常人了。"
            scene chapter1 night_e with dissolve
            roommate_e "喂！你怎么刚来第一天就帮他说话？！那不是袜子，那是青春挥洒过的痕迹！"
            scene chapter1 night_f_think with dissolve
            roommate_f "那你把你的青春挪回盆里泡着，别晾在阳台扶手底下发芽。"
            scene chapter1 night_e_point with dissolve
            roommate_e "为了挽回我的声誉，今晚我请大家喝“补水啦”！"
            $ f_affection += 1
        "一个管精神文明，一个管物质文明。":
            p "别吵了。王力豪负责寝室的精神文明建设，李哥负责物质文明和卫生监督。两手都要抓，怎么样？"
            scene chapter1 night_f_think with dissolve
            roommate_f "听起来像我一个人干所有活，他负责在旁边鼓掌。"
            scene chapter1 night_e with dissolve
            roommate_e "诶，话不能这么说，鼓掌也是很消耗情绪价值的。我看这个分工就很科学！"
            p "那作为精神文明总设计师，你总得先表示点什么吧？"
            scene chapter1 night_e_point with dissolve
            roommate_e "为了庆祝咱们寝室正式确立领导班子，今晚我请大家喝“补水啦”！"
    "！？"
    scene chapter1 night_f_smile with dissolve
    roommate_f "你不是说“请”吗？怎么把我那瓶拿走了？"
    scene chapter1 night_e_point with dissolve
    roommate_e "因为我需要它。"
    p "所以，这瓶原本是李哥的？"
    roommate_e "明天还你两瓶。"
    scene chapter1 night_f_smile with dissolve
    roommate_f "...先把你阳台的袜子收了。"
    scene chapter1 night_e_point with dissolve
    roommate_e "这个可以稍后再议。"
    "寝室总算安静下来了。不对，得趁熄灯前先洗漱。"
    "我拿着牙杯回到寝室时，王力豪提着桶冲了进来，头发还滴着水。"
    "不是，合着你下午没洗啊！"
    stop music fadeout 1.0
    scene black with fade
    "熄灯铃响了。头顶的灯突然灭掉，宿舍遁入了黑暗。"
    "……并没有。王力豪打开了自带的台灯。"
    scene chapter1 night_e with dissolve
    roommate_e "正好，夜谈会——"
    scene chapter1 night_f_think with dissolve
    roommate_f "不是你睡不睡了？"
    scene chapter1 night_e with dissolve
    roommate_e "...那我们小声开。"
    p "明天几点起来着？"
    scene chapter1 night_f_think with dissolve
    roommate_f "6点半起床铃，7点28分前到教室。"
    scene chapter1 night_e with dissolve
    roommate_e "6：30...那夜谈会只剩七个多小时了。"
    scene chapter1 night_f_think with dissolve
    roommate_f "不是你真不睡啊！"
    scene chapter1 night_e with dissolve
    roommate_e "那更得抓紧了!!!"
    scene chapter1 night_f_think with dissolve
    roommate_f "睡觉。"
    menu:
        "睡觉！再不睡明天得靠“补水啦”续命了。":
            p "睡觉。再不睡，明天早读真得靠“补水啦”续命了。"
            scene black with fade
            "王力豪关上台灯，可能还在嘟囔什么，但我的睡意压过了好奇心。"
        "第一议题：明早六点半谁把你从床上撬起来？":
            p "行，夜谈会第一议题：明天早上六点半，谁负责把你从床上撬起来？"
            roommate_f "附议。第二议题：阳台袜子什么时候收。"
            scene chapter1 night_e with dissolve
            roommate_e "……"
            roommate_e "我突然觉得睡眠质量也很重要，明天再议，晚安。"
            scene black with fade
            "啪嗒一声，王力豪火速关上了台灯。看来“袜子”才是终极封印术。"
        "不如摸黑预习一下高中数学？":
            p "既然都要抓紧时间，不如把发的新书拿出来，摸黑预习一下明天的数学？"
            "寝室陷入了长达三秒的死寂。"
            scene chapter1 night_e with dissolve
            roommate_e "……兄弟，你比我还狠。"
            scene chapter1 night_f_think with dissolve
            roommate_f "……我也支持现在立刻睡觉。"
            scene black with fade
            "王力豪默默关上了台灯，动作快得像怕我真掏出课本。"

    return
