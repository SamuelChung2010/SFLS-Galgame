## 来源：story/chapter1/1.1.2.md

label chapter1_1_2:

    scene chapter1 class_route with dissolve
    if arrival_companion == "a":
        "我和倒霉熊并肩走着，手里拿着他刚给的“补水啦”。"
        a "你那几个舍友怎么样？"
        p "王力豪挺能聊的，李哥好像不太爱说话。"
        a "那还挺好。我那寝室已经有人为空调温度吵起来了。"
        p "这么快？"
        a "可不是嘛。对了，你那瓶“补水啦”开开看，我刚刚那瓶没中。"
        p "你还惦记这个啊。"
        a "万一中了呢？"
        "我拧开瓶盖。"
        p "诶，免费畅饮。"
        a "我去，真中了！你运气可以啊。"
        p "给你吧，反正是你买的。"
        a "不用不用，送你就是你的。"
        p "真不要？"
        a "下次中奖了记得请我一瓶就行。"
        p "哈哈，行。"
        $ a_affection += 1
    else:
        "我们三人走在路上，我手里拿着倒霉熊之前给的“补水啦”。"
        roommate_e "从门口贴的名单来看，我们寝应该就三个人了。三缺一，这真是 abnormal，不常见。"
        p "四人寝住三个人，不挺好吗？"
        roommate_e "Exactly！人均居住面积直接提升，这就是生活品质。"
        roommate_f "那空出来的床可以放我的画板和模型。"
        roommate_e "你就惦记你那些宝贝。"
        roommate_f "是作品。"
        roommate_e "行行行，作品。"
        roommate_e "对了，倒霉熊不是给了你瓶“补水啦”吗？听说有概率再来一瓶，快开开看。"
        p "你们比我还急。"
        "王力豪凑了过来，李哥也默默靠近半步。我拧开瓶盖，看了一眼。"
        p "谢谢惠顾。"
        roommate_e "啧，看来今天运气一般。"
        roommate_f "中奖率本来就不高。"
        roommate_e "没事，运气得留给更重要的事。走了走了！"
    scene chapter1 class_courts with dissolve
    "路边的球场很显眼，我默默记了一下这个位置。"
    scene chapter1 class_field_view with dissolve
    "从连廊望过去，操场和跑道就在不远处。"
    scene chapter1 class_building with dissolve
    "那天下午，我们按时参加了集合。把接下来的安排记好后，我回宿舍收拾完剩下的行李。"
    scene black with fade
    "第二天早晨。"
    scene chapter1 b_enter with fade
    "来到教室后，我按照讲台上的座位表找到了自己的位置。"
    "靠窗第二排……应该就是这里。"
    "我把书包暂时放在旁边的空座位上。过了一会儿，一个男生走了过来。"
    b "不好意思，这里是我的位置。"
    p "哦，你就是我同桌吧？"
    "我也报了自己的名字。"
    b "我叫齐文昌。"
    p "以后请多指教。"
    b "嗯，请多关照。"
    scene chapter1 b_seated with dissolve
    "我把书包拿回自己这边。齐文昌坐下来，安静地整理着书包。"
    p "你也来得挺早啊。"
    b "嗯。"
    p "你之前也是深外初中部的吗？"
    b "不是，从别的学校考进来的。"
    p "这样啊，感觉学校还挺大的。"
    b "……确实。"
    "他的话不多，但每次都会认真回答，似乎不太擅长主动找话题。"
    scene chapter1 b_pen_reach with dissolve
    "我正准备拿出课本，一支笔却不小心从桌边滚了下去。齐文昌伸手接住。"
    scene chapter1 b_pen_return with dissolve
    "他把笔递给了我。"
    p "啊，谢谢。"
    b "没事。"
    scene chapter1 b_seated with dissolve
    "他低头翻开课本，没有继续说话。"
    "虽然不太爱说话，不过感觉还挺好相处的。"

    return
