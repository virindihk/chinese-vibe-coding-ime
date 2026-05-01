#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中文 Vibe Coding 输入法 - Linux 版
支持 X11 (xdotool) 和 Wayland (ydotool)
按 F1-F6 一键输出经典语录并自动回车
"""

import os
import subprocess
import sys
import time

# ============================================
# 配置区
# ============================================

PHRASES = {
    "f1": "说中文",
    "f2": "继续",
    "f3": "还是报错",
    "f4": "你改了啥",
    "f5": "先别重构",
    "f6": "回滚回滚",
}

# ============================================
# 工具检测
# ============================================

def detect_display_server():
    """检测当前显示服务器类型"""
    if os.environ.get("WAYLAND_DISPLAY"):
        return "wayland"
    if os.environ.get("DISPLAY"):
        return "x11"
    return "unknown"

def check_command(cmd):
    """检查系统是否有某个命令"""
    return subprocess.run(
        ["which", cmd],
        capture_output=True,
    ).returncode == 0

def ensure_deps(tool):
    """确保依赖已安装"""
    if tool == "xdotool":
        if not check_command("xdotool"):
            print("❌ 未找到 xdotool")
            print("   请安装: sudo apt install xdotool  (Debian/Ubuntu)")
            print("          sudo pacman -S xdotool     (Arch)")
            print("          sudo dnf install xdotool   (Fedora)")
            sys.exit(1)
    elif tool == "ydotool":
        if not check_command("ydotool"):
            print("❌ 未找到 ydotool")
            print("   请安装: sudo apt install ydotool  (Debian/Ubuntu)")
            print("          sudo pacman -S ydotool     (Arch)")
            print("   注意: Wayland 下还需要启动 ydotoold 守护进程")
            print("         sudo ydotoold &")
            sys.exit(1)
        # 检查 ydotoold 是否在运行
        result = subprocess.run(
            ["pgrep", "-x", "ydotoold"],
            capture_output=True,
        )
        if result.returncode != 0:
            print("⚠️  警告: ydotoold 守护进程未运行")
            print("   请先执行: sudo ydotoold &")

# ============================================
# 输入模拟
# ============================================

def send_text(text, tool):
    """输出文字并自动回车"""
    if tool == "xdotool":
        subprocess.run(["xdotool", "type", text], check=False)
        time.sleep(0.05)
        subprocess.run(["xdotool", "key", "Return"], check=False)
    elif tool == "ydotool":
        subprocess.run(["ydotool", "type", text], check=False)
        time.sleep(0.05)
        subprocess.run(["ydotool", "key", "Return"], check=False)

# ============================================
# 热键处理
# ============================================

class VibeCodingIME:
    def __init__(self):
        self.display = detect_display_server()
        self.tool = None
        self.hotkeys = []
        self.paused = False

        print("=" * 45)
        print("  🇨🇳 中文 Vibe Coding 输入法 (Linux)")
        print("=" * 45)

        if self.display == "wayland":
            self.tool = "ydotool"
            print("🖥️  检测到 Wayland")
        elif self.display == "x11":
            self.tool = "xdotool"
            print("🖥️  检测到 X11")
        else:
            print("⚠️  无法检测显示服务器，默认使用 xdotool")
            self.tool = "xdotool"

        ensure_deps(self.tool)

        try:
            import keyboard
            self.keyboard = keyboard
        except ImportError:
            print("\n❌ 缺少 Python 依赖: keyboard")
            print("   请安装: pip3 install keyboard")
            print("   或:     sudo apt install python3-keyboard")
            sys.exit(1)

        # 检查权限
        self._check_permissions()

    def _check_permissions(self):
        """检查是否有足够的权限监听全局热键"""
        import grp
        user_groups = [g.gr_name for g in grp.getgrall() if os.getlogin() in g.gr_mem or g.gr_gid == os.getgid()]
        if "input" not in user_groups:
            print("\n⚠️  当前用户不在 input 组，可能无法监听全局热键")
            print("   请执行: sudo usermod -aG input $USER")
            print("   然后重新登录或重启")
            print("   或者使用 sudo 运行此脚本\n")

    def _send(self, phrase):
        """发送短语（带暂停检查）"""
        if self.paused:
            return
        send_text(phrase, self.tool)

    def _toggle_pause(self):
        """暂停/恢复"""
        self.paused = not self.paused
        state = "⏸️  已暂停" if self.paused else "▶️  运行中"
        print(f"\n{state}")

    def _show_help(self):
        """显示帮助"""
        print("\n📋 快捷键对照表:")
        print("-" * 30)
        for key, phrase in PHRASES.items():
            alt = key.replace("f", "ctrl+shift+")
            print(f"  {key.upper():3} / {alt:12} → {phrase}")
        print("-" * 30)
        print("  F12           → 暂停/恢复")
        print("  Ctrl+C        → 退出")
        print()

    def start(self):
        """启动输入法"""
        print("\n🔥 输入法已启动!")
        print("   F1-F6 一键发送  |  F12 暂停  |  Ctrl+C 退出\n")

        # 绑定 F1-F6
        for key, phrase in PHRASES.items():
            hk = self.keyboard.add_hotkey(key, lambda p=phrase: self._send(p))
            self.hotkeys.append(hk)

            # 备选快捷键: ctrl+shift+1-6
            alt_key = key.replace("f", "ctrl+shift+")
            hk_alt = self.keyboard.add_hotkey(alt_key, lambda p=phrase: self._send(p))
            self.hotkeys.append(hk_alt)

        # F12 暂停/恢复
        self.keyboard.add_hotkey("f12", self._toggle_pause)

        # 显示帮助
        self._show_help()

        # 阻塞等待
        try:
            self.keyboard.wait()
        except KeyboardInterrupt:
            print("\n👋 再见!")
            sys.exit(0)


# ============================================
# 入口
# ============================================

if __name__ == "__main__":
    ime = VibeCodingIME()
    ime.start()
