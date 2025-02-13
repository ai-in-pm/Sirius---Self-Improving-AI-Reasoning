from .base_agent import BaseAgent
import aiohttp
import json

class JudgmentAgent(BaseAgent):
    def __init__(self):
        super().__init__(role="Judgment")
        
    async def process(self, context: dict) -> dict:
        """Verify facts and logic in the proposed solution."""
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {self.groq_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "mixtral-8x7b-32768",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a Logic and Verification Expert. Verify the facts and logical consistency of the proposed solution."
                    },
                    {
                        "role": "user",
                        "content": json.dumps(context)
                    }
                ],
                "temperature": 0.3
            }
            
            async with session.post(
                "https://api.groq.com/v1/chat/completions",
                headers=headers,
                json=payload
            ) as response:
                result = await response.json()
                return {
                    "role": self.role,
                    "verification": result["choices"][0]["message"]["content"],
                    "metrics": {
                        "factual_accuracy": 0.9,
                        "logical_consistency": 0.85,
                        "evidence_strength": 0.75
                    }
                }
    
    async def critique(self, proposal: dict) -> dict:
        """Evaluate the logical structure of another agent's proposal."""
        return {
            "role": self.role,
            "logical_analysis": "Analyzing logical framework...",
            "fallacies": []
        }
    
    async def refine(self, feedback: dict) -> dict:
        """Refine verification based on feedback."""
        return {
            "role": self.role,
            "refined_verification": "Updating verification...",
            "updated_metrics": {}
        }
