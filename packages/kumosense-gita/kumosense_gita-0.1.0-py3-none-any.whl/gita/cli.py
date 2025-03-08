import click
from .git_helper import get_diff, commit_and_push
from .commit import generate_commit_message

@click.group()
def cli():
    """Gita - AI yordamida avtomatik commit yozish CLI"""
    pass

@click.command()
@click.option('--push', is_flag=True, help="Commitdan keyin avtomatik push qilish")
def commit(push):
    """AI tomonidan avtomatik commit yozish"""
    
    diff = get_diff()

    if not diff.strip():
        print("❌ Hech qanday o'zgarish topilmadi. Commit kerak emas.")
        return

    # AI Model API chaqirish logikasi
    message = generate_commit_message(diff)  # Bu yerga haqiqiy AI model kodini qo‘shish kerak
    
    commit_and_push(message)
        
    if push:
        print("✅ O'zgarishlar GitHub'ga push qilindi.")


cli.add_command(commit)

if __name__ == "__main__":
    cli()

