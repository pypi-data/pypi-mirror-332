# PINAI Agent SDK Development Guide

## Introduction

PINAI Agent SDK is a powerful toolkit that allows developers to quickly create and deploy intelligent agents. This guide will help you get started and provide best practices and API references.

## Installation

```bash
pip install pinai-agent-sdk
```

## Quick Start

Here are the basic steps to create a simple agent:

```python
import os
from pinai_agent_sdk import PINAIAgentSDK, AGENT_CATEGORY_SOCIAL

# Initialize the SDK client
API_KEY = os.environ.get("PINAI_API_KEY", "your_api_key_here")
# For blockchain integration (optional)
PRIVATE_KEY = os.environ.get("ETHEREUM_PRIVATE_KEY")
RPC_URL = os.environ.get("BLOCKCHAIN_RPC_URL", "https://sepolia.base.org")

client = PINAIAgentSDK(api_key=API_KEY)

# Define message handling function
def handle_message(message):
    """
    Process incoming messages and respond
    
    Args:
        message (dict): Message object with format:
            {
                "session_id": "unique-session-id",
                "id": 12345,  # Message ID
                "content": "user message text",
                "created_at": "2023-01-01T12:00:00"
            }
    """
    print(f"Received: {message['content']}")

    session_id = message.get("session_id")
    if not session_id:
        print("Message missing session_id, cannot respond")
        return
    
    # Get user's message
    user_message = message.get("content", "")

    # Get persona info
    persona_info = client.get_persona(session_id)
    
    # Create your response (this is where your agent logic goes)
    response = f"Echo: {user_message}"
    
    # Send response back to user
    client.send_message(content=response)
    print(f"Sent: {response}")

# Register a new agent
agent_info = client.register_agent(
    name="My Hackathon Agent",
    description="A simple agent built during the hackathon",
    category=AGENT_CATEGORY_SOCIAL
)
agent_id = agent_info.get("id")
print(f"Agent registered with ID: {agent_id}")

# Start the agent and listen for messages
print("Starting agent... Press Ctrl+C to stop")
client.start_and_run(
    on_message_callback=handle_message,
    agent_id=agent_id
)
```

## Core Concepts

### Agent

An agent is the intelligent assistant you create that can interact with users. Each agent has a unique ID, name, description, and category.

### Session

A session represents a conversation with a user. Each session has a unique `session_id` used to track interactions with a specific user.

### Message

A message is the unit of information exchanged between the agent and users. Messages can contain text content and media (images, videos, audio, or files).

## Agent Categories

PINAI platform supports the following agent categories:

| Category Constant | Display Name | Description |
|---------|---------|------|
| `AGENT_CATEGORY_SOCIAL` | Social | Social agents |
| `AGENT_CATEGORY_DAILY` | Daily Life/Utility | Daily life and utility agents |
| `AGENT_CATEGORY_PRODUCTIVITY` | Productivity | Productivity tool agents |
| `AGENT_CATEGORY_WEB3` | Web3 | Web3-related agents |
| `AGENT_CATEGORY_SHOPPING` | Shopping | Shopping agents |
| `AGENT_CATEGORY_FINANCE` | Finance | Finance agents |
| `AGENT_CATEGORY_AI_CHAT` | AI Chat | AI chat agents |
| `AGENT_CATEGORY_OTHER` | Other | Other types of agents |

## API Reference

### Initializing the SDK

```python
from pinai_agent_sdk import PINAIAgentSDK

client = PINAIAgentSDK(
    api_key="your_api_key",  # Required: PINAI API key
    base_url="https://api.example.com",  # Optional: API base URL
    timeout=30,  # Optional: Request timeout in seconds
    polling_interval=1.0,  # Optional: Message polling interval in seconds
    privatekey="your_private_key",  # Optional: Ethereum private key for blockchain interactions
    blockchainRPC="https://sepolia.base.org"  # Optional: Blockchain RPC URL for on-chain agent registration
)
```

### Registering an Agent

```python
agent_info = client.register_agent(
    name="My Agent",  # Required: Agent name
    description="This is an example agent",  # Required: Agent description
    category=AGENT_CATEGORY_SOCIAL,  # Required: Agent category
    wallet="your_wallet_address",  # Optional: Wallet address
    cover="cover_image_url",  # Optional: Cover image URL
    metadata={"key": "value"},  # Optional: Additional metadata
    agent_owner="0x123..."  # Optional: Ethereum address of the agent owner (for blockchain registration)
)
```

### Unregistering an Agent

```python
result = client.unregister_agent(agent_id=123)
```

### Starting an Agent

```python
# Non-blocking mode
client._start(
    on_message_callback=handle_message,
    agent_id=123,
    blocking=False
)

# Blocking mode (until Ctrl+C)
client.start_and_run(
    on_message_callback=handle_message,
    agent_id=123
)
```

### Sending Messages

```python
response = client.send_message(
    content="Hello, world!",  # Required: Message content
    session_id="unique-session-id",  # Optional: Session ID
    media_type="image",  # Optional: Media type, default is "none"
    media_url="https://example.com/image.jpg",  # Optional: Media URL
    meta_data={"key": "value"}  # Optional: Additional metadata
)
```

### Getting User Information

```python
persona = client.get_persona(session_id="unique-session-id")
```

### Uploading Media

```python
media_info = client.upload_media(
    file_path="/path/to/image.jpg",  # File path
    media_type="image"  # Media type: "image", "video", "audio", "file"
)
media_url = media_info.get("url")
```

## Media Types and Limitations

| Media Type | Supported Extensions | Size Limit |
|---------|------------|---------|
| image | .jpg, .jpeg, .png, .gif, .webp | 10MB |
| video | .mp4, .webm, .mov | 100MB |
| audio | .mp3, .wav, .ogg | 50MB |
| file | .pdf, .txt, .zip, .docx | 20MB |

## Error Handling

The SDK provides various exception types to help handle different error scenarios:

- `AuthenticationError`: API authentication failure (401 errors)
- `PermissionError`: Insufficient permissions (403 errors)
- `ResourceNotFoundError`: Requested resource not found (404 errors)
- `ResourceConflictError`: Resource conflict (409 errors)
- `ValidationError`: Request validation failure (400 errors)
- `ServerError`: Server returns 5xx errors
- `NetworkError`: Network connection issues
- `Web3Error`: Blockchain interaction failures

Example:

```python
try:
    client.send_message(content="Hello")
except ValidationError as e:
    print(f"Validation error: {e}")
except AuthenticationError as e:
    print(f"Authentication error: {e}")
except Exception as e:
    print(f"Other error: {e}")
```

## Best Practices

### 1. Securely Store API Keys

Don't hardcode API keys in your code. Use environment variables or secure key management services.

```python
import os
API_KEY = os.environ.get("PINAI_API_KEY")
```

### 2. Implement Robust Message Handling

Always check if messages contain necessary fields and handle exceptions properly.

```python
def handle_message(message):
    if not message or "content" not in message:
        print("Received invalid message")
        return
    
    session_id = message.get("session_id")
    if not session_id:
        print("Message missing session_id, cannot respond")
        return
    
    # Process message...
```

### 3. Use Asynchronous Processing for Long-Running Tasks

For tasks that require long processing times, consider using asynchronous processing to avoid blocking the message loop.

### 4. Regularly Save Agent State

If your agent needs to maintain state, save it regularly to prevent data loss.

### 5. Monitoring and Logging

Implement appropriate logging and monitoring to track your agent's performance and issues in production.

## Example Applications

### Echo Bot

```python
def handle_message(message):
    session_id = message.get("session_id")
    content = message.get("content", "")
    
    # Simply reply with the user's message
    client.send_message(
        content=f"You said: {content}",
        session_id=session_id
    )
```

### Image Generation Bot

```python
def handle_message(message):
    """
    Process incoming messages and respond
    
    Args:
        message (dict): Message object with format:
            {
                "session_id": "unique-session-id",
                "id": 12345,  # Message ID
                "content": "user message text",
                "created_at": "2023-01-01T12:00:00"
            }
    """
    print(f"Received: {message['content']}")

    session_id = message.get("session_id")
    if not session_id:
        print("Message missing session_id, cannot respond")
        return
    
    # Get user's message
    user_message = message.get("content", "")

    # Get persona info
    persona_info = client.get_persona(session_id)
    
    # Create your response (this is where your agent logic goes)
    response = f"Echo: {user_message}"
    
    # Send response back to user
    client.send_message(content=response)
    print(f"Sent: {response}")
```

## Frequently Asked Questions

**Q: How do I get an API key?**  
A: You can obtain an API key from the [PINAI Agent platform](https://agent.pinai.tech/profile) after login.

**Q: How many agents can one account create?**  
A: No limit.

**Q: How do I handle a large number of concurrent users?**  
A: Consider using multi-threading or asynchronous processing, and implement appropriate rate limiting and load balancing.

## Support and Resources

- [PINAI Official Documentation](https://docs.pinai.com)
- [GitHub Repository](https://github.com/PIN-AI/pinai_agent_sdk)
- [Community Forum](https://community.pinai.com)

---

Good luck with your Hackathon! If you have any questions, feel free to contact the PINAI team. 