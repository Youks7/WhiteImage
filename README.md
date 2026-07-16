# KeRo Sunglasses White Background Skill

面向墨镜、眼镜电商商品图的 Codex 批量白底精修 Skill。

它使用 Codex 内置图像生成/图像编辑能力逐张处理原图，重点解决：

- 镜片灰尘、污点、划痕、光带及环境/灯具倒影；
- 黄色透明、黑灰透明、银色及彩色偏光镜片的原色与透明度保护；
- 均匀纯白背景和主体下方商品倒影清除；
- 镜框、镜腿、铰链、开孔、角度、构图和商品比例锁定；
- 递归目录、PNG 命名、数量、尺寸和文件可读性核验。

## 核心原则

每张输入原图是该商品结构、可见镜片颜色、透明度、拍摄角度和构图的唯一依据。确认样图和其他参考图只提供镜片洁净度、白底、清晰度及主体下方处理标准，不能提供其他商品的颜色或结构。

本地脚本只允许用于建立清单、目录、复制、命名和检查结果，不用于抠图、阈值换色或重绘商品。

## 安装

### 从 GitHub 安装

在 Codex 新任务中发送：

```text
请使用 $skill-installer，从公开 GitHub 仓库
https://github.com/Youks7/KeRo-Sunglasses-White-Background-Skill
的 main 分支安装：
skills/refine-sunglasses-white-background

安装后检查 SKILL.md、agents/openai.yaml、references 和 scripts 是否完整。
```

### 导入独立安装包

下载并导入：

[`packages/refine-sunglasses-white-background.skill`](./packages/refine-sunglasses-white-background.skill)

## 使用

安装后在新任务中调用：

```text
使用 $refine-sunglasses-white-background 批量精修墨镜白底图。

输入目录：[原图目录]
输出目录：[输出目录]
合格效果参考目录：[参考目录]

先递归统计图片并处理一张代表样图，等我确认后再完成剩余图片。
每张原图决定自己的款式、颜色、透明度、角度和构图。
```

Skill 默认采用保守提速：样图及各镜片类型颜色校准通过后，最多同时处理两张；每张仍使用独立原图、独立编辑调用和逐张视觉验收。

## 目录结构

```text
skills/
└── refine-sunglasses-white-background/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    │   ├── prompt-templates.md
    │   └── quality-standard.md
    └── scripts/check_batch.ps1

packages/
└── refine-sunglasses-white-background.skill
```

## 构建安装包

```powershell
python scripts/build_package.py
```

构建脚本会生成确定性的 `.skill` 压缩包和 `packages/SHA256SUMS.txt`。
