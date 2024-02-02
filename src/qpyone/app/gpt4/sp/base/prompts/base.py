from qpyone.app.gpt4.sp.base.schemas import Messages


def format_prompt(messages: Messages, add_special_tokens=False) -> str:
    """
    Format a series of messages into a single string, optionally adding special tokens.

    Args:
        messages (Messages): A list of message dictionaries, each containing 'role' and 'content'.
        add_special_tokens (bool): Whether to add special formatting tokens.

    Returns:
        str: A formatted string containing all messages.
    """
    if not add_special_tokens and len(messages) <= 1:
        return messages[0]["content"]
    formatted = "\n".join([
        f'{message["role"].capitalize()}: {message["content"]}'
        for message in messages
    ])
    return f"{formatted}\nAssistant:"
