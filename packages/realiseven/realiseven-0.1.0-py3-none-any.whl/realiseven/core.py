from openai import OpenAI

from realiseven.models import IsEven

client = OpenAI()


def is_even(n: int) -> bool:
    """
    Determines whether a given integer is even or odd.

    This function takes an integer as input
    and returns True if the number is even,
    and False if the number is odd.

    Args:
        n (int): The integer to be checked.

    Returns:
        bool: True if the number is even, False if the number is odd.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant who helps "
                    "user with his math questions.",
                },
                {"role": "user", "content": f"Is number {n} even?"},
            ],
            response_format=IsEven,
        )
        event = completion.choices[0].message.parsed
        return event.is_even
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        raise e
