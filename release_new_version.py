#!/usr/bin/env python3

"""Script that releases a new version of the software."""

from releaser import Releaser
from releaser.steps import (
    Shell,
    CheckRstFiles,
    CheckTravis,
    InteractivelyApprovePackage,
    SetFutureVersion,
    SetVersionNumberInteractively,
    TwineUploadSource,
    TwineUploadWheel,
    Warn,
)
from releaser.git_steps import (
    EnsureGitClean,
    EnsureGitBranch,
    GitCommitVersionNumber,
    GitTag,
    GitPush,
    GitPushTags,
)

# These settings are used by multiple release steps below.
config = dict(
    github_user="nandoflorestan",  # TODO infer from .git/config
    github_repository="nine",
    branch="master",  # Only release new versions in this git branch
    changes_file=None,
    version_file="pyproject.toml",  # Read and write version number on this file
    version_keyword="version",  # Part of the variable name in that file
    log_file="release.log.utf-8.tmp",
    verbosity="info",  # debug | info | warn | error
)

# You can customize your release process below.
# Comment out any steps you don't desire and add your own steps.
Releaser(
    config,
    # ==================  Before releasing, do some checks  ===================
    Shell("py.test -s --tb=native nine"),  # First of all ensure tests pass
    # CheckRstFiles,  # Documentation: recursively verify ALL .rst files, or:
    CheckRstFiles("README.rst", "LICENSE.rst"),  # just a few.
    EnsureGitClean,  # There are no uncommitted changes in tracked files.
    EnsureGitBranch,  # I must be in the branch specified in config
    # InteractivelyEnsureChangesDocumented,     # Did you update CHANGES.rst?
    # Shell("poetry install")  # Ensure the package can be installed
    # CheckTravis,  # We run this late, so travis-ci has more time to build
    # ======================  All checks pass. RELEASE!  ======================
    SetVersionNumberInteractively,  # Ask for version and write to source code
    # Shell("./build_sphinx_documentation.sh"),  # You can write it easily
    Shell("poetry build"),  # Build sdist + wheel with poetry
    InteractivelyApprovePackage,  # Ask user to manually verify wheel content
    GitCommitVersionNumber,
    GitTag,  # Locally tag the current commit with the new version number
    Shell("poetry publish"),  # Upload source and wheel to https://pypi.org
    # ===========  Post-release: set development version and push  ============
    SetFutureVersion,  # Writes incremented version, now with 'dev1' suffix
    GitCommitVersionNumber("future_version", msg="Bump version to {0} after release"),
    # ErrorStep,  # You can use this step while testing - it causes a rollback.
    GitPush,  # Cannot be undone. If successful, previous steps won't roll back
    GitPushTags,
    # Warn("Do not forget to upload the documentation now!"),
).release()
