from fastapi import FastAPI, Request, HTTPException
from twilio.twiml.messaging_response import MessagingResponse
from fastapi.responses import Response
from graph import make_graph
from pydantic import BaseModel
from typing import List
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


app = FastAPI()

# Singleton agent instance
_agent = None


async def get_agent():
    global _agent
    if _agent is None:
        _agent = await make_graph()
    return _agent


class ChatInput(BaseModel):
    messages: List[str]
    thread_id: str



@app.post("/whatsapp")
async def sms_reply(request: Request):
    """Respond to incoming messages with a simple text message."""
    form_data = await request.form()

    incoming_msg = form_data.get("Body", "")
    from_number = form_data.get("From", "")

    chat_input = ChatInput(messages=[incoming_msg], thread_id=from_number)

    # Get the singleton agent instance
    agent = await get_agent()

    config = {"configurable": {"thread_id": chat_input.thread_id}}
    response = await agent.ainvoke({"messages": chat_input.messages}, config=config)
    real_text = response["messages"][-1].content
    resp = MessagingResponse()

    msg = resp.message(real_text)

    return Response(content=str(resp), media_type="application/xml")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
