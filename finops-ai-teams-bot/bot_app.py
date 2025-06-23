from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
from flask import Flask, request, Response
from teams_bot import FinOpsBot

app = Flask(__name__)
adapter_settings = BotFrameworkAdapterSettings("", "")
adapter = BotFrameworkAdapter(adapter_settings)
bot = FinOpsBot()

@app.route("/api/messages", methods=["POST"])
def messages():
    activity = Activity().deserialize(request.json)
    auth_header = request.headers.get("Authorization", "")
    async def aux():
        await adapter.process_activity(activity, auth_header, bot.on_turn)
        return Response(status=200)
    return aux()
