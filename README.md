# DevOps-Toolkit
This repository is a one-stop shop for Code Quality tools and Development Environment setup, specifically DevContainers. It offers a complete suite of DevContainer configurations, standardized scripts for Code Quality tools, and Azure DevOps pipeline templates.

## 📝 Related blog posts

- 📈 **Automatically Generate and Visualize Python Code Coverage in VSCode** <sup>[krijnvanderburg.github.io](https://krijnvanderburg.github.io/blog/automatic-tests-code-coverage/) | [medium](https://medium.com/@krijnvanderburg/automatically-generate-and-visualize-python-code-coverage-308e65627925)</sup><br>
    *Learn how I automated my Python code coverage in VSCode! Instantly visualize coverage data in the editor for faster, more efficient development.*

- 👮‍♂️ **How to enforce Code Quality standards using CI/CD** <sup>[krijnvanderburg.github.io](https://krijnvanderburg.github.io/blog/enforce-code-quality-via-cicd/) | [medium](https://krijnvanderburg.medium.com/enforce-code-quality-standards-using-cicd-c2b08d812550)</sup><br>
    *Learn how to enforce code quality standards with CI/CD pipelines for tools like Ruff, ensuring consistency and security in your software development.*

- 🤖 **DevContainers Mastered: Automating Manual Workflows with VSCode Tasks - Part 3/3** <sup>[krijnvanderburg.github.io](https://krijnvanderburg.github.io/blog/devcontainers-automate-workflow-tasks/) | [medium](https://krijnvanderburg.medium.com/how-i-automate-my-entire-ide-vscode-akin-to-cicd-992568ee7fb5)</sup><br>
    *Automate your local development workflows with VSCode tasks and DevContainers akin to CICD. Remove all manual forms testing, dependencies, and more!*

- 🛡️ **DevContainers Improved: Integrating Code Quality Checks for Continuous Feedback - Part 2/3** <sup>[krijnvanderburg.github.io](https://krijnvanderburg.github.io/blog/devcontainers-add-code-quality-tools/) | [medium](https://krijnvanderburg.medium.com/add-code-quality-tools-in-your-ide-840df78c64d5)</sup><br>
    *Improve your workflow with DevContainers! Integrate code quality checks in VSCode for real-time feedback and error-free code. Boost productivity now!*

- 👨‍💻 **DevContainers Introduction: The Ideal Standardized Team Development Environment — Part 1/3** <sup>[krijnvanderburg.github.io](https://krijnvanderburg.github.io/blog/decontainers-the-ideal-team-environment/) | [medium](https://krijnvanderburg.medium.com/devcontainers-the-ideal-standardised-team-dev-environment-zero-bs-2-7eb77f0cb4ee)</sup><br> 
    *Discover how DevContainers streamline team workflows, ensure consistent environments, and automate setups for faster development and easier onboarding.*

- 🚀 **Distribute Tests with Pytest-Split for Faster CI/CD Execution** <sup>[krijnvanderburg.github.io](https://krijnvanderburg.github.io/blog/distribute-tests-with-pytest/) | [medium](https://krijnvanderburg.medium.com/how-to-distribute-tests-in-ci-cd-for-faster-execution-zero-bs-1-b86d4d69b19d)</sup><br>
    *Speed up your CI/CD with pytest-split! Learn how to distribute tests across agents for faster execution in Azure Pipelines and other platforms.*


# Getting Started
Clone this repository and test its implementations, ensuring to respect the copyright and license. No additional configuration is required. Works only with VS code and Azure DevOps pipelines.

1. Refer to the [DevContainers](#DevContainers) section for setup instructions.
2. Create an Azure pipeline using the provided `azure-pipelines.yml` file.

For a practical demonstration of these v1/templates in action, refer to the live pipeline example: 
https://krijnvdburg.visualstudio.com/public/_build?definitionId=11


## DevContainer
1. <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>P</kbd> or <kbd>F1</kbd>: `Dev Containers: Build Container`
2. Select the respective Devcontainer. The .devcontainer folder contains subfolder for each monorepo product.
3. Open VScode folder in Dev Container via either:
    - <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>P</kbd> : Dev Containers: Open Container
    - Click on `remote window` button, light blue in bottom-left corner of VScode.

### Known limitations
https://code.visualstudio.com/docs/devcontainers/containers#_dev-containers-limitations

- *Windows container images are not supported.*
- *Local proxy settings are not reused inside the container, which can prevent extensions from working unless the appropriate proxy information is configured (for example global HTTP_PROXY or HTTPS_PROXY environment variables with the appropriate proxy information).*

### WSL config
Dev containers use WSL2. This can use a lot of resources, limits can be defined in `.wslconfig` and placed in `C:\Users\<username>\.wslconfig`. See `./.devcontainer/.wslconfig` for example config.


## Code Quality tools
Sorted alphabetically (mostly). Recommended tool:

    Ruff, Flake8, Pylance, Pylint, Mypy, Pyright, Bandit, Semgrep, Gitleaks, Trufflehog, Ossaudit, OWASP, Pytest, Pytest coverage, Sphinx.

### Formatters

- **Black** <sup>[Docs](https://black.readthedocs.io/en/stable/) | [Github](https://github.com/psf/black) | [Pypi](https://pypi.org/project/black/) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)</sup> - Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters. [Config file](.tools/v1/configs/.black) | [AzDO pipeline](.azuredevops/v1/templates/formatter_black.yml) | [DevContainer config](#black)

- **Isort** <sup>[Docs](https://pycqa.github.io/isort/) | [Github](https://github.com/PyCQA/isort) | [Pypi](https://pypi.org/project/isort/) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)</sup> - isort is a Python utility / library to sort imports alphabetically and automatically separate into sections and by type. It provides a command line utility, Python library and plugins for various editors to quickly sort all your imports. It requires Python 3.8+ to run but supports formatting Python 2 code too. [Config file](.tools/v1/configs/.isort.cfg) | [AzDO pipeline](.azuredevops/v1/templates/formatter_isort.yml) | [DevContainer config](#isort)

- **Ruff** <sup>[Docs](https://docs.astral.sh/ruff/) | [Github](https://github.com/astral-sh/ruff) | [Pypi](https://pypi.org/project/ruff/) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)</sup> - An extremely fast Python linter and code formatter, written in Rust. [Config file](.tools/v1/configs/ruff.toml) | [AzDO pipeline](.azuredevops/v1/templates/formatter_ruff.yml) | [DevContainer config](#ruff)

### Linters

- **Flake8** <sup>[Github](https://github.com/PyCQA/flake8) | [Docs](https://flake8.pycqa.org/en/latest/) | [Pypi](https://pypi.org/project/flake8/) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)</sup> - Flake8 is a python tool that glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code. [Config file](.tools/v1/configs/.flake8) | [AzDO pipeline](.azuredevops/v1/templates/linter_flake8.yml) | [DevContainer config](#flake8)

- **Pylance** <sup>[Github](https://github.com/microsoft/pylance-release) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)</sup> - Pylance is an extension that works alongside Python in Visual Studio Code to provide performant language support. Under the hood, Pylance is powered by Pyright, Microsoft's static type checking tool. Using Pyright, Pylance has the ability to supercharge your Python IntelliSense experience with rich type information, helping you write better code faster. [DevContainer config](#pylance)

- **Pylint** <sup>[Docs](https://pylint.org/) | [Github](https://github.com/pylint-dev/pylint) | [Pypi](https://pypi.org/project/pylint/) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)</sup> - Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored. [Config file](.tools/v1/configs/.pylintrc) | [AzDO pipeline](.azuredevops/v1/templates/linter_pylint.yml) | [DevContainer config](#pylint)

- **Ruff** <sup>[Docs](https://docs.astral.sh/ruff/) | [Github](https://github.com/astral-sh/ruff) | [Pypi](https://pypi.org/project/ruff/) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)</sup> - An extremely fast Python linter and code formatter, written in Rust. [Config file](.tools/v1/configs/ruff.toml) | [AzDO pipeline](.azuredevops/v1/templates/linter_ruff.yml) | [DevContainer config](#ruff)

- **SonarLint** <sup>[Docs](https://www.sonarsource.com/products/sonarlint/) | [Github](https://github.com/SonarSource/sonarlint-core) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode)</sup> - A clean code linter for your IDE to help find & fix bugs, security issues & analysis across several programming languages to provide real-time feedback. [DevContainer config](#sonarlint)

### Type checker

- **Mypy** <sup>[Docs](https://mypy-lang.org/) | [Github](https://github.com/python/mypy) | [Pypi](https://pypi.org/project/mypy/) | [VS Code Marketplace](https://github.com/microsoft/vscode-mypy)</sup> - Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking. Mypy type checks standard Python programs; run them using any Python VM with basically no runtime overhead.  [Config file](.tools/v1/configs/mypy.ini) | [AzDO pipeline](.azuredevops/v1/templates/typechecker_mypy.yml) | [DevContainer config](#mypy)

- **Pyre** <sup>[Docs](https://pyre-check.org/) | [Github](https://github.com/facebook/pyre-check) | [Pypi](https://pypi.org/project/pyre-check/)</sup> - Pyre is a performant type checker for Python compliant with PEP 484. Pyre can analyze codebases with millions of lines of code incrementally – providing instantaneous feedback to developers as they write code. You can try it out on examples in the Pyre Playground. [Config file](.tools/v1/configs/.pyre_configuration) | [AzDO pipeline](.azuredevops/v1/templates/typechecker_pyre.yml)

- **Pyright** <sup>[Docs](https://microsoft.github.io/pyright) | [Github](https://github.com/microsoft/pyright) | [Pypi](https://pypi.org/project/pyright/) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright)</sup> - Pyright is a full-featured, standards-based static type checker for Python. It is designed for high performance and can be used with large Python source bases. [Config file](.tools/v1/configs/.pyright) | [AzDO pipeline](.azuredevops/v1/templates/typechecker_pyright.yml)

### Scanner

- **Bandit** <sup>[Docs](https://bandit.readthedocs.io) | [Github](https://github.com/PyCQA/bandit) | [Pypi](https://pypi.org/project/bandit/) | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=nwgh.bandit)</sup> - Bandit is a tool designed to find common security issues in Python code. To do this, Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files, it generates a report. [Config file](.tools/v1/configs/.bandit) | [AzDO pipeline](.azuredevops/v1/templates/scanner_bandit.yml) | [DevContainer config](#bandit)

- **Semgrep** (free version, limited rules) <sup>[Docs](https://semgrep.dev/p/python) | [Github](https://github.com/semgrep/semgrep) | [Pypi](https://pypi.org/project/semgrep/) | [VS Code Marketplace]()</sup> - Semgrep OSS is a fast, open-source, static analysis tool for searching code, finding bugs, and enforcing code standards at editor, commit, and CI time. (Poor CICD support, see AzDO template internal notes) [Config file](.tools/v1/configs/semgrep.yaml) | [AzDO pipeline](.azuredevops/v1/templates/scanner_semgrep.yml)

- **SonarQube** (TODO) <sup>[Docs](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/languages/python/) | [Github](https://github.com/SonarSource/sonar-scanner-python)</sup> - Sonar's Clean Code solutions help developers deliver high-quality, efficient code standards that benefit the entire team or organization. [Config file](.tools/v1/configs/vulture.toml) | [AzDO pipeline](.azuredevops/v1/templates/scanner_vulture.yml)

- **Vulture** <sup>[Github](https://github.com/jendrikseipp/vulture) | [Pypi](https://pypi.org/project/vulture/#history)</sup> - Vulture finds unused code in Python programs. This is useful for cleaning up and finding errors in large code bases. If you run Vulture on both your library and test suite you can find untested code.[Config file]() | [AzDO pipeline]() | [DevContainer config]()

- **DevSkim** <sup>[Docs](https://github.com/microsoft/DevSkim/wiki) | [Github](.tools/v1/configs/devskim.json) | [Download](https://github.com/microsoft/DevSkim?tab=readme-ov-file#command-line-interface)</sup> - DevSkim is a framework of IDE extensions and language analyzers that provide inline security analysis in the dev environment as the developer writes code. It has a flexible rule model that supports multiple programming languages. The goal is to notify the developer as they are introducing a security vulnerability in order to fix the issue at the point of introduction, and to help build awareness for the developer. [VS code extension has no option to load config file] [Config file](.tools/v1/configs/devskim.json) | [AzDO pipeline](.azuredevops/v1/templates/scanner_devskim.yml) | [DevContainer config](#devskim)

#### Credentials scanner

- **Gitleaks** <sup>[Github](https://github.com/gitleaks/gitleaks)</sup> - Gitleaks is a SAST tool for detecting and preventing hardcoded secrets like passwords, api keys, and tokens in git repos. Gitleaks is an easy-to-use, all-in-one solution for detecting secrets, past or present, in your code. [Config file](.tools/v1/configs/.gitleaks.toml) | [AzDO pipeline](.azuredevops/v1/templates/scanner_gitleaks.yml)

- **Trufflehog** <sup>[Github](https://github.com/trufflesecurity/trufflehog)</sup> - TruffleHog™ is a secrets scanning tool that digs deep into your code repositories to find secrets, passwords, and sensitive keys. [Config file](.tools/v1/configs/trufflehog.toml) | [AzDO pipeline](.azuredevops/v1/templates/scanner_trufflehog.yml)

#### Dependency scanner

- **Ossaudit** <sup>[Github](https://github.com/illikainen/ossaudit) | [Pypi](https://pypi.org/project/ossaudit/)</sup> - Ossaudit uses Sonatype OSS Index to audit Python packages for known vulnerabilities. [Config file](.tools/v1/configs/ossaudit.yaml) | [AzDO pipeline](.azuredevops/v1/templates/scanner_ossaudit.yml)

- **OWASP dependency-check** <sup>[Docs](https://owasp.org/www-project-dependency-check/) | [Github](https://github.com/jeremylong/DependencyCheck) | [Pypi](https://pypi.org/project/dependency-check/) | [VS Code Marketplace]()</sup> - Dependency-Check is a Software Composition Analysis (SCA) tool that attempts to detect publicly disclosed vulnerabilities contained within a project’s dependencies. It does this by determining if there is a Common Platform Enumeration (CPE) identifier for a given dependency. If found, it will generate a report linking to the associated CVE entries. [Config file](.tools/v1/configs/cve_suppressions.xml) | [AzDO pipeline](.azuredevops/v1/templates/scanner_owasp-dependency-check.yml)

- **Safety** (Paid tool, not implemented) <sup>[Docs](https://docs.safetycli.com/) | [Github](https://github.com/pyupio/safety) | [Pypi](https://pypi.org/project/safety/)</sup> - Safety CLI is a Python dependency vulnerability scanner designed to enhance software supply chain security by detecting packages with known vulnerabilities and malicious packages in local development environments, CI/CD, and production systems. Safety CLI can be deployed in minutes and provides clear, actionable recommendations for remediation of detected vulnerabilities.

### Testing

- **Pytest** <sup>[Docs](https://docs.pytest.org) | [Github](https://github.com/pytest-dev/pytest) | [Pypi](https://pypi.org/project/pytest/)</sup> - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries. [Config file](.tools/v1/configs/pytest.ini) | [AzDO pipeline](.azuredevops/v1/templates/test_pytest.yml) | [DevContainer config](#pytest)

- **Coverage** <sup>[coverage.py](https://coverage.readthedocs.io/)</sup>: Checks code coverage of Python tests with coverage.py. [Config file](.tools/v1/configs/.coveragerc) | [AzDO pipeline](.azuredevops/v1/templates/test_pytest.yml) | [DevContainer config](#pytest)


### Dependency management

- **Poetry** <sup>[Docs](https://python-poetry.org/) | [Github](https://github.com/python-poetry/poetry) | [Pypi]()</sup> - Poetry helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack everywhere. [AzDO pipeline](.azuredevops/v1/templates/install_poetry_requirements.yml)

- **Pip** <sup>[Docs](https://pip.pypa.io) | [Github](https://github.com/pypa/pip) | [Pypi](https://pypi.org/project/pip/)</sup> - pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes. [AzDO pipeline](.azuredevops/v1/templates/install_pip_requirements.yml)

### Packaging

- **Python Build** <sup>[Website](https://packaging.python.org) | [Docs](https://build.pypa.io) | [Pypi](https://pypi.org/project/build/)</sup> - A simple, correct Python packaging build frontend. [AzDO pipeline](.azuredevops/v1/templates/build_wheel_bdist.yml)

- **Twine** <sup>[Docs](https://twine.readthedocs.io) | [Github](https://github.com/pypa/twine) | [Pypi](https://pypi.org/project/twine/)</sup> - Twine is a utility for publishing Python packages on PyPI. It provides build system independent uploads of source and binary distribution artifacts for both new and existing projects. [AzDO pipeline](.azuredevops/v1/templates/deploy_artifacts_python_wheel.yml)

### Profilers (TODO)
- **cProfile**: Profiles Python code with cProfile. [cProfile](https://docs.python.org/3/library/profile.html)
- **py_spy**: Profiles Python code with py-spy. [py-spy](https://github.com/benfred/py-spy)
- **line_profiler**: Profiles Python code with line_profiler. [line_profiler](https://pypi.org/project/)
- **memory_profiler**: Profiles memory usage of Python code with memory-profiler. [memory-profiler](https://pypi.org/project/memory-profiler/)
- **plop**: Profiles Python code with Plop. [Plop](https://pypi.org/project/plop/)
- **vprof**: Profiles Python code with vprof. [vprof](https://github.com/nvdv/vprof)
- **yappi**: Profiles Python code with Yappi. [Yappi](https://pypi.org/project/yappi/)

### Documentation

- **Sphinx** <sup>[Docs](https://www.sphinx-doc.org/) | [Github](https://github.com/sphinx-doc/sphinx) | [Pypi](https://pypi.org/project/Sphinx/)</sup> - Sphinx makes it easy to create intelligent and beautiful documentation. [Config file]() | [AzDO pipeline](.azuredevops/v1/templates/docs_sphinx.yml)

### TODO
- **Docker Linter** (TODO)
- **hadolint** (TODO)
- **dockerlint** (TODO)  
- **dive** (TODO) 
- **docker-bench-security** (TODO) 
- **dockle** (TODO) 
- **snyk** (TODO) Checks dependencies for vulnerabilities with Snyk. [Snyk](https://snyk.io/)
- scanner_anchore (TODO) Analyzes Docker images for vulnerabilities with Anchore. [Anchore](https://anchore.com/)
- **trivy** (TODO) A Simple and Comprehensive Vulnerability Scanner for Containers and other Artifacts, Suitable for CI. [Trivy](https://github.com/aquasecurity/trivy)
- **clair** (TODO) Vulnerability Static Analysis for Containers. [Clair](https://github.com/quay/clair)



## DevContainers
DevContainers in Visual Studio Code provide a fully configured and isolated development environment inside a container. This allows you to maintain a consistent, reproducible, and platform-independent setup, which can be  beneficial for teams.

1. **Install Docker**: Ensure Docker is installed on your machine. You can download it from the [official Docker website](https://www.docker.com/products/docker-desktop).

2. **Install the Remote - Containers extension in VS Code**: This extension is necessary to work with DevContainers. You can install it from the [VS Code marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

3. **Configure your DevContainer**: Create a `.devcontainer` directory in your project root. Inside this directory, you'll need a `devcontainer.json` file to configure your DevContainer, and optionally a `Dockerfile` to define the container itself.

    This implementation utilizes a `docker-compose.yml` file specified in the `devcontainer.json`. The Docker Compose process uses a local Dockerfile located in the `.devcontainer` directory, which installs all the necessary tools for development. Docker Compose is employed due to its ability to effortlessly add additional supporting containers as needed. This can include Spark nodes, Azurite, or Airflow, depending on your code's dependencies.

4. Add the following lines to `.gitattributes` file in project root. This prevents git from thinking ALL files changed due to different line endings when opening devcontainer from windows machine.
    ```bash
    * text=auto
    *.sh text eol=lf
    *.conf text eol=lf
    ```

5. Optional: Dev containers use WSL2. This can use a lot of resources, limits can be defined in `.wslconfig` and placed in `C:\Users\<username>\.wslconfig`. See `./.devcontainer/.wslconfig` for example config.

    ```ini
    [wsl2]
    # Limits VM memory to use no more than 4 GB, this can be set as whole numbers using GB or MB
    memory=6GB 
    # Sets the VM to use two virtual processors
    processors=4
    # Sets amount of swap storage space to 8GB, default is 25% of available RAM
    swap=8GB
    # Disable (false) page reporting so WSL retains all allocated memory claimed from Windows and releases none back when free
    pageReporting=true
    ```

6. **Open your project in a DevContainer**: With your project open in VS Code, press `F1` to open the command palette, then select the "Remote-Containers: Reopen in Container" command. VS Code will build (if necessary) and start your DevContainer, then reopen your project inside it.

For more detailed information, refer to the [official VS Code DevContainers documentation](https://code.visualstudio.com/docs/remote/containers).


### DevContainer VSCode Extensions

#### Ruff
Code formatter combining Black, isort, pylint and flake8 all together in one tool with near rules parity and extremely fast. Automatically runs on <kbd>file save</kbd> action for opened file.

Using Ruff in combination with said tools it replaces makes no sense unless ruff does not have certian specific rules implemented.

```json
"extensions": [
    "charliermarsh.ruff"
],
"settings": {
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.defaultFormatter": "charliermarsh.ruff"
    },
    "ruff.lint.args": [
        "--config=${workspaceFolder}/path/to/.ruff.toml"
    ],
    "ruff.format.args": [
        "--config=${workspaceFolder}/path/to/.ruff.toml"
    ],
},
```

#### Black
Code formatter of pep8. Automatically runs on <kbd>file save</kbd> action for opened file.

```json
"extensions": [
    "ms-python.black-formatter"
],
"settings": {
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
    },
    "black-formatter.args": [
        "--config",
        "${workspaceFolder}/path/to/.black"
    ],
    "black-formatter.cwd": "${workspaceFolder}",
    "black-formatter.enabled": true,
    "black-formatter.showNotification": "onError"
},
```

#### Isort
Import organizer of Pep8. Automatically runs on <kbd>file save</kbd> action for opened file. Press <kbd>Alt</kbd>+<kbd>shift</kbd>+<kbd>O</kbd> to manually run for currently open file. 

```json
"extensions": [
    "ms-python.isort"
],
"settings": {
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    },
    "isort.args": [
        "--settings-path",
        "${workspaceFolder}/path/to/.isort.cfg"
    ],
    "isort.serverEnabled": false,
    "isort.check": false,
    "isort.showNotification": "onError"
},
```

#### Pylint
Code formatter of Pep8 and more. Automatically runs on <kbd>file save</kbd> action for opened file. Shows its result in code UI and in the `problems` section of VScode integrated terminal.

```json
"extensions": [
    "ms-python.pylint"
],
"settings": {

    "pylint.args": [
        "--rcfile",
        "${workspaceFolder}/path/to/.pylintrc"
    ],
    "pylint.cwd": "${workspaceFolder}",
    "pylint.enabled": true,
    "pylint.showNotification": "onError",
    "pylint.lintOnChange": true,
},
```

#### Flake8
Linter of Pep8 and more. Automatically runs on <kbd>file save</kbd> action for opened file. Shows its result in code UI and in the `problems` section of VScode integrated terminal.

```json
"extensions": [
    "ms-python.flake8"
],
"settings": {
    "flake8.args": [
        "--config",
        "${workspaceFolder}/path/to/.flake8" 
    ],
    "flake8.cwd": "${workspaceFolder}",
    "flake8.showNotification": "onError",
    "flake8.enabled": true,
},
```

#### Bandit
Code scanner of vulnerabilities and code quality. Automatically runs on <kbd>file save</kbd> action for opened file. Shows its result in code UI and in the `problems` section of VScode integrated terminal.

```json
"extensions": [
    "nwgh.bandit"
],
"settings": {
    "bandit.args": [
        "-c",
        "${workspaceFolder}/path/to/.bandit"
    ],
    "bandit.cwd": "${workspaceFolder}",
    "bandit.logLevel": "warning",
    "bandit.enabled": true,
    "bandit.showNotification": "onError"
},
```

#### DevSkim
Code scanner of vulnerabilities and code quality. Automatically runs on <kbd>file save</kbd> action for opened file. Shows its result in code UI and in the `problems` section of VScode integrated terminal.

Cannot find proper documentation on settings, cant find a way to use config file either. Personally I am not a fan of this tool and don't recommend it.

```json
"extensions": [
    "ms-cst-e.vscode-devskim"
],
"settings": {},
```

#### Mypy
Type checker and type hinting. Automatically runs on <kbd>file save</kbd> action for opened file. Shows its result in code UI and in the `problems` section of VScode integrated terminal.

```json
"extensions": [
    "ms-python.flake8"
],
"settings": {
    "flake8.args": [
        "--config",
        "${workspaceFolder}/path/to/.flake8"
    ],
    "flake8.cwd": "${workspaceFolder}",
    "flake8.showNotification": "onError",
    "flake8.enabled": true,
    // ...
},
```

#### Pytest
Automatically discovers unit tests and can run them via extension pytest tab.

```json
"extensions": [],
"settings": {
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [
        "-c",
        "${workspaceFolder}/path/to/pytest.ini"
    ],
    "python.languageServer": "Default",
```

#### Pylance
Code validator and type checker. Runs automatically for all files. Shows its result in the `problems` section of VScode integrated terminal.

```json
"extensions": [
    "ms-python.vscode-pylance"
],
"settings": {
    "python.analysis.typeCheckingMode": "strict",
    "python.analysis.diagnosticMode": "workspace",
    "python.analysis.diagnosticSeverityOverrides": {
        "reportUnknownParameterType": false,
        "reportUnknownArgumentType": false,
        "reportUnknownVariableType": false,
        "reportUnknownMemberType": false,
        "reportMissingParameterType": false,
        "reportMissingTypeArgument": false,
        "reportGeneralTypeIssues": false
    },
    "python.analysis.completeFunctionParens": true,
    "python.analysis.inlayHints.variableType": true,
    "python.analysis.inlayHints.functionReturnTypes": true,
    "python.analysis.inlayHints.callArgumentName": true,
    "python.analysis.inlayHints.pytestParameters": true,
},
```

#### SonarLint
Code linter by SonarQube/SonarCloud. Runs automatically for files. Shows its results in the `problems` section of VScode integrated terminal.

Gives error popup when opening Json files: `SonarLint failed to analyze JSON code: Node.js runtime version 18.17.0 or later is required`. This devcontainer will not have a node.js configured simply because its a lot just for json files scanning for 1 extension. Just click 'do not show again' once.

```json
"extensions": [
    "sonarsource.sonarlint-vscode"
],
"settings": {
    "sonarlint.rules": {},
    "sonarlint.testFilePattern": "**/tests/**,test_*.py, *_test.py",
    "sonarlint.disableTelemetry": true,
    "sonarlint.output.showAnalyzerLogs": true,
    // "sonarlint.connectedMode.project": {},
    // "sonarlint.connectedMode.connections.sonarqube": [
    //     {
    //         "connectionId": "",
    //         "serverUrl": "",
    //         "token": ""
    //     }
    // ],
    // "sonarlint.connectedMode.connections.sonarcloud": [],
},
```

#### Coverage Gutter
1. Generate a code coverage. This can be automated by providing additional args in the pytest extension and by configuring a vscode task to run coverage on folder open.
    ```python
    pytest ./ -s --cache-clear -c ./path/to/pytest.ini --cov ./ --cov-report xml:./coverage.xml --cov-config ./path/to/.coveragerc
    ```
    (requires `pytest`, `pytest-cov`)
    
2. <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>P</kbd>: Coverage Gutter: Display Coverage. Or toggle `Coverage Gutter: Watch`, this will watch the coverage.xml for changes. 

    Though this might give error pop-ups as it might try to read while coverage.xml is still being generated.

If no coverage.xml is generated then its likely an issue with `.coveragerc`.


## Copyright
This work is copyright © 2024 by Krijn van der Burg. This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. For the full license text, see the [LICENSE](./LICENSE) file. For inquiries, contact Krijn van der Burg on [linkedin.com/in/krijnvanderburg/](https://www.linkedin.com/in/krijnvanderburg/).
