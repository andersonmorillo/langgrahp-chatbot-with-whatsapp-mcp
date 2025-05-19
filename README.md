# LangGraph WhatsApp Chatbot

A WhatsApp chatbot built with LangGraph, FastAPI, and Twilio that can handle both text and image responses.

## Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose (for containerized setup)
- A Twilio account with WhatsApp enabled
- A Tavily API key
- An Ngrok account (for exposing your local server)

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env


# Tavily API Key
TAVILY_API_KEY=your_tavily_api_key

# Ngrok Configuration
NGROK_AUTHTOKEN=your_ngrok_auth_token
HOST=your-reserved-domain.ngrok.io
```

## Running with Docker Compose

1. Build and start the services:
```bash
docker-compose up --build
```

This will start:
- MCP Server (port 8001)
- WhatsApp Bot (port 8000)
- Ngrok tunnel (port 4040)

## Running Manually

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the MCP server:
```bash
python mcp_server.py
```

3. In a new terminal, start the WhatsApp bot:
```bash
python whatsapp_chatbot_client.py
```

4. In another terminal, start ngrok:
```bash
ngrok http 8000
```

## Testing the Bot

1. Configure your Twilio WhatsApp sandbox:
   - Go to your Twilio Console
   - Navigate to Messaging > Try it out > Send a WhatsApp message
   - Set the webhook URL to your ngrok URL + `/whatsapp`
   - Example: `https://your-domain.ngrok.io/whatsapp`

2. Send a test message to your WhatsApp bot:
   - Text: "Hello"
   - The bot should respond with a message

## Project Structure

```
.
├── docker-compose.yml    # Docker services configuration
├── Dockerfile           # Container definition
├── requirements.txt     # Python dependencies
├── .env                # Environment variables
├── mcp_server.py       # MCP server implementation
├── whatsapp_chatbot_client.py  # WhatsApp bot implementation
└── graph.py            # LangGraph agent configuration
```

## Features

- WhatsApp integration via Twilio
- LangGraph agent for intelligent responses
- Support for both text and image responses
- Docker containerization for easy deployment
- Ngrok integration for exposing local server

## Troubleshooting

1. If you get authentication errors:
   - Verify your Twilio credentials in the `.env` file
   - Check if your Twilio account is active
   - Ensure your WhatsApp sandbox is properly configured

2. If the bot doesn't respond:
   - Check if all services are running
   - Verify the ngrok tunnel is active
   - Check the logs for any error messages

3. If Docker services fail to start:
   - Ensure Docker and Docker Compose are installed
   - Check if ports 8000, 8001, and 4040 are available
   - Verify your `.env` file is properly configured

## Contributing

Feel free to submit issues and enhancement requests!
