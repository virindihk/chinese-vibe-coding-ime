; ============================================
; 中文 Vibe Coding 输入法 (Windows 版)
; AutoHotkey v2 脚本
; F1-F6 一键输出，自动回车
; ============================================
#Requires AutoHotkey v2.0
#SingleInstance Force

; 托盘提示
trayTip := A_ScriptName
A_IconTip := "中文 Vibe Coding 输入法`nF1-F6 一键发送"

; 可选：添加托盘菜单项
TraySetIcon("shell32.dll", 44)  ; 键盘图标

; ============================================
; F1-F6 主快捷键
; ============================================

F1:: {
    SendInput("说中文")
    Sleep(50)
    Send("{Enter}")
}

F2:: {
    SendInput("继续")
    Sleep(50)
    Send("{Enter}")
}

F3:: {
    SendInput("还是报错")
    Sleep(50)
    Send("{Enter}")
}

F4:: {
    SendInput("你改了啥")
    Sleep(50)
    Send("{Enter}")
}

F5:: {
    SendInput("先别重构")
    Sleep(50)
    Send("{Enter}")
}

F6:: {
    SendInput("回滚回滚")
    Sleep(50)
    Send("{Enter}")
}

; ============================================
; 备选快捷键（避免 F1 冲突）
; Ctrl + Shift + 1-6
; ============================================

^+1:: {
    SendInput("说中文")
    Sleep(50)
    Send("{Enter}")
}

^+2:: {
    SendInput("继续")
    Sleep(50)
    Send("{Enter}")
}

^+3:: {
    SendInput("还是报错")
    Sleep(50)
    Send("{Enter}")
}

^+4:: {
    SendInput("你改了啥")
    Sleep(50)
    Send("{Enter}")
}

^+5:: {
    SendInput("先别重构")
    Sleep(50)
    Send("{Enter}")
}

^+6:: {
    SendInput("回滚回滚")
    Sleep(50)
    Send("{Enter}")
}

; ============================================
; 控制快捷键
; ============================================

; F12 = 暂停/恢复脚本
F12:: {
    Suspend
    state := A_IsSuspended ? "已暂停" : "运行中"
    TrayTip(trayTip, "输入法 " . state, 1500)
}

; Ctrl + Alt + R = 重新加载脚本
^!r:: Reload

; ============================================
; 启动提示
; ============================================
TrayTip(trayTip, "中文 Vibe Coding 输入法已启动`nF1-F6 一键发送`nF12 暂停/恢复", 2000)
