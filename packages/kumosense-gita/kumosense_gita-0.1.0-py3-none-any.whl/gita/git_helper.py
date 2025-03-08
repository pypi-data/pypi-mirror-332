import git

def get_repo():
    return git.Repo(".")

def get_diff():
    repo = get_repo()
    return repo.git.diff()

def commit_and_push(message):
    repo = get_repo()
    repo.git.add(A=True)
    repo.index.commit(message)
    origin = repo.remote(name="origin")
    origin.push()
    print(f"✅ AI commit yaratildi va push qilindi: {message}")

