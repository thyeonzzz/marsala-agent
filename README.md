# Marsala · Beta 1.5.3

一个做营销策略判断的 Proto-Agent。不写文案、不管投放、不发邮件——只回答一个问题：**品牌下一步该做什么，以及为什么。**

---

**本分支（`main`）不存储任何代码。** 请根据你使用的平台切换到对应分支：

## 分支导航

| 分支 | 平台 | 启动方式 |
|------|------|---------|
| [`reasonix`](../../tree/reasonix) | Reasonix Code | 打开目录自动加载，或输入 `/marsala` |
| [`claude-code`](../../tree/claude-code) | Claude Code | 打开目录自动加载，或输入 `/marsala` |

两个分支的技能文件（`.marsala/skills/`）完全共用，本质是同一套系统在不同平台的适配。

## 快速切换

```bash
git clone https://gitcode.com/thyeon/Marsala-Agent.git
cd Marsala-Agent

# Reasonix Code 用户
git checkout reasonix

# Claude Code 用户
git checkout claude-code
```

---

## 架构

```
🧠 客户总监                   诊断 · 调度 · 审核 · 熔断
   │
   ├── 🤚 手一：商业战略       增长路径 · 利润结构 · 定价策略 · 流失预防 · GTM 发布
   ├── 🤚 手二：市场研究       行业分析 · 竞品地图 · 趋势扫描 · 创新扩散预测
   ├── 🤚 手三：消费者洞察     用户画像 · JTBD · 动机挖掘 · RFM · CLV 双轨
   ├── 🤚 手四：品牌策划       九道定位闸门 · 11 项校验 · 四层命题分类
   ├── 🤚 手五：创意总监       Big Idea · 文案 · 视觉方向 · 去 Logo 测试
   └── 🤚 手六：媒介策划       媒介组合 · 预算分配 · KOL 策略 · CRO 审计

🛡️ 四个审查层               P&L 经营审查 · 组织政治审查 · 危机应对 · 证据治理 (E1-E6)
```

---

## 它和别的 AI 营销工具有什么区别

大多数 AI 营销工具帮你**执行**——生成文案、设计图片、群发邮件。Marsala 做的是这些事发生之前的判断：选什么方向、为什么选这个方向、怎么知道选对了还是选错了。

**底线：不确定的时候不编造。定位层可以为空。信息不足时承认信息不足。**

---

## 作者

© thyeon
