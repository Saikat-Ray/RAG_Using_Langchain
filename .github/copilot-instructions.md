# Git check-in workflow

When the user asks to "check in" changes, review the diff, create a concise commit message that describes the changes, commit them, and push the current branch to its configured remote.

- Include intended source code, notebooks, documentation, and project configuration changes.
- Exclude cache files, temporary files, virtual environments, secrets, and generated local data such as vector-store databases and indexes.
- Inspect untracked files before staging; stage only intended project files rather than using an unqualified `git add .`.
- Do not include unrelated pre-existing changes in the commit.
- Confirm the current branch and remote status before committing, then verify the push succeeded and report the commit.
- Ask before proceeding if it is unclear whether an untracked or generated file is meant to be part of the project.
