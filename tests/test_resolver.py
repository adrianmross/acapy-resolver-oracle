"""Test Github Resolver."""

import pytest
from acapy_resolver_oracle.resolver import OracleResolver


@pytest.fixture
def resolver():
    yield OracleResolver()


@pytest.fixture
def profile():
    yield None


@pytest.mark.asyncio
async def test_resolve_dbluhm(resolver, profile):
    doc = await resolver.resolve(profile, "did:orcl:test")
    assert doc["id"] == "did:orcl:test"
