from cocotst.event.message import GroupMessage
from cocotst.message.parser.base import QCommandMatcher
from cocotst.network.model import Target
from cocotst.app import Cocotst
from cocotst.message.element import Voice
from graia.saya.builtins.broadcast.shortcut import listen, decorate

@listen(GroupMessage)
@decorate(QCommandMatcher("music"))
async def hello_listener(app: Cocotst, target: Target):
    await app.send_group_message(target, element=Voice(path="./BUDDIES.silk"))