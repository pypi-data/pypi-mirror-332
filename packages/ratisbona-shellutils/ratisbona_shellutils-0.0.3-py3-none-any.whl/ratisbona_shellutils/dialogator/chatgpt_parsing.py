import json
from datetime import datetime, date
from fnmatch import fnmatch
from pathlib import Path
from typing import Dict, List, Iterable, Any

from ratisbona_utils.functional import nth_element, first
from ratisbona_utils.monads import has_keyvalue, Just, Maybe, Nothing
from ratisbona_utils.strings import shorten

ChatTitle = str
ChatGptConversation = dict
ChatGptFileContent = Iterable[ChatGptConversation]
ChatGptMessage = Any


def find_root_messages(message_dict: Dict) -> List[Dict]:
    result = [
        message
        for message in message_dict.values()
        if not has_keyvalue(message, "parent")
    ]
    return result


def get_message_sequence(root_message, message_dict, indent=""):
    maybe_root_message = Just(root_message)
    print(indent + "INFO: Get Message Sequence for: id=", maybe_root_message["id"])
    all_childs = []
    for maybe_child_id in Just(root_message)["children"]:
        maybe_child = Just(message_dict)[maybe_child_id]
        if not maybe_child:
            print(indent + f"Warning! Message {maybe_child_id} could not be found!")
            continue
        print(indent + "INFO: Child found: id=", maybe_child_id)
        all_childs.append(maybe_child)

    sequence = [root_message]
    all_childs.sort(key=message_key_function)

    for idx, child in enumerate(all_childs):
        if idx > 0:
            print(indent + "WARNING: More than one child is unexpected!")
        maybe_child_childs = child.bind(get_message_sequence, message_dict, indent + " ")
        if maybe_child_childs:
            sequence.extend(maybe_child_childs.unwrap_value())
    return sequence


def detect_date(message) -> Maybe[datetime]:
    maybe_message = Just(message)
    return maybe_message["message"]["create_time"].bind(datetime.fromtimestamp)


def extract_create_time_from_conversation(
    conversation: ChatGptConversation,
) -> Maybe[datetime]:
    return Just(conversation)["create_time"].bind(datetime.fromtimestamp)


def maybe_parse_json(a_string: str) -> Maybe[Dict]:
    try:
        return Just(json.loads(a_string))
    except json.JSONDecodeError as jde:
        print(
            f"Cannot parse {a_string} as JSON: {jde}. Line: {jde.lineno}, Column: {jde.colno} Pos {jde.pos} Text there: ->{a_string[jde.pos-10:jde.pos+10]}<-"
        )
        print(jde.__dict__)
    return Nothing


def try_hard_parsing_json(a_string: str) -> Maybe[Dict]:
    stripped_start = a_string.lstrip()[:10]

    if (
        len(stripped_start) == 0 or stripped_start[0] not in "{["
    ):  # Ok, I don't see how it could be a JSON-String...
        print("INFO: Not a JSON-String: ", shorten(a_string, 80))
        return Nothing

    a_string = a_string.replace(r"\-", r"\\-")

    maybe_parseresult = maybe_parse_json(a_string)
    if maybe_parseresult:
        return maybe_parseresult

    manipulated_string = a_string.replace("\\\\", "\\")
    maybe_parseresult = maybe_parse_json(manipulated_string)
    if maybe_parseresult:
        return maybe_parseresult

    print("WARNING: Looks like json but it seems it isnt: ", shorten(a_string, 80))

    return Nothing


def handle_string_message(part):
    content = part.replace("\\n", "\n")
    if len(content.strip()) > 0:
        if not content.endswith("\n"):
            content += "\n"
        return content
    return ""


def maybe_code_message(json_partcontent: Dict) -> Maybe[str]:
    maybe_partcontent = Just(json_partcontent)
    maybe_language = (
        maybe_partcontent["type"].bind(str.split, "/", 1).bind(nth_element(1))
    )
    maybe_content = maybe_partcontent["content"].bind(str.replace, "```", "''")
    return maybe_language.bind(
        lambda language, content: Just(f"```{language}\n{content}\n```\n"),
        maybe_content,
    )


def maybe_update_message(json_partcontent: Dict) -> Maybe[str]:
    maybe_partcontent = Just(json_partcontent)
    maybe_updates = maybe_partcontent["updates"]

    result = ""
    for maybe_update in maybe_updates:
        maybe_pattern = maybe_update["pattern"]
        maybe_replacement = maybe_update["replacement"]
        if not maybe_pattern or not maybe_replacement:
            print("WARNING! Incomprehensible Update: ", maybe_update)
            result += f"#Warning incomprehensible update!\n```\n{maybe_update}\n```"
        result += maybe_pattern.bind(
            lambda p, r: f"**Update**\nPattern: `{p}`\n```{r}\n```\n", ""
        ).default_or_throw("")
    return Just(result)


def maybe_textid_message(json_partcontent: Dict) -> Maybe[str]:
    maybe_partcontent = Just(json_partcontent)

    if not maybe_partcontent["textdoc_id"]:
        return Nothing

    return maybe_partcontent["result"]


def handle_json_str_message(json_partcontent: Maybe[Dict]):

    maybe_result = (
        json_partcontent.bind(maybe_code_message)
        or json_partcontent.bind(maybe_textid_message)
        or json_partcontent.bind(maybe_update_message)
    )

    if not maybe_result:
        print("ERROR! Unhandled JSON-Content: ", json_partcontent)

    return maybe_result


def handle_text_message_parts(maybe_parts: Maybe[List[str]]) -> str:
    result = ""
    for maybe_part in maybe_parts:
        maybe_understood = maybe_part.bind(try_hard_parsing_json).bind(
            handle_json_str_message
        ) or maybe_part.bind(handle_string_message)
        if not maybe_understood:
            print(f"WARNING! Unhandled text message part: {maybe_part}")
        else:
            result += maybe_understood.unwrap_value()
    return result


def search_dir(dir: Path, pointer: str) -> Maybe[Path]:
    """
    Search for a file in a directory fitting an (sanitized, remove protocol and file- prefix) assess-pointer.
    Prefers everything over webp.

    Args:
        dir: The directory to search in.
        pointer: The pointer to search for.
    Returns:
        Maybe[Path]: The found file or Nothing.
    """
    if not dir.exists():
        return Nothing

    found_file = Nothing
    for file in dir.iterdir():
        if pointer in file.name:
            if file.suffix.lower() in [".webp"]:
                found_file = Just(file)
            else:
                return Just(file)
    return found_file

def find_file_from_pointer(pointer: str) -> Maybe[Path]:
    # search in dalle-generations
    dalle_generations = Path("dalle-generations")

    # Remove prefixes from pointer
    remove_words = ["file-service", ":", "/", "file-"]
    while True:
        did_something = False
        for word in remove_words:
            if pointer.startswith(word):
                pointer = pointer.removeprefix(word)
                did_something = True
        if not did_something:
            break

    # Try tp find it...
    return search_dir(dalle_generations, pointer) or search_dir(Path("."), pointer)






def handle_multimodal_message_parts(maybe_parts: Maybe[List[str]]) -> str:
    result = ""
    for maybe_part in maybe_parts:

       # Handle asset-pointers.
       if maybe_part["content_type"] == "image_asset_pointer":
            maybe_file = maybe_part["asset_pointer"].bind(find_file_from_pointer).maybe_warn("Could not find file!")
            if maybe_file:
                file = maybe_file.unwrap_value()
                result += f"![{file.name}]({file})\n"
            continue

       print(f"WARNING! Unhandled multimodal_message_part: {maybe_part}")

    return result


def translate_message(message: ChatGptMessage)->str:
    maybe_message = Just(message)
    print("INFO: Translate Message:" + maybe_message["id"])
    maybe_inner = maybe_message["message"]
    author = maybe_inner["author"]["role"].default_or_throw("?")
    maybe_content_type = maybe_inner["content"]["content_type"]
    print("INFO: Content-Type: " + maybe_content_type)
    maybe_parts = maybe_inner["content"]["parts"]

    if maybe_content_type == "text":
        result = handle_text_message_parts(maybe_parts)
    elif maybe_content_type == "multimodal_text":
        result = handle_multimodal_message_parts(maybe_parts)
    else:
        print("WARNING: Unknown Content-Type: " + maybe_content_type)
        result = ""

    if result:
        result = f"## {author}\n\n" + result
    return result


def message_key_function(message):
    maybe_date = detect_date(message)
    if not maybe_date:
        print(
            f"WARNING: Message-Key-Function: Could not extract date from message:"
            + shorten(str(message), 80)
        )
    return maybe_date.default_or_throw(datetime.min)


def debug_print_message(message):
    the_id_or_replacement = Just(message)["id"].default_or_throw("No ID")
    message_date = (
        Just(message)
        .bind(detect_date)
        .bind(datetime.isoformat)
        .default_or_throw("No Date")
    )
    message_content = (
        Just(message)["message"]["content"]
        .bind(str)
        .bind(shorten, 80)
        .default_or_throw("No Content")
    )
    children = (
        "children"
        if Just(message)["children"].bind(len).default_or_throw(0) > 0
        else "no children"
    )
    print(
        f"Root-Message id: {the_id_or_replacement} Date: {message_date} {children} "
        f"Content: ->{message_content}<-"
    )


def maybe_extract_title(conversation: ChatGptConversation) -> Maybe[str]:
    return Just(conversation)["title"]


def filter_conversations(
    conversations: ChatGptFileContent,
    title_filter: str = "*",
    date_filter_after: datetime = None,
    date_filter_before: datetime = None,
) -> list[tuple[ChatTitle, date, ChatGptConversation]]:

    output_conversations = []

    for conversation in conversations:
        title = maybe_extract_title(conversation).default_or_throw("No Title found")

        the_date = (
            extract_create_time_from_conversation(conversation)
            .bind(datetime.date)
            .default_or_throw(date.min)
        )

        if (
            (title_filter is None or fnmatch(title.lower(), title_filter.lower()))
            and (date_filter_after is None or the_date >= date_filter_after.date())
            and (date_filter_before is None or the_date <= date_filter_before.date())
        ):
            output_conversations.append((title, the_date, conversation))

    output_conversations.sort(key=nth_element(1))
    return output_conversations


def translate_conversation(conversation) -> tuple[str, str, Maybe[date]]:
    maybe_conversation = Just(conversation)

    title = maybe_conversation["title"].default_or_throw("No Title found")
    maybe_messages = maybe_conversation["mapping"]
    maybe_root_msgs = maybe_messages.bind(find_root_messages)
    maybe_root_msgs = maybe_root_msgs.bind(sorted, key=message_key_function)

    num_root_msgs = maybe_root_msgs.bind(len).default_or_throw(0)

    if num_root_msgs == 0:
        print("WARNING: No Root-message found")
    if num_root_msgs > 1:
        print("WARNING: More than one Root-message found")
        for maybe_root_msg in maybe_root_msgs:
            maybe_root_msg.bind(debug_print_message)
        print()

    result = ""
    last_date = Nothing
    first_date = Nothing
    for maybe_root_msg in maybe_root_msgs:
        print(
            "INFO: Translate Conversation: Tackling first rootmessage: id="
            + maybe_root_msg["id"]
            + " keys:"
            + maybe_root_msg.bind(dict.keys)
        )

        maybe_message_sequence = maybe_root_msg.bind(
            get_message_sequence, maybe_messages
        )

        for maybe_message in maybe_message_sequence:
            new_date = maybe_message.bind(detect_date).bind(datetime.date)
            first_date = first_date or new_date

            if new_date and new_date != last_date:
                result += (
                    f"# {new_date.bind(date.isoformat).default_or_throw('??')}\n\n"
                )
                last_date = new_date
            result += translate_message(maybe_message)

    return title, result, first_date
