# 需求

1.系统使用python语言开发，django框架等其他技术完成整体开发

2.系统分为三种角色，游客，普通用户和管理员，每个角色登录系统拥有不同得功能权限

3.游客直接访问系统，只能查看当前得所有农贸市场得摊位信息

4.普通用户可以注册也可登录系统，查看农贸市场摊位信息，也可以按照不同维度有条件得搜索摊位信息，
    比如可租赁/不可租赁/按照面积/价位/位置进行快速搜索，农场摊位列表拥有自动分页功能
    
5.普通用户可以预定，也可以退订摊位信息，也可以查看自己得摊位信息，可以修改自己得个人信息

6.普通用户可以查看当前租赁率最高的摊位信息（以折线图形式动态展示当前租赁排行前五得摊位信息）

7.管理员账户预设密码登录，可以对摊位信息增删改查操作

8.当普通用户退订摊位信息时，管理员需要审核

9.管理员可以查看当前用户得租赁情况，以及用户得详细信息，可以更改当前租赁率最高得摊位信息

10.系统使用纯英文开发，预计开发周期（3-4周），可根据情况加急

补充功能：
1.就是在用户点击确认租摊位之前，得有一个合同，让用户浏览后，才可以确认租摊位，用户确认后，管理员需要审核（选做），用户才可以租摊位；
合同里需要说明，有些摊位如果租赁中间由于特殊情况终止租赁，都要在合同里明确约定，就如同合同到期，不能及时离开一样，
在签订合同条款中都明确约定好，是管理员约定好的处理方式。如果用户特殊情况终止租赁，需要交一定的违约金才可以终止租赁；
如果用户的合同到期了，就要延期租赁并且支付延期的租金。

2.模拟支付功能，给一个二维码，下面点击一下支付，就算支付了。

# 相关账号

## 超级管理员
- admin
- admin123456

## 用户
- user1
- user123456

# 相关库

- django==2.2.5
- django-filter==2.2.4
