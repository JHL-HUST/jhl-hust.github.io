---
title: 人才队伍
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}人才队伍

华中科技大学John Hopcroft计算中心汇聚了计算机科学领域的顶尖学者和青年才俊。中心由图灵奖得主John Hopcroft教授领衔，何琨教授担任执行主任，在理论计算机科学、算法设计、机器学习、数据挖掘、人工智能等前沿领域开展深度研究。团队在国际顶级期刊和会议上持续产出高质量成果，承担多项国家重大科研项目，致力于计算科学理论与应用的创新突破。

中心秉承"引育并举、开放包容"的人才理念，为每一位成员提供国际化的学术平台和广阔的发展空间，着力打造具有全球影响力的高水平研究团队。

# {% include icon.html icon="fa-regular fa-user" %}中心主任

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}

# {% include icon.html icon="fa-regular fa-user" %}教学科研人员

{% include list.html data="members" component="portrait" filter="role == 'researchers'" %}

# {% include icon.html icon="fa-regular fa-user" %}客座教授

{% include list.html data="members" component="portrait" filter="role == 'vp'" %}

# {% include icon.html icon="fa-regular fa-user" %}博士后

{% include list.html data="members" component="portrait" filter="role == 'postdoc'" %}

# {% include icon.html icon="fa-regular fa-user" %}博士生

{% include list.html data="members" component="portrait" filter="role == 'phd'" %}

# {% include icon.html icon="fa-regular fa-user" %}硕士生

{% include list.html data="members" component="portrait" filter="role == 'postgraduate'" %}

# {% include icon.html icon="fa-regular fa-user" %}本科生团队
{% include list.html data="members" component="portrait" filter="role == 'undergrad'" %}


{% include section.html background="images/background.png" dark=true %}

# {% include icon.html icon="fa-solid fa-camera" %}团队风采

中心团队不仅在学术研究方面展现出卓越的实力，更汇聚了一群充满激情与创造力的成员。我们注重团队协作与交流，定期组织学术研讨会、前沿讲座、学术沙龙以及丰富多彩的团队建设活动，促进成员间的思想碰撞与合作创新。开放包容的学术氛围让每一位成员都能充分发挥潜力，收获成长与友谊，共同推动中心不断迈向新的高峰。

{% include section.html %}

{% capture content %}

{% include figure.html image="images/members/team_photos/team_photo_1.png" %}
{% include figure.html image="images/members/team_photos/team_photo_2.png" %}
<!-- {% include figure.html image="images/members/team_photos/team_photo_3.png" %} -->
{% include figure.html image="images/members/team_photos/team_photo_2025_10_09_thumbnail.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
