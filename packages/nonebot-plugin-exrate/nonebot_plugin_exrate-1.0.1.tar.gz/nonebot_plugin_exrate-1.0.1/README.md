<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# nonebot-plugin-exrate

_✨ 一个Nonebot2插件用于查询各大银行的货币汇率✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/bankcarddev/nonebot-plugin-exrate.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-exrate">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-exrate.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>



</details>

## 📖 介绍

一个Nonebot2插件用于查询各大银行的货币汇率

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-exrate

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-exrate
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-exrate
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-exrate
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-exrate
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_exrate"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| exrate_appcode | 是 | 无 | 你的汇率查询appcode秘钥 |
> [!NOTE]
> ### 🔑 如何获取API Key？
>
> 前往以下页面申请API Key：
> [申请页面](https://market.aliyun.com/apimarket/detail/cmapi00063246#sku=yuncode5724600001)



## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| ex [银行代码] | 群员 | 是 | 全局 | 查询对应银行汇率 |


