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
| 4 | **大文件拆分**：account-director.md 100KB → 核心 82KB + `review-rules.md`（审核校验规则）+ `evidence-governance.md` | 客户总监常驻文件不再背负审核规则；审核时才加载 |
| 5 | **记忆文件化**：`remember` 工具 → `memory/` 目录（USER / CLIENTS / LESSONS） | ChatGPT 无 remember；文件化记忆跨会话持久、可人工审阅、可随仓库版本化 |
| 6 | **工具映射**：AnySearch / web_fetch / chrome-devtools → 内置搜索 / 网页读取 / 文件 / 文档 / 代码工具 | 平台数据缺口明确声明，不假装能拿到 |
| 7 | **清理**：删除 `5hand.txt`（五手时代草稿）；`platform-wechat.md` 移入 `skills/_archive/`（已禁用）；README 术语统一（十一闸门 → 九道闸门） | 消除会让 AI 混淆的过时与矛盾信息 |
| 8 | **交付质量门**：SKILL.md 内置六项交付前自检（Ghost Deck / 证据标注 / 假设概率 / 纠错绑定 / 商业四问 / 标题即断言） | 把 Reasonix 里分散的校验收拢成一条交付前的强制流程 |
| 9 | **Codex 全局通道**：技能安装到 `~/.codex/skills/marsala/`（Codex 专属技能目录），不写入 `~/.agents/skills` | `~/.agents/skills` 是跨工具共享目录（reasonix / hermes / Claude Code 都会读）；`~/.codex/skills` 只有 Codex 读取，对本机所有 Codex 项目生效——按用户要求走 Codex 全局通道 |
| 10 | **review-rules 压缩**：47KB → ~7KB。删除案例与叙事冗余；定位审核与 hand-4 九道闸门去重；元规则独立成章；校验重编为一~十三（含追问表编号） | 校验体系从「合规机器」回归「审核工具」——核心契约确立后，正确性由闸门承担，审查层只做查漏 |
| 11 | **双模式入口**：一个入口两种模式——品牌咨询（手一~四）/ 营销策划（手五~六）/ 全管线承接；交付标准按模式分，核心契约共用 | 不再强制所有客户走完六手全程——品牌客户不被媒介排期拖累，campaign 客户不被品牌理论淹没 |
| 12 | **创意层**：`creative-layer.md`——上半场生成纪律（骨架扫描 + 品类适配 + 品牌事实注入 + 3-5 候选），下半场品味选择（五测 + 拥有 + 反例 + 一致性）；与 hand-5 分工为「选 vs 验」 | 回应蘑界第八章心虚：创意不是碰运气，是重组引擎 + 被拥有的选择；用户是品味的最终拥有者 |

---

## 为什么这样能超过 Reasonix

1. **上下文效率**：Reasonix 加载整份 100KB 客户总监文件；ChatGPT 版核心常驻更小，审核与专题内容按需加载——长会话中判断质量更稳定。
2. **规则无冲突**：证据等级只有一份权威版本，AI 不会被三套权重带偏。
3. **记忆可审计**：文件化记忆可以打开检查、手动修正、随仓库提交——`remember` 的记忆是黑盒。
4. **原生交付件**：ChatGPT 可以直接产出提案文档、对比表格、汇报演示文稿——咨询交付闭环更完整。
5. **对抗性证伪可执行**：内置搜索让「反证搜索」真正跑得起来（校验十三）。

---

## 安装

### ChatGPT / Codex 桌面版

`chatgpt` 分支是技能源（SKILL.md / MEMORY.md / skills/ / memory/ / agents/ 在仓库根目录），
安装到 Codex 全局技能目录：

1. 在本目录运行 `.\install-codex.ps1`（复制到 `C:\Users\<你的用户名>\.codex\skills\marsala\`）
2. 新建任意 Codex 会话（技能列表在新会话中刷新）
3. 说「启动 Marsala」，或直接提出营销策略需求

**不要**复制到 `C:\Users\<你的用户名>\.agents\skills\marsala\`——那是跨工具共享目录，
会覆盖/干扰其他平台共用的同名技能。`~\.codex\skills\marsala` 是 Codex 专属位置：
reasonix / hermes / workbuddy / Claude Code 都不会读它，但本机所有 Codex 项目都会生效（设计如此）。
若只想让单个项目生效，把技能放进该项目根目录的 `.codex\skills\marsala\` 并删除全局副本。

### 其他 ChatGPT 形式（通用）

- **ChatGPT 项目**：把 `SKILL.md`、`MEMORY.md`、`skills/`、`memory/` 上传到项目，并在项目说明中写「项目包含 Marsala 技能，按 SKILL.md 加载」
- **自定义 GPT**：把 `SKILL.md` 的加载协议写入 Instructions，`skills/` 作为 Knowledge 上传

## 从 reasonix 同步内容（开发流程）

Reasonix 分支是内容基准，把新内容搬进 ChatGPT 通道时按以下映射操作：

| reasonix 分支 | chatgpt 分支（本目录） |
|---------------|----------------------|
| `MEMORY.md` | `MEMORY.md`（仓库根目录） |
| `skills/` | `skills/`（仓库根目录） |
| `marsala.md` 中仍有效的内容 | 合并进 `SKILL.md`（仓库根目录） |

注意事项：
- `memory/` 是 ChatGPT 会话的活记忆，同步时不要整体覆盖，只补种子内容
- reasonix 特有的工具引用（`remember`、`AnySearch`、`MARSALA_HOME`）不要带入，
  对应能力在 ChatGPT 版已映射为内置搜索 / 文件工具 / `memory/` 目录
- 同步后运行本机校验：`quick_validate.py .`（仓库根目录），再执行 `.\install-codex.ps1` 刷新全局安装
- 会话记忆累积在 `~\.codex\skills\marsala\memory\`，需要入库时把该目录内容复制回仓库 `memory/` 再提交

---

## 验证清单（安装后建议跑一遍）

- [ ] 触发后输出「Marsala 已启动……」，并先问 ≤3 个诊断问题，而不是直接给方案
- [ ] 要求做一次竞品分析：输出应标注证据等级、区分品牌宣称与消费者行为、漏斗式提问
- [ ] 故意给一个模糊需求（如「帮我定位」）：应追问商业背景，而不是直接给一个漂亮 slogan
- [ ] 项目结束后说「先到这里」：应自动把客户信息写入 `memory/CLIENTS.md`
- [ ] 涉及利润下降的话题：应先触发 P&L 审查而不是直接给营销方案
