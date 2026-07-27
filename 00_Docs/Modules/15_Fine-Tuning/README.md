# Session 15: 📉 Fine-Tuning 

🎯 Learn to fine-tuning open source LLMs and why you want to when building agentic systems today 

📚 **Learning Outcomes**

- Understand PEFT, LoRA, and quantization
- Understand test-time compute and LLM reasoning
- Learn to train a model to get better at reasoning

## 📛 Required Tooling & Account Setup

System Requirments
- **NVIDIA GPU, Ampere or newer (compute capability >= 8.0)** — e.g. RTX 30/40/50-series, A10, A100. Recent vLLM releases dropped pre-Ampere (T4/Turing) support.
- **16 GB+ VRAM** (24 GB is comfortable).
- **Linux or WSL2 only.**
- **~10 GB of free disk** for model weights and training checkpoints.
- **A Hugging Face account** with the [Llama 3.2 license accepted](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) (then `hf auth login`), or swap in the ungated `unsloth/Llama-3.2-3B-Instruct` mirror inside the notebook.

Alternatively you can access more powerful hardware for this assignment through [google colab](https://colab.research.google.com/signup) if needed.
    

# 🙋 Why Fine-Tune LLMs?

When it comes to fine-tuning, we must ask ourselves about the two primary dimensions of consideration that are always at play: performance and cost.

While we will focus on the performance aspects of fine-tuning during our lesson, it’s important to understand that `fine-tuning smaller models to achieve the same task performance as larger models is one key way enterprises can increase the efficiency of serving models, especially at scale.` 

Recalling the task-specific spectrum (from the [GPT-3 Paper](https://arxiv.org/abs/2005.14165)), we can articulate three primary behaviors that we use fine-tuning to achieve in our LLMs.

1. 🏂 **Task training**: Training the **behavior** of the LLM response
2. 🤖 **Constraining I-O schema**: Training the **format** of the LLM response
3. 🗣️ **Language training**: Training the **interpretation** of new words



Importantly, fine-tuning often helps us to *explicitly define the user experience* in terms of what goes in, and what comes out of a generative LLM.



Task training is, naturally, focused on achieving a specific task like creating a summary or answering a question. Simple, and this is the most like doing classic ML.

Constraining the I-O schema is all about putting rigid constraints on the types of input and output the model can use.  The models that have been [fine-tuned for function calling](https://gorilla.cs.berkeley.edu/leaderboard.html) are one popular example of this (e.g., always output JSON)!  We can constrain the output to fit into an X (Twitter) post, a haiku, or many other formats.  

Finally, Language Training is akin to the domain-adapted retrieval we looked at last class.  Through Language training, we can teach our LLM new words and vocabulary by updating the correlations present within its existing vocabulary and the understanding that was trained and developed during unsupervised pretraining.  

Practically, the technique for language training is to update weights (parameters).  Effectively, we’re reparameterizing the weights of the LLM.  In other words, the number of parameters (weights) in the model does not change, we’re simply updating some of their values.  That means that we’re `mapping the new tokens from our particular domain into the language patterns that the LLM already knows`.  We’re **not teaching the LLM new knowledge**, rather we’re mapping its current understanding of token relationships to our new words (tokens).  In short, *we’re teaching it jargon by association*.


# 🤗 Parameter-Efficient Fine-Tuning with Quantized Low-Rank Adaptation (PEFT-QLoRA)

Recall the discussion of reparameterization above.  Here is where we get into the code to make it happen.  To accomplish fine-tuning, there are some essential steps we need to walk through:

1. Choose model
2. Configure quantization libraries 
3. Download open-source model weights & tokenizer
4. Employ a parameter-efficient fine-tuning method (e.g. LoRA) to accomplish weight updates

Since we’ve already chosen our model, the first step is quantization, which we accomplish using the `bitsandbytes` library [Ref](https://github.com/bitsandbytes-foundation/bitsandbytes).  Quantization is about representing our parameters (weights) as floating point numbers with the right precision.  How much precision do we need?  It turns out that full precision (32-bit) is often overkill for producing consistent outputs from an LLM.  Interesting research has shown that even going down to a [single bit](https://arxiv.org/html/2402.11295v3) can be effective.

Once we have configured quantization libraries, we must download our model and tokenizer.  The model is typically downloaded in a 4-bit quantized format.  Technically speaking, the quantization type is `NF4`, a data type close to *empirically* optimal [Ref]. The tokenizer converts the [input, output] text data we need for fine-tuning into tokens that can be fed into the LLM during training.

The actual training process we’ll leverage is the one used in QLoRA, and it leverages a hybrid approach that includes quantization and dequantization.  When making updates to the network, we ensure that all computations at each step are done in half-precision (16-bit), and then stored in low-precision (4-bit).  In other words, just before any calculation is done during the backpropagation and weight update process, the parameters (floating point numbers) are up-casted to 16-bit to do the calculation.  Everything is handled behind the scenes easily for us using Hugging Face’s PEFT library.

# **🧱 Low Rank Adaptation**

LoRA, or Low-Rank Adaptation, aims to greatly reduce the number of parameters that need to be trained to accomplish downstream tasks.  LoRA works because it “freezes pre-trained model weights and injects trainable rank decomposition matrices into each layer of the transformer architecture.”  Effectively, this is doing the same thing as the Matryoshka loss that we saw during the last session; it’s allowing us to focus on the intrinsically important dimensions that are the most important for accomplishing our task.

The best overview of LoRA concepts comes from the Wiz: check it out here.

What are the key benefits of LoRA?

- More **efficient**
- Adapters for **many tasks**
- **Combine** with other PEFT methods
- Comparable to full fine-tuning
- **No** additional inference **latency**

The most interesting of these for enterprises is the `adapters for many tasks`.  When we speak with enterprise leaders, we often hear that the plan is to leverage a single large LLM - that is, to serve and make a model like Llama 3.1 70B available for inference - and then to swap out adapters as necessary while running applications in production.  It turns out that LoRA adapters can be fine-tuned and swapped out *at inference.*  This is a powerful pattern, and we expect to see companies leverage it more as proprietary AI capabilities and products get built out across industries. 

# 🕳️ Go Deeper

- 📜 The original LoRA paper is a THE read this week!
- 📜 The QLoRA paper is the right one to follow it up with!  Follow Tim Dettmers to stay in the loop on the latest!
