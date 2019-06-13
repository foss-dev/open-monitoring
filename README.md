# Open Monitoring

Free & Open Source Server Monitoring and Management Tool

## Motivation

We are a group of people who develop free and open source applications. Our aim is developing free and open source server monitoring and management tool.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Your pull requests are should be clear. You should create a branch for your changes. For example;

**Bug fix**

`git checkout -b bug-fix-user-login-session-problem`

**New Feature**

`git checkout -b new-feature-system-ram-usage`

**Refactoring**

`git checkout -b refactoring-optimize-system-user-list-query`

As you understand, your branch's name should explain what have you done.

**Commits**

Your commits are should be clear. Your commits shouldn't be inconsistent. For example, these are the files you've changed.

```bash
system_users.py

installed_apps.py
```

You should add commit message for each one.

**Do**

```bash
git add system_users.py

git commit -m "System users changed"

git add installed_apps.py

git commit -m "Installed apps changed"
```

**Don't**

```bash
git add system_users.py installed_apps.py

git commit -m "System users changed"

# or

git commit -m "System users and installed apps changed"
```

**Don't Forget**

- Don't be shy to open an issue or send a pull request. No one will judge you.
- You're responsible for your commits. If someone opens an issue about your commit, try to solve.
- Try to write tests for your changes.
- Try to add changelog entry for your changes.
- Try to write document for your codes.