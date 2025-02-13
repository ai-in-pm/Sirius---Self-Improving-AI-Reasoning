import asyncio
from typing import Dict, List
from agents import (
    LeadSolver,
    CriticAgent,
    JudgmentAgent,
    StrategistAgent,
    DataAugmentorAgent,
    ConsensusBuilderAgent
)

class MultiAgentSystem:
    def __init__(self):
        self.agents = {
            'lead_solver': LeadSolver(),
            'critic': CriticAgent(),
            'judgment': JudgmentAgent(),
            'strategist': StrategistAgent(),
            'data_augmentor': DataAugmentorAgent(),
            'consensus_builder': ConsensusBuilderAgent()
        }
        
    async def solve_problem(self, problem: Dict) -> Dict:
        """
        Orchestrate the multi-agent problem-solving process.
        
        Args:
            problem: The problem description
            
        Returns:
            Dict containing the final solution and reasoning process
        """
        context = {
            "problem": problem,
            "agent_responses": []
        }
        
        try:
            # Step 1: Generate initial solution
            initial_solution = await self.agents['lead_solver'].process(context)
            context["agent_responses"].append(initial_solution)
            print("\nInitial Solution:", initial_solution)

            # Step 2: Get critique
            critique = await self.agents['critic'].process(context)
            context["agent_responses"].append(critique)
            print("\nCritique:", critique)

            # Step 3: Verify facts and logic
            verification = await self.agents['judgment'].process(context)
            context["agent_responses"].append(verification)
            print("\nVerification:", verification)

            # Step 4: Analyze strategic implications
            strategic_analysis = await self.agents['strategist'].process(context)
            context["agent_responses"].append(strategic_analysis)
            print("\nStrategic Analysis:", strategic_analysis)

            # Step 5: Augment with learned patterns
            augmented_solution = await self.agents['data_augmentor'].process(context)
            context["agent_responses"].append(augmented_solution)
            print("\nAugmented Solution:", augmented_solution)

            # Step 6: Build consensus
            consensus = await self.agents['consensus_builder'].process(context)
            print("\nFinal Consensus:", consensus)

            return {
                "final_solution": consensus,
                "reasoning_process": context["agent_responses"]
            }

        except Exception as e:
            print(f"Error: {str(e)}")
            return {
                "error": str(e),
                "reasoning_process": context["agent_responses"]
            }

async def main():
    system = MultiAgentSystem()
    problem = {
        "description": "How can we optimize a machine learning model for real-time prediction?",
        "domain": "machine_learning",
        "constraints": {
            "max_latency": "100ms"
        }
    }
    solution = await system.solve_problem(problem)
    print("\nSolution:", solution)

if __name__ == "__main__":
    asyncio.run(main())
