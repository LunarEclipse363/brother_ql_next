## Developement Workflow
- commits in the `main` branch are set in stone
- commits in other branches may be shuffled around
- [API docs](https://lunareclipse363.github.io/brother_ql_next/) are a good starting point to understanding the codebase
- please clean up your commits in PRs:
  - the goal is to have meaningful commits with useful diffs
  - so merge small fixups within a PR into a single commit
  - make use of `git rebase -i` to merge/reorder commits
  - (optional) make use of `git add -i` for precise selection of diffs

## Release Checklist
1. [ ] update the version in `pyproject.toml`
2. [ ] update the version in `CHANGELOG.md`
3. [ ] create a tag following semver (example: `v0.11.1`)
4. [ ] create a GitHub release, include relevant part of the changelog
5. [ ] verify that CI ran successfully and a PyPi release was published
