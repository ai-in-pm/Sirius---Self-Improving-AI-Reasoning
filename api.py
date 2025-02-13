from aiohttp import web
import json
from typing import Dict, List, Optional
import asyncio
from datetime import datetime
from agents import (
    LeadSolver,
    CriticAgent,
    JudgmentAgent,
    StrategistAgent,
    DataAugmentorAgent,
    ConsensusBuilderAgent
)

# Initialize agents
agents = {
    "lead_solver": LeadSolver(),
    "critic": CriticAgent(),
    "judgment": JudgmentAgent(),
    "strategist": StrategistAgent(),
    "data_augmentor": DataAugmentorAgent(),
    "consensus_builder": ConsensusBuilderAgent()
}

async def solve_problem(request):
    """
    Solve a problem using the multi-agent system.
    """
    try:
        # Parse request body
        body = await request.json()
        
        # Validate input
        if "description" not in body:
            return web.json_response(
                {"error": "Problem description is required"},
                status=400
            )
            
        # Create context
        context = {
            "problem": body,
            "timestamp": datetime.utcnow().isoformat(),
            "agent_responses": []
        }
        
        # Step 1: Generate initial solution
        initial_solution = await agents["lead_solver"].process(context)
        context["agent_responses"].append(initial_solution)
        
        # Step 2: Get critique
        critique = await agents["critic"].process(context)
        context["agent_responses"].append(critique)
        
        # Step 3: Verify facts and logic
        verification = await agents["judgment"].process(context)
        context["agent_responses"].append(verification)
        
        # Step 4: Analyze strategic implications
        strategic_analysis = await agents["strategist"].process(context)
        context["agent_responses"].append(strategic_analysis)
        
        # Step 5: Augment with learned patterns
        augmented_solution = await agents["data_augmentor"].process(context)
        context["agent_responses"].append(augmented_solution)
        
        # Step 6: Build consensus
        consensus = await agents["consensus_builder"].process(context)
        
        response = {
            "problem_id": str(hash(body["description"])),
            "initial_solution": initial_solution,
            "critiques": [critique],
            "verification": verification,
            "strategic_analysis": strategic_analysis,
            "augmented_solution": augmented_solution,
            "final_consensus": consensus,
            "metadata": {
                "timestamp": context["timestamp"],
                "processing_time": "calculated_time",
                "confidence_score": consensus["agreement_metrics"]["harmony_score"]
            }
        }
        
        return web.json_response(response)
        
    except Exception as e:
        return web.json_response(
            {"error": str(e)},
            status=500
        )

async def list_agents(request):
    """
    List all available agents and their roles.
    """
    return web.json_response({
        name: str(agent) for name, agent in agents.items()
    })

async def health_check(request):
    """
    Check system health and agent availability.
    """
    return web.json_response({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "agents_available": len(agents),
        "version": "1.0.0"
    })

def init_app():
    app = web.Application()
    app.router.add_post("/solve", solve_problem)
    app.router.add_get("/agents", list_agents)
    app.router.add_get("/health", health_check)
    return app

if __name__ == "__main__":
    app = init_app()
    web.run_app(app, host="0.0.0.0", port=8001)
