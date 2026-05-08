from langgraph.graph import StateGraph
from langgraph.graph import END

from graph.state import AgentState

from graph.supervisor import supervisor

from agents.system_agent import system_agent
from agents.browser_agent import browser_agent
from agents.coding_agent import coding_agent


workflow = StateGraph(AgentState)


# ====================================
# NODES
# ====================================

workflow.add_node(
    "supervisor",
    supervisor
)

workflow.add_node(
    "system_agent",
    system_agent
)

workflow.add_node(
    "browser_agent",
    browser_agent
)

workflow.add_node(
    "coding_agent",
    coding_agent
)


# ====================================
# ENTRY POINT
# ====================================

workflow.set_entry_point(
    "supervisor"
)


# ====================================
# CONDITIONAL ROUTING
# ====================================

workflow.add_conditional_edges(
    "supervisor",
    lambda state: state["next_agent"],
    {
        "system_agent": "system_agent",
        "browser_agent": "browser_agent",
        "coding_agent": "coding_agent"
    }
)


# ====================================
# EXITS
# ====================================

workflow.add_edge(
    "system_agent",
    END
)

workflow.add_edge(
    "browser_agent",
    END
)

workflow.add_edge(
    "coding_agent",
    END
)


# ====================================
# COMPILE GRAPH
# ====================================

jarvis_graph = workflow.compile()