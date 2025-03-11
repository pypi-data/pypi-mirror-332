from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import requests
import json
from typing import Dict, Any, List, Optional


def search_api_docs(api_name: str, serper_api_key: str) -> Dict[str, Any]:
    """
    Search for API documentation using Serper and prepare a prompt for the OpenAI API.

    Args:
        api_name: Name of the API to search for documentation
        serper_api_key: API key for Serper

    Returns:
        Dictionary with search results and prompt for OpenAI
    """
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q": f"{api_name} python library documentation",
        "gl": "us",
        "hl": "en"
    })

    headers = {
        'X-API-KEY': serper_api_key,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    search_results = response.json()

    # Extract top result
    top_result = None
    if 'organic' in search_results and len(search_results['organic']) > 0:
        top_result = search_results['organic'][0]

    # Create prompt for OpenAI
    prompt = ""
    if top_result:
        prompt = f"""
Search result for "{api_name} python library documentation":
Title: {top_result.get('title', 'No title')}
Link: {top_result.get('link', 'No link')}
Snippet: {top_result.get('snippet', 'No snippet')}

If this result is documentation for a Python library, please:
1. Provide a brief description of the library
2. Show a trivial example of its usage
If this is not relevant documentation, please inform the user that appropriate documentation was not found.
"""
    else:
        prompt = f"No search results found for {api_name} documentation. Please inform the user that documentation wasn't found."

    return {
        "search_results": search_results,
        "top_result": top_result,
        "prompt_for_openai": prompt
    }


def query_vector_db_for_function(
    function_query: str,
    index_path: str,
    db_data_path: str,
    model_name: str = "all-MiniLM-L6-v2",
    top_k: int = 3
) -> Dict[str, Any]:
    """
    Query a vector database for function information and prepare results for OpenAI API.

    Args:
        function_query: Query describing the function to search for
        index_path: Path to the FAISS index file (if None, creates an example index)
        db_data_path: Path to the function metadata (if None, creates example data)
        model_name: SentenceTransformer model to use
        top_k: Number of top results to return

    Returns:
        Dictionary with query results and prompt for OpenAI
    """
    # Load or create model
    model = SentenceTransformer(model_name)

    # Load existing index and data
    index = faiss.read_index(index_path)
    with open(db_data_path, 'r') as f:
        function_data = json.load(f)

    # Query the index
    query_vector = model.encode([function_query])
    faiss.normalize_L2(query_vector)

    # Create arrays for distances and indices
    distances = np.empty((1, top_k), dtype=np.float32)
    indices = np.empty((1, top_k), dtype=np.int64)

    # Search the index (labels parameter is same as indices in Python API)
    index.search(query_vector.astype(np.float32),
                 top_k, distances, indices, None)

    # Collect results
    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(function_data):
            result = function_data[idx].copy()
            result["similarity_score"] = float(
                1 - distances[0][i])  # Convert to similarity
            results.append(result)

    # Create prompt for OpenAI
    prompt = f"""
Query: "{function_query}"

Found {len(results)} potential function matches:

"""

    for i, result in enumerate(results):
        prompt += f"""
Match {i+1} (Similarity: {result['similarity_score']:.2f}):
- Function: {result['function_name']}
- Package: {result['package']}
- Description: {result['description']}
- Signature: {result['signature']}
- Example: 
```python
{result['example']}
```

"""

    prompt += """
Based on these results, please:
1. Determine if any of these functions match what the user is looking for
2. If there's a match, provide a detailed description of:
   - The package the function belongs to
   - The function's purpose and key parameters
   - A simple usage example
3. If there's no good match, please inform the user that no suitable function was found
"""

    return {
        "query": function_query,
        "results": results,
        "prompt_for_openai": prompt
    }
