# Marsala Agent · Alpha 1.9

一款营销咨询 AI Agent。

**本分支（`main`）不存储任何代码。** 请根据你使用的平台切换到对应分支：

---

## 分支导航

| 分支 | 平台 | 说明 |
|------|------|------|
| [`reasonix`](../../tree/reasonix) | Reasonix Code | 基于Reasonix的原始开发版本。
| [`claude-code`](../../tree/claude-code) | Claude Code | Claude Code 适配版。

两个分支的技能文件（`.marsala/skills/`）完全共用，本质是同一套 Agent 的不同平台适配。

---

## 快速切换

```bash
# Reasonix Code 用户
git clone https://gitcode.com/thyeon/Marsala-Agent.git
cd Marsala-Agent
git checkout reasonix

# Claude Code 用户
git clone https://gitcode.com/thyeon/Marsala-Agent.git
cd Marsala-Agent
git checkout claude-code
```

---

## 这是什么

Marsala 是一个为广告策略和品牌营销咨询场景设计的 AI Agent。从客户 Brief 拆解开始，经过商业战略、市场研究、消费者研究、品牌策划、创意方向，最终输出媒介执行方案。

**核心承诺：不确定时不编造。定位层可以为空。信息不足时承认信息不足。**

## 架构

一脑六手 + 四层审查：

- 🧠 **大脑：客户总监** — 诊断引擎，调度六手
- 🤚 **手一：商业战略** — 增长路径、利润归因、资源配置
- 🤚 **手二：市场研究** — 行业分析、竞品地图、趋势扫描
- 🤚 **手三：消费者研究** — 用户画像、购买动机、JTBD
- 🤚 **手四：品牌策划** — 品牌定位（含十一闸门校验体系）
- 🤚 **手五：创意总监** — Big Idea、文案、视觉方向
- 🤚 **手六：媒介策划** — 媒介组合、预算规划、KOL 策略
- 🛡️ **审查层** — P&L 经营审查、组织政治审查、危机应对审查、证据等级审查

## 作者

©thyeon
