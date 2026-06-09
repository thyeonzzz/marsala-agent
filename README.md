# Marsala Agent · Alpha 1.2

一脑六手营销咨询 AI Agent。支持 **Reasonix Code** 和 **Claude Code** 双平台。

---

## 这是什么

Marsala 是一个为广告策略和品牌营销咨询场景设计的 AI Agent。从客户 Brief 拆解开始，经过商业战略判断、市场研究、消费者研究，最终输出品牌定位和创意方向。

**核心承诺：不确定时不编造。定位层可以为空。信息不足时承认信息不足。**

## 架构

一脑六手 + 三层审查：

- **🧠 大脑：客户总监** — 诊断引擎
- **🤚 手一：商业战略** — 增长路径、利润归因、资源配置
- **🤚 手二：市场研究** — 行业分析、竞品地图、趋势扫描
- **🤚 手三：消费者研究** — 用户画像、购买动机、JTBD
- **🤚 手四：品牌策划** — 品牌定位（含十一闸门校验体系 + 四层命题分类）
- **🤚 手五：创意总监** — Big Idea、文案、视觉方向
- **🤚 手六：媒介策划** — 媒介组合、预算规划、KOL 策略
- **🛡️ 审查层** — P&L 经营审查、组织政治审查、危机应对审查

## 平台版本

本仓库使用分支管理不同平台的适配版本：

| 分支 | 平台 | 关键文件 | 启动方式 |
|------|------|---------|---------|
| `main` | Reasonix Code | `MEMORY.md` + `BOOTSTRAP.md` | `/startMSA` 或「启动 Marsala」 |
| `claude` | Claude Code | `CLAUDE.md` + `.claude/skills/marsala.md` | `/marsala` 或「启动 Marsala」 |

**切换方式：**
```bash
git checkout main      # Reasonix 版本
git checkout claude    # Claude Code 版本
```

本质是同一套 Agent 的不同平台适配——类似 iOS 版和安卓版。技能文件（`.marsala/skills/`）在两端完全共用。

## 快速开始

### Reasonix Code
打开项目目录，输入 `/startMSA` 或说「启动 Marsala」。

### Claude Code
打开项目目录，输入 `/marsala` 或说「启动 Marsala」。

## 作者

©thyeon
