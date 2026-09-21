# 食堂冲刺：独立、可替换美术的像素风原型。
# 剧情使用 call cafeteria_runner；所有成绩从 cafeteria_runner_return 返回调用处。

default cafeteria_runner_result = None

init python:
    import time

    class CafeteriaRunnerState:
        FINISH = 740.0

        def __init__(self):
            self.distance = 0.0
            self.elapsed = 0.0
            self.lane = 1
            self.stamina = 100.0
            self.boost_left = 0.0
            self.slow_left = 0.0
            self.overtaken = 0
            self.collisions = 0
            self.finished = False
            self.last_tick = None
            # position 是离教学楼的米数；速度单位为米/秒。
            self.npcs = [
                self.student(28, 1, 7.0, "normal"),
                self.student(41, 0, 8.0, "normal"),
                self.student(52, 1, 6.5, "pair"),
                self.student(76, 1, 7.5, "lateral", 0.0),
                self.student(88, 2, 7.0, "normal"),
                self.student(50, 0, 11.3, "fast"),
                self.student(112, 0, 7.0, "pair"),
                self.student(130, 2, 8.0, "lateral", 1.3),
                self.student(151, 1, 8.0, "normal"),
                self.student(80, 2, 11.6, "fast"),
                self.student(175, 1, 6.5, "pair"),
                self.student(205, 0, 9.0, "normal"),
            ]

        def student(self, position, lane, speed, kind, phase=0.0):
            return {
                "position": float(position), "lane": lane, "speed": speed,
                "kind": kind, "phase": phase, "passed": False, "hit": False,
            }

        def stage(self):
            d = self.distance
            if d < 100: return 0       # 教学楼起跑
            if d < 650: return 1       # 林荫柏油路
            return 2                  # 食堂前冲刺

        def stage_name(self):
            return ("教学楼出发", "林荫柏油路", "食堂前冲刺")[self.stage()]

        def move(self, direction):
            if not self.finished:
                self.lane = max(0, min(2, self.lane + direction))

        def boost(self):
            # 按一次冲刺 1.4 秒；消耗体力，耗尽后必须恢复。
            if not self.finished and self.boost_left <= 0 and self.stamina >= 12:
                self.boost_left = 1.4

        def tick(self):
            if self.finished:
                return
            now = time.monotonic()
            dt = 0.05 if self.last_tick is None else min(0.10, max(0.0, now - self.last_tick))
            self.last_tick = now
            if dt <= 0:
                return

            self.elapsed += dt
            boosted = self.boost_left > 0 and self.stamina > 0
            if boosted:
                self.boost_left = max(0.0, self.boost_left - dt)
                self.stamina = max(0.0, self.stamina - 30.0 * dt)
                speed = 27.0
            else:
                self.boost_left = 0.0
                self.stamina = min(100.0, self.stamina + 24.0 * dt)
                speed = 12.5

            if self.slow_left > 0:
                speed *= 0.50
                self.slow_left = max(0.0, self.slow_left - dt)
            self.distance = min(self.FINISH, self.distance + speed * dt)

            for npc in self.npcs:
                npc["position"] += npc["speed"] * dt
                if npc["kind"] == "lateral":
                    npc["lane"] = int((self.elapsed + npc["phase"]) / 2.5) % 3
                lanes = (npc["lane"], npc["lane"] + 1) if npc["kind"] == "pair" else (npc["lane"],)
                if not npc["hit"] and self.lane in lanes and abs(self.distance - npc["position"]) < 2.4:
                    npc["hit"] = True
                    self.collisions += 1
                    self.slow_left = 1.6
                    self.boost_left = 0.0
                if not npc["passed"] and self.distance > npc["position"] + 3.0:
                    npc["passed"] = True
                    self.overtaken += 2 if npc["kind"] == "pair" else 1

            if self.distance >= self.FINISH:
                self.finished = True

        def result(self):
            seconds = round(self.elapsed, 1)
            rating = "很快" if seconds < 40.0 else ("普通" if seconds < 60.0 else "很慢")
            return {"seconds": seconds, "overtaken": self.overtaken,
                    "collisions": self.collisions, "rating": rating}


# 下列角色和场景都由纯色像素块绘制，是便于以后替换的首版占位图。
screen cafeteria_runner_student(cx, top, shirt):
    fixed:
        xpos (cx - 36)
        ypos top
        xysize (72, 100)
        add Solid("#172331") xpos 19 ypos 0 xysize (34, 11)
        add Solid("#f0c69e") xpos 19 ypos 11 xysize (34, 23)
        add Solid(shirt) xpos 13 ypos 34 xysize (46, 36)
        add Solid("#dce9ed") xpos 28 ypos 36 xysize (16, 28)
        add Solid("#f0c69e") xpos 3 ypos 39 xysize (10, 30)
        add Solid("#f0c69e") xpos 59 ypos 39 xysize (10, 30)
        add Solid("#28354d") xpos 16 ypos 70 xysize (16, 25)
        add Solid("#28354d") xpos 40 ypos 70 xysize (16, 25)
        add Solid("#15202c") xpos 13 ypos 95 xysize (21, 5)
        add Solid("#15202c") xpos 38 ypos 95 xysize (21, 5)


screen cafeteria_runner_tree(cx, top, leaf, light):
    # 一棵 180×210 的纯色块像素树；林荫道两侧各重复两列。
    fixed:
        xpos (cx - 90)
        ypos top
        xysize (180, 210)
        add Solid("#28563b") xpos 15 ypos 184 xysize (150, 16)
        add Solid("#73533e") xpos 76 ypos 117 xysize (28, 72)
        add Solid("#8c6749") xpos 83 ypos 124 xysize (8, 53)
        add Solid("#654936") xpos 60 ypos 179 xysize (60, 13)
        add Solid("#194934") xpos 27 ypos 51 xysize (126, 98)
        add Solid("#194934") xpos 43 ypos 28 xysize (94, 118)
        add Solid("#194934") xpos 61 ypos 8 xysize (58, 126)
        add Solid(leaf) xpos 18 ypos 74 xysize (144, 55)
        add Solid(leaf) xpos 36 ypos 43 xysize (108, 81)
        add Solid(leaf) xpos 57 ypos 21 xysize (66, 73)
        add Solid(light) xpos 55 ypos 33 xysize (34, 19)
        add Solid(light) xpos 36 ypos 77 xysize (29, 26)
        add Solid(light) xpos 110 ypos 65 xysize (29, 23)
        add Solid(light) xpos 79 ypos 103 xysize (35, 18)


screen cafeteria_runner_play():
    modal True
    default runner = CafeteriaRunnerState()
    $ lanes = (760, 960, 1160)
    $ stage = runner.stage()
    $ mark_shift = int(runner.distance * 9) % 170
    $ tree_shift = int(runner.distance * 6) % 270

    timer 0.05 action Function(runner.tick) repeat True modal True
    key ["anyrepeat_K_a", "anyrepeat_K_LEFT"] action Function(runner.move, -1)
    key ["anyrepeat_K_d", "anyrepeat_K_RIGHT"] action Function(runner.move, 1)
    key "K_LSHIFT" action Function(runner.boost)
    key "K_RSHIFT" action Function(runner.boost)
    key "K_SPACE" action Function(runner.boost)

    # 连续的柏油路、路肩、斑驳路面及清晰的虚线车道标记。
    add Solid("#4d8157") xysize (1920, 1080)
    add Solid("#3e704b") xpos 0 ypos 0 xysize (550, 1080)
    add Solid("#3e704b") xpos 1370 ypos 0 xysize (550, 1080)
    add Solid("#29343a") xpos 548 ypos 0 xysize (824, 1080)
    add Solid("#b6b19d") xpos 574 ypos 0 xysize (772, 1080)
    add Solid("#454d50") xpos 608 ypos 0 xysize (704, 1080)
    add Solid("#363e42") xpos 623 ypos 0 xysize (674, 1080)
    add Solid("#ddd9c8") xpos 648 ypos 0 xysize (8, 1080)
    add Solid("#ddd9c8") xpos 1264 ypos 0 xysize (8, 1080)
    for i in range(13):
        $ road_y = i * 96 + int(runner.distance * 7) % 96 - 96
        add Solid("#424a4d") xpos (684 + (i % 3) * 165) ypos road_y xysize (72, 7)
        add Solid("#2e373a") xpos (717 + (i % 4) * 125) ypos (road_y + 52) xysize (36, 5)
    for i in range(9):
        $ line_y = i * 170 + mark_shift - 170
        add Solid("#f1eddd") xpos 856 ypos line_y xysize (9, 83)
        add Solid("#f1eddd") xpos 1056 ypos line_y xysize (9, 83)

    # 教学楼和食堂只作出发/终点提示，路面始终保持同一条柏油路。
    if stage == 0:
        add Solid("#627985") xpos 5 ypos 208 xysize (325, 292)
        add Solid("#304957") xpos 0 ypos 187 xysize (340, 27)
        add Solid("#a8cdd0") xpos 62 ypos 249 xysize (76, 65)
        add Solid("#a8cdd0") xpos 189 ypos 249 xysize (76, 65)
        text "教学楼" xpos 85 ypos 372 size 43 color "#ffffff"
    elif stage == 2:
        add Solid("#a57a59") xpos 1584 ypos 204 xysize (325, 292)
        add Solid("#684e43") xpos 1573 ypos 183 xysize (347, 27)
        add Solid("#e7c37f") xpos 1630 ypos 248 xysize (235, 75)
        text "食堂" xpos 1706 ypos 355 size 49 color "#ffffff"

    # 左右各两排树，错开排列并随跑步滚动。
    for i in range(6):
        $ row_y = i * 270 + tree_shift - 300
        use cafeteria_runner_tree(165, row_y + 124, "#31714a", "#4b9660")
        use cafeteria_runner_tree(1755, row_y + 124, "#31714a", "#4b9660")
        use cafeteria_runner_tree(432, row_y, "#286642", "#429257")
        use cafeteria_runner_tree(1488, row_y, "#286642", "#429257")

    for npc in runner.npcs:
        $ gap = npc["position"] - runner.distance
        if -8.0 <= gap <= 60.0:
            $ npc_y = int(770 - gap * 10)
            if npc["kind"] == "pair":
                use cafeteria_runner_student(lanes[npc["lane"]] - 55, npc_y, "#5e9d9b")
                use cafeteria_runner_student(lanes[npc["lane"] + 1] - 55, npc_y, "#5e9d9b")
                text "聊天" xpos (lanes[npc["lane"]] + 25) ypos (npc_y - 28) size 28 color "#ffffff"
            elif npc["kind"] == "fast":
                use cafeteria_runner_student(lanes[npc["lane"]], npc_y, "#805baf")
            elif npc["kind"] == "lateral":
                use cafeteria_runner_student(lanes[npc["lane"]], npc_y, "#d9794d")
            else:
                use cafeteria_runner_student(lanes[npc["lane"]], npc_y, "#5c80b6")

    use cafeteria_runner_student(lanes[runner.lane], 772, "#f0b548")
    if runner.boost_left > 0 and runner.stamina > 0:
        add Solid("#f4de73") xpos (lanes[runner.lane] - 24) ypos 884 xysize (48, 13)

    # HUD：大号文字和高对比条，方便按键与速度变化辨认。
    add Solid("#152238dd") xpos 0 ypos 0 xysize (1920, 142)
    text "食堂冲刺" xpos 58 ypos 24 size 52 color "#ffffff"
    text runner.stage_name() xpos 375 ypos 28 size 42 color "#f6e6a8"
    text ("%.1f 秒" % runner.elapsed) xpos 1510 ypos 25 size 48 color "#ffffff"
    add Solid("#435567") xpos 598 ypos 71 xysize (700, 22)
    add Solid("#83cf9e") xpos 598 ypos 71 xysize (max(1, int(700 * runner.distance / runner.FINISH)), 22)
    text "体力" xpos 59 ypos 88 size 32 color "#ffffff"
    add Solid("#435567") xpos 150 ypos 99 xysize (330, 25)
    add Solid("#f4c566") xpos 150 ypos 99 xysize (max(1, int(330 * runner.stamina / 100.0)), 25)
    text ("超越 %d  ·  碰撞 %d" % (runner.overtaken, runner.collisions)) xpos 1390 ypos 95 size 30 color "#ffffff"
    text "A / D 或 ← / → 换道     Shift / Space 短时加速" xpos 440 ypos 976 size 34 color "#ffffff" outlines [(2, "#172637", 0, 0)]

    if runner.finished:
        add Solid("#102030dd") xysize (1920, 1080)
        add Solid("#24384d") xpos 525 ypos 245 xysize (870, 610)
        text "到达食堂！" xalign 0.5 ypos 290 size 64 color "#f4d783"
        text ("用时 %.1f 秒" % runner.elapsed) xalign 0.5 ypos 405 size 43 color "#ffffff"
        text ("超越 %d 人    碰撞 %d 次" % (runner.overtaken, runner.collisions)) xalign 0.5 ypos 475 size 40 color "#ffffff"
        text ("评价：" + runner.result()["rating"]) xalign 0.5 ypos 555 size 47 color "#aee6b7"
        textbutton "返回主线" xalign 0.5 ypos 713 text_size 46 action Return(runner.result())


label cafeteria_runner:
    call screen cafeteria_runner_play
    $ cafeteria_runner_result = _return
    if cafeteria_runner_result["rating"] == "很快":
        "你很快赶到食堂，队伍还短。"
    elif cafeteria_runner_result["rating"] == "普通":
        "你正常到达食堂，队伍刚排起来。"
    else:
        "等你到食堂时，队伍已经很长了。"
    jump cafeteria_runner_return

label cafeteria_runner_return:
    # 所有成绩在此回到同一个剧情调用点。
    return
