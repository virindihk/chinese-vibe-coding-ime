-- ============================================
-- 中文 Vibe Coding 输入法
-- F1-F6 一键输出，自动回车
-- ============================================

-- 启用 IPC 支持，方便命令行控制
require("hs.ipc")

local vibeCodingPhrases = {
  F1  = "说中文",
  F2  = "继续",
  F3  = "还是报错",
  F4  = "你改了啥",
  F5  = "先别重构",
  F6  = "回滚回滚",
}

-- 绑定按键的通用函数
local function bindVibeKey(key, phrase)
  local function sendPhrase()
    -- 输出文字
    hs.eventtap.keyStrokes(phrase)
    -- 稍微延迟后按回车，确保文字已输入
    hs.timer.doAfter(0.1, function()
      hs.eventtap.keyStroke({}, "return")
    end)
  end

  -- 主快捷键：F1-F6
  -- 注意：macOS 默认 F1-F12 是媒体键，需要按 Fn+F1 触发，
  -- 或在「系统设置 → 键盘 → 键盘快捷键」中勾选「将 F1、F2 等键用作标准功能键」
  hs.hotkey.bind({}, key, sendPhrase)

  -- 备选快捷键：Cmd+Shift+1-6（不受 F1 媒体键影响）
  local num = key:gsub("F", "")
  hs.hotkey.bind({"cmd", "shift"}, num, sendPhrase)
end

-- 绑定所有按键
for key, phrase in pairs(vibeCodingPhrases) do
  bindVibeKey(key, phrase)
end

-- 提示已加载
hs.alert.show("中文 Vibe Coding 输入法已启动 ✓\nF1-F6 或 ⌘⇧1-6", 3)
print("[VibeCoding] 中文 Vibe Coding 输入法已加载")
print("[VibeCoding] F1:说中文 F2:继续 F3:还是报错 F4:你改了啥 F5:先别重构 F6:回滚回滚")
print("[VibeCoding] 备选: Cmd+Shift+1/2/3/4/5/6")
