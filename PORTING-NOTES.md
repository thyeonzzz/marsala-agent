# Marsala · ChatGPT 适配说明（chatgpt 分支）

**版本：** Beta 3.3.2（ChatGPT 适配版）
**内容基准：** `reasonix` 分支
**目标：** 在 ChatGPT 应用环境中达到并超过 Reasonix 的表现。

---

## 为什么存在本分支

Reasonix 表现最好，但它「只适合作为开发环境，不适合作为应用环境」。Reasonix 版本依赖平台特有的加载命令（`/marsala` + `MARSALA_HOME` 环境变量）、`remember` 记忆工具和平台工具集（AnySearch、web_fetch、chrome-devtools）。ChatGPT 没有这些机制，直接复制文件会导致：入口找不到、记忆无法持久化、证据规则互相矛盾。

---

## 改了什么（对照 reasonix）

| # | 改动 | 为什么 |
|---|------|--------|
| 1 | **入口机制**：`/marsala` + 环境变量 → `SKILL.md`（ChatGPT/Codex 原生技能格式） | 无需环境变量，任务相关时自动触发，用户说「启动 Marsala」即可 |
| 2 | **双阶段加载协议**：固定核心（MEMORY + 证据治理 + 输出规则）+ 按任务按需加载 | 省上下文：核心常驻约 40KB，审核规则等重文件只在需要时读 |
| 3 | **证据治理统一**：account-director / hand-2 / hand-3 三处互相矛盾的证据表 → `skills/evidence-governance.md` 唯一权威 | 三套权重并存会让 AI 读到互相冲突的规则；统一后只剩一份标准 |
| 4 | **大文件拆分**：account-director.md 100KB → 核心 82KB + `review-rules.md`（审核校验规则 365 行）+ `evidence-governance.md` | 客户总监常驻文件不再背负 350 行审核规则；审核时才加载 |
| 5 | **记忆文件化**：`remember` 工具 → `memory/` 目录（USER / CLIENTS / LESSONS） | ChatGPT 无 remember；文件化记忆跨会话持久、可人工审阅、可随仓库版本化 |
| 6 | **工具映射**：AnySearch / web_fetch / chrome-devtools → 内置搜索 / 网页读取 / 文件 / 文档 / 代码工具 | 平台数据缺口明确声明，不假装能拿到 |
| 7 | **清理**：删除 `5hand.txt`（五手时代草稿）；`platform-wechat.md` 移入 `skills/_archive/`（已禁用）；README 术语统一（十一闸门 → 九道闸门） | 消除会让 AI 混淆的过时与矛盾信息 |
| 8 | **交付质量门**：SKILL.md 内置六项交付前自检（Ghost Deck / 证据标注 / 假设概率 / 纠错绑定 / 商业四问 / 标题即断言） | 把 Reasonix 里分散的校验收拢成一条交付前的强制流程 |
| 9 | **项目级作用域**：技能安装在 `.codex/skills/marsala/`（Codex/ChatGPT 项目级技能目录），不写入全局技能目录 | 全局目录（`~/.agents/skills`、`~/.codex/skills`）会被所有项目和其他 Agent 工具共享；项目级目录让 Marsala 只在本项目生效，形成 ChatGPT 专属通道 |

---

## 为什么这样能超过 Reasonix

1. **上下文效率**：Reasonix 加载整份 100KB 客户总监文件；ChatGPT 版核心常驻更小，审核与专题内容按需加载——长会话中判断质量更稳定。
2. **规则无冲突**：证据等级只有一份权威版本，AI 不会被三套权重带偏。
3. **记忆可审计**：文件化记忆可以打开检查、手动修正、随仓库提交——`remember` 的记忆是黑盒。
4. **原生交付件**：ChatGPT 可以直接产出提案文档、对比表格、汇报演示文稿——咨询交付闭环更完整。
5. **对抗性证伪可执行**：内置搜索让「反证搜索」真正跑得起来（校验三十三）。

---

## 安装

### ChatGPT / Codex 桌面版

本项目文件夹本身就是 `chatgpt` 分支的仓库，技能包位于 `.codex/skills/marsala/`：

1. 在 ChatGPT / Codex 桌面版中打开本文件夹（项目级技能目录自动生效）
2. 新建会话（技能列表在新会话中刷新）
3. 说「启动 Marsala」，或直接提出营销策略需求

**不要**复制到 `C:\Users\<你的用户名>\.agents\skills\marsala\` 或 `~\.codex\skills\marsala\`——
那是全局技能目录，会让 Marsala 出现在你所有项目里，也会覆盖/干扰其他平台共用的同名技能。
如需让技能在其他项目也生效，再考虑全局安装；本项目只走项目级专属通道。

### 其他 ChatGPT 形式（通用）

- **ChatGPT 项目**：把 `SKILL.md`、`MEMORY.md`、`skills/`、`memory/` 上传到项目，并在项目说明中写「项目包含 Marsala 技能，按 SKILL.md 加载」
- **自定义 GPT**：把 `SKILL.md` 的加载协议写入 Instructions，`skills/` 作为 Knowledge 上传

## 从 reasonix 同步内容（开发流程）

Reasonix 分支是内容基准，把新内容搬进 ChatGPT 通道时按以下映射操作：

| reasonix 分支 | chatgpt 分支（本目录） |
|---------------|----------------------|
| `MEMORY.md` | `.codex/skills/marsala/MEMORY.md` |
| `skills/` | `.codex/skills/marsala/skills/` |
| `marsala.md` 中仍有效的内容 | 合并进 `.codex/skills/marsala/SKILL.md` |

注意事项：
- `memory/` 是 ChatGPT 会话的活记忆，同步时不要整体覆盖，只补种子内容
- reasonix 特有的工具引用（`remember`、`AnySearch`、`MARSALA_HOME`）不要带入，
  对应能力在 ChatGPT 版已映射为内置搜索 / 文件工具 / `memory/` 目录
- 同步后运行本机校验：`quick_validate.py .codex/skills/marsala`

---

## 验证清单（安装后建议跑一遍）

- [ ] 触发后输出「Marsala 已启动……」，并先问 ≤3 个诊断问题，而不是直接给方案
- [ ] 要求做一次竞品分析：输出应标注证据等级、区分品牌宣称与消费者行为、漏斗式提问
- [ ] 故意给一个模糊需求（如「帮我定位」）：应追问商业背景，而不是直接给一个漂亮 slogan
- [ ] 项目结束后说「先到这里」：应自动把客户信息写入 `memory/CLIENTS.md`
- [ ] 涉及利润下降的话题：应先触发 P&L 审查而不是直接给营销方案
