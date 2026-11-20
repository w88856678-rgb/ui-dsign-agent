---
name: ui-dsign-agent
license: MIT
description: Design or refine mobile and web UI from a brief, reference screenshot, wireframe, or Figma file. Use for multi-screen visual consistency, UI asset prompting, design-to-implementation handoff, or a focused visual review.
---

# UI DSign Agent

## 把要求写成可检查的设计约束

- 明确用户要交付的是线框、视觉稿、可编辑的 Figma 文件还是可运行的界面。记录目标平台、关键用户任务、页面清单和首要操作。已有产品先读设计系统、实际页面和组件状态。
- 多屏任务先约定共用规则，包括颜色角色、字级、间距、圆角、图标风格和控件状态，再逐屏写模块、顺序、文案、操作和状态差异。可以先做代表性页面来验证规则。
- 从参考截图提炼布局、信息权重、平台控件和视觉特征。多张参考图分别标注控制项，例如图 1 决定页面结构，图 2 只提供配色。改稿按区域明确要保留的内容和要修改的变量。

## 按任务选用专长

只在阶段需要且技能可用时调用。已有项目的框架、组件库和设计约束优先。

| 需求 | 可用 Skill |
|---|---|
| 新设计的整体方向、布局和 UX | `ui-ux-pro-max` |
| iOS、Android 页面结构和控件 | `mobile-app-design` |
| Web 信息层级、排版和前端实现 | `frontend-design` |
| 官网、落地页的主题和页面结构 | `hallmark` |
| 配色、光影和材质打磨 | `design-taste-frontend` |
| 同一图标库内搜索并取 SVG | `better-icons` |
| 已使用或指定 shadcn/ui 的项目 | `shadcn-ui` |
| 视觉审计与界面收尾 | `impeccable` |
| Web 规范和无障碍验收 | `web-design-guidelines`、`web-accessibility` |

多屏从线框开始时，先验证整套布局，再调整目标平台的排版、颜色和光影，最后做质检。只做局部修改时，直接进入对应阶段。做网页 3D 首屏时，选用 `threejs-fundamentals`、`threejs-animation` 或 `threejs-react-three-fiber`。做商品模型嵌入时，参考 `web3d-model-viewer`。

## 生成素材与交付

需要概念图、活动主视觉、3D 图标、IP、艺术标题字或循环微动时，读取 [视觉提示词参考](references/visual-prompts.md)。概念图可用于确认方向。需要可编辑稿或代码时，用独立文字、组件和素材重建可交互的界面。

交付前按实际范围核对。有多屏时验证组件和状态的一致性。有实现时在典型视口检查版式、主要交互、键盘焦点和对比度。涉及异步数据时覆盖实际出现的加载、空、失败和完成状态。
