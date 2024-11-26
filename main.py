# src/main.py
from cocotst.app import Cocotst
from cocotst.network.model import WebHookConfig
from creart import it
from graia.saya import Saya
from graia.saya.builtins.broadcast import BroadcastBehaviour

app = Cocotst(
    appid="", # 你的 APPID
    clientSecret="", # 你的 ClientSecret
    webhook_config=WebHookConfig(host="127.0.0.1", port=2099), # 你的 WebHook 配置
    is_sand_box=True,
)

# 创建 Saya 实例
saya = it(Saya)
# 安装 BroadcastBehaviour
saya.install_behaviours(BroadcastBehaviour(broadcast=app.broadcast))

# 使用 Saya 的模块上下文管理器加载插件
with saya.module_context():
    # 加载插件
    saya.require("module.ping")

if __name__ == "__main__":
    app.launch_blocking()