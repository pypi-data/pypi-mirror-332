from typing import TYPE_CHECKING, Any, List, Optional, Tuple, Union

import structlog

from rasa.dialogue_understanding.patterns.validate_slot import (
    ValidateSlotPatternFlowStackFrame,
)
from rasa.shared.constants import (
    ACTION_ASK_PREFIX,
    UTTER_ASK_PREFIX,
)
from rasa.shared.core.events import Event, SlotSet
from rasa.shared.core.slots import Slot
from rasa.shared.core.trackers import DialogueStateTracker

if TYPE_CHECKING:
    from rasa.dialogue_understanding.commands import StartFlowCommand
    from rasa.shared.core.flows import FlowsList

structlogger = structlog.get_logger()


def start_flow_by_name(
    flow_name: str, flows: "FlowsList"
) -> Optional["StartFlowCommand"]:
    from rasa.dialogue_understanding.commands import StartFlowCommand

    if flow_name in flows.user_flow_ids:
        return StartFlowCommand(flow=flow_name)
    else:
        structlogger.debug(
            "command_parser.start_flow_by_name.invalid_flow_id", flow=flow_name
        )
        return None


def extract_cleaned_options(options_str: str) -> List[str]:
    """Extract and clean options from a string."""
    delimiters = [",", " "]

    for delimiter in delimiters:
        options_str = options_str.replace(delimiter, " ")

    return sorted(
        opt.strip().strip('"').strip("'") for opt in options_str.split() if opt.strip()
    )


def is_none_value(value: str) -> bool:
    """Check if the value is a none value."""
    if not value:
        return True
    return value in {
        "[missing information]",
        "[missing]",
        "None",
        "undefined",
        "null",
    }


def clean_extracted_value(value: str) -> str:
    """Clean up the extracted value from the llm."""
    # replace any combination of single quotes, double quotes, and spaces
    # from the beginning and end of the string
    return value.strip("'\" ")


def get_nullable_slot_value(slot_value: str) -> Union[str, None]:
    """Get the slot value or None if the value is a none value.

    Args:
        slot_value: the value to coerce

    Returns:
        The slot value or None if the value is a none value.
    """
    return slot_value if not is_none_value(slot_value) else None


def initialize_pattern_validate_slot(
    slot: Slot,
) -> Optional[ValidateSlotPatternFlowStackFrame]:
    """Initialize the pattern to validate a slot value."""
    if not slot.requires_validation():
        return None

    validation = slot.validation
    slot_name = slot.name
    return ValidateSlotPatternFlowStackFrame(
        validate=slot_name,
        refill_utter=validation.refill_utter or f"{UTTER_ASK_PREFIX}{slot_name}",  # type: ignore[union-attr]
        refill_action=f"{ACTION_ASK_PREFIX}{slot_name}",
        rejections=validation.rejections,  # type: ignore[union-attr]
    )


def create_validate_frames_from_slot_set_events(
    tracker: DialogueStateTracker,
    events: List[Event],
    validate_frames: List[ValidateSlotPatternFlowStackFrame] = [],
    should_break: bool = False,
    update_corrected_slots: bool = False,
) -> Tuple[DialogueStateTracker, List[ValidateSlotPatternFlowStackFrame]]:
    """Process SlotSet events and create validation frames.

    Args:
        tracker: The dialogue state tracker.
        events: List of events to process.
        should_break:  whether or not to break after the first non-SlotSet event.
            if True, break out of the event loop as soon as the first non-SlotSet
            event is encountered.
            if False, continue processing the events until the end.
        update_corrected_slots: whether or not corrected slots in the last
            correction frame need to be updated.

    Returns:
        Tuple of (updated tracker, list of validation frames).
    """
    for event in events:
        if not isinstance(event, SlotSet):
            if should_break:
                # we want to only process the most recent SlotSet events
                # so we break once we encounter a different event
                break
            continue

        slot = tracker.slots.get(event.key)
        frame = initialize_pattern_validate_slot(slot)

        if frame:
            validate_frames.append(frame)
            if update_corrected_slots:
                tracker = update_corrected_slots_in_correction_frame(
                    tracker, event.key, event.value
                )

    return tracker, validate_frames


def update_corrected_slots_in_correction_frame(
    tracker: DialogueStateTracker, slot_name: str, slot_value: Any
) -> DialogueStateTracker:
    """Update the corrected_slots and new_slot_values of the
    CorrectionPatternFlowStackFrame with only valid values.
    """
    stack = tracker.stack
    top_frame = stack.top()
    del top_frame.corrected_slots[slot_name]  # type: ignore[union-attr]
    top_frame.new_slot_values.remove(slot_value)  # type: ignore[union-attr]

    # since we can't directly modify a stack we have to pop first
    # and then push back the updated frame
    stack.pop()
    stack.push(top_frame)
    new_events = tracker.create_stack_updated_events(stack)
    tracker.update_with_events(new_events)
    return tracker
