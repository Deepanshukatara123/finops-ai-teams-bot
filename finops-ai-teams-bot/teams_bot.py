from botbuilder.core import TurnContext, ActivityHandler
from botbuilder.schema import Activity, ActivityTypes
from finops_tools import analyze_usage
from report_agent import summarize_with_gpt

class FinOpsBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_input = turn_context.activity.text.strip().lower()

        if "underutilized" in user_input:
            usage_data = analyze_usage()
            summary = summarize_with_gpt(usage_data)
            await turn_context.send_activity(Activity(
                type=ActivityTypes.message,
                text=summary
            ))
        else:
            await turn_context.send_activity("Hi! Ask me something like 'show underutilized resources'.")
