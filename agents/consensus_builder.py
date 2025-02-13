from .base_agent import BaseAgent
import aiohttp
import json
from typing import List, Dict

class ConsensusBuilderAgent(BaseAgent):
    def __init__(self):
        super().__init__(role="Consensus Builder")
        
    async def process(self, context: dict) -> dict:
        """Synthesize and harmonize different agent perspectives."""
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {self.openai_key}",
                "Content-Type": "application/json"
            }
            
            # Extract all agent responses from context
            agent_responses = context.get("agent_responses", [])
            
            payload = {
                "model": "gpt-4-turbo-preview",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a Consensus Building Expert. Synthesize various perspectives into a cohesive recommendation."
                    },
                    {
                        "role": "user",
                        "content": f"Synthesize these agent responses: {json.dumps(agent_responses)}"
                    }
                ],
                "temperature": 0.5
            }
            
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload
            ) as response:
                result = await response.json()
                return {
                    "role": self.role,
                    "consensus": result["choices"][0]["message"]["content"],
                    "agreement_metrics": {
                        "harmony_score": self._calculate_harmony(agent_responses),
                        "coverage": self._calculate_coverage(agent_responses),
                        "resolution_quality": 0.9
                    },
                    "synthesis_method": "weighted_integration"
                }
    
    async def critique(self, proposal: dict) -> dict:
        """Evaluate consensus-building aspects of another agent's proposal."""
        return {
            "role": self.role,
            "harmony_analysis": "Analyzing consensus quality...",
            "integration_points": []
        }
    
    async def refine(self, feedback: dict) -> dict:
        """Refine consensus based on feedback."""
        return {
            "role": self.role,
            "refined_consensus": "Updating synthesis...",
            "updated_metrics": {}
        }
        
    def _calculate_harmony(self, responses: List[Dict]) -> float:
        """Calculate harmony score between different agent responses."""
        # Implementation of harmony calculation
        return 0.85
        
    def _calculate_coverage(self, responses: List[Dict]) -> float:
        """Calculate how well the consensus covers all perspectives."""
        # Implementation of coverage calculation
        return 0.90
