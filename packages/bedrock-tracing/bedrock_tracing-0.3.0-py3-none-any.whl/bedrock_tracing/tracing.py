import json
import logging
from functools import wraps
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader


# Set up logging
logger = logging.getLogger(__name__)

# Configure OpenTelemetry resource and tracer provider
resource = Resource.create()
tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)

# Configure the OTLP exporter and span processor
otlp_exporter = OTLPSpanExporter()
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)

# Create the tracer
tracer = trace.get_tracer(__name__)


# Configure OpenTelemetry Metrics
metric_reader = PeriodicExportingMetricReader(OTLPMetricExporter())
meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(__name__)

# Define Metrics
llm_token_usage = meter.create_counter("llm_token_usage", "tokens", "Counts tokens used in LLM calls")
llm_call_count = meter.create_counter("llm_call_count", "calls", "Counts LLM invocations")
orchestration_duration = meter.create_histogram("orchestration_duration", "seconds", "Measures orchestration time")

def process_trace_data(event, parent_span):
    """Extracts and processes trace data from Bedrock response event."""
    trace_data = event.get("trace", {})
    
    orchestration_trace = trace_data.get("trace", {}).get("orchestrationTrace", {})
    guardrail_trace = trace_data.get("trace", {}).get("guardrailTrace", {})
    failure_trace = trace_data.get("trace", {}).get("failureTrace", {})
    pre_processing_trace = trace_data.get("trace", {}).get("preProcessingTrace", {})
    post_processing_trace = trace_data.get("trace", {}).get("postProcessingTrace", {})
    logger.debug("Processed Trace Data: %s", json.dumps(trace_data, indent=2))

            
    def create_invocation_type(trace_segment):
        return (
            trace_segment.get("observation", {}).get("type")
            or trace_segment.get("modelInvocationInput", {}).get("type")
            or (
                f"GUARDRAIL_ACTION:{guardrail_trace.get('action')}"
                if guardrail_trace.get("action")
                else None
            )
            or ("LLM_RESPONSE" if trace_segment.get("modelInvocationOutput", {}).get("rawResponse", {}).get("content") else None)
            or "bedrock-agent-execution"
        )
    for parent_name, trace_segment in [
        ("preprocessing", pre_processing_trace),
        ("orchestration", orchestration_trace),
        ("guardrails", guardrail_trace),
        ("postprocessing", post_processing_trace),
        ("failure", failure_trace),
    ]:
        if trace_segment:
            with tracer.start_as_current_span(parent_name, context=trace.set_span_in_context(parent_span)) as parent_trace_span:
                invocation_type = create_invocation_type(trace_segment)
                with tracer.start_as_current_span(invocation_type, context=trace.set_span_in_context(parent_trace_span)) as child_span:
                    def parse_dict(prefix, data, child_span):
                        if isinstance(data, dict):
                            for k, v in data.items():
                                parse_dict(f"{prefix}.{k}" if prefix else k, v, child_span)
                        elif isinstance(data, list):
                            for i, item in enumerate(data):
                                parse_dict(f"{prefix}[{i}]", item, child_span)
                        else:
                            child_span.set_attribute(prefix, str(data))
                            
                    parse_dict("trace", trace_data, child_span)

                    if failure_trace:
                        child_span.set_attribute("failure.reason", failure_trace.get("failureReason", "unknown"))
                    
                    # # Guardrail tracing attributes
                    if guardrail_trace:
                        #with tracer.start_as_current_span("guardrail") as guardrail_span:
                        child_span.set_attribute("guardrail.action", guardrail_trace.get("action", "unknown"))
                        for assessment in guardrail_trace.get("inputAssessments", []) + guardrail_trace.get("outputAssessments", []):
                            for topic in assessment.get("topicPolicy", {}).get("topics", []):
                                child_span.set_attribute(f"guardrail.topic.{topic['name']}.type", topic.get("type", "unknown"))
                                child_span.set_attribute(f"guardrail.topic.{topic['name']}.action", topic.get("action", "unknown"))
                            for filter in assessment.get("contentPolicy", {}).get("filters", []):
                                child_span.set_attribute(f"guardrail.filter.{filter['type']}.confidence", filter.get("confidence", "unknown"))
                                child_span.set_attribute(f"guardrail.filter.{filter['type']}.action", filter.get("action", "unknown"))
                            for word in assessment.get("wordPolicy", {}).get("customWords", []):
                                child_span.set_attribute(f"guardrail.word.{word['match']}.action", word.get("action", "unknown"))
                            for entity in assessment.get("sensitiveInformationPolicy", {}).get("piiEntities", []):
                                child_span.set_attribute(f"guardrail.pii.{entity['type']}.match", entity.get("match", "unknown"))
                                child_span.set_attribute(f"guardrail.pii.{entity['type']}.action", entity.get("action", "unknown"))
                    
                    # Agent-specific attributes
                    child_span.set_attribute("agent.id", trace_data.get("agentId", "unknown"))
                    child_span.set_attribute("agent.name", trace_data.get("agentName", "unknown"))
                    child_span.set_attribute("agent.collaboratorName", trace_data.get("collaboratorName", "unknown"))
                    child_span.set_attribute("agent.sessionId", trace_data.get("sessionId", "unknown"))
                    child_span.set_attribute("agent.alias_id", trace_data.get("agentAliasId", "unknown"))
                    child_span.set_attribute("agent.version", trace_data.get("agentVersion", "unknown"))
                    
                    # # Orchestration details
                    if orchestration_trace:            
                        child_span.set_attribute("orchestration.observation.type", orchestration_trace.get("observation", {}).get("type", "unknown"))
                        child_span.set_attribute("orchestration.trace_id", orchestration_trace.get("observation", {}).get("traceId", "unknown"))
                        child_span.set_attribute("orchestration.final_response", orchestration_trace.get("observation", {}).get("finalResponse", {}).get("text", "unknown"))
                        #print("*********", orchestration_trace.get("observation", {}).get("type", "unknown"))
                    
                    if pre_processing_trace:
                        child_span.set_attribute("pre_processing.modelInvocationOutput.rawResponse.content", orchestration_trace.get("modelInvocationOutput", {}).get("rawResponse", {}).get("content",{}))
                        child_span.set_attribute("pre_processing.modelInvocationOutput.parsedResponse.rationale", orchestration_trace.get("modelInvocationOutput", {}).get("parsedResponse", {}).get("rationale",{}))
                        child_span.set_attribute("pre_processing.modelInvocationOutput.parsedResponse.isValid", orchestration_trace.get("modelInvocationOutput", {}).get("parsedResponse", {}).get("isValid",{}))
                        child_span.set_attribute("pre_processing.modelInvocationOutput.traceId", orchestration_trace.get("modelInvocationOutput", {}).get("traceId", {}))
                    
                    if post_processing_trace:
                        child_span.set_attribute("post_processing_trace.modelInvocationOutput.rawResponse.content", orchestration_trace.get("modelInvocationOutput", {}).get("rawResponse", {}).get("content",{}))
                        child_span.set_attribute("post_processing_trace.modelInvocationOutput.parsedResponse.text", orchestration_trace.get("modelInvocationOutput", {}).get("parsedResponse", {}).get("text",{}))
                        child_span.set_attribute("post_processing_trace.modelInvocationOutput.traceId", orchestration_trace.get("modelInvocationOutput", {}).get("traceId", {}))
                    
                    llm_output = trace_segment.get("modelInvocationOutput", {}).get("metadata", {}).get("usage", {})
                    input_tokens = llm_output.get("inputTokens", 0)
                    output_tokens = llm_output.get("outputTokens", 0)

                    llm_call_count.add(1)
                    child_span.set_attribute(f"{parent_name}.input_tokens", input_tokens)
                    child_span.set_attribute(f"{parent_name}.output_tokens", output_tokens)
                    child_span.set_attribute(f"{parent_name}.status", trace_segment.get("status", "unknown"))
                    child_span.set_attribute(f"{parent_name}.metadata", json.dumps(trace_segment.get("metadata", {})))
        
        logger.debug("Processed Trace Data: %s", json.dumps(trace_data, indent=2))

def trace_decorator(func):
    """Decorator to handle tracing for Bedrock agent responses."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        with tracer.start_as_current_span("bedrock-agent-execution") as span:
            span.set_attribute("session.id", kwargs.get("session_id", "unknown"))
            agent_id = kwargs.get("agent_id")
            agent_alias_id = kwargs.get("agent_alias_id")

            if agent_id:
                span.set_attribute("agent.id", agent_id)
            if agent_alias_id:
                span.set_attribute("agent.alias_id", agent_alias_id)

            processed_events = []
            for event in func(*args, **kwargs):
                if isinstance(event, dict):
                    if "chunk" in event:
                        agent_answer = event["chunk"]["bytes"].decode('utf-8').replace("\n", " ")
                        span.set_attribute("agent.answer", agent_answer)
                        yield f"{agent_answer}"
                    elif "trace" in event:
                        process_trace_data(event, span)
                    elif "preGuardrailTrace" in event:
                        logger.debug(json.dumps(event["preGuardrailTrace"], indent=2))
                    else:
                        raise Exception("Unexpected event format", event)
                else:
                    yield event
    return wrapper
