"""ACA-Py Resolver Oracle."""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.resolver.did_resolver import DIDResolver

from .resolver import OracleResolver


async def setup(context: InjectionContext):
    """Setup the plugin."""
    registry = context.inject(DIDResolver)
    resolver = OracleResolver()
    await resolver.setup(context)
    registry.append(resolver)
