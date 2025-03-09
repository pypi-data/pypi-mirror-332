from pathlib import Path

import git
import git.exc


def root() -> Path:
    repo = git.Repo(search_parent_directories=True)
    return Path(repo.working_dir)


def root_safe() -> Path:
    try:
        return root()
    except git.exc.InvalidGitRepositoryError:
        return Path()
