Build an AI-Powered Multimodal MCP Chatbot#
This step-by-step guide will walk you through building a modern chatbot that can chat with your documents, images, and videos. By the end, you'll have a working multimodal AI assistant and understand how to use Jac's unique programming features to build intelligent applications.

What You'll Build#
You'll create a chatbot that can:

Upload and chat with PDFs, text files, images, and videos
Search your documents and provide context-aware answers
Answer general questions using web search
Understand and discuss images and videos using AI vision
Route different types of questions to specialized AI handlers
What You'll Learn#
Object Spatial Programming: Use Jac's node-walker architecture to organize your application
Mean Typed Programming (MTP): Let AI classify and route user queries automatically with just simple definitions
Model Context Protocol (MCP): Build modular, reusable AI tools
Multimodal AI: Work with text, images, and videos in one application
Technologies We'll Use#
Jac Language: For the main application logic
Jac Cloud: Backend server infrastructure
Streamlit: User-friendly web interface
ChromaDB: Document search and storage
OpenAI GPT: AI chat and vision capabilities
Serper API: Real-time web search
Project Structure#
We'll create six main files:

client.jac: The web interface for chat and file uploads
server.jac: The main application using Object Spatial Programming
server.impl.jac: Implementation details and function bodies for server.jac (automatically imported by Jac)
mcp_server.jac: Tool server for document search and web search
mcp_client.jac: Interface to communicate with tools
tools.jac: Document processing and search logic