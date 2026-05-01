# 统一版安装说明（推荐）

> 一个 Python3 脚本跨 macOS / Windows / Linux，无需 Hammerspoon / AutoHotkey。

## 安装依赖

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

## 运行

```bash
python3 unified/vibe-coding-ime.py
```

看到 `🔥 输入法已启动!` 就可以用了。

## 权限（重要）

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

## 快捷键

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

## 自定义词库

编辑 `unified/vibe-coding-ime.py`，修改顶部的 `PHRASES` 字典，保存后立即生效。

```python
PHRASES = {
    "f1": "说中文",
    "f2": "继续",
    # ...改成你想要的
}
```

## 技术细节

统一版会根据你的系统自动选择底层引擎：

| 系统 | 热键监听 | 模拟输入 |
|:-----|:---------|:---------|
| macOS | pynput | pynput |
| Windows | pynput | pynput |
| Linux X11 | pynput | pynput |
| Linux Wayland | keyboard (evdev) | ydotool |

所有平台差异都被封装在 `InputBackend` 和 `HotkeyBackend` 类里，上层代码完全一致。
