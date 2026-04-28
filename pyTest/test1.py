from pyweixin import Navigator
from pyweixin.WeChatAuto import Messages

# 打开会话并发送
Messages.send_messages_to_friend(friend="易", messages=['测试1','测试2'], close_weixin=False)