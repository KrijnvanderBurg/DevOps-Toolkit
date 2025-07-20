---
title: "Shared Configuration Architecture: Why Your DevOps Setup is Broken and How to Fix It"
date: 2025-01-20
excerpt: "Most DevOps setups fail because local development and CI/CD use different configurations. Learn how shared configuration architecture with nested submodules solves this fundamental problem."
tags:
- devops
- configuration
- submodules
- consistency
- architecture
image: /assets/graphics/2025-01-20-shared-configuration-architecture/thumbnail-shared-config.png
pin: false
---

Every developer knows the frustration: code passes locally but fails in CI/CD. You format with Black locally using 88 characters, but the pipeline runs with 120. You run `pytest` with specific flags in development, but the CI uses completely different parameters. The result? Endless debugging cycles and configuration drift that wastes hours of productive time every week.

This isn't just an inconvenience—it's a fundamental architectural flaw in how we approach DevOps tooling. Most setups treat local development and CI/CD as separate worlds, each with their own configurations, scripts, and execution patterns. What starts as "optimized" settings for each environment inevitably becomes a maintenance nightmare where nobody remembers why the configurations diverged in the first place.

## The Core Problem: Configuration Drift by Design

The typical DevOps setup looks something like this:

**Local Development:**
```bash
# In your IDE or terminal
ruff --line-length=88 --select=E,F src/
mypy --strict --config-file=local-mypy.ini src/
pytest tests/ --cov=src --cov-report=html
```

**CI/CD Pipeline:**
```yaml
# In your pipeline
- script: ruff --line-length=120 --select=E,F,W src/
- script: mypy --ignore-missing-imports src/
- script: pytest tests/ --cov=src --cov-report=xml --junit-xml=results.xml
```

Notice the differences? Different line lengths, different mypy configurations, different pytest outputs. This isn't an accident—it's how most teams set up their tooling, with "optimized" settings for each environment.

**The inevitable result:** Code that passes locally fails in CI, or worse, code that passes CI fails when colleagues pull it and run local checks. This problem has gotten worse as development tools have multiplied. Modern Python projects routinely use 10+ quality tools—formatters, linters, type checkers, security scanners—each with their own configuration files and CLI parameters. 

Multiplying this across local development, CI/CD, and multiple team members creates a configuration management nightmare that traditional approaches can't solve. You end up with a dozen different `.yml`, `.ini`, `.toml`, and `.json` files scattered across repositories, each slightly different, and nobody quite sure which one is the "source of truth" for any given environment.

## The Solution: Shared Configuration Architecture

Instead of maintaining separate configurations, what if both local and CI/CD environments used **exactly the same command with exactly the same configuration file**? This is where the shared configuration architecture comes in—not as a theoretical concept, but as a proven implementation with real-world examples.

> 🎯 **See it in action:** The [zero-drift-devops-framework](https://github.com/KrijnvanderBurg/zero-drift-devops-framework) demonstrates this exact architecture with 25+ CI/CD templates and 20+ integrated development tools—all using shared configuration patterns you can study and adapt.

The core principle is simple but powerful: **One script, one config, consistent execution everywhere.** This means your local development environment and your CI/CD pipeline don't just use similar configurations—they use the identical configuration files and execution scripts. When something works locally, it's guaranteed to work in CI/CD because there's literally no difference between the two environments.

![DevContainer Startup Tasks](https://github.com/KrijnvanderBurg/zero-drift-devops-framework/raw/main/docs/devcontainer_startup_tasks_and_problems.gif)
*Watch 20+ development tools configure automatically in a DevContainer using shared configurations*

![Azure DevOps Pipeline Screenshot](https://github.com/KrijnvanderBurg/zero-drift-devops-framework/raw/main/docs/azure_devops_pipeline_screenshot.png)
*Azure DevOps pipeline using the same shared configurations and scripts that run locally*

### The Architecture: Nested Submodules Pattern

The solution uses a two-tier submodule structure:

```
your-project/
├── .devcontainer/           # Git submodule for development environments
│   └── .dotfiles/           # Nested submodule with shared configs & scripts
├── .azuredevops/           # Git submodule for CI/CD templates  
│   └── .dotfiles/           # Same nested submodule again (shared)
└── your-source-code/
```

The `.dotfiles` repository contains three essential components that make this work: **Configuration files** for every development tool (your `ruff.toml`, `mypy.ini`, `pytest.ini`, etc.), **standardized shell scripts** that execute tools with consistent parameters across environments, and **unified output formats** for reports and logging that work identically whether you're running locally or in CI/CD.

This isn't just about copying config files around—it's about creating a single source of truth that's automatically synchronized across every environment where your code runs.

### The Nested Submodule Strategy

The architectural genius lies in how the `.dotfiles` repository is embedded as a nested submodule within both `.devcontainer` and `.azuredevops`. This creates a modular system where each component is completely self-contained while sharing the same configuration foundation.

When you add the `.devcontainer` submodule to a project, you're not just getting the DevContainer configuration—you're getting the entire `.dotfiles` ecosystem embedded within it. The same applies to `.azuredevops` templates. This means each solution can operate independently while maintaining perfect configuration synchronization. If a team only wants to adopt the DevContainer setup without touching CI/CD, they simply add the `.devcontainer` submodule and instantly have access to all shared configurations, scripts, and tooling standards.

**⚠️ Critical Setup Note:** Because of the nested submodule structure, you must always use `git submodule update --recursive --init` when cloning or updating repositories that use this architecture. The `--recursive` flag is essential—without it, the nested `.dotfiles` submodule won't be initialized, and your shared configurations will be missing.

This nested approach solves a critical adoption problem: teams can incrementally adopt shared configuration architecture without requiring wholesale changes to their existing setup. Start with just local development consistency, then add CI/CD templates later, all while using the same underlying configuration foundation.

### How It Works in Practice

When you run a code quality check locally in VS Code:

```jsonc
// VS Code Task Definition
{
   "label": "ruff-linter",
   "type": "shell",
   "command": "${workspaceFolder}/.devcontainer/.dotfiles/python/scripts/ruff_linter.sh", // Same script
   "args": [
      "${workspaceFolder}/src", // Same target path
      "${workspaceFolder}/.devcontainer/.dotfiles/python/ruff.toml" // Same config file
   ],
   "group": "test",
   "presentation": {
      "echo": true,
      "reveal": "always",
      "panel": "new"
   }
}
```

When your CI/CD pipeline runs the same check:

```js
// Azure DevOps Pipeline Template
resources:
  repositories:
    - repository: templates
      type: git
      name: YourOrg/.azuredevops

steps:
- checkout: self
  submodules: recursive
- script: |
    $(Build.Repository.LocalPath)/.azuredevops/.dotfiles/python/scripts/ruff_linter.sh \ // Same script
      $(Build.Repository.LocalPath)/src \ // Same target path
      $(Build.Repository.LocalPath)/.azuredevops/.dotfiles/python/ruff.toml // Same config file
  displayName: 'Ruff Linter'
```

**Critical insight:** Both environments execute the **exact same shell script** with the **exact same configuration file**. The `.dotfiles` submodule ensures this consistency automatically, eliminating the possibility of configuration drift between environments.

The technical implementation has one crucial detail that's actually a feature, not a limitation: Azure DevOps can't see inside submodules when creating pipelines—it only sees the submodule URL reference. This forces you to structure the templates correctly, with external repository references that ensure proper submodule checkout during execution. What initially seems like a constraint becomes an architectural advantage that enforces best practices.

> 💡 **Want to see this in action right now?** Clone the [complete implementation repository](https://github.com/KrijnvanderBurg/zero-drift-devops-framework) and run `git submodule update --recursive --init` to see how the nested submodule structure works with real-world examples.

## Why This Changes Everything

### Perfect Quality Gate Alignment

When local checks pass, remote execution is **guaranteed** to pass because both environments use the same script, same config, and same containerized environment. This eliminates the guesswork and debugging cycles that plague traditional DevOps setups where you're constantly wondering if some subtle configuration difference will cause a surprise failure.

Think about the last time you had a CI/CD pipeline fail on a linting check that passed locally. You probably spent too long investigating the differences, updating configurations, and re-running the pipeline. With shared configuration architecture, this category of failure simply doesn't exist—if it passes locally, it passes in CI/CD, period.

### Single Point of Maintenance  

Need to update your linting rules? Change them once in the `.dotfiles` repository and they automatically apply to every developer's local environment and every CI/CD pipeline. No more hunting down configuration files scattered across different systems, no more "I forgot to update the CI config when I changed the local rules," and no more debugging sessions where you discover that someone updated the local config six months ago but never synchronized it with the pipeline.

This single point of maintenance extends beyond just linting rules. Want to add a new pre-commit hook? Update a security scanning policy? Change the test runner configuration? You make the change once, and it propagates instantly to every environment. The maintenance overhead drops from "update N different places and hope you didn't miss one" to "update one place and you're done."

> 🔧 **See the maintenance magic:** The [zero-drift-devops-framework](https://github.com/KrijnvanderBurg/zero-drift-devops-framework) repository demonstrates this single-source-of-truth approach with real configurations. Browse the `.dotfiles` submodule to see how 20+ tools share configurations seamlessly.

## The Technical Implementation

The magic happens through a nested submodule structure where the same `.dotfiles` repository is shared between your DevContainer and CI/CD templates.

```bash
.dotfiles/
├── python/
│   ├── ruff.toml               # Ruff configuration
│   ├── .pylintrc               # Pylint rules  
│   ├── mypy.ini                # Type checking config
│   └── scripts/
│       ├── ruff_linter.sh      # Standardized Ruff execution
│       ├── pylint.sh           # Standardized Pylint execution
│       └── mypy.sh             # Standardized type checking
```

Every script follows the same pattern: it takes a target path and config file, installs the tool if needed, then executes with consistent parameters. Here's the actual implementation:

```bash
#!/bin/bash
target_path="${1:-$PWD}" && echo "Scanning folder: $target_path"
config_filepath="${2}" && echo "Config file: $config_filepath"

# Install ruff if not already installed (handles fresh containers)
if ! command -v ruff &> /dev/null; then
    echo "Installing ruff..."
    pip install ruff --quiet
fi
echo -n "ruff version: " && ruff --version

# Execute with the shared configuration
ruff check "$target_path" --config "$config_filepath" --no-fix --diff --show-files
```

The beauty is in the simplicity—same script, same config, consistent execution everywhere. No more wondering if your local Ruff version matches CI, or if the flags are the same, or if the config file is even being found.

> 💻 **Study the real implementations:** The [.dotfiles repository](https://github.com/KrijnvanderBurg/.dotfiles) contains the actual scripts shown above. Explore Python, security, infrastructure, and Git automation scripts that you can copy and adapt for your own projects.

## Beyond Python: A Universal Pattern

While this example focuses on Python, the same architecture works for any technology stack. The implementation I'm showing you already includes security scanning (Semgrep, Bandit), infrastructure validation (OpenTofu/Terraform), Git operations, and more. Think of it as a universal pattern that scales horizontally across your entire development ecosystem rather than just vertically within one technology.

The pattern is technology-agnostic: if you have a command-line tool with configuration files, you can apply this architecture. JavaScript teams use it for ESLint and Prettier, Infrastructure teams use it for Terraform validation, Security teams use it for vulnerability scanning, and DevOps teams use it for Docker builds and deployments.

The key insight is that most development tools follow the same pattern: `tool-name target-path config-file`. Once you standardize this into shared scripts, the consistency benefits compound across every tool in your stack. You're not just solving the linting inconsistency problem—you're solving the entire "configuration drift between environments" problem that affects every single tool in modern software development.

> 📖 **Interested in the broader DevOps philosophy?** Read about [enforcing code quality via CI/CD](2024-12-11-enforce-code-quality-via-cicd.md) and how this shared configuration approach fits into a complete zero-drift DevOps strategy.

## Getting Started

Start small with surgical precision. Pick one tool that's causing you the most local/CI inconsistency headaches—usually a code formatter like Ruff or Black. Don't try to boil the ocean on day one; focus on proving the pattern works with something that's already frustrating you daily.

Here's your first-day implementation that you can complete in under an hour:

1. **Create a `.dotfiles` repository** with a simple structure: `python/ruff.toml` for config and `python/scripts/ruff_formatter.sh` for execution
2. **Write a basic script** that takes a target path and config file path as parameters
3. **Add it as a submodule** to your existing project: `git submodule add <your-dotfiles-repo> .dotfiles`
4. **Initialize the submodule properly**: `git submodule update --recursive --init` (the `--recursive` flag is critical for nested submodules)
5. **Create a VS Code task** that calls your script with the shared config
6. **Update your CI/CD pipeline** to call the same script with the same config

> 🚀 **Ready to dive deeper?** Check out my comprehensive guide on [DevContainers with automated workflow tasks](2024-11-11-devcontainers-automate-workflow-tasks.md) to see how VS Code tasks integrate with this shared configuration approach.

Once you see how much debugging time you save with just one tool, expanding to your entire toolchain becomes compelling. The initial complexity pays off immediately once you have even 2-3 tools configured consistently. More importantly, once your teammates experience the reliability of perfectly consistent tooling, they'll start asking when you're going to add the same treatment to other tools.

## The Result

This architecture eliminates the fundamental inconsistency that plagues most DevOps setups. When developers can trust that local success means CI/CD success, everything changes—their relationship with the development workflow, their confidence in making changes, and their willingness to actually use quality tools rather than treating them as necessary evils.

No more surprise pipeline failures that kill momentum. No more environment debugging sessions that turn a 5-minute fix into a 45-minute investigation. No more "I'll just disable this check locally because I can never get it to match CI" workarounds. Just reliable, consistent tooling that actually works the same way everywhere, every time.

The shared configuration architecture isn't just about technical consistency—it's about creating DevOps workflows that developers actually want to use instead of workflows they merely tolerate.

![DevContainer Startup Tasks](https://github.com/KrijnvanderBurg/zero-drift-devops-framework/raw/main/docs/devcontainer_startup_tasks_and_problems.gif)
*Watch 20+ development tools configure automatically in a DevContainer using shared configurations*


## Take Action: Start Your Zero-Drift DevOps Journey

Ready to eliminate configuration drift from your development workflow? Here's how to get started:

### 🛠️ **Explore the Complete Implementation**
- **Main Repository**: [zero-drift-devops-framework](https://github.com/KrijnvanderBurg/zero-drift-devops-framework) - The complete example repository demonstrating this architecture with 25+ CI/CD templates and 20+ integrated development tools
- **DevContainer Setup**: [.devcontainer](https://github.com/KrijnvanderBurg/.devcontainer) - Experience shared configuration in action with specialized environments for Python, Spark, and infrastructure
- **CI/CD Templates**: [.azuredevops](https://github.com/KrijnvanderBurg/.azuredevops) - Study 25+ production-ready pipeline templates that compose into complete CI/CD solutions
- **Shared Configurations**: [.dotfiles](https://github.com/KrijnvanderBurg/.dotfiles) - The magic behind the consistency—explore the actual config files and scripts that make everything work
- **⚠️ Remember**: Always run `git submodule update --recursive --init` when cloning these repositories due to the nested submodule structure

### 📚 **Deep Dive into Related Concepts**
Transform your entire DevOps approach with these complementary guides:
- [DevContainers: Add Code Quality Tools](2024-10-22-devcontainers-add-code-quality-tools.md) - Learn how quality tools integrate with this architecture
- [DevContainers: Automate Workflow Tasks](2024-11-11-devcontainers-automate-workflow-tasks.md) - See how VS Code tasks work with shared configurations  
- [Enforce Code Quality via CI/CD](2024-12-11-enforce-code-quality-via-cicd.md) - Understand how shared configuration fits into broader quality strategies
- [Automatic Tests and Code Coverage](2024-12-14-automatic-tests-code-coverage.md) - Apply the same consistency principles to testing workflows
- [Local Multi-Node Spark Cluster](2025-04-20-local-spark-cluster-devcontainer.md) - See shared configuration applied to distributed computing environments

### 💬 **Connect and Share Your Experience**
Found this approach useful? Have questions about implementing it in your specific stack? 
- **Follow my work**: [Medium profile](https://medium.com/@krijnvandenburg) for more DevOps insights and practical implementations
- **Star the main repository**: [zero-drift-devops-framework](https://github.com/KrijnvanderBurg/zero-drift-devops-framework) - if this solves a real problem for your team, starring helps other developers discover these solutions
- **Explore the methodology**: Check out the [complete blog series](https://medium.com/@krijnvandenburg) covering DevContainers, CI/CD templates, and zero-drift DevOps philosophy
- **Share your implementation** - I'd love to see how you adapt this architecture for your specific technology stack

> 🎯 **Quick Start Challenge:** Can you get the [zero-drift-devops-framework](https://github.com/KrijnvanderBurg/zero-drift-devops-framework) running in a DevContainer in under 5 minutes? Clone it, run `git submodule update --recursive --init`, open in VS Code, and select "Reopen in Container." Watch as 20+ tools configure automatically!

---

*The goal isn't perfect DevOps - it's DevOps that actually works consistently. Start with one tool, prove the pattern, then expand. Your future debugging-free self will thank you.*
