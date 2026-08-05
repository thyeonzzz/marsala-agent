# install-codex.ps1 - 把 chatgpt 分支的 Marsala 技能安装到 Codex 全局技能目录
#
# 用法：powershell -ExecutionPolicy Bypass -File .\install-codex.ps1
#
# 作用域说明：
#   - 安装到 $HOME\.codex\skills\marsala（Codex 专属技能目录），对本机所有 Codex 项目生效；
#   - 不写入 $HOME\.agents\skills（跨工具共享目录），reasonix / hermes / workbuddy /
#     Claude Code 等工具不会加载它。
#
# 记忆说明：
#   - memory/ 只在目标目录不存在时播种（首次安装）；
#   - 之后重复运行会保留会话中累积的记忆，不覆盖；
#   - 如需重置记忆，先删除 $HOME\.codex\skills\marsala\memory 再运行本脚本。

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$dest = Join-Path (Join-Path $HOME '.codex\skills') 'marsala'

Write-Host "==> 安装 Marsala 到 Codex 全局技能目录：$dest"
New-Item -ItemType Directory -Path $dest -Force | Out-Null

foreach ($name in @('SKILL.md', 'MEMORY.md', 'skills', 'memory', 'agents')) {
    $src = Join-Path $repoRoot $name
    if (-not (Test-Path -LiteralPath $src)) {
        Write-Host "    跳过 $name（仓库中不存在）"
        continue
    }
    $target = Join-Path $dest $name
    if ($name -eq 'memory' -and (Test-Path -LiteralPath $target)) {
        Write-Host "    跳过 memory/（保留现有会话记忆；重置请先删除目标目录）"
        continue
    }
    Copy-Item -LiteralPath $src -Destination $dest -Recurse -Force
    Write-Host "    已复制 $name"
}

Write-Host '==> 完成。新开任意 Codex 会话后生效；说「启动 Marsala」或直接提营销策略需求。'
