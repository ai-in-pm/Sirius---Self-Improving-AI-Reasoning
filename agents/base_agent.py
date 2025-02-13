import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv

class BaseAgent(ABC):
    def __init__(self, role: str):
        load_dotenv()
        self.role = role
        self._setup_api_keys()
        
    def _setup_api_keys(self):
        """Load API keys from environment variables."""
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        self.groq_key = os.getenv('GROQ_API_KEY')
        self.google_key = os.getenv('GOOGLE_API_KEY')
        self.cohere_key = os.getenv('COHERE_API_KEY')
        self.emergence_key = os.getenv('EMERGENCEAI_API_KEY')
        
    @abstractmethod
    async def process(self, context: dict) -> dict:
        """Process input and return response based on agent's role."""
        pass
        
    @abstractmethod
    async def critique(self, proposal: dict) -> dict:
        """Critique a proposal from another agent."""
        pass
        
    @abstractmethod
    async def refine(self, feedback: dict) -> dict:
        """Refine response based on feedback."""
        pass
        
    def __str__(self):
        return f"{self.role} Agent"
