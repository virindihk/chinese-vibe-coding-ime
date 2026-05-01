# Linux 版安装说明

## 前置要求

- Python 3.7+
- 全局热键需要 `keyboard` 库
- 输入模拟需要 `xdotool` (X11) 或 `ydotool` (Wayland)

## 快速开始

### 1. 安装依赖

```bash
# Debian / Ubuntu
sudo apt update
sudo apt install python3-pip xdotool

# Arch Linux
sudo pacman -S python-pip xdotool

# Fedora
sudo dnf install python3-pip xdotool
```

```bash
# 安装 Python 依赖
pip3 install keyboard
```

> **Wayland 用户**: 把 `xdotool` 换成 `ydotool`，并确保 `ydotoold` 守护进程在运行：
> ```bash
> sudo ydotoold &
> ```

### 2. 运行

```bash
python3 linux/vibe-coding-ime.py
```

看到 `🔥 输入法已启动!` 就可以用了。

## 快捷键

| 按键 | 输出内容 |
|:----:|:---------|
| **F1** | `说中文` ↵ |
| **F2** | `继续` ↵ |
| **F3** | `还是报错` ↵ |
| **F4** | `你改了啥` ↵ |
| **F5** | `先别重构` ↵ |
| **F6** | `回滚回滚` ↵ |
| **Ctrl + Shift + 1-6** | 同上（备选） |
| **F12** | 暂停 / 恢复 |
| **Ctrl + C** | 退出 |

## 权限问题

`keyboard` 库需要读取 `/dev/input/event*` 设备来监听全局热键。

**方式一（推荐）**：将当前用户加入 `input` 组
```bash
sudo usermod -aG input $USER
# 然后重新登录或重启
```

**方式二**：每次用 `sudo` 运行
```bash
sudo python3 linux/vibe-coding-ime.py
```

## 开机自启（systemd 用户服务）

```bash
# 1. 复制脚本到 PATH
mkdir -p ~/.local/bin
cp linux/vibe-coding-ime.py ~/.local/bin/
chmod +x ~/.local/bin/vibe-coding-ime.py

# 2. 复制服务文件
mkdir -p ~/.config/systemd/user
cp linux/vibe-coding-ime.service ~/.config/systemd/user/

# 3. 启用并启动
systemctl --user daemon-reload
systemctl --user enable vibe-coding-ime
systemctl --user start vibe-coding-ime

# 查看状态
systemctl --user status vibe-coding-ime

# 查看日志
journalctl --user -u vibe-coding-ime -f
```

## 自定义词库

编辑 `linux/vibe-coding-ime.py`，修改 `PHRASES` 字典：

```python
PHRASES = {
    "f1": "说中文",
    "f2": "继续",
    # ...改成你想要的
}
```

保存后重启脚本即可生效。
