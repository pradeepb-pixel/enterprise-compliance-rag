"""
Enterprise Compliance RAG Platform
Built with Claude API + AWS Bedrock Knowledge Bases
Author: Pradeep B | AI Engineer @ Visa
"""

from retrieval.bedrock_kb import BedrockKnowledgeBase
from generation.claude_client import ClaudeClient

def query_compliance(question: str) -> dict:
    """
    Query the compliance RAG pipeline.
    
    Args:
        question: Natural language compliance question
        
    Returns:
        dict with answer and source citations
    """
    kb = BedrockKnowledgeBase()
    claude = ClaudeClient()

    # Step 1: Retrieve relevant document chunks
    retrieved_docs = kb.retrieve(question, top_k=5)

    # Step 2: Generate grounded answer with citations
    answer = claude.generate(question, retrieved_docs)

    return {
        "question": question,
        "answer": answer["response"],
        "sources": answer["citations"]
    }


if __name__ == "__main__":
    question = "What are the KYC requirements for onboarding a new corporate client?"
    print(f"Question: {question}\n")
    result = query_compliance(question)
    print(f"Answer: {result['answer']}")
    print(f"Sources: {result['sources']}")
