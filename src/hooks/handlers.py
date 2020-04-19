from uplink.decorators import _BaseHandlerAnnotation
from uplink.hooks import RequestAuditor


class request_handler(_BaseHandlerAnnotation, RequestAuditor):
    pass


@request_handler(requires_consumer=True)
def static_locale(consumer, request_builder):
    request_builder.info["params"].update(
        {"namespace": "static-" + consumer.client_config.region.name}
    )


@request_handler(requires_consumer=True)
def dynamic_locale(consumer, request_builder):
    request_builder.info["params"].update(
        {"namespace": "dynamic-" + consumer.client_config.region.name}
    )
