"""
🇨🇳 中文 Vibe Coding 输入法

一个 Python3 脚本跨 macOS / Windows / Linux (X11 & Wayland)
按 F1-F6 一键输出经典语录并自动回车。
"""

import os
import platform
import subprocess
import sys
import time

__version__ = "1.0.0"

# ============================================
# 配置
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
# 平台检测
# ============================================

SYSTEM = platform.system()
IS_MACOS = SYSTEM == "Darwin"
IS_WINDOWS = SYSTEM == "Windows"
IS_LINUX = SYSTEM == "Linux"


def detect_linux_display():
    """检测 Linux 显示服务器类型"""
    if os.environ.get("WAYLAND_DISPLAY"):
        return "wayland"
    if os.environ.get("DISPLAY"):
        return "x11"
    return "unknown"


# ============================================
# 输入后端
# ============================================

class InputBackend:
    """统一的键盘输入后端"""

    def send(self, text: str) -> None:
        raise NotImplementedError


class PynputInput(InputBackend):
    """基于 pynput 的输入后端 (macOS / Windows / Linux X11)"""

    def __init__(self):
        from pynput.keyboard import Controller, Key
        self.controller = Controller()
        self.Key = Key

    def send(self, text: str) -> None:
        self.controller.type(text)
        time.sleep(0.05)
        self.controller.press(self.Key.enter)
        self.controller.release(self.Key.enter)


class YdotoolInput(InputBackend):
    """基于 ydotool 的输入后端 (Linux Wayland)"""

    def send(self, text: str) -> None:
        subprocess.run(["ydotool", "type", text], check=False)
        time.sleep(0.05)
        subprocess.run(["ydotool", "key", "Return"], check=False)


# ============================================
# 热键后端
# ============================================

class HotkeyBackend:
    """统一的热键监听后端"""

    def add_hotkey(self, key: str, callback) -> None:
        raise NotImplementedError

    def add_pause_hotkey(self, callback) -> None:
        raise NotImplementedError

    def run(self) -> None:
        raise NotImplementedError


class PynputHotkey(HotkeyBackend):
    """基于 pynput 的热键监听 (macOS / Windows / Linux X11)"""

    def __init__(self):
        from pynput import keyboard
        self.keyboard = keyboard
        self.hotkeys = {}

    def add_hotkey(self, key: str, callback) -> None:
        pynput_key = f"<{key}>"
        self.hotkeys[pynput_key] = callback

    def add_pause_hotkey(self, callback) -> None:
        self.hotkeys["<f12>"] = callback

    def run(self) -> None:
        with self.keyboard.GlobalHotKeys(self.hotkeys) as h:
            h.join()


class KeyboardLibHotkey(HotkeyBackend):
    """基于 keyboard 库的热键监听 (Linux Wayland / 备选)"""

    def __init__(self):
        import keyboard
        self.keyboard = keyboard

    def add_hotkey(self, key: str, callback) -> None:
        self.keyboard.add_hotkey(key, callback)

    def add_pause_hotkey(self, callback) -> None:
        self.keyboard.add_hotkey("f12", callback)

    def run(self) -> None:
        self.keyboard.wait()


# ============================================
# 主程序
# ============================================

class VibeCodingIME:
    def __init__(self):
        self.paused = False
        self.input_backend: InputBackend | None = None
        self.hotkey_backend: HotkeyBackend | None = None

        self._detect_platform()
        self._check_deps()

    def _detect_platform(self):
        """根据平台选择后端"""
        print("=" * 50)
        print("  🇨🇳 中文 Vibe Coding 输入法")
        print("=" * 50)
        print(f"🖥️  检测到系统: {SYSTEM}")

        if IS_MACOS or IS_WINDOWS:
            self.input_backend = PynputInput()
            self.hotkey_backend = PynputHotkey()
            print("🔧 使用 pynput 后端")

        elif IS_LINUX:
            display = detect_linux_display()
            print(f"🖥️  显示服务器: {display}")

            if display == "wayland":
                self.input_backend = YdotoolInput()
                self.hotkey_backend = KeyboardLibHotkey()
                print("🔧 使用 keyboard + ydotool 后端")
            else:
                self.input_backend = PynputInput()
                self.hotkey_backend = PynputHotkey()
                print("🔧 使用 pynput 后端")
        else:
            print(f"❌ 不支持的操作系统: {SYSTEM}")
            sys.exit(1)

    def _check_deps(self):
        """检查并提示安装依赖"""
        missing = []

        try:
            import pynput  # noqa: F401
        except ImportError:
            missing.append("pynput")

        if IS_LINUX and detect_linux_display() == "wayland":
            try:
                import keyboard  # noqa: F401
            except ImportError:
                missing.append("keyboard")

            if not self._cmd_exists("ydotool"):
                print("\n❌ 未找到 ydotool")
                print("   Wayland 下需要安装: sudo apt install ydotool")
                print("   并启动守护进程: sudo ydotoold &")
                sys.exit(1)

        if IS_LINUX and detect_linux_display() != "wayland":
            try:
                import Xlib  # noqa: F401
            except ImportError:
                print("\n⚠️  建议安装 python3-xlib 以获得更好的 X11 支持")
                print("   sudo apt install python3-xlib")

        if missing:
            print(f"\n❌ 缺少 Python 依赖: {', '.join(missing)}")
            print(f"   请执行: pip3 install {' '.join(missing)}")
            sys.exit(1)

        if IS_MACOS:
            print("\n⚠️  首次运行需要授权辅助功能权限:")
            print("   系统设置 → 隐私与安全性 → 辅助功能")
            print("   将「终端」或「Python」加入列表并开启")

        if IS_LINUX:
            self._check_linux_input_group()

    def _cmd_exists(self, cmd: str) -> bool:
        return subprocess.run(
            ["which", cmd], capture_output=True
        ).returncode == 0

    def _check_linux_input_group(self):
        """检查 Linux 用户是否在 input 组"""
        try:
            import grp
            user_groups = [
                g.gr_name for g in grp.getgrall()
                if os.getlogin() in g.gr_mem or g.gr_gid == os.getgid()
            ]
            if "input" not in user_groups:
                print("\n⚠️  当前用户不在 input 组，可能无法监听全局热键")
                print("   请执行: sudo usermod -aG input $USER")
                print("   然后重新登录或重启")
                print("   或者临时使用 sudo 运行此脚本\n")
        except Exception:
            pass

    def _send(self, phrase: str):
        """发送短语"""
        if self.paused:
            return
        self.input_backend.send(phrase)

    def _toggle_pause(self):
        """暂停/恢复切换"""
        self.paused = not self.paused
        state = "⏸️  已暂停" if self.paused else "▶️  运行中"
        print(f"\n{state}")

    def _show_help(self):
        """显示帮助信息"""
        print("\n📋 快捷键对照表:")
        print("-" * 30)
        for key, phrase in PHRASES.items():
            alt = key.replace("f", "Ctrl+Shift+")
            print(f"  {key.upper():3} / {alt:12} → {phrase}")
        print("-" * 30)
        print("  F12           → 暂停/恢复")
        print("  Ctrl+C        → 退出\n")

    def run(self):
        """启动输入法"""
        print("\n🔥 输入法已启动!")
        print("   F1-F6 一键发送  |  F12 暂停  |  Ctrl+C 退出\n")

        for key, phrase in PHRASES.items():
            self.hotkey_backend.add_hotkey(key, lambda p=phrase: self._send(p))
            alt_key = key.replace("f", "ctrl+shift+")
            self.hotkey_backend.add_hotkey(alt_key, lambda p=phrase: self._send(p))

        self.hotkey_backend.add_pause_hotkey(self._toggle_pause)
        self._show_help()

        try:
            self.hotkey_backend.run()
        except KeyboardInterrupt:
            print("\n👋 再见!")
            sys.exit(0)


def main():
    """命令行入口"""
    ime = VibeCodingIME()
    ime.run()
