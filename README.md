# 🇨🇳 中文 Vibe Coding 输入法

> 专为中文开发者设计的 Vibe Coding 快捷输入工具。按 **F1-F6**，一键输出程序员与 AI 结对编程时的经典语录，自动回车发送。

<p align="center">
  <img src="assets/keyboard.webp" alt="中文 Vibe Coding 键盘" width="500">
</p>

*灵感来源：那张在开发者圈子里疯传的 6 键小键盘 meme*

---

## ✨ 功能

| 按键 | 输出内容 | 使用场景 |
|:----:|:---------|:---------|
| **F1** | `说中文` | 让 AI 用中文回答 / 描述需求 |
| **F2** | `继续` | AI 生成到一半停了，催它输出 |
| **F3** | `还是报错` | AI 说修好了，一跑又崩了 |
| **F4** | `你改了啥` | AI 偷偷改了一堆文件，想看 diff |
| **F5** | `先别重构` | AI 突然想重写整个项目，赶紧按住 |
| **F6** | `回滚回滚` | 彻底搞砸了，一键回到上一版本 |

**特点：**
- ✅ 一键输入，**自动回车**
- ✅ 全局生效，任何输入框都能用（IDE、浏览器、微信、飞书……）
- ✅ **macOS / Windows / Linux 三平台**，一个 Python 脚本全搞定
- ✅ 备选快捷键，无需担心 F1 被系统占用
- ✅ 随时可改词，改完立即生效

---

## 🚀 安装

```bash
pip3 install pynput keyboard
```

### 平台额外依赖

| 平台 | 额外依赖 | 安装命令 |
|:-----|:---------|:---------|
| **macOS** | 无 | 只需 `pip3 install pynput keyboard` |
| **Windows** | 无 | 只需 `pip3 install pynput keyboard` |
| **Linux X11** | python3-xlib | `sudo apt install python3-xlib` |
| **Linux Wayland** | ydotool | `sudo apt install ydotool` |

> **Linux Wayland 用户**: 还需要启动 ydotoold 守护进程：
> ```bash
> sudo ydotoold &
> ```

---

## 🎮 使用

```bash
git clone https://github.com/virindihk/chinese-vibe-coding-ime.git
cd chinese-vibe-coding-ime
python3 -m vibe_coding_ime
```

看到 `🔥 输入法已启动!` 就可以用了。

| 按键 | 输出 |
|:----:|:-----|
| **F1** / Ctrl+Shift+1 | `说中文` ↵ |
| **F2** / Ctrl+Shift+2 | `继续` ↵ |
| **F3** / Ctrl+Shift+3 | `还是报错` ↵ |
| **F4** / Ctrl+Shift+4 | `你改了啥` ↵ |
| **F5** / Ctrl+Shift+5 | `先别重构` ↵ |
| **F6** / Ctrl+Shift+6 | `回滚回滚` ↵ |
| **F12** | 暂停/恢复 |
| **Ctrl+C** | 退出 |

---

## ⚙️ 权限

### macOS
首次运行需要授权**辅助功能权限**：
**系统设置 → 隐私与安全性 → 辅助功能**，将「终端」（或你运行 Python 的 app）加入列表并开启。

### Linux
需要把用户加入 `input` 组才能监听全局热键：
```bash
sudo usermod -aG input $USER
# 重新登录或重启后生效
```

Windows 无需额外权限。

---

## 🛠️ 自定义词库

编辑 `vibe_coding_ime/__init__.py`，修改顶部的 `PHRASES` 字典：

```python
PHRASES = {
    "f1": "说中文",
    "f2": "继续",
    "f3": "还是报错",
    "f4": "你改了啥",
    "f5": "先别重构",
    "f6": "回滚回滚",
    # 可以继续加...
}
```

保存后重启脚本即可生效。

---

## 🔧 技术细节

统一版会根据你的系统自动选择底层引擎：

| 系统 | 热键监听 | 模拟输入 |
|:-----|:---------|:---------|
| macOS | pynput | pynput |
| Windows | pynput | pynput |
| Linux X11 | pynput | pynput |
| Linux Wayland | keyboard (evdev) | ydotool |

所有平台差异都被封装在 `InputBackend` 和 `HotkeyBackend` 类里，上层代码完全一致。

---

## 📂 项目结构

```
.
├── vibe_coding_ime/
│   └── __init__.py          # 核心代码
├── assets/
│   └── keyboard.webp        # 项目灵感图
├── legacy/                  # 历史原生方案（Hammerspoon/AutoHotkey）
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🤝 贡献

欢迎提交 Issue 和 PR！

- 有新的「Vibe Coding 经典语录」？欢迎补充
- 发现 Bug？随时提 Issue

---

## 📄 License

MIT © [virindihk](https://github.com/virindihk)

---

<p align="center">
  <sub>Made with 🧋 and rage against AI hallucinations</sub>
</p>
