# 食堂冲刺：独立、可替换美术的像素风原型。
# 剧情使用 call cafeteria_runner；所有成绩从 cafeteria_runner_return 返回调用处。

default cafeteria_runner_result = None

init python:
    import time

    class CafeteriaRunnerState:
        FINISH = 680.0

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
            if d < 130: return 0       # 教学楼起跑
            if d < 170: return 1       # 第一段楼梯
            if d < 220: return 2       # 转角
            if d < 550: return 3       # 长通道
            if d < 590: return 4       # 第二段楼梯
            return 5                  # 食堂冲刺

        def stage_name(self):
            return ("教学楼起跑", "第一段楼梯", "上楼右转", "长通道",
                    "第二段楼梯", "食堂冲刺")[self.stage()]

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
                speed = 26.0
            else:
                self.boost_left = 0.0
                self.stamina = min(100.0, self.stamina + 24.0 * dt)
                speed = 12.5

            if self.stage() in (1, 4):
                speed *= 0.78
            elif self.stage() == 2:
                speed *= 0.84
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
        xpos (cx - 27)
        ypos top
        xysize (54, 72)
        add Solid("#1b2635") xpos 14 ypos 0 xysize (26, 8)
        add Solid("#f0c69e") xpos 14 ypos 8 xysize (26, 16)
        add Solid(shirt) xpos 10 ypos 24 xysize (34, 27)
        add Solid("#f0c69e") xpos 2 ypos 28 xysize (8, 22)
        add Solid("#f0c69e") xpos 44 ypos 28 xysize (8, 22)
        add Solid("#28354d") xpos 12 ypos 51 xysize (12, 17)
        add Solid("#28354d") xpos 30 ypos 51 xysize (12, 17)
        add Solid("#15202c") xpos 10 ypos 68 xysize (15, 4)
        add Solid("#15202c") xpos 29 ypos 68 xysize (15, 4)


screen cafeteria_runner_play():
    modal True
    default runner = CafeteriaRunnerState()
    $ lanes = (760, 960, 1160)
    $ stage = runner.stage()
    $ stripe_shift = int(runner.distance * 8) % 110

    timer 0.05 action Function(runner.tick) repeat True modal True
    key ["anyrepeat_K_a", "anyrepeat_K_LEFT"] action Function(runner.move, -1)
    key ["anyrepeat_K_d", "anyrepeat_K_RIGHT"] action Function(runner.move, 1)
    key "K_LSHIFT" action Function(runner.boost)
    key "K_RSHIFT" action Function(runner.boost)
    key "K_SPACE" action Function(runner.boost)

    # 校园、道路与分段路标。角色始终在屏幕下方，地砖向后滚动。
    add Solid("#6b9a70") xysize (1920, 1080)
    add Solid("#315a49") xpos 0 ypos 0 xysize (580, 1080)
    add Solid("#315a49") xpos 1340 ypos 0 xysize (580, 1080)
    add Solid("#263647") xpos 580 ypos 0 xysize (760, 1080)
    add Solid("#b8b5a5") xpos 620 ypos 0 xysize (680, 1080)
    add Solid("#d4d0bb") xpos 638 ypos 0 xysize (644, 1080)
    for i in range(11):
        add Solid("#a6a390") xpos 640 ypos (i * 110 + stripe_shift - 110) xysize (640, 7)
    add Solid("#e7dca9") xpos 850 ypos 120 xysize (8, 850)
    add Solid("#e7dca9") xpos 1060 ypos 120 xysize (8, 850)

    if stage == 0:
        add Solid("#466881") xpos 170 ypos 130 xysize (390, 370)
        for i in range(3):
            add Solid("#a9d2d5") xpos (220 + i * 105) ypos 200 xysize (65, 70)
        text "教学楼" xpos 275 ypos 320 size 48 color "#ffffff"
    elif stage in (1, 4):
        for i in range(11):
            add Solid("#7d8e95") xpos 625 ypos (160 + i * 72) xysize (670, 17)
        text ("第一段楼梯" if stage == 1 else "第二段楼梯") xpos 75 ypos 320 size 48 color "#ffffff"
    elif stage == 2:
        add Solid("#263647") xpos 1300 ypos 300 xysize (620, 310)
        add Solid("#d4d0bb") xpos 1300 ypos 330 xysize (620, 250)
        add Solid("#f5e28b") xpos 1350 ypos 443 xysize (480, 14)
        text "右转 →" xpos 1350 ypos 370 size 62 color "#ffffff"
    elif stage == 3:
        for i in range(7):
            add Solid("#9dc6b2") xpos 185 ypos (120 + i * 140) xysize (220, 20)
            add Solid("#9dc6b2") xpos 1500 ypos (120 + i * 140) xysize (220, 20)
        text "通道" xpos 145 ypos 320 size 48 color "#ffffff"
    else:
        add Solid("#5d756a") xpos 1380 ypos 120 xysize (400, 350)
        add Solid("#e8c17e") xpos 1430 ypos 170 xysize (300, 100)
        text "食堂" xpos 1510 ypos 187 size 54 color "#423c3b"

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
        add Solid("#f4de73") xpos (lanes[runner.lane] - 20) ypos 856 xysize (40, 14)

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

