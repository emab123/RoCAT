# RoCAT (Rocket Cycle Analysis Tool)

RoCAT is a comprehensive Python-based tool for rocket engine cycle analysis and design optimization. This repository is a fork of the original RoCAT project, specifically adapted and enhanced for the development of the **RAPID (Rocket with Affordable Propellant Injection Design)** project at **UFSC (Universidade Federal de Santa Catarina)**.

The tool provides detailed thermodynamic analysis of various rocket engine cycles, including propellant flow calculations, heat transfer analysis, combustion chamber design, and nozzle optimization. RoCAT integrates with NASA's CEA (Chemical Equilibrium with Applications) for accurate combustion modeling and uses CoolProp for thermophysical property calculations.

## RAPID Project

This fork is being developed as part of the RAPID initiative at UFSC, focusing on creating cost-effective rocket propulsion systems with innovative propellant injection designs. The modifications and enhancements made to the original RoCAT codebase are tailored to support the specific research objectives and design requirements of the RAPID project.

## Development Setup

This project uses **Dev Containers** for a consistent development environment across all platforms.

### Prerequisites
- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/emab123/RoCAT.git
   cd RoCAT
   ```

2. Open in VS Code:
   ```bash
   code .
   ```

3. When prompted, click **"Reopen in Container"** or:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type "Dev Containers: Reopen in Container"
   - Press Enter

4. Wait for the container to build (first time only - takes a few minutes)

5. Once complete, you'll have a fully configured development environment with:
   - Python 3.12 with virtual environment
   - All dependencies installed (including gfortran)
   - VS Code extensions pre-installed
   - Proper Python interpreter configured

That's it! Your development environment is ready to use.

## Development Guidelines

This project uses **Conventional Commits** to maintain a clean and meaningful commit history. The Dev Container automatically includes the "Conventional Commits" VS Code extension to help you format commit messages properly.

### Using the Conventional Commits Extension

1. **Stage your changes** in VS Code's Source Control panel or using `git add`

2. **Start a commit** by clicking the commit button or pressing `Ctrl+Enter` in the Source Control panel

3. **Use the extension** by clicking the "Conventional Commits" icon (🎯) in the commit message box, or:
   - Press `Ctrl+Shift+P` and type "Conventional Commits"
   - Select "Conventional Commits"

4. **Follow the guided prompts:**
   - Select commit type (feat, fix, docs, etc.)
   - Choose scope (optional - e.g., engine, cea, cycles)
   - Write description (what you changed)
   - Add body (optional - more detailed explanation)
   - Add breaking change info (if applicable)

5. **Commit** - The extension will format your message automatically

### Commit Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

### Example Workflow
```
# Your formatted commit will look like:
feat(engine): add new cooling channel analysis module

Added comprehensive heat transfer calculations for cooling channels
including convective and radiative heat transfer models.

# Or simpler:
fix(cea): resolve pressure ratio calculation error
```

## Prerequisites

This project uses Dev Containers, so you only need:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

All Python dependencies, compilers, and tools are automatically installed in the container.

## Installation

Installation is handled automatically by the Dev Container. Simply follow the Development Setup instructions above.

## Usage

[Add usage examples and documentation here]

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Make your changes following the [Development Guidelines](#development-guidelines)
4. Commit your changes (`git commit -m 'feat: add amazing feature'`)
5. Push to the branch (`git push origin feat/amazing-feature`)
6. Open a Pull Request

## License

[Add license information here]

## Acknowledgments

- Original RoCAT developer [@RubenvdBerg](https://github.com/RubenvdBerg)
- UFSC RAPID project team
