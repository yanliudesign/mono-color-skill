<div align="center">

**中文** · [English](./README.md)

# 单色编辑印刷

**为海报、Zine、肖像与视觉观察笔记而生的单色编辑图像 Skill。**

[![Version](https://img.shields.io/badge/VERSION-1.0.0-2ea44f?style=flat-square&labelColor=333)](./SKILL.md)
[![Skills](https://img.shields.io/badge/SKILLS-1-2ea44f?style=flat-square&labelColor=333)](./SKILL.md)
[![Stars](https://img.shields.io/github/stars/yanliudesign/monocolor?style=flat-square&label=STARS&color=e37f2c&labelColor=333)](https://github.com/yanliudesign/monocolor/stargazers)

[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-d97757?style=flat-square&labelColor=1a1a1a&logo=anthropic&logoColor=white)](https://claude.ai/code)
[![SKILL.md](https://img.shields.io/badge/Agent-SKILL.md-214f9b?style=flat-square&labelColor=1a1a1a)](./SKILL.md)

</div>

把一个主题、一句话、一个物件或一张照片，转成原创的单色编辑印刷作品。它使用暖色纸张、严格的一种彩色油墨、网点图像、主动留白，以及衬线字体与功能字体之间的强烈层级。

它保留的是一套视觉系统，而不是照抄参考图。每次构图都会根据主体、意图、文字和图像角色重新建立。

## 它能做什么

| 系统 | 方向 |
|---|---|
| **输入** | 主题、短句、物件、文章想法或用户提供的照片 |
| **配色** | 暖色非涂布纸 + 严格一种钴蓝或植物绿油墨 |
| **图像** | 网点、孔版颗粒、蓝晒曝光感或复印机破碎质感 |
| **留白** | 25%–55% 可见纸面，采用非对称编辑网格 |
| **字体** | 编辑感衬线字体 + 窄体无衬线或等宽功能字体 |
| **输出** | 生成位图、完整生产 Prompt 与简短配方说明 |

## 工作方式

```text
1  读取输入      →  确定主体、意图、文字与图像角色
2  选择版式      →  图像场、标本注释、文字宣言、信息海报、档案图版或编辑封面
3  建立单色层次  →  用网点密度和纸张代替额外颜色
4  组织画面      →  保留 25%–55% 留白，并加入一个有意的打破点
5  生成并检查    →  核对油墨数量、主体身份、层级、材质与原创性
```

## 视觉规则

1. **只用一种彩色油墨。** 默认钴蓝；植物绿只在主题需要时替代钴蓝，绝不作为第二种颜色叠加。
2. **纸张必须可见。** 结果应像真实印刷页面，而不是数字化单色滤镜。
3. **机械复制质感优先。** 照片要转成网点、颗粒、断裂高光、积墨和轻微套印偏移。
4. **留白参与叙事。** 空白纸面占画布的 25%–55%，用于控制阅读节奏。
5. **字体必须有张力。** 最大文字是微型文字的 5–12 倍，全图不超过三种字体声音。
6. **主体身份保持不变。** 用户提供的人物、物件和场景必须可辨认。
7. **参考图是语法，不是模板。** 相对每张参考图，至少改变四个结构变量。

## 不做这些

- 不是给全彩照片套一个单色滤镜
- 不是光滑样机、3D 渲染、渐变海报或电影感场景
- 不是居中模板、卡片网格、贴纸拼贴或装饰色块系统
- 不是密集的剪贴簿 Grunge 或撕纸风格
- 不写营销文案，不虚构品牌、赞助商、网址或二维码
- 不复刻参考海报，也不模仿艺术家签名

## 安装

克隆到 Claude Code 的 skills 目录：

```bash
git clone https://github.com/yanliudesign/monocolor.git \
  ~/.claude/skills/mono-color
```

安装后重启 Claude Code。其他 Agent 环境可以直接把 [`SKILL.md`](./SKILL.md) 作为 skill 入口加载。

## 试一试

```text
用 mono-color 做一张关于凌晨便利店的竖版海报，文案是“still open”。
```

```text
把这张人物照片做成钴蓝单色编辑 Zine 封面，保留人物身份和表情。
```

```text
做一张蕨类植物主题的绿色孔版观察笔记，标题是“field note 07”。
```

## 交付格式

每次运行返回：

1. 在有图像生成工具时生成一张位图；
2. 实际使用的完整生产级 Prompt；
3. 一份配方说明，列出油墨、版式家族、字体搭配、印刷工艺与原创性变化。

如果当前环境不能生成图像，skill 会明确说明限制，并提供可直接使用的生产级 Prompt。

## 仓库结构

```text
monocolor/
├── SKILL.md          # 触发规则、视觉系统、工作流与质量门槛
├── README.md         # 英文说明
├── README.zh.md      # 中文说明
└── evals/
    └── evals.json    # 典型触发语与预期输出
```

## 原创性

这个 skill 提取的是配色、印刷工艺、空间密度、字体层级和沟通语气等系统特征。它不会复制参考图的构图、文案、标签、Logo、边框系统或标志性排列。

当用户提供照片时，主体身份会被保留，但裁切、网点、网格、文字位置和信息标注都会重新设计。

---

Created by [Dreameryanyan](https://www.linkedin.com/in/yanliudesign/) · [LinkedIn](https://www.linkedin.com/in/yanliudesign/) · [X](https://x.com/yanliudreamer)