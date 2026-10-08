# 临时 QA 脚本：只放入隔离副本，不随游戏发布。
init python:
    from renpy.test.testsettings import _test as campus_qa_settings
    import os
    campus_qa_settings.screenshot_directory = os.environ.get("SFLS_UI_QA_OUTPUT", "tests/screenshots")
    campus_qa_settings.vc_revision = ""

    campus_qa_settings.timeout = 12.0
    if os.environ.get("SDL_VIDEODRIVER") == "dummy":
        config.periodic_callbacks.append(renpy.restart_interaction)
    config.autosave_on_quit = False
    config.developer = False
    # SDL dummy 的显示 surface 缺少 alpha；软件合成使用独立 RGBA surface。
    import renpy.display.swdraw as qa_sw
    import renpy.pygame as qa_pg
    qa_sw_init = qa_sw.SWDraw.init
    def campus_qa_sw_init(self, virtual_size):
        rv = qa_sw_init(self, virtual_size)
        self.screen = qa_pg.Surface(self.screen.get_size(), qa_pg.SRCALPHA, 32)
        self.window = qa_pg.Surface(virtual_size, qa_pg.SRCALPHA, 32)
        print("QA_DISPLAY", self.screen.get_size(), renpy.config.variants)
        return rv
    if os.environ.get("SDL_VIDEODRIVER") == "dummy":
        qa_sw.SWDraw.init = campus_qa_sw_init


label campus_qa_photo:
    scene expression "gui/main_menu.jpg"
    "新的班级，新的舍友……也不知道大家好不好相处。"
    a "一会儿回班，你要不要跟我一起走？收拾好了来隔壁找我就行。"
    menu:
        "跟舍友一起去":
            p "那就一起走吧。"
        "和 A 一起去":
            p "好，我先把床铺上，弄好就去找你。"
    "阳光穿过树叶，落在教学楼前的路上。"
    return

label campus_qa_long:
    scene expression "gui/main_menu.jpg"
    $ qa_speaker = Character("何云泽 / Alexios · 十班同学", color="#FFE680")
    qa_speaker "新学期的第一天，我把行李箱抬上最后几级台阶，靠着墙喘了口气。\n新的班级，新的舍友，新的课程……一切都刚刚开始。\n窗外是熟悉的校园，身边却多了许多还叫不出名字的同学。\n也许过不了多久，我们就会一起把这些普通的日子，变成值得记住的时光。"
    menu:
        "一起去图书馆，顺便看看新学期有哪些活动，等大家都收拾好以后再沿着教学楼旁边的小路慢慢走过去":
            pass
        "去食堂":
            pass
        "在宿舍休息":
            pass
        "去操场":
            pass
        "去教学楼":
            pass
        "去社团":
            pass
        "去校门":
            pass
        "最后一项：一起出发":
            pass
    p "选择完成。"
    return

testsuite campus_ui_qa:
    teardown:
        exit

    testcase photo:
        pause 0.4
        screenshot "main-menu"
        run Start("campus_qa_photo")
        pause 0.4
        screenshot "dialogue-narrator-or-player"
        assert id "what"
        assert not id "namebox"
        advance
        pause 0.3
        screenshot "dialogue-campus"
        python:
            win = renpy.get_displayable("say", "window")
            bar = renpy.get_displayable("quick_menu", "campus_toolbar")
            wr = renpy.render(win, 1920, 1080, 0, 0)
            qr = renpy.render(bar, 1920, 1080, 0, 0)
            assert wr.width == (1640 if renpy.variant("small") else 1480)
            assert wr.height <= (230 if renpy.variant("small") else 200), ("short card", wr.height)
            assert bar.style.background is None
            assert qr.height <= (58 if renpy.variant("touch") else 42), ("footer", qr.height)
            print("COMPACT_OK", wr.width, wr.height, qr.height)
            if os.environ.get("SDL_VIDEODRIVER") == "dummy":
                qa_pg.image.save(renpy.display.draw.screen, os.path.join(campus_qa_settings.screenshot_directory, "dialogue-physical.png"))

        click id "play_more"
        assert screen "gameplay_tools"
        screenshot "quick-menu-more"
        click id "play_quicksave"
        assert not screen "gameplay_tools"
        advance until screen "choice"
        run Hide("notify")
        move pos (0, 0)
        pause 0.2
        screenshot "choice-idle"
        python:
            cb = renpy.get_displayable("choice", "campus_choice_0", base=True)
            assert cb.style.xmaximum == (1664 if renpy.variant("small") else 1200)
            assert cb.style.background is not None

        move id "campus_choice_0"
        pause 0.2
        screenshot "choice-hover"
        click id "campus_choice_0"
        assert not screen "choice"
        click id "play_more"
        click id "play_quickload"
        if screen "confirm":
            click "确定"
        pause 0.3
        assert "一会儿回班"
        if eval not renpy.variant("touch"):
            click id "play_save"
            assert screen "save"
            keysym "K_ESCAPE"
            assert screen "say"
            click id "play_settings"
            assert screen "preferences"
            keysym "K_ESCAPE"
            assert screen "say"
            click id "play_history"
            assert screen "history"
            keysym "K_ESCAPE"
            assert screen "say"
        else:
            click id "play_menu"
            assert screen "save"
            keysym "K_ESCAPE"
            assert screen "say"
        click id "play_auto"
        assert eval preferences.afm_enable
        click id "play_auto"
        assert eval not preferences.afm_enable
        click id "play_more"
        click id "play_hide"
        assert not screen "quick_menu"
        click pos (0.5, 0.5)
        assert screen "quick_menu"


    testcase roommates:
        run MainMenu(confirm=False)
        click id "title_start"
        advance until screen "choice"
        click id "campus_choice_0"
        assert eval arrival_companion == "roommates"
        advance until screen "main_menu"

    testcase with_a:
        click id "title_start"
        advance until screen "choice"
        click id "campus_choice_1"
        assert eval arrival_companion == "a"
        advance until screen "main_menu"

    testcase long_content:
        run Start("campus_qa_long")
        pause 0.4
        screenshot "long-name-four-lines"
        python:
            win = renpy.get_displayable("say", "window")
            name = renpy.get_displayable("say", "namebox")
            body = renpy.get_displayable("say", "what")
            wr = renpy.render(win, 1920, 1080, 0, 0)
            nr = renpy.render(name, 1920, 1080, 0, 0)
            br = renpy.render(body, 1920, 1080, 0, 0)
            assert wr.width == (1640 if renpy.variant("small") else 1480), ("window", wr.width, wr.height)
            assert nr.width <= 1040, ("name", nr.width, nr.height)
            content = renpy.get_displayable("say", "campus_body")
            assert br.height + content.style.top_padding <= wr.height - content.style.bottom_padding, ("body", br.width, br.height, wr.height)
            assert wr.height <= 450, ("long card", wr.height)
            print("LAYOUT_OK", wr.width, wr.height, nr.width, br.width, br.height)

        assert id "who"
        advance until screen "choice"
        pause 0.2
        screenshot "many-long-choices"
        scroll amount 18 id "campus_choices"
        pause 0.3
        screenshot "many-choices-scrolled"
        click id "campus_choice_7"
        assert "选择完成"
