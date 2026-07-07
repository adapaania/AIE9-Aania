# Local Deploy Guide

This guide is for running the Session 09 LangGraph backend locally in a Docker container and exposing it with a tunnel. Even with this local backend option, the frontend still needs to be deployed to Vercel.

## 1. Start From Session 09

```bash
cd /Users/aaniaadap/Desktop/AI-Eng-Certification/09_Agent_Servers
uv sync
cp .env.example .env
```

Fill in `.env`:

```text
OPENAI_API_KEY=...
TAVILY_API_KEY=...
LANGSMITH_API_KEY=...
LANGSMITH_TRACING=true
```

## 2. Test the Agent Locally

```bash
uv run langgraph dev
```

Open LangGraph Studio and test the `agent` assistant with a question like:

```text
How often should I deworm my cat?
```

Stop the dev server after testing.

## 3. Run the Backend in Docker

Make sure Docker Desktop is running, then run:

```bash
uv run langgraph up
```

The local deployed backend should run at:

```text
http://localhost:2024
```

## 4. Expose the Backend With a Tunnel

In a second terminal:

```bash
ngrok http 2024
```

Copy the HTTPS forwarding URL. It will look like:

```text
https://your-ngrok-url.ngrok-free.app
```

This is the backend URL you will use for the Vercel frontend environment variable.

## 5. Run the Frontend Locally First

```bash
cd /Users/aaniaadap/Desktop/AI-Eng-Certification/09_Agent_Servers/frontend
cp .env.local.example .env.local
```

For local testing, use:

```text
LANGGRAPH_API_URL=http://localhost:2024
LANGSMITH_API_KEY=
NEXT_PUBLIC_API_URL=http://localhost:3000/api
```

Then run:

```bash
npm install
npm run dev
```

Open:

```text
http://localhost:3000
```

## 6. Deploy the Frontend to Vercel

Deploy the `frontend` folder to Vercel. In Vercel, set these environment variables:

```text
LANGGRAPH_API_URL=https://your-ngrok-url.ngrok-free.app
LANGSMITH_API_KEY=
NEXT_PUBLIC_API_URL=https://your-vercel-app.vercel.app/api
```

Then redeploy the Vercel project.

## 7. What to Show in the Loom

- LangGraph Studio showing the agent graph
- The Docker/local backend running
- The tunnel URL
- The Vercel site sending a message to the agent
- A LangSmith trace showing the agent run

