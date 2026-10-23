---
title: 首页
description: 华中科技大学霍普克罗夫特计算科学研究中心，由 John Hopcroft 教授领衔，开展人工智能与理论计算机科学研究、学术交流及人才培养。
---

# 华中科技大学John Hopcroft计算中心

华中科技大学霍普克罗夫特计算科学研究中心（Hopcroft Center on Computer Science，HCCS）依托计算机科学与技术学院建设，由图灵奖得主 John Hopcroft 教授担任主任，何琨教授担任执行主任。中心致力于人工智能与理论计算机科学的基础研究和人才培养，研究方向涵盖可信人工智能、智能优化与决策、机器学习、计算机视觉、自然语言处理及 AI4Science。

{% include section.html %}

## 最新动态

{% assign latest_posts = site.posts | sort: "date" | reverse | slice: 0, 3 %}
{% for post in latest_posts %}
  {% include post-excerpt.html lookup=post.slug %}
{% endfor %}

{% include button.html link="/news/" text="查看全部动态" icon="fa-solid fa-arrow-right" flip=true style="bare" %}
{% include button.html link="/enrollment/" text="了解招生与申请" icon="fa-solid fa-user-graduate" style="bare" %}

{% include section.html %}

## 中心建设

{% capture text %}

中心在计算科学理论与算法、智能科学与技术等领域取得了一系列重要成果，在国际顶级期刊和会议上发表高质量学术论文，承担国家重大科研项目，致力于推动计算科学理论与应用的创新发展。

{%
  include button.html
  link="research"
  text="查看研究成果"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/covers/NAGphormer.png"
  link="research"
  title="研究成果"
  text=text
%}

{% capture text %}

中心定期举办学术讲座、研讨会和各类学术交流活动，积极参与国内外学术合作与交流，推动学科交叉与创新发展。中心成员在科研、教学、社会服务等方面不断取得新进展，相关动态和成果将持续更新，欢迎关注我们的最新消息。

{%
  include button.html
  link="/news/"
  text="查看中心动态"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/posts/2025-06-08-teacher-recruitment/image_1.png"
  link="/news/"
  title="中心动态"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

中心拥有一支由知名教授、青年学者、博士后、博士生和硕士生组成的高水平人才队伍。中心注重人才的引进与培养，鼓励学术创新与合作交流，为成员提供良好的学术环境和发展平台，致力于打造具有国际影响力的研究团队。

{%
  include button.html
  link="team"
  text="查看人才队伍"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/members/team_photos/team_photo_2025_10_09.jpg"
  link="team"
  title="人才队伍"
  text=text
%}
