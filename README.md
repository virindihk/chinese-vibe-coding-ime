# 🇨🇳 中文 Vibe Coding 输入法

> 专为中文开发者设计的 Vibe Coding 快捷输入工具。按 F1-F6，一键输出程序员与 AI 结对编程时的经典语录。

![Vibe Coding Keyboard](https://github.com/user-attachments/assets/placeholder)

*灵感来源：那张传说中的 6 键小键盘 meme*

---

## ✨ 功能

| 按键 | 输出内容 | 场景 |
|------|----------|------|
| **F1** / ⌘⇧1 | `说中文` | 让 AI 用中文回答 |
| **F2** / ⌘⇧2 | `继续` | AI 生成到一半停了 |
| **F3** / ⌘⇧3 | `还是报错` | AI 说修好了但没修好 |
| **F4** / ⌘⇧4 | `你改了啥` | AI 偷偷改了一堆文件 |
| **F5** / ⌘⇧5 | `先别重构` | AI 突然想重写整个项目 |
| **F6** / ⌘⇧6 | `回滚回滚` | 彻底搞砸了 |

所有按键都会**自动输出文字 + 自动回车**。

---

## 🚀 安装

### 1. 安装 Hammerspoon

```bash
brew install --cask hammerspoon
```

或从 [hammerspoon.org](https://www.hammerspoon.org/) 下载。

### 2. 复制配置

```bash
cp init.lua ~/.hammerspoon/init.lua
```

### 3. 授权辅助功能

前往 **系统设置 → 隐私与安全性 → 辅助功能**，将 **Hammerspoon** 加入列表并开启。

### 4. 启动 Hammerspoon

打开 Hammerspoon 应用，点击菜单栏图标 → **Reload Config**。

---

## ⌨️ 关于 F1-F6

macOS 默认将 F1-F12 作为媒体键（亮度/音量等）。

**方案一（推荐）：** 前往「系统设置 → 键盘 → 键盘快捷键 → 功能键」，勾选「将 F1、F2 等键用作标准功能键」。

**方案二：** 直接使用备选快捷键 **Cmd + Shift + 1-6**，无需修改系统设置。

---

## 🛠️ 自定义

编辑 `~/.hammerspoon/init.lua`，修改 `vibeCodingPhrases` 表中的内容，然后 Reload Config。

```lua
local vibeCodingPhrases = {
  F1  = "说中文",
  F2  = "继续",
  -- ...改成你想要的任何文字
}
```

---

## 📄 License

MIT
