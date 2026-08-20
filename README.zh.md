<div align="center">

**中文** · [English](./README.md)

# 单色编辑印刷

**为海报、Zine、肖像、包装与视觉观察笔记而生的单色 / 受控双色编辑图像 Skill。**

[![Version](https://img.shields.io/badge/VERSION-1.1.0-2ea44f?style=flat-square&labelColor=333)](./SKILL.md)
[![Skills](https://img.shields.io/badge/SKILLS-1-2ea44f?style=flat-square&labelColor=333)](./SKILL.md)
[![Stars](https://img.shields.io/github/stars/yanliudesign/mono-color-skill?style=flat-square&label=STARS&color=e37f2c&labelColor=333)](https://github.com/yanliudesign/mono-color-skill/stargazers)

[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-d97757?style=flat-square&labelColor=1a1a1a&logo=anthropic&logoColor=white)](https://claude.ai/code)
[![SKILL.md](https://img.shields.io/badge/Agent-SKILL.md-214f9b?style=flat-square&labelColor=1a1a1a)](./SKILL.md)

</div>

把一个主题、一句话、一个物件或一张照片，转成原创的编辑印刷作品。Skill 默认使用单色；当内容需要信息分层、物件对照或叠印张力时，进入受控双色分支。暖色纸张、网点图像、主动留白与强烈字体对比，让两种模式保持同一套视觉识别。

它保留的是一套视觉系统，而不是照抄参考图。每次构图都会根据主体、意图、文字和图像角色重新建立。

## 视觉参考

| 01 | 02 | 03 |
|:---:|:---:|:---:|
| <img src="./examples/reference-01.png" alt="单色编辑印刷视觉参考 01" width="280"> | <img src="./examples/reference-02.png" alt="单色编辑印刷视觉参考 02" width="280"> | <img src="./examples/reference-03.png" alt="单色编辑印刷视觉参考 03" width="280"> |
| 04 | 05 | 06 |
| <img src="./examples/reference-04.png" alt="单色编辑印刷视觉参考 04" width="280"> | <img src="./examples/reference-05.png" alt="单色编辑印刷视觉参考 05" width="280"> | <img src="./examples/reference-06.png" alt="单色编辑印刷视觉参考 06" width="280"> |
| 07 | 08 | 09 |
| <img src="./examples/reference-07.png" alt="单色编辑印刷视觉参考 07" width="280"> | <img src="./examples/reference-08.png" alt="单色编辑印刷视觉参考 08" width="280"> | <img src="./examples/reference-09.png" alt="单色编辑印刷视觉参考 09" width="280"> |
| 10 | 11 | 12 |
| <img src="./examples/reference-10.png" alt="单色编辑印刷视觉参考 10" width="280"> | <img src="./examples/reference-11.jpg" alt="单色编辑印刷视觉参考 11" width="280"> | <img src="./examples/reference-12.jpg" alt="单色编辑印刷视觉参考 12" width="280"> |

这组图片用于界定视觉方向，不是供复刻的固定构图。每次新作品都会从头建立主体、裁切、网格、字体层级与印刷处理。

## 它能做什么

| 系统 | 方向 |
|---|---|
| **输入** | 主题、短句、物件、文章想法或用户提供的照片 |
| **配色** | 暖色非涂布纸 + 默认一种油墨，或九组受控双色配方之一 |
| **模式** | 纯单色、彩色 + 黑墨、互补双色或叠印双色 |
| **图像** | 网点、孔版颗粒、蓝晒曝光感或复印机破碎质感 |
| **留白** | 25%–55% 可见纸面，采用非对称编辑网格 |
| **字体** | 编辑感衬线字体 + 窄体无衬线或等宽功能字体 |
| **输出** | 生成位图、完整生产 Prompt 与简短配方说明 |

## 工作方式

```text
1  读取输入      →  确定主体、意图、文字与图像角色
2  选择版式      →  图像、标本、文字宣言、物件场、叠印拼贴、编辑日志或封面
3  分配印版      →  默认单色；使用双色时为每块印版指定明确职责
4  组织画面      →  保留 25%–55% 留白，并加入一个有意的打破点
5  生成并检查    →  核对油墨数量、主体身份、层级、材质与原创性
```

## 油墨系统

**单色主题：**钴蓝、皇家蓝、植物绿、薄荷绿、陶土橙、信号红、茄紫与炭黑。

| 图例 | 油墨 | Hex |
|---|---|---|
| ![钴蓝](https://img.shields.io/badge/■■■■-2148B8?style=flat-square&labelColor=2148B8&color=2148B8) | 钴蓝 / 群青 | `#2148B8` |
| ![皇家蓝](https://img.shields.io/badge/■■■■-2058D4?style=flat-square&labelColor=2058D4&color=2058D4) | 皇家蓝 | `#2058D4` |
| ![植物绿](https://img.shields.io/badge/■■■■-008A4B?style=flat-square&labelColor=008A4B&color=008A4B) | 植物绿 | `#008A4B` |
| ![薄荷绿](https://img.shields.io/badge/■■■■-5EB783?style=flat-square&labelColor=5EB783&color=5EB783) | 薄荷绿 | `#5EB783` |
| ![陶土橙](https://img.shields.io/badge/■■■■-C65F38?style=flat-square&labelColor=C65F38&color=C65F38) | 陶土橙 | `#C65F38` |
| ![信号红](https://img.shields.io/badge/■■■■-C83232?style=flat-square&labelColor=C83232&color=C83232) | 信号红 | `#C83232` |
| ![茄紫](https://img.shields.io/badge/■■■■-63365F?style=flat-square&labelColor=63365F&color=63365F) | 茄紫 | `#63365F` |
| ![炭黑](https://img.shields.io/badge/■■■■-30343A?style=flat-square&labelColor=30343A&color=30343A) | 炭黑 | `#30343A` |

**双色配方：**粉蓝 + 信号红、钴蓝 + 陶土橙、植物绿 + 酒红、炭黑 + 信号红、电光蓝 + 碳黑、薄荷绿 + 炭黑、群青 + 安全橙、青蓝 + 砖红、橘色 + 灰蓝。

| 图例 | 双色配方 | Hex |
|---|---|---|
| ![粉蓝](https://img.shields.io/badge/■-9EB8D3?style=flat-square&labelColor=9EB8D3&color=9EB8D3) ![信号红](https://img.shields.io/badge/■-C83232?style=flat-square&labelColor=C83232&color=C83232) | 粉蓝 + 信号红 | `#9EB8D3` + `#C83232` |
| ![钴蓝](https://img.shields.io/badge/■-2148B8?style=flat-square&labelColor=2148B8&color=2148B8) ![陶土橙](https://img.shields.io/badge/■-C65F38?style=flat-square&labelColor=C65F38&color=C65F38) | 钴蓝 + 陶土橙 | `#2148B8` + `#C65F38` |
| ![植物绿](https://img.shields.io/badge/■-008A4B?style=flat-square&labelColor=008A4B&color=008A4B) ![酒红](https://img.shields.io/badge/■-8F3434?style=flat-square&labelColor=8F3434&color=8F3434) | 植物绿 + 酒红 | `#008A4B` + `#8F3434` |
| ![炭黑](https://img.shields.io/badge/■-30343A?style=flat-square&labelColor=30343A&color=30343A) ![信号红](https://img.shields.io/badge/■-C83232?style=flat-square&labelColor=C83232&color=C83232) | 炭黑 + 信号红 | `#30343A` + `#C83232` |
| ![电光蓝](https://img.shields.io/badge/■-173AE3?style=flat-square&labelColor=173AE3&color=173AE3) ![碳黑](https://img.shields.io/badge/■-242321?style=flat-square&labelColor=242321&color=242321) | 电光蓝 + 碳黑 | `#173AE3` + `#242321` |
| ![薄荷绿](https://img.shields.io/badge/■-5EB783?style=flat-square&labelColor=5EB783&color=5EB783) ![炭黑](https://img.shields.io/badge/■-302D2E?style=flat-square&labelColor=302D2E&color=302D2E) | 薄荷绿 + 炭黑 | `#5EB783` + `#302D2E` |
| ![群青](https://img.shields.io/badge/■-263E99?style=flat-square&labelColor=263E99&color=263E99) ![安全橙](https://img.shields.io/badge/■-E55D2B?style=flat-square&labelColor=E55D2B&color=E55D2B) | 群青 + 安全橙 | `#263E99` + `#E55D2B` |
| ![青蓝](https://img.shields.io/badge/■-159DDA?style=flat-square&labelColor=159DDA&color=159DDA) ![砖红](https://img.shields.io/badge/■-B64032?style=flat-square&labelColor=B64032&color=B64032) | 青蓝 + 砖红 | `#159DDA` + `#B64032` |
| ![橘色](https://img.shields.io/badge/■-E46C2D?style=flat-square&labelColor=E46C2D&color=E46C2D) ![灰蓝](https://img.shields.io/badge/■-4773A5?style=flat-square&labelColor=4773A5&color=4773A5) | 橘色 + 灰蓝 | `#E46C2D` + `#4773A5` |

双色作品通常由主墨承担 70%–85% 的印刷面积，辅墨承担 15%–30%，并只负责日期、注释、特定物件或叠印交叉等明确任务。纸色不算第三色，两块印版重叠后形成的深色也不算第三种油墨。

## 视觉规则

1. **最多使用两种印刷油墨。** 默认单色；双色必须有明确的印版职责与内容理由。
2. **纸张必须可见。** 结果应像真实印刷页面，而不是数字化单色滤镜。
3. **机械复制质感优先。** 照片要转成网点、颗粒、断裂高光、积墨和印版之间的轻微套印偏移。
4. **留白参与叙事。** 空白纸面占画布的 25%–55%，用于控制阅读节奏。
5. **字体必须有张力。** 最大文字是微型文字的 5–12 倍，全图不超过三种字体声音。
6. **主体身份保持不变。** 用户提供的人物、物件和场景必须可辨认。
7. **参考图是语法，不是模板。** 相对每张参考图，至少改变四个结构变量。

## 不做这些

- 不是给全彩照片套一个单色滤镜
- 不是随意的双色装饰，也不使用两块以上的印版
- 不是光滑样机、3D 渲染、渐变海报或电影感场景
- 不是居中模板、卡片网格、贴纸拼贴或装饰色块系统
- 不是密集的剪贴簿 Grunge 或撕纸风格
- 不写营销文案，不虚构品牌、赞助商、网址或二维码
- 不复刻参考海报，也不模仿艺术家签名

## 安装

克隆到 Claude Code 的 skills 目录：

```bash
git clone https://github.com/yanliudesign/mono-color-skill.git \
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

```text
用群青 + 安全橙做一张城市骑行叠印海报，让自行车与超大标题在局部交叉。
```

```text
把这个产品做成青蓝 + 砖红的重复物件封面，为标题和事实型小字保留一块空白区域。
```

## 交付格式

每次运行返回：

1. 在有图像生成工具时生成一张位图；
2. 实际使用的完整生产级 Prompt；
3. 一份配方说明，列出印刷模式、准确油墨配方、版式家族、字体搭配、印刷工艺与原创性变化。

如果当前环境不能生成图像，skill 会明确说明限制，并提供可直接使用的生产级 Prompt。

## 仓库结构

```text
mono-color-skill/
├── examples/         # README 中展示的视觉参考
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