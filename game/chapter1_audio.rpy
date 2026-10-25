## 音乐默认降低到滑块 55%；曲目另保留 60% 的播放增益。
define config.default_music_volume = 0.55
default persistent.chapter1_quiet_music_v1 = False

label before_main_menu:
    # 兼容已经保存为大音量的旧偏好，只降低一次；更低的音量和静音保持不变。
    if not persistent.chapter1_quiet_music_v1:
        python hide:
            target = config.default_music_volume
            if config.quadratic_volumes:
                target = target ** 2
            else:
                target = 10 ** ((target - 1.0) * config.volume_db_range / 20.0)
            was_muted = _preferences.get_mute("music")
            current = _preferences.volumes.get("music", 1.0)
            _preferences.set_volume("music", min(current, target))
            _preferences.set_mute("music", was_muted)
            persistent.chapter1_quiet_music_v1 = True
    return
