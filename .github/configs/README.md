# .dotfiles - Shared Configuration & Script Architecture

The foundation of consistent DevOps workflows across local development and CI/CD environments. This repository contains shared configuration files and standardized shell scripts that ensure identical tool execution whether running locally in DevContainers or remotely in Azure Pipelines.

## 🎯 The Core Problem This Solves

Most DevOps setups fail and thus frustrate because local development and CI/CD use different configurations:
- **Local**: `ruff --line-length=88 src/`
- **CI/CD**: `ruff --line-length=120 --select=E,F src/`

Result? Code passes locally but fails in CI/CD, or vice versa. Endless debugging and configuration drift.

## 🔧 The Solution: Single Source of Truth

This `.dotfiles` repository provides **identical configurations and execution scripts** used by both:
- **DevContainers** - Your local development environment
- **Azure DevOps Templates** - Your CI/CD pipelines

When both environments use the same script with the same config file, consistency is guaranteed.

> **💡 Want to see this in action locally?** The [DevContainer environments](https://github.com/KrijnvanderBurg/.devcontainer) use these exact same configurations and scripts. **Zero-config development** with perfect CI/CD alignment guaranteed.

## 📁 Repository Structure

```bash
.dotfiles/
├── python/                          # Python tooling ecosystem
│   ├── configs/                       # All Python tool configuration files
│   │   ├── ruff.toml                    # Ruff formatter & linter settings
│   │   ├── .pylintrc                    # Pylint code analysis rules
│   │   ├── pyproject.toml               # Black, isort, pytest configuration
│   │   ├── mypy.ini                     # Type checking configuration
│   │   ├── bandit.yaml                  # Security scanning rules
│   │   └── ...                          # Additional tool configs
│   └── scripts/                       # Executable shell scripts per tool
│       ├── ruff-format.sh               # Standardized Ruff formatting execution
│       ├── ruff-lint.sh                 # Standardized Ruff linting execution
│       ├── pylint.sh                    # Standardized Pylint execution
│       ├── mypy.sh                      # Standardized type checking execution
│       ├── bandit.sh                    # Standardized security scanning
│       └── ...                          # Additional execution scripts
```

## 🚀 How It Works: Execution Flow

### Local Development (DevContainer)
```jsonc
// VS Code Task Definition
{
   "label": "ruff-lint",
   "command": "${workspaceFolder}/.devcontainer/.dotfiles/python/scripts/ruff-lint.sh",
   "args": [
      "${workspaceFolder}/src",
      "--config", "${workspaceFolder}/.devcontainer/.dotfiles/python/configs/ruff.toml"
   ]
}
```

### CI/CD Pipeline (Azure DevOps)
```yaml
# Azure DevOps Pipeline Step
steps:
- script: |
    $(Build.Repository.LocalPath)/.azuredevops/.dotfiles/python/scripts/ruff-lint.sh \
      $(Build.Repository.LocalPath)/src \
      --config $(Build.Repository.LocalPath)/.azuredevops/.dotfiles/python/configs/ruff.toml
  displayName: 'Ruff Linter'
```

**Result**: Both environments execute the **exact same shell script** with the **exact same configuration file**.

## 🛠️ Tool Categories & Structure

### Python Development Ecosystem
Complete configuration and execution standardization for 20+ Python tools:

**📋 Configuration Files** (`python/configs/`):
- **ruff.toml** - Formatting and linting rules
- **.pylintrc** - Code quality analysis settings
- **mypy.ini** - Type checking configuration
- **bandit.yaml** - Security scanning rules
- **semgrep.yml** - Static analysis patterns
- **...**

**⚡ Execution Scripts** (`python/scripts/`):
- **ruff-format.sh** - Code formatting with consistent parameters
- **ruff-lint.sh** - Code linting with standardized output
- **pylint.sh** - Code analysis with unified reporting
- **mypy.sh** - Type checking with consistent settings
- **pytest.sh** - Test execution with coverage reporting
- **bandit.sh** - Security scanning with XML output
- **...**



## 📖 Script Standardization Benefits

### Consistent Parameters
Every script accepts standardized parameters:
```bash
# Standard pattern: tool.sh <target_path> <config_filepath> [additional_args]
./python/scripts/ruff-lint.sh src/ ./python/configs/ruff.toml
./python/scripts/mypy.sh src/ ./python/configs/mypy.ini
./python/scripts/pytest.sh tests/ ./python/configs/pytest.ini
```

### Unified Output Format
All scripts provide consistent output formatting:
- **Exit Codes**: 0 for success, 1+ for failures
- **Output Format**: Standardized reporting (JUnit XML, coverage XML)
- **Error Handling**: Consistent error messages and logging

### Environment Independence
Scripts work identically across environments:
- **DevContainers**: Full development environment
- **Azure DevOps**: CI/CD pipeline execution
- **Local Development**: Direct script execution

## 🔄 Architecture Benefits

### Perfect Quality Gate Alignment
When local checks pass, remote execution is **guaranteed** to pass because:
- **Same Script**: Identical execution logic
- **Same Config**: Identical tool parameters
- **Same Environment**: Containerized consistency

### Single Point of Maintenance
Update tool configurations in one place, benefit everywhere:
- **Configuration Changes**: Edit config file once, applies to all environments
- **Script Updates**: Improve execution logic once, benefits all consumers
- **Version Updates**: Update tool versions centrally


The power of this architecture lies in its simplicity: **one script, one config, consistent execution everywhere**.

---

## 🚀 Experience the Complete Workflow

**Local Development First:** Start with the [DevContainer environments](https://github.com/KrijnvanderBurg/.devcontainer) to experience these configurations locally. **20+ tools** with zero setup and perfect CI/CD preview.

**Scale to Production:** Deploy with [Azure DevOps CI/CD templates](https://github.com/KrijnvanderBurg/.azuredevops) that use these exact same configurations. **25+ pipeline templates** for seamless local-to-production workflows.

**See the Big Picture:** Explore the [complete DevOps Toolkit](https://github.com/KrijnvanderBurg/DevOps-Toolkit) to understand how shared configurations create **perfect consistency** across all environments.
