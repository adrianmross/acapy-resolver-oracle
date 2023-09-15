"""ACA-Py Resolver Github."""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.resolver.did_resolver import DIDResolver

from .resolver import OracleResolver


async def setup(context: InjectionContext):
    """Setup the plugin."""
    registry = context.inject(DIDResolver)
    assert isinstance(registry, DIDResolver)
    registry.register(OracleResolver())
