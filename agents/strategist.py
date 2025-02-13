from .base_agent import BaseAgent
import aiohttp
import json

class StrategistAgent(BaseAgent):
    def __init__(self):
        super().__init__(role="Strategist")
        
    async def process(self, context: dict) -> dict:
        """Analyze long-term implications and strategic considerations."""
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {self.cohere_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "command",
                "prompt": f"As a Strategic Planning Expert, analyze the long-term implications of this solution: {json.dumps(context)}",
                "max_tokens": 1000,
                "temperature": 0.4
            }
            
            async with session.post(
                "https://api.cohere.ai/v1/generate",
                headers=headers,
                json=payload
            ) as response:
                result = await response.json()
                return {
                    "role": self.role,
                    "strategic_analysis": result["generations"][0]["text"],
                    "implications": {
                        "short_term": [],
                        "medium_term": [],
                        "long_term": []
                    },
                    "risks": [],
                    "opportunities": []
                }
    
    async def critique(self, proposal: dict) -> dict:
        """Evaluate strategic aspects of another agent's proposal."""
        return {
            "role": self.role,
            "strategic_critique": "Analyzing strategic implications...",
            "recommendations": []
        }
    
    async def refine(self, feedback: dict) -> dict:
        """Refine strategic analysis based on feedback."""
        return {
            "role": self.role,
            "refined_strategy": "Updating strategic analysis...",
            "updated_implications": {}
        }
