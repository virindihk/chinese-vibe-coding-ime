# Windows 版安装说明

## 前置要求

下载并安装 **AutoHotkey v2**：

🔗 https://www.autohotkey.com/v2/

> ⚠️ 注意：必须安装 **v2 版本**，v1 版本的语法不兼容。

## 使用方法

### 方式一：直接运行脚本（推荐）

1. 双击 `vibe-coding-ime.ahk`
2. 右下角托盘区出现键盘图标即表示运行中
3. 在任意输入框按 **F1-F6** 即可一键发送

### 方式二：编译成独立 exe（无需安装 AutoHotkey）

1. 右键 `vibe-coding-ime.ahk` → **Compile Script**（需要安装 AutoHotkey）
2. 会生成 `vibe-coding-ime.exe`
3. 双击 exe 即可运行，**无需安装 AutoHotkey**
4. 可以把 exe 放到「启动」文件夹实现开机自启

### 开机自启

把 `vibe-coding-ime.ahk` 或 `vibe-coding-ime.exe` 放入以下目录：

```
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
```

按 `Win + R`，输入 `shell:startup`，回车即可打开该文件夹。

## 快捷键说明

| 按键 | 输出内容 |
|:----:|:---------|
| **F1** | `说中文` ↵ |
| **F2** | `继续` ↵ |
| **F3** | `还是报错` ↵ |
| **F4** | `你改了啥` ↵ |
| **F5** | `先别重构` ↵ |
| **F6** | `回滚回滚` ↵ |
| **Ctrl + Shift + 1-6** | 同上（备选，避免 F1 冲突） |
| **F12** | 暂停 / 恢复脚本 |
| **Ctrl + Alt + R** | 重新加载脚本 |

## 自定义词库

用记事本打开 `vibe-coding-ime.ahk`，找到对应按键修改文字，保存后按 `Ctrl + Alt + R` 立即生效。

```autohotkey
F1:: {
    SendInput("你想说的任何话")
    Sleep(50)
    Send("{Enter}")
}
```
