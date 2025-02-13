from .base_agent import BaseAgent
import aiohttp
import json

class CriticAgent(BaseAgent):
    def __init__(self):
        super().__init__(role="Critic")
        
    async def process(self, context: dict) -> dict:
        """Analyze and critique the proposed solution."""
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {self.anthropic_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "claude-3-opus-20240229",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a Critical Thinking Expert with PhD-level expertise. Analyze the proposed solution and provide constructive criticism."
                    },
                    {
                        "role": "user",
                        "content": json.dumps(context)
                    }
                ],
                "max_tokens": 1000
            }
            
            async with session.post(
                "https://api.anthropic.com/v1/messages",
                headers=headers,
                json=payload
            ) as response:
                result = await response.json()
                return {
                    "role": self.role,
                    "critique": result["content"][0]["text"],
                    "aspects": {
                        "feasibility": 0.8,
                        "completeness": 0.7,
                        "innovation": 0.6
                    }
                }
    
    async def critique(self, proposal: dict) -> dict:
        """Meta-critique of another agent's critique."""
        return {
            "role": self.role,
            "meta_critique": "Analyzing critique methodology...",
            "improvement_points": []
        }
    
    async def refine(self, feedback: dict) -> dict:
        """Refine critique based on feedback."""
        return {
            "role": self.role,
            "refined_critique": "Incorporating feedback...",
            "updated_aspects": {}
        }
