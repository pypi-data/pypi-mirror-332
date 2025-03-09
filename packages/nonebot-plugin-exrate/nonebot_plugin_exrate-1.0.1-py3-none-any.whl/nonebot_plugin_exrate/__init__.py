from nonebot import get_plugin_config, on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.log import logger
from typing import Dict, Optional
import httpx
import json
from nonebot.plugin import PluginMetadata



from .config import Config

__plugin_meta__ = PluginMetadata(
    name="汇率查询",
    description="用于查询各大银行的货币汇率，进行货币转换",
    homepage="https://github.com/bankcarddev/nonebot-plugin-exrate",
    usage="/ex [银行代码]",
    type="application",
    config=Config,
)

config = get_plugin_config(Config)


BANK_MAPPING = {
    "ICBC": ("ICBC", "工商银行", "工行"),
    "BOC": ("BOC", "中国银行", "中行"),
    "ABCHINA": ("ABCHINA", "农业银行", "农行"),
    "BANKCOMM": ("BANKCOMM", "交通银行", "交行"),
    "CCB": ("CCB", "建设银行", "建行"),
    "CMBCHINA": ("CMBCHINA", "招商银行", "招行"),
    "CEBBANK": ("CEBBANK", "光大银行", "光大"),
    "SPDB": ("SPDB", "浦发银行", "浦发"),
    "CIB": ("CIB", "兴业银行", "兴业"),
    "ECITIC": ("ECITIC", "中信银行", "中信")
}


BANK_ALIAS_MAP = {}
for code, names in BANK_MAPPING.items():
    for name in names[1:]:  
        BANK_ALIAS_MAP[name] = code

ex_rate = on_command("ex", aliases={"汇率", "查汇率"}, priority=5, block=True)

def get_bank_code(input_str: str) -> str | None:


    if input_str.upper() in BANK_MAPPING:
        return input_str.upper()
    

    return BANK_ALIAS_MAP.get(input_str.strip())

async def fetch_exchange_rate(bank_code: str) -> tuple[dict | None, str]:

    url = "https://tysjhlcx.market.alicloudapi.com/exchange_rate/top10"
    headers = {"Authorization": f"APPCODE {config.exrate_appcode}"}
    
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(
                url,
                params={"bankCode": bank_code},
                headers=headers
            )
            
            if response.status_code != 200:
                return None, f"API请求失败，状态码：{response.status_code}"
            
            data = response.json()
            if not data.get("success") or data["data"]["ret_code"] != "0":
                return None, data.get("msg", "接口返回数据异常")
            
            return data["data"], None
            
    except httpx.TimeoutException:
        return None, "请求超时，请稍后再试"
    except httpx.HTTPError as e:
        return None, f"网络请求失败：{str(e)}"
    except json.JSONDecodeError:
        return None, "接口返回数据解析失败"
def format_currency(price: str) -> str:
    if price == "" or price == "--":
        return "暂无"
    return f"{float(price):.4f}".rstrip('0').rstrip('.')


def format_rate_message(bank_code: str, rate_data: dict) -> Message:
    """生成格式化消息"""
    bank_name = BANK_MAPPING[bank_code][1]
    update_time = f"{rate_data['day']} {rate_data['time']}"
    
   
    content = [
        MessageSegment.text(f"🏦 {bank_name} 最新汇率\n"),
        MessageSegment.text(f"⏰ 更新时间：{update_time}\n"),
        MessageSegment.text("────────────────\n")
    ]
    
    for currency in rate_data["codeList"][:10]: 
        name = currency["name"] or currency["code"]
        line = (
            f"🌍 {name}({currency['code']})\n"
            f"  现汇买入：{format_currency(currency['hui_in'])}\n"
            f"  现钞买入：{format_currency(currency['chao_in'])}\n"
            f"  现汇卖出：{format_currency(currency['hui_out'])}\n"
            f"  现钞卖出：{format_currency(currency['chao_out'])}\n"
        )
        content.append(MessageSegment.text(line + "────────────────\n"))
    
    content.append(MessageSegment.text("💡 数据单位：100外币兑人民币元"))
    return Message(content)

@ex_rate.handle()
async def handle_ex_rate(args: Message = CommandArg()):
    input_bank = args.extract_plain_text().strip()
    if not input_bank:
        banks = "\n".join([f"- {names[1]} ({names[0]})" for names in BANK_MAPPING.values()])
        await ex_rate.finish(
            "请指定银行名称或代码，例如：\n"
            "/ex 工行\n/ex ICBC\n\n"
            "支持银行列表：\n" + banks
        )
    

    bank_code = get_bank_code(input_bank)
    if not bank_code:
        await ex_rate.finish("未找到对应的银行，请输入以下有效名称：\n" + 
                           "\n".join([f"{names[1]} ({names[0]})" for names in BANK_MAPPING.values()]))
    

    rate_data, error = await fetch_exchange_rate(bank_code)
    if error:
        await ex_rate.finish(f"❌ 获取汇率失败：{error}")
    

    message = format_rate_message(bank_code, rate_data)
    await ex_rate.finish(message)