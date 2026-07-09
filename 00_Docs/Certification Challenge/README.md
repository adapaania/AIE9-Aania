# The Certification Challenge v1.0

Submission From: https://forms.gle/xtM9F38nfRKcdjH97

Due: 7pm ET 7/14

# Overview

Welcome to the middle of the course!  We’re 5 weeks in, and we’ve covered a lot of ground - you all certainly have enough prototyping skill to be dangerous!

At this point, it’s important to consider everything in front of us as a blank page - blue sky!

It’s time to align the general skills we’ve learned (and will continue to learn!) in the specific direction aligned with what you’re aiming at.

What are your goals for the rest of 2026?

How can you build 🏗️, ship 🚢, and share 🚀 your way towards achieving them?

It all starts now, with the Certification Challenge, which is the next step towards continuing your journey to Demo Day!

**Your Certification Challenge is due Tuesday, July 14th.**

>[!Note]
💡Remember, *you know enough already to be dangerous*. You already know enough of the concepts and code you need to build, ship, and share production AI applications! 

</aside>

And this is what the Certification challenge is all about - putting **your skills to the tes**t!

# Setting Expectations

During our last cohort, here is how the numbers shook out. It took an average of 24.7 hours for people to complete the challenge.

![image.png](image.png)

It’s very much worth considering that the kind of AI Engineering work we’re doing; that is, scoping a problem, creating a solution to that problem that solves a specific pain point for real customers or stakeholders, and engineering it for scale from day 1, is extremely valuable work.

In our opinion, **this is the kind of pilot project work that you should be charging $5-20k as a solo consultant**.

It is also the kind of work that, after you take a few shots on goal, will become faster and faster for you to knock out.

Finally, it’s worth noting that [Certified AI Engineers](https://aimakerspace.io/graduates/) not only are at the top of hiring lists within our network, but we’ve worked with multiple former students & solo consultants in the past to fill up their plate with project work, and we’ve helped certified students running startups to build out their teams.

What is in your future as an AI Engineer or AI Engineering Leader?

# Your Project Idea

1. What **problem** are you trying to solve?  
*Why is this a problem?*
2. What is your proposed **solution**?  
*Why is this the best solution?*
3. Who is the **audience** that has this problem and would use your solution?  
*Do they nod their head up and down when you talk to them about it?*

Problem, Solution, Audience. 

That’s really all you need. 

We might call this *AI Product Management*. This work asks “**what** should I build and why?”

From there, we need to do some *AI Engineering*. This work asks “**how** should I build, evaluate, and improve?”

The best AI engineers can do both.

Once you know the problem to be solved, you must be capable of guiding your team towards implementation.

# Task 1: Defining Problem, Audience, and Scope

**You are an AI Solutions Engineer**.

**What** problem do you want to solve?  **Who** is it a problem for?

>[!TIP]
>📝 Task 1: Articulate the problem and the user of your application\
>*Hints:*
>- First read [Concrete Startup Idea](https://docs.google.com/document/d/1hgI39NNFhMibVONUJJyKrMK4XLF4H32t6m4ob07uG7k/edit?tab=t.0) from the AI Fund.
>- *What is the user’s job title, and what is the part of their job function that you’re trying to automate?*
</aside>

**✅ Deliverables**

1. Write a succinct 1-sentence description of the problem. Do not mention or imply a solution.
2. Write 1-2 paragraphs on why this is a problem for your specific user including:
    1. Who has the problem?
    2. What are they trying to do
    3. How do they handle it today?
    4. Why isn't that good enough?
3. **Create a workflow diagram** illustrating how the user solves this problem today. Your diagram should clearly show:
    1. The sequence of steps the user takes
    2. The tools, systems, or documents they interact with
    3. The points where the workflow is slow, repetitive, or error-prone
4. Create a list of questions or input-output pairs that you can use to evaluate your application

# Task 2: Propose a Solution

Now that you’ve defined a problem and a user, *there are many possible solution implementations.*

Choose one, and articulate it.

>[!TIP]
>📝Task 2: Articulate your proposed solution\
*Hint:*
>- *Recall the [LLM Application stack](https://a16z.com/emerging-architectures-for-llm-applications/) we’ve discussed*
>- What architectural decisions do you need to make, and what tradeoffs come with those decisions?
</aside>

**✅ Deliverables**

1. **Describe your solution in one sentence.**
2. **Create an infrastructure diagram** showing the technologies that make up your system. Write one sentence explaining why you chose each component. *"What technologies make up your system?”*
    1. LLM(s)
    2. Agent orchestration framework 
    3. Tool(s)
    4. Embedding model
    5. Vector Database
    6. Monitoring tool
    7. Evaluation framework
    8. User interface
    9. Deployment tool
    10. Any other components you need

**3. Create an Agent Workflow Diagram** illustrating how your application solves the user's problem from end to end. Accompany the diagram with **1–2 paragraphs** explaining the workflow.

*"How does the application solve the user's problem?”*

Your workflow should include:

1. The user's input
2. The agent's reasoning and decision points
3. When the agent retrieves information (RAG)
4. What tools the agent calls and why
5. The final output returned to the user
6. Any human review or approval steps

Requirements:

- Use an LLM gateway of your choice
- Must have a memory component
- Be able to run it on my phone and laptop in a browser

# Task 3: Dealing with the Data

**You are an AI Systems Engineer.**  The AI Solutions Engineer has handed off the plan to you.  *At a minimum*, you’ll need to implement a simple Agentic RAG solution that includes two aspects:

1. Your own personal data, uploaded to your application (e.g., RAG)
2. The ability to search publicly available data (e.g., a simple agentic search tool like [Tavily](https://tavily.com/))

>[!TIP]
>📝 Task 3: Collect your own data (RAG) and choose at least one external API to use (Agent)  
*Hint:*  
>- *Ask other real people (ideally the people you’re building for!) what they think.*
>- *What are the specific questions that your user is likely to ask of your application?  **Write these down**.*
</aside>

**✅ Deliverables**

1. Describe the default chunking strategy that you will use for your data.  Why did you make this decision?
2. Describe your data source and the external API you plan to use, as well as what role they will play in your solution. Discuss how they interact during usage. 

# Task 4: Building an End-to-End Agentic RAG Prototype

>[!TIP]
>📝Task 4: Build an end-to-end Agentic RAG application using a production-grade stack and your choice of commercial off-the-shelf model(s)

</aside>

**✅ Deliverables**

1. Build an end-to-end prototype
2. Deploy your prototype to public endpoint using a tool like [Vercel](http://vercel.com/), [Render](https://render.com/), or [FastAPI Cloud](https://fastapicloud.com/)

# Task 5: Evals

**You are an AI Evaluation & Performance Engineer.**  The AI Systems Engineer who built the initial RAG system has asked for your help and expertise in creating an evaluation harness.

>[!TIP]
>📝Task 5: Prepare a test data set (either by generating synthetic data or by assembling an existing dataset) to baseline an initial evaluation.

</aside>

**✅ Deliverables**

1. Prepare a test data set (either by generating synthetic data or by assembling an existing dataset)
2. Create an evaluation harness that's relevant to your problem space (you can use prompted LLM-as-a-Judge, RAG-specific tools like RAGAS, Agent-specific evaluations like [Tau2-infinity](https://vibrantlabs.com/research/tau2-infinity) , etc.)
3. What conclusions can you draw about the performance and effectiveness of your pipeline with this information?

# Task 6: Improving Your Prototype

**You are an AI Systems Engineer.**  The AI Evaluation and Performance Engineer has asked for your help in making stepwise improvements to the application. You will work together with them on this task.

>[!TIP]
>📝Task 6: Install an advanced retriever of your choosing in our Agentic RAG application. 

</aside>

**✅ Deliverables**

1. Choose and implement an advanced retrieval technique that you believe will improve your application’s ability to retrieve the most appropriate context.  Write 1-2 sentences on why you believe it will be useful for your use case.
2. How does the performance compare to your original RAG application?  Provide results in a table.
3. Identify and implement change to atleast one other piece of solution. Using the evaluation harness as hard evidence, demonstrate a meaningfully improved response

# Task 7: Next Steps

You are the **AI Solutions Engineer**. **AI Evaluation & Performance Engineer**. 

1. Reflecting on what you've built so far, what parts of your current implementation do you plan to keep for Demo Day, and what parts would you change or improve? Explain your reasoning.

# Your Final Submission

Please include the following in your final submission:

1. A public (or otherwise shared) link to a **GitHub repo** that contains:
    1. A 10-minute (OR LESS) Loom video of a live **demo of your application** that also describes the use case.
    2. A **written document** addressing each deliverable and answering each question
    3. All relevant code

Questions? Email `jacob@aimakerspace.io`
