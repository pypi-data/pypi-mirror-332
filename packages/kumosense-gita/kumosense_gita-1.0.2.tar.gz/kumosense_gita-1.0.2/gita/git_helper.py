import git


def get_repo():
    return git.Repo(".")


def get_diff():
    repo = get_repo()
    # Staged o‘zgarishlarni ham qo‘shish
    return repo.git.diff() + "\n" + repo.git.diff("--cached")


def commit_git(message):
    repo = get_repo()
    repo.git.add(A=True)
    repo.index.commit(message)
    # "push qilindi" olib tashlandi
    print(f"✅ AI commit yaratildi:\n\n{message}")


def commit_and_push_git(message):
    repo = get_repo()
    commit_git(message)
    origin = repo.remote(name="origin")
    origin.push()  # Push qilish kerak
    print("✅ O'zgarishlar GitHub'ga push qilindi.")
