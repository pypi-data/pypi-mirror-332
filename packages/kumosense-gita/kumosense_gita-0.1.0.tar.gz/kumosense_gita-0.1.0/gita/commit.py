from g4f.client import Client

client = Client()

def generate_commit_message(changes):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sen git uchun O'zbekcha commit message yozadigan AI bot san."},
            {"role": "user", "content": f"Mana koddagi o‘zgarishlar:\n{changes}\nYaxshi commit yoz."}
        ],
        web_search=False
    )
    return response.choices[0].message.content
