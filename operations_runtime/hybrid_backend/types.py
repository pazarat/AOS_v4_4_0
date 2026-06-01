"""
AOS Hybrid Backend Framework - Core Types & Contracts
Mimics FastAPI architecture while integrating Agent & Layer patterns
"""

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any, List, Dict, Callable, Optional, Coroutine
from datetime import datetime
from enum import Enum
import uuid
from abc import ABC, abstractmethod


# ============================================================================
# CORE ENUMS & CONSTANTS
# ============================================================================

class OperationMode(str, Enum):
    """Types of operations agents can perform"""
    ANALYSIS = "analysis"          # Read-only analysis
    EXECUTION = "execution"        # Perform action
    PROPOSAL = "proposal"          # Generate proposal
    SYNTHESIS = "synthesis"        # Combine insights
    GOVERNANCE = "governance"      # Policy check
    

class TruthProvenance(str, Enum):
    """Origin/reliability of information"""
    VERIFIED = "verified"          # From project contracts/files
    INFERRED = "inferred"          # Logically derived
    ASSUMED = "assumed"            # Reasonable assumption
    BLOCKED = "blocked"            # Cannot determine
    

class AgentStatus(str, Enum):
    """Health status of an agent"""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"
    ERROR = "error"


class RiskLevel(str, Enum):
    """Risk assessment levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


# ============================================================================
# REQUEST/CONTEXT TYPES
# ============================================================================

@dataclass
class OperationRequest:
    """Initial request entering the hybrid backend"""
    query: str
    user: str
    project_root: str
    intent_hint: Optional[str] = None
    timeout_ms: int = 10000
    context_data: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class OperationContext:
    """
    Injected into every agent.
    Manages request lifecycle & shared state.
    Similar to FastAPI Request object.
    """
    operation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = field(default_factory=lambda: datetime.now().timestamp())
    user: str = ""
    project_root: str = ""
    intent: Dict[str, Any] = field(default_factory=dict)
    original_request: Optional[OperationRequest] = None
    request_deadline: float = 0.0
    
    # Shared state across all agents
    shared_state: Dict[str, Any] = field(default_factory=dict)
    trace_log: List[Dict[str, Any]] = field(default_factory=list)
    
    # Governance context
    governance_policies: Dict[str, Any] = field(default_factory=dict)
    user_permissions: List[str] = field(default_factory=list)
    
    @classmethod
    def from_request(
        cls,
        request: OperationRequest,
        policies: Dict[str, Any],
        permissions: List[str]
    ) -> OperationContext:
        """Factory method - create context from incoming request"""
        context = cls(
            user=request.user,
            project_root=request.project_root,
            original_request=request,
            request_deadline=datetime.now().timestamp() + (request.timeout_ms / 1000),
            governance_policies=policies,
            user_permissions=permissions
        )
        # Parse intent from query
        context.intent = {
            'query': request.query,
            'hint': request.intent_hint,
            'raw': request.context_data
        }
        return context
    
    def add_trace(self, agent: str, event: str, data: Dict[str, Any] = None):
        """Log events during orchestration"""
        self.trace_log.append({
            'timestamp': datetime.now().isoformat(),
            'agent': agent,
            'event': event,
            'data': data or {}
        })
    
    def time_remaining_ms(self) -> float:
        """Get remaining time before deadline"""
        remaining = self.request_deadline - datetime.now().timestamp()
        return max(0, remaining * 1000)


# ============================================================================
# AGENT CONTRIBUTION TYPES
# ============================================================================

@dataclass
class RiskAssessment:
    """Risk identified by agent"""
    risk_type: str                 # 'security', 'data', 'performance', etc
    description: str
    severity: RiskLevel
    mitigation: Optional[str] = None
    impact_score: float = 0.0      # 0.0-1.0


@dataclass
class LayerContribution:
    """
    Typed response from every agent/layer.
    Standard contract for all layer outputs.
    """
    # Identity
    layer: str                     # 'identity', 'intent', 'project_truth', etc
    mode: OperationMode           # What type of operation
    
    # Main payload
    value: Any                     # Primary result
    evidence: List[str] = field(default_factory=list)  # Sources/reasoning
    
    # Quality markers
    confidence: float = 0.9        # 0.0-1.0, how sure are we?
    provenance: TruthProvenance = TruthProvenance.VERIFIED
    completeness: float = 1.0      # 0.0-1.0, how complete?
    
    # Issues identified
    risks: List[RiskAssessment] = field(default_factory=list)
    contradictions: List[Dict[str, Any]] = field(default_factory=list)
    
    # Next steps
    next_needs: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    
    # Data filtering
    ignored_noise: List[str] = field(default_factory=list)
    
    # Performance
    processing_time_ms: float = 0.0
    memory_used_mb: float = 0.0
    
    # Metadata
    agent_version: str = "1.0"
    execution_timestamp: float = field(default_factory=lambda: datetime.now().timestamp())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dict for serialization"""
        return {
            'layer': self.layer,
            'mode': self.mode.value,
            'value': self.value,
            'evidence': self.evidence,
            'confidence': self.confidence,
            'provenance': self.provenance.value,
            'completeness': self.completeness,
            'risks': [asdict(r) for r in self.risks],
            'contradictions': self.contradictions,
            'next_needs': self.next_needs,
            'suggestions': self.suggestions,
            'ignored_noise': self.ignored_noise,
            'processing_time_ms': self.processing_time_ms,
            'memory_used_mb': self.memory_used_mb,
        }


# ============================================================================
# AGENT BASE CLASS (Like FastAPI routes/endpoints)
# ============================================================================

@dataclass
class AgentHealthStatus:
    """Health check response from agent"""
    agent_name: str
    status: AgentStatus
    last_error: Optional[str] = None
    memory_mb: float = 0.0
    uptime_seconds: float = 0.0
    request_count: int = 0
    error_count: int = 0
    avg_response_ms: float = 0.0


class LayerAgent(ABC):
    """
    Base class for all layer agents.
    Similar to FastAPI route handler, but for agent patterns.
    """
    
    def __init__(self, agent_id: str, agent_name: str, version: str = "1.0"):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.version = version
        self._metrics = {
            'request_count': 0,
            'error_count': 0,
            'total_time_ms': 0.0,
            'start_time': datetime.now().timestamp()
        }
    
    @abstractmethod
    async def invoke(
        self,
        context: OperationContext,
        request_data: Dict[str, Any]
    ) -> LayerContribution:
        """
        Main entry point - called by Operations Room.
        Must return LayerContribution within deadline.
        
        Args:
            context: Request context with shared state
            request_data: Input data for this agent
            
        Returns:
            LayerContribution with typed response
        """
        raise NotImplementedError()
    
    async def health_check(self) -> AgentHealthStatus:
        """Called by Operations Room health monitoring"""
        uptime = datetime.now().timestamp() - self._metrics['start_time']
        avg_ms = (
            self._metrics['total_time_ms'] / max(1, self._metrics['request_count'])
        )
        
        return AgentHealthStatus(
            agent_name=self.agent_name,
            status=AgentStatus.HEALTHY,
            memory_mb=0.0,
            uptime_seconds=uptime,
            request_count=self._metrics['request_count'],
            error_count=self._metrics['error_count'],
            avg_response_ms=avg_ms
        )
    
    def _record_request(self, processing_time_ms: float, is_error: bool = False):
        """Track metrics"""
        self._metrics['request_count'] += 1
        self._metrics['total_time_ms'] += processing_time_ms
        if is_error:
            self._metrics['error_count'] += 1
    
    def _create_contribution(
        self,
        value: Any,
        mode: OperationMode = OperationMode.ANALYSIS,
        confidence: float = 0.9,
        provenance: TruthProvenance = TruthProvenance.VERIFIED,
        **kwargs
    ) -> LayerContribution:
        """Helper to create standard LayerContribution"""
        return LayerContribution(
            layer=self.agent_name,
            mode=mode,
            value=value,
            confidence=confidence,
            provenance=provenance,
            agent_version=self.version,
            **kwargs
        )


# ============================================================================
# ORCHESTRATION & ROUTING
# ============================================================================

@dataclass
class LayerRegistration:
    """Registration entry for a layer/agent"""
    layer_id: str
    agent_name: str
    agent_instance: LayerAgent
    category: str                  # 'identity', 'core', 'capability'
    priority: int = 0              # Execution priority
    required: bool = False         # Must succeed for operation to complete
    timeout_ms: int = 2000         # Individual timeout
    enabled: bool = True


@dataclass
class OrchestrationResponse:
    """Response from orchestration engine"""
    operation_id: str
    status: str                    # 'success', 'partial', 'failed'
    contributions: Dict[str, LayerContribution]  # Results from each agent
    synthesis: Optional[Dict[str, Any]] = None   # Synthesized insight
    governance_verdict: Optional[Dict[str, Any]] = None  # Policy check result
    
    # Metrics
    total_time_ms: float = 0.0
    agents_called: int = 0
    agents_succeeded: int = 0
    agents_failed: List[str] = field(default_factory=list)
    
    # Trace
    trace_log: List[Dict[str, Any]] = field(default_factory=list)


# ============================================================================
# API ROUTER (Like FastAPI Router)
# ============================================================================

class HybridBackendRouter:
    """
    Routes requests to appropriate agents.
    Similar to FastAPI APIRouter with dependency injection.
    """
    
    def __init__(self):
        self.routes: Dict[str, Callable] = {}
        self.middleware: List[Callable] = []
    
    def route(self, path: str, methods: List[str] = None):
        """Decorator to register a route"""
        if methods is None:
            methods = ["POST"]
        
        def decorator(func: Callable):
            route_key = f"{methods[0]}:{path}"
            self.routes[route_key] = func
            return func
        
        return decorator
    
    def add_middleware(self, middleware: Callable):
        """Add middleware (like FastAPI)"""
        self.middleware.append(middleware)


# ============================================================================
# OPERATIONAL INSIGHT (Final Response)
# ============================================================================

@dataclass
class OperationalInsight:
    """
    Final synthesized response from Operations Room.
    Ready for user delivery.
    """
    operation_id: str
    status: str                    # 'success', 'partial', 'failed'
    
    # Main content
    answer: str                    # Primary response
    insight_type: str              # 'analysis', 'recommendation', 'action', etc
    
    # Supporting details
    reasoning: List[str] = field(default_factory=list)
    evidence: Dict[str, List[str]] = field(default_factory=dict)
    next_steps: List[str] = field(default_factory=list)
    
    # Governance
    risk_score: float = 0.0        # 0.0-1.0
    approval_status: str = "auto"  # 'auto', 'pending', 'approved', 'rejected'
    
    # Metadata
    user_intent_match: float = 0.9
    confidence: float = 0.9
    alternative_views: List[Dict[str, Any]] = field(default_factory=list)
    
    # Observability
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dict for JSON serialization"""
        return {
            'operation_id': self.operation_id,
            'status': self.status,
            'answer': self.answer,
            'insight_type': self.insight_type,
            'reasoning': self.reasoning,
            'evidence': self.evidence,
            'next_steps': self.next_steps,
            'risk_score': self.risk_score,
            'approval_status': self.approval_status,
            'user_intent_match': self.user_intent_match,
            'confidence': self.confidence,
            'alternative_views': self.alternative_views,
            'metadata': self.metadata,
        }


__all__ = [
    'OperationMode',
    'TruthProvenance',
    'AgentStatus',
    'RiskLevel',
    'OperationRequest',
    'OperationContext',
    'RiskAssessment',
    'LayerContribution',
    'AgentHealthStatus',
    'LayerAgent',
    'LayerRegistration',
    'OrchestrationResponse',
    'HybridBackendRouter',
    'OperationalInsight',
]
