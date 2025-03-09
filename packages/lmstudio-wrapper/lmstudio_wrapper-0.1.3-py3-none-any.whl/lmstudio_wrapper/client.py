import json
import requests
import time
import sys
import os
from typing import Dict, List, Union, Optional, Iterator, Callable

try:
    from .exceptions import LMStudioAPIError, LMStudioInvalidResponseError, LMStudioRequestError
    from .utils import format_prompt, format_notes
except ImportError:
    # When running directly
    from lmstudio_wrapper.exceptions import LMStudioAPIError, LMStudioInvalidResponseError, LMStudioRequestError
    from lmstudio_wrapper.utils import format_prompt, format_notes

class LMStudioClient:
    """Client for interacting with LM Studio's API with an OpenAI-compatible interface."""
    
    def __init__(self, api_key=None, base_url="http://localhost:1234/v1"):
        """Initialize the LM Studio client.
        
        Args:
            api_key: Optional API key (not required for local LM Studio servers)
            base_url: Base URL for the LM Studio server, defaults to localhost:1234
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }
        if api_key:
            self.headers["Authorization"] = f"Bearer {self.api_key}"
    
    def generate_summary(self, video_info, stream=False, callback=None):
        """Generate a summary of the video using LM Studio model.
        
        Args:
            video_info: Dictionary containing video information
            stream: Whether to stream the response
            callback: Optional callback function for streaming responses
            
        Returns:
            String containing the generated summary or iterator if stream=True
            
        Raises:
            LMStudioAPIError: If video_info is None or invalid
        """
        if video_info is None:
            raise LMStudioAPIError("Summary generation failed: video_info cannot be None")
            
        try:
            prompt = format_prompt(video_info)
            
            if stream:
                return self._generate_completion_stream(prompt, callback=callback)
            else:
                response = self._generate_completion(prompt)
                # Add a small delay to allow cleanup
                time.sleep(0.1)
                return response
                
        except Exception as e:
            print(f"Error in LM Studio API: {str(e)}")
            raise LMStudioAPIError(f"Summary generation failed: {str(e)}")
    
    def generate_notes(self, processed_data, stream=False, callback=None):
        """Generate detailed notes from the video data.
        
        Args:
            processed_data: Dictionary containing processed video data
            stream: Whether to stream the response
            callback: Optional callback function for streaming responses
            
        Returns:
            String containing the generated notes or iterator if stream=True
            
        Raises:
            LMStudioAPIError: If processed_data is None or invalid
        """
        if processed_data is None:
            raise LMStudioAPIError("Notes generation failed: processed_data cannot be None")
            
        try:
            prompt = format_notes(processed_data)
            
            if stream:
                return self._generate_completion_stream(prompt, callback=callback)
            else:
                response = self._generate_completion(prompt)
                # Add a small delay to allow cleanup
                time.sleep(0.1)
                return response
                
        except Exception as e:
            print(f"Error in LM Studio API: {str(e)}")
            raise LMStudioAPIError(f"Notes generation failed: {str(e)}")
    
    def _generate_completion(self, prompt, model=None, max_tokens=2048, temperature=0.7):
        """Generate completion using the LM Studio API.
        
        Args:
            prompt: The prompt to send to the model
            model: Optional model name (uses default if not specified)
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated text response
        """
        endpoint = f"{self.base_url}/chat/completions"
        
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        if model:
            payload["model"] = model
            
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    return result["choices"][0]["message"]["content"]
                else:
                    raise LMStudioInvalidResponseError("Invalid response format")
            else:
                raise LMStudioRequestError(f"API request failed with status {response.status_code}: {response.text}")
                
        except requests.exceptions.RequestException as e:
            raise LMStudioRequestError(f"Request error: {str(e)}")
    
    def _generate_completion_stream(self, prompt, model=None, max_tokens=2048, temperature=0.7, callback=None):
        """Generate streaming completion using the LM Studio API.
        
        Args:
            prompt: The prompt to send to the model
            model: Optional model name (uses default if not specified)
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            callback: Optional callback function that receives each token
            
        Returns:
            Iterator yielding generated text chunks
        """
        endpoint = f"{self.base_url}/chat/completions"
        
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": True
        }
        
        if model:
            payload["model"] = model
            
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload, stream=True)
            
            if response.status_code == 200:
                collected_chunks = []
                for line in response.iter_lines():
                    if line:
                        line = line.decode('utf-8')
                        if line.startswith('data: '):
                            data = line[6:]  # Skip 'data: ' prefix
                            if data == '[DONE]':
                                break
                                
                            try:
                                chunk = json.loads(data)
                                content = chunk['choices'][0]['delta'].get('content', '')
                                if content:
                                    collected_chunks.append(content)
                                    if callback:
                                        callback(content)
                                    yield content
                            except (json.JSONDecodeError, KeyError) as e:
                                print(f"Error processing chunk: {str(e)}")
                
                # If no callback was provided but caller isn't consuming the iterator,
                # return the full response as a convenience
                if not callback and not collected_chunks:
                    return ''.join(collected_chunks)
            else:
                raise LMStudioRequestError(f"API request failed with status {response.status_code}: {response.text}")
                
        except requests.exceptions.RequestException as e:
            raise LMStudioRequestError(f"Request error: {str(e)}")
    
    def chat_completion(self, messages, model=None, max_tokens=2048, temperature=0.7, stream=False, callback=None):
        """Generate a chat completion using a list of messages.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Optional model name (uses default if not specified)
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            stream: Whether to stream the response
            callback: Optional callback function for streaming responses
            
        Returns:
            Generated response text or iterator if stream=True
        """
        endpoint = f"{self.base_url}/chat/completions"
        
        payload = {
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        if stream:
            payload["stream"] = True
        
        if model:
            payload["model"] = model
            
        try:
            if stream:
                response = requests.post(endpoint, headers=self.headers, json=payload, stream=True)
                
                if response.status_code == 200:
                    collected_chunks = []
                    for line in response.iter_lines():
                        if line:
                            line = line.decode('utf-8')
                            if line.startswith('data: '):
                                data = line[6:]  # Skip 'data: ' prefix
                                if data == '[DONE]':
                                    break
                                    
                                try:
                                    chunk = json.loads(data)
                                    content = chunk['choices'][0]['delta'].get('content', '')
                                    if content:
                                        collected_chunks.append(content)
                                        if callback:
                                            callback(content)
                                        yield content
                                except (json.JSONDecodeError, KeyError) as e:
                                    print(f"Error processing chunk: {str(e)}")
            else:
                response = requests.post(endpoint, headers=self.headers, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    if "choices" in result and len(result["choices"]) > 0:
                        return result["choices"][0]["message"]["content"]
                    else:
                        raise LMStudioInvalidResponseError("Invalid response format")
                else:
                    raise LMStudioRequestError(f"API request failed with status {response.status_code}: {response.text}")
                    
        except requests.exceptions.RequestException as e:
            raise LMStudioRequestError(f"Request error: {str(e)}")
    
    def list_models(self):
        """List available models from LM Studio server.
        
        Returns:
            List of available models
        """
        endpoint = f"{self.base_url}/models"
        
        try:
            response = requests.get(endpoint, headers=self.headers)
            
            if response.status_code == 200:
                return response.json()
            else:
                raise LMStudioRequestError(f"Failed to list models: {response.text}")
                
        except requests.exceptions.RequestException as e:
            raise LMStudioRequestError(f"Request error: {str(e)}")
            
    def generate_text(self, prompt, model=None, max_tokens=2048, temperature=0.7, stream=False, callback=None):
        """Generate text using completions endpoint (not chat).
        
        Args:
            prompt: Text prompt to complete
            model: Optional model name (uses default if not specified)
            max_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            stream: Whether to stream the response
            callback: Optional callback function for streaming responses
            
        Returns:
            Generated text or iterator if stream=True
        """
        endpoint = f"{self.base_url}/completions"
        
        payload = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        if stream:
            payload["stream"] = True
        
        if model:
            payload["model"] = model
            
        try:
            if stream:
                response = requests.post(endpoint, headers=self.headers, json=payload, stream=True)
                
                if response.status_code == 200:
                    for line in response.iter_lines():
                        if line:
                            line = line.decode('utf-8')
                            if line.startswith('data: '):
                                data = line[6:]  # Skip 'data: ' prefix
                                if data == '[DONE]':
                                    break
                                    
                                try:
                                    chunk = json.loads(data)
                                    content = chunk['choices'][0].get('text', '')
                                    if content:
                                        if callback:
                                            callback(content)
                                        yield content
                                except (json.JSONDecodeError, KeyError) as e:
                                    print(f"Error processing chunk: {str(e)}")
            else:
                response = requests.post(endpoint, headers=self.headers, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    if "choices" in result and len(result["choices"]) > 0:
                        return result["choices"][0]["text"]
                    else:
                        raise LMStudioInvalidResponseError("Invalid response format")
                else:
                    raise LMStudioRequestError(f"API request failed with status {response.status_code}: {response.text}")
                    
        except requests.exceptions.RequestException as e:
            raise LMStudioRequestError(f"Request error: {str(e)}")
            
    def get_embeddings(self, input_text):
        """Generate embeddings for input text.
        
        Args:
            input_text: String or list of strings to embed
            
        Returns:
            List of embeddings
        """
        endpoint = f"{self.base_url}/embeddings"
        
        # Handle both single strings and lists of strings
        if isinstance(input_text, str):
            input_list = [input_text]
        else:
            input_list = input_text
            
        payload = {
            "input": input_list
        }
            
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                if "data" in result:
                    # Return the embedding arrays
                    return [item["embedding"] for item in result["data"]]
                else:
                    raise LMStudioInvalidResponseError("Invalid embeddings response format")
            else:
                raise LMStudioRequestError(f"API request failed with status {response.status_code}: {response.text}")
                
        except requests.exceptions.RequestException as e:
            raise LMStudioRequestError(f"Request error: {str(e)}")