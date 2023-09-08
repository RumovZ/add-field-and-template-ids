import random
from typing import Callable

from aqt.gui_hooks import models_did_init_buttons
from aqt.models import Models
from aqt.operations.notetype import update_notetype_legacy
from aqt.utils import show_info

__version__ = "1.0.0"
__license__ = "AGPL 3"
__author__ = "RumovZ"
__url__ = "https://github.com/RumovZ/add-field-and-template-ids"

ModelButtons = list[tuple[str, Callable[[], None]]]


def generate_id() -> int:
    return random.randint(-(2**63), 2**63 - 1)


def on_add_ids(dialog: Models) -> None:
    field_ids = 0
    template_ids = 0
    notetype = dialog.current_notetype()
    templates = notetype["tmpls"]
    fields = notetype["flds"]

    for field in fields:
        if field["id"] is None:
            field_ids += 1
            field["id"] = generate_id()

    for template in templates:
        if template["id"] is None:
            template_ids += 1
            template["id"] = generate_id()

    if field_ids == template_ids == 0:
        show_info("All fields and templates already have IDs.")
        return

    update_notetype_legacy(parent=dialog, notetype=notetype).success(
        lambda _: show_info(
            f"Added IDs to {field_ids} of {len(fields)} fields and {template_ids} of "
            f"{len(templates)} templates of notetype {notetype['name']}."
        )
    ).run_in_background()


def on_models_did_init_buttons(buttons: ModelButtons, dialog: Models) -> ModelButtons:
    return buttons + [("Add IDs", lambda: on_add_ids(dialog))]


models_did_init_buttons.append(on_models_did_init_buttons)
