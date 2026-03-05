"""AI-generated unit tests for interactions module."""

import pytest
from app.routers.interactions import filter_by_max_item_id
from app.models.interaction import InteractionLog

def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    from datetime import datetime
    return InteractionLog(
        id=id,
        learner_id=learner_id,
        item_id=item_id,
        created_at=datetime.now(),
        kind="view"
    )

# KEPT: tests filtering with empty list edge case
def test_filter_empty_list_returns_empty_list() -> None:
    result = filter_by_max_item_id(interactions=[], max_item_id=5)
    assert result == []

# KEPT: tests filtering with negative max_item_id
def test_filter_with_negative_max_item_id() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 1, 2)]
    result = filter_by_max_item_id(interactions=interactions, max_item_id=-1)
    assert result == []

# DISCARDED: duplicates existing test_filter_includes_interaction_at_boundary
# def test_filter_boundary_duplicate() -> None:
#     interactions = [_make_log(1, 1, 2)]
#     result = filter_by_max_item_id(interactions=interactions, max_item_id=2)
#     assert len(result) == 1
