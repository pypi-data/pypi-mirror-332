import inspect
from types import FrameType
from typing import Any
from pypactum._evaluation_semantic import EvaluationSemantic
from pypactum._assertion_kind import AssertionKind
from pypactum._contract_violation import ContractViolation
from pypactum._contract_violation_handler import invoke_contract_violation_handler
from pypactum._predicate import Predicate


def __handle_contract_violation(
    semantic: EvaluationSemantic,
    kind: AssertionKind,
    location: inspect.Traceback | None,
    kwargs: dict[str, Any],
    comment: str = "",
) -> None:
    """Handles a contract violation by invoking the contract violation handler and/or terminating if required"""

    violation = ContractViolation(
        comment=comment,
        kind=kind,
        location=location,
        semantic=semantic,
        kwargs=kwargs,
    )

    if semantic == EvaluationSemantic.check:
        invoke_contract_violation_handler(violation)


def assert_contract(
    semantic: EvaluationSemantic,
    kind: AssertionKind,
    calling_frame: FrameType | None,
    predicate: Predicate,
    predicate_kwargs: dict[str, Any],
) -> None:
    """Evaluates the given predicate and handles a contract violation if the result was false"""

    if semantic == EvaluationSemantic.ignore:
        return

    kwargs = {
        k: v
        for k, v in predicate_kwargs.items()
        if k in inspect.signature(predicate).parameters
    }
    pred_result = predicate(**kwargs)
    if not pred_result:
        __handle_contract_violation(
            semantic=semantic,
            kind=kind,
            location=(
                inspect.getframeinfo(calling_frame)
                if calling_frame is not None
                else None
            ),
            kwargs=kwargs,
        )
