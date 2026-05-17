---
title: 中心四篇论文被CVPR及ACL 2026录用！
image: /images/posts/cover.webp
tags: 新闻
last_modified_at: ""
---

近日，计算机视觉与自然语言处理领域顶级国际会议 CVPR 2026 和 ACL 2026 论文录用结果相继揭晓，<!-- excerpt start -->华中科技大学霍普克罗夫特计算科学研究中心共有 4 篇论文被录用，其中 2 篇被 CVPR 2026 录用，2 篇被 ACL 2026 录用。<!-- excerpt end -->

## 会议情况

国际计算机视觉与模式识别会议（IEEE/CVF Conference on Computer Vision and Pattern Recognition，CVPR）是计算机视觉领域最具影响力的国际学术会议之一，也是中国计算机学会（CCF）推荐的 A 类国际学术会议。CVPR 2026 将于 2026 年 6 月 3 日至 7 日在美国科罗拉多州丹佛举行。本届会议共收到 16,092 篇投稿，最终 4,090 篇论文被主会录用，录用率为 25.42%。华中科技大学霍普克罗夫特计算科学研究中心有两篇论文被 CVPR 2026 录用。

### 01

**论文标题：** Anchoring the Mind of Multimodal Reasoners: Cognitive Bias as a Vector for Jailbreak Attacks (CVPR 2026)

**论文作者：** 丛林华（24级硕），司马丙瑞（24级博），何琨*（指导老师）

**论文概述：** 该工作从认知层面出发，提出并系统揭示了一类此前缺乏充分研究的安全问题：多模态大推理模型（Multimodal Large Reasoning Models, MLRMs）的安全判断会受到认知偏差的影响，并可能因此被系统性利用。具体而言，论文发现 MLRMs 在安全相关判断中存在明显的锚定效应，即最先接收到的信息会对后续判断产生不成比例的影响，并持续偏置其后续推理。

基于这一发现，论文提出 RA-Attack（Reasoning-chain Anchoring Attack）。其核心思路是在跨模态输入中先构造一个结构化视觉安全锚点：使用一张与有害主题相关、但内容本身安全的思维导图，配合文本安全锚点与后续有害意图引导，预先为模型建立一个带有「安全」偏置的认知起点。由于思维导图的层次化视觉结构与 MLRMs 渐进式、路径依赖的推理过程高度契合，因此后续风险意图更容易被模型理解为既有安全推理链的自然延伸。

实验结果表明，结构化思维导图锚点优于普通安全场景图片；即便将思维导图替换为通过 OCR 提取、并尽可能保留层级关系的文本版本，其效果仍弱于原始视觉思维导图版本，说明视觉结构化锚点比非结构化安全图片、也比文本层级结构更能有效偏置模型判断。RA-Attack 在 7 个主流闭源和开源模型上均展现出显著攻击效果，例如在 GPT-4o 上达到 82%，在 Gemini-2.5-Pro 上达到 92% 的攻击成功率。与此同时，论文还提出锚点去偏提示（ADP）这一轻量级防御方法，能够在基本不损害模型通用能力的同时显著降低攻击成功率。整体来看，该工作表明，认知安全应成为多模态大推理模型安全研究中的一个关键议题。

<div align="center">
  <img src="/images/posts/2026-05-17-cvpr-acl-accepted-papers/ra_attack_framework.png" alt="RA-Attack整体框架图" style="max-width: 600px; width: 100%; height: auto;">
  <p class="center">图1：RA-Attack整体框架图</p>
</div>

### 02

**论文标题：** KVSmooth: Mitigating Hallucination in Multi-modal Large Language Models through Key-Value Smoothing (CVPR 2026)

**论文作者：** 姜丝雨（24级博），陈飞扬（24级硕），张晓今，何琨*（指导老师）

**论文概述：** 多模态大语言模型（MLLM）在图文理解和生成等任务上取得了显著进展，但幻觉现象——生成与图像不一致的对象、属性或关系——仍是其可靠应用的一大障碍。与纯语言模型不同，MLLM 需要在生成过程中紧密依赖视觉信息，但随着解码进行，早期视觉信息在隐藏状态中的影响会逐渐减弱，导致语义漂移，使生成文本逐渐偏离图像内容。

针对这一问题，本文提出了一种无需训练、即插即用的轻量方法 KVSmooth。该方法通过对 KV-Cache 中的 key 和 value 进行指数移动平均（EMA）平滑，同时根据每个 token 的注意力行熵动态调整平滑强度，从而有效抑制隐藏状态的剧烈变化和幻觉生成。

实验结果表明，KVSmooth 在多项基准测试中显著降低了幻觉现象，例如 CHAIRS 指标由 41.8 降至 18.2，同时整体生成性能也得到提升，F1 分数由 77.5 提升至 79.2。该方法在保持精确率和召回率平衡的同时，验证了其有效性与通用性，为安全可靠的多模态生成提供了新的思路。

<div align="center">
  <img src="/images/posts/2026-05-17-cvpr-acl-accepted-papers/kvsmooth_comparison.png" alt="KVSmooth效果对比图" style="max-width: 600px; width: 100%; height: auto;">
  <p class="center">图2：KVSmooth效果对比图</p>
</div>

## 会议情况

国际计算语言学协会年会（Annual Meeting of the Association for Computational Linguistics，ACL）是自然语言处理与计算语言学领域最具影响力的国际学术会议之一，也是中国计算机学会（CCF）推荐的 A 类会议。ACL 2026 将于 2026 年 7 月 2 日至 7 日在美国加利福尼亚州圣地亚哥召开。这次 ACL 2026 共有 12,148 篇投稿，最终 2308 篇被主会录用（录用率 19%）+ 2186 篇论文被 Findings 录用（录取率 18%）。华中科技大学霍普克罗夫特计算科学研究中心有两篇论文被 ACL 2026 录用。

### 03

**论文标题：** Mitigating Safety Context Amnesia in Multimodal Reasoning Models via Intent-Guided Safety Reasoning (ACL 2026)

**论文作者：** 董锡耀（24级博），程广圣（25级硕），陈奕龙（25级硕），张晓今（指导老师），何琨*（指导老师）

**论文概述：** 随着多模态大推理模型不断发展，模型不仅「看得见、答得出」，也越来越擅长进行复杂链式推理。但能力增强的同时，也带来了更隐蔽的安全风险。该工作发现，当有害目标被包装在看似正常、合理的图文上下文中时，模型虽然能够感知潜在风险线索，却往往会在后续推理过程中被「表面合理性」牵引，逐渐忽视原本应当坚持的安全约束。论文将这一现象定义为安全上下文遗忘（Safety Context Amnesia, SCA）。

针对这一问题，论文提出了一种新的推理时防御框架 IGSR（Intent-Guided Safety Reasoning）。其核心思想是：在模型真正开始回答之前，先将输入中的「表层良性意图」与「潜在风险意图」显式拆分出来，再通过专门的安全仲裁机制判断当前请求是否会触发风险，从而避免模型在推理链条中被「看似无害」的上下文误导。为支撑这一框架，作者基于 VLGuard 和 SPA-VL 中的图文样本，借助教师模型自动构建了带有「良性意图—风险意图」双路径标注的结构化数据集，共包含 3881 条样本，其中包括 977 条 helpfulness 样本和 2904 条 safety 样本。

实验结果表明，IGSR 在 VLSBench、MM-SafetyBench 和 HADES 等多个多模态安全基准上，对 6 个开源模型和 3 个闭源模型均表现出稳定优势。相较现有基线方法，整体防御成功率提升 62% 以上；在 VLSBench 上平均带来约 48% 的防御增益；在闭源模型 GPT-4o 上，防御成功率可由 43.33% 提升至 81.33%；在高难度基准 HADES 上，LLaMA3.2-V 的防御成功率可由 4.67% 提升至 72.67%。同时，IGSR 在 MM-Vet 上仍较好保持了模型的通用能力，说明其并不是以牺牲可用性为代价换取安全性。整体来看，该工作表明，多模态大模型的安全对齐需要进一步迈向一种结构化、证据驱动、可解释的安全推理范式。

<div align="center">
  <img src="/images/posts/2026-05-17-cvpr-acl-accepted-papers/igsr_framework.png" alt="IGSR整体框架图" style="max-width: 600px; width: 100%; height: auto;">
  <p class="center">图3：IGSR整体框架图</p>
</div>

### 04

**论文标题：** Latent Attention Denoising: A Training-Free Energy-Based Framework for Mitigating Hallucinations in Vision-Language Models (ACL 2026)

**论文作者：** 罗志文（22级本），姜丝雨（24级博），姜伟龙（23级硕），何琨*（指导老师）

**论文概述：** 该工作聚焦于大视觉语言模型（Large Vision-Language Models, LVLMs）中的视觉幻觉问题，提出了一种无需训练的推理时干预框架 Latent Attention Denoising（LAD），用于缓解模型在生成过程中出现的不忠实描述现象。论文指出，视觉幻觉问题的一个根源在于传统 softmax 注意力机制隐含地假设噪声满足独立同分布（i.i.d.），而真实的 LVLM 注意力模式往往存在明显的结构性与竞争性偏置，例如 attention sinks 等现象，这使得传统建模假设与实际分布之间产生失配。

针对这一问题，作者将注意力校准过程重新建模为一步式基于 score 的去噪过程，并设计了具有良好可解释性的能量函数，用于解析刻画注意力 logits 的偏移方向。在此基础上，LAD 通过一次受 Langevin 动力学启发的更新，对受扰动的注意力 logits 进行主动校正，从而将模型生成过程引导至更加忠实于视觉输入的注意力配置。该方法无需额外训练，可直接应用于现有大视觉语言模型，计算开销几乎可以忽略，推理速度与标准贪心解码相当。

实验结果表明，LAD 在多种不同架构上均表现出良好的泛化能力，能够同时在生成类任务和判别类任务上有效缓解幻觉问题，并在保持高效推理的同时取得优异性能。这一工作为提升大视觉语言模型的可靠性与可解释性提供了新的思路。

<div align="center">
  <img src="/images/posts/2026-05-17-cvpr-acl-accepted-papers/lad_framework.png" alt="LAD整体框架图" style="max-width: 600px; width: 100%; height: auto;">
  <p class="center">图4：LAD整体框架图</p>
</div>
