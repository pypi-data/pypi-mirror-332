from g4f.client import Client
import asyncio

if asyncio.get_event_loop().is_closed():
    asyncio.set_event_loop(asyncio.new_event_loop())


def generate_commit_message(changes: str, use_sticker: bool = False) -> str:
    """
    Git commit uchun AI yordamida commit xabarini generatsiya qiladi.

    Args:
        changes (str): Git o'zgarishlar diff ma'lumoti.
        use_sticker (bool): Agar True bo'lsa, commitga emoji yoki sticker qo'shiladi.

    Returns:
        str: AI tomonidan generatsiya qilingan commit xabari.
    """
    if not changes.strip():
        raise ValueError("O'zgarishlar bo'sh bo'lishi mumkin emas.")

    client = Client()

    system_prompt = "Sen git uchun O'zbekcha commit message yozadigan AI botisan."
    if use_sticker:
        system_prompt += " Emoji yoki sticker bilan commitni yanada aniqroq va chiroyliroq yoz."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Mana koddagi o‘zgarishlar:\n{changes}\nYaxshi commit yoz."}
        ],
        web_search=False
    )

    try:
        return response.choices[0].message.content.strip()
    except (AttributeError, IndexError):
        raise RuntimeError("AI javobida kutilmagan xatolik yuz berdi.")
