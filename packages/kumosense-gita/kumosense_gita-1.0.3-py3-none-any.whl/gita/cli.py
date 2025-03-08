import click
import threading
from .git_helper import get_diff, commit_and_push_git, commit_git
from .commit import generate_commit_message


@click.group()
def cli():
    """Gita - AI yordamida avtomatik commit yozish CLI"""
    pass


@click.command()
@click.option('--push', is_flag=True, help="Commitdan keyin avtomatik push qilish")
@click.option('--use-sticker', is_flag=True, help="Commit xabari oldiga emoji yoki sticker qo'shish")
def commit(push, use_sticker):
    """AI tomonidan avtomatik commit yozish"""
    diff = get_diff()

    if not diff.strip():
        click.echo("❌ Hech qanday o'zgarish topilmadi. Commit kerak emas.")
        return

    print("\r⏳ AI commit xabarini generatsiya qilmoqda...")
    # AI modeldan commit xabarini olish
    try:
        message = generate_commit_message(
            changes=diff, use_sticker=use_sticker)
    except ValueError as e:
        click.echo(f"❌ AI commit yaratishda xatolik: {e}")
        return
    except Exception as e:
        click.echo(f"❌ Kutilmagan xatolik: {e}")
        return

    # Commit xabarini ko‘rsatish va amalni bajarish
    click.echo(f"✅ Generated commit message: {message}")
    if push:
        commit_and_push_git(message)
    else:
        commit_git(message)


cli.add_command(commit)

if __name__ == "__main__":
    cli()
