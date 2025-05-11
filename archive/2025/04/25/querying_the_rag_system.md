---
title: Querying the RAG System
date: 2025-04-25
keywords: [rag, query, search, retrieval, nlp, semantic search, metadata search]
topics: [system usage, agent core]
summary: Explains how to effectively query the Retrieval-Augmented Generation (RAG) system built with RetrievalModule and RAGAgent. Covers query syntax (natural language) and provides tips for better results.
---

## How to Query the RAG System

The RAG (Retrieval-Augmented Generation) system, primarily through the `answer_query_with_rag` function, is designed to understand and respond to your information needs by retrieving relevant context from the knowledge base and preparing it for an LLM.

### Query Syntax: Natural Language

The primary way to query the system is using **natural language**. There is no complex query syntax (like SQL) to learn for basic usage.

*   **Semantic Search:** The system uses a Sentence Transformer model to understand the *meaning* of your query. It finds document chunks that are semantically similar, even if they don't use the exact same words.
*   **Metadata Search:** The system also performs simple keyword, topic, and text matching against the document frontmatter and specific fields:
    *   **Keywords/Topics:** It checks for exact (case-insensitive) matches between your query terms and the `keywords` or `topics` listed in the frontmatter.
    *   **Text Fields:** It checks if your query term appears as a substring (case-insensitive) within fields like `title` or `summary`.

**Examples:**

*   Ask a direct question: `"What are the steps to configure the indexer?"`
*   State a topic: `"information about Faiss index types"`
*   Use known keywords: `"retrieval module find_similar method"`

### Tips for Effective Querying

1.  **Be Specific:** Clear, specific queries generally yield more relevant results than vague ones.
    *   *Less Effective:* `"Tell me about the agent."`
    *   *More Effective:* `"Explain the role of the ContextProcessor in the RAG agent."`

2.  **Leverage Keywords/Topics:** If you know relevant `keywords` or `topics` exist in the frontmatter of documents you're interested in, including them can improve retrieval accuracy.
    *   Example: If you know documents about testing use the `testing` topic, querying `"RAG agent testing"` might be more effective than just `"how is the agent tested?"`

3.  **Iterate and Refine:** If your initial query doesn't provide the desired context:
    *   **Rephrase:** Try asking the question differently.
    *   **Check Sources:** Examine the `Source:` lines included in the generated prompt's context. This tells you which documents and chunks were retrieved. If they seem off-topic, adjust your query accordingly.
    *   **Add Detail:** Include more context or constraints in your query.

4.  **Adjust Retrieved Chunk Count (`k`):** The `answer_query_with_rag` function accepts a `k` parameter (defaulting to 5) controlling the *initial* number of chunks retrieved by `find_similar`.
    *   If the final context seems too broad or contains irrelevant information, try calling the function with a smaller `k` (e.g., `k=3`).
    *   If you suspect relevant information is being missed, try a larger `k` (e.g., `k=7`), but remember the `ContextProcessor` will still truncate the final context based on its token limit.

5.  **Consider Different Prompt Templates:** While currently using `rag_default`, you could create specialized templates (e.g., `rag_summary`, `rag_elaborate`) and specify which one to use via the `template_name` parameter in `answer_query_with_rag` for different types of tasks.

By understanding that the system uses natural language combined with some metadata matching, and by applying these tips, you can significantly improve the quality and relevance of the context retrieved for your LLM interactions. 