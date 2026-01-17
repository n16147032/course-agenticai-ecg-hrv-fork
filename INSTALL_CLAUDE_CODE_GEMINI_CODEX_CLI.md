# Installing Claude Code, Gemini CLI, and Codex CLI

This guide provides installation instructions for three AI-powered command-line coding assistants across macOS, Linux, and Windows, plus container-based deployment.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
   - [Windows Built-in Tools](#windows-built-in-tools)
   - [uv (Python Package Manager)](#uv-recommended-python-package-manager)
   - [Node.js](#nodejs-required-for-npm-installations)
   - [Container Runtime](#container-runtime-required-for-container-setup)
2. [Claude Code](#claude-code)
3. [Google Gemini CLI](#google-gemini-cli)
4. [OpenAI Codex CLI](#openai-codex-cli)
5. [Understanding Containers](#understanding-containers)
6. [Docker vs Podman](#docker-vs-podman)
   - [macOS GPU Limitations](#macos-gpu-limitations-apple-silicon)
7. [Container Setup](#container-setup)
   - [Docker Compose with Model Runner](#docker-compose-with-model-runner-macos-gpu-inference)
8. [Troubleshooting](#troubleshooting)
9. [References](#references)

---

## Prerequisites

### Windows Built-in Tools

Windows 10/11 comes with several command-line tools pre-installed. Understanding what's available helps you know what needs to be installed separately.

**Pre-installed on Windows 10 (1809+) and Windows 11:**

| Tool | Status | Notes |
|------|--------|-------|
| **Windows PowerShell 5.1** | Pre-installed | Built into Windows, used for all `powershell` commands in this guide |
| **winget** | Pre-installed | Windows Package Manager (Windows 11, Windows 10 1809+) |
| **curl** | Pre-installed | Available since Windows 10 1803 |
| **tar** | Pre-installed | Available since Windows 10 1803 |
| **OpenSSH Client** | Pre-installed | May need enabling in Settings > Apps > Optional Features |

**NOT pre-installed (must be installed):**

| Tool | Install Command |
|------|-----------------|
| **Git** | `winget install Git.Git` |
| **GitHub CLI** | `winget install GitHub.cli` |
| **Node.js** | `winget install OpenJS.NodeJS.LTS` |
| **Python** | `winget install Python.Python.3.12` |
| **PowerShell 7** | `winget install Microsoft.PowerShell` (optional, newer cross-platform version) |

> **Note:** Windows PowerShell 5.1 (pre-installed) is sufficient for all commands in this guide. PowerShell 7 is optional and installs alongside 5.1.

**Verify winget is available:**
```powershell
winget --version
```

If winget is missing (older Windows 10), install it from the [Microsoft Store](https://apps.microsoft.com/detail/9nblggh4nns1) or via the [App Installer](https://github.com/microsoft/winget-cli/releases).

### uv (Recommended Python Package Manager)

uv is a fast Python package and project manager written in Rust. Use it instead of pip for faster, more reliable installations.

**macOS:**
```bash
brew install uv
```

**Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Node.js (Required for npm installations)

All three CLIs can be installed via npm, which requires Node.js 18+.

**macOS:**
```bash
brew install node
```

**Linux (Ubuntu/Debian):**
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install nodejs
```

**Windows:**
```powershell
winget install OpenJS.NodeJS.LTS
```

### Container Runtime (Required for container setup)

Choose either Docker or Podman. See [Docker vs Podman](#docker-vs-podman) for guidance.

**macOS:**
```bash
# Docker
brew install --cask docker

# Podman
brew install podman
```

**Linux:**
```bash
# Docker (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install docker.io docker-compose
sudo usermod -aG docker $USER
# Log out and back in for group changes to take effect

# Podman (Ubuntu/Debian)
sudo apt-get install podman podman-compose
```

**Windows:**
```powershell
# Docker
winget install Docker.DockerDesktop

# Podman
winget install RedHat.Podman-Desktop
```

---

## Claude Code

Claude Code is Anthropic's official CLI for Claude, providing an interactive coding assistant in your terminal.

**Current Version:** v2.1.12 (January 2026)

### macOS

**Homebrew (recommended):**
```bash
brew install --cask claude-code
```
> Note: Does not auto-update. Run `brew upgrade claude-code` periodically.

**Alternative (curl with auto-update):**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Linux

**Homebrew (recommended if available):**
```bash
brew install --cask claude-code
```

**Alternative (curl with auto-update):**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows

**WinGet (recommended):**
```powershell
winget install Anthropic.ClaudeCode
```
> Note: Does not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically.

**Alternative (PowerShell with auto-update):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

### Requirements

- A Claude subscription (Pro, Max, Teams, or Enterprise) OR
- Claude Console account (for API access)

### Quick Start

After installation, navigate to your project directory and run:
```bash
claude
```

On first run, you'll be prompted to authenticate with your Anthropic account.

---

## Google Gemini CLI

Gemini CLI brings the power of Google's Gemini models directly to your terminal with a generous free tier (60 requests/min, 1,000 requests/day).

**Current Version:** v0.24.0 (January 2026)

### macOS

**Homebrew (recommended):**
```bash
brew install gemini-cli
```

**npm:**
```bash
npm install -g @google/gemini-cli
```

### Linux

**npm (recommended):**
```bash
npm install -g @google/gemini-cli
```

**npx (no installation):**
```bash
npx @google/gemini-cli
```

### Windows

**npm (recommended):**
```bash
npm install -g @google/gemini-cli
```

**npx (no installation):**
```powershell
npx @google/gemini-cli
```

### Quick Start

After installation, run:
```bash
gemini
```

On first run, authenticate with your Google account. The free tier provides access to Gemini 2.5 Pro with 1M token context window.

---

## OpenAI Codex CLI

Codex CLI is OpenAI's lightweight coding agent that runs in your terminal.

**Current Version:** v0.87.0 (January 2026)

### macOS

**Homebrew (recommended):**
```bash
brew install --cask codex
```

**npm:**
```bash
npm install -g @openai/codex
```

### Linux

**npm (recommended):**
```bash
npm install -g @openai/codex
```

**Manual download:**
- x86_64: Download `codex-x86_64-unknown-linux-musl.tar.gz`
- ARM64: Download `codex-aarch64-unknown-linux-musl.tar.gz`

From: https://github.com/openai/codex/releases/latest

Extract and install:
```bash
tar -xzf codex-*.tar.gz
sudo mv codex /usr/local/bin/
```

### Windows

**npm (recommended):**
```powershell
npm install -g @openai/codex
```

### Quick Start

After installation, run:
```bash
codex
```

Select "Sign in with ChatGPT" to authenticate using your ChatGPT Plus, Pro, Team, Edu, or Enterprise account.

### Upgrading

```bash
npm install -g @openai/codex@latest
```

---

## Understanding Containers

### What is a Container?

A container is an isolated process with all of the files it needs to run. Unlike virtual machines, containers share the host system's kernel while maintaining complete isolation from one another and the host system.

### Why Use Containers?

Containers solve critical development challenges:

| Benefit | Description |
|---------|-------------|
| **Reproducibility** | Identical environments across development, CI/CD, and production |
| **Isolation** | Applications run independently without conflicting dependencies |
| **Portability** | A container works the same on any machine with a container runtime |
| **Efficiency** | Multiple containers share resources more efficiently than VMs |
| **Version Control** | Pin exact versions of all dependencies, tools, and runtimes |

### When to Use Containers for AI CLIs

Containers are useful when you want to:
- Isolate AI tools from your system (security)
- Share a consistent development environment with a team
- Run multiple versions of tools simultaneously
- Quickly spin up a pre-configured coding environment
- Avoid modifying your host system

---

## Docker vs Podman

### Architecture Comparison

| Aspect | Docker | Podman |
|--------|--------|--------|
| **Architecture** | Daemon-based (dockerd service) | Daemonless (direct process spawning) |
| **Root Access** | Daemon runs as root by default | Rootless by design |
| **Single Point of Failure** | Daemon crash affects all containers | No central service to fail |
| **CLI Compatibility** | Original syntax | Docker-compatible (`alias docker=podman`) |

### Platform Comparison

#### macOS

| Feature | Docker Desktop | Podman Desktop |
|---------|---------------|----------------|
| **Installation** | `brew install --cask docker` | `brew install podman` |
| **Maturity** | Very polished, years of refinement | Functional but less refined |
| **Resource Usage** | ~2GB RAM for VM | ~1.5GB RAM for VM |
| **GUI** | Comprehensive dashboard | Basic but improving |
| **License** | Paid for companies >250 employees | Free and open source |

#### Linux

| Feature | Docker | Podman |
|---------|--------|--------|
| **Installation** | `apt install docker.io` | `apt install podman` |
| **Native Performance** | Excellent | Excellent |
| **Rootless Mode** | Supported (extra config) | Default behavior |
| **Systemd Integration** | Requires configuration | Native support |
| **SELinux/AppArmor** | Supported | Better integration |

#### Windows

| Feature | Docker Desktop | Podman Desktop |
|---------|---------------|----------------|
| **Installation** | `winget install Docker.DockerDesktop` | `winget install RedHat.Podman-Desktop` |
| **WSL2 Support** | Excellent | Good |
| **GUI Quality** | More polished | Improving rapidly |
| **GPU Support** | Supported via WSL2 | Limited (see below) |

### GPU Access

Both Docker and Podman support NVIDIA GPU passthrough on Linux via the NVIDIA Container Toolkit, but there are important differences:

| Aspect | Docker | Podman |
|--------|--------|--------|
| **Linux GPU Support** | `--gpus all` flag | `--device nvidia.com/gpu=all` flag |
| **macOS GPU Support** | Not supported (VM isolation) | Not supported (VM isolation) |
| **Windows GPU Support** | Supported via WSL2 | Limited/experimental |
| **Setup Complexity** | Simpler with `--gpus` flag | Requires CDI configuration |
| **Rootless GPU** | Supported | Requires `no-cgroups=true` config |

**GPU Setup on Linux:**
```bash
# Install NVIDIA Container Toolkit (works for both Docker and Podman)
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit

# Configure for Docker
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

# Configure for Podman
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```

### macOS GPU Limitations (Apple Silicon)

**Important:** Native Apple GPU access (Metal/MLX) is **not available** in containers on macOS. This is a fundamental limitation that applies to Docker, Podman, and Apple's native container tool.

#### Why It Doesn't Work

Containers on macOS run inside a Linux VM via Apple's Hypervisor.framework, which doesn't expose:
- **Metal API** - Apple's native graphics/compute API
- **MLX** - Apple's machine learning framework (built on Metal)
- **Neural Engine** - Apple's dedicated ML accelerator
- **Core ML** - Apple's ML inference framework

#### Apple's Native Container Tool (macOS 26+)

Apple introduced a first-party container framework at WWDC 2025, included in macOS 26 "Tahoe". However, **GPU passthrough is not supported**.

The maintainers confirmed: *"We do not currently support this."* ([GitHub Discussion #62](https://github.com/apple/container/discussions/62))

**Installation (macOS 26 Tahoe required):**
```bash
# Download from GitHub releases
# https://github.com/apple/container/releases

# After installing the .pkg, start the service
container system start

# Test basic container (no GPU)
container run --rm -it ubuntu:latest
```

**Testing for GPU devices (will be empty):**
```bash
container run --rm -it ubuntu:latest ls -la /dev/dri
# Expected: No such file or directory (GPU not exposed)
```

#### Available Workarounds

| Option | Description | Limitations |
|--------|-------------|-------------|
| **Apple Container** | Native macOS 26 container tool | No GPU support, CPU only |
| **Podman + libkrun** | Vulkan passthrough via Venus/MoltenVK | Only Vulkan works, ~60-80% native performance, requires Fedora containers |
| **Docker Model Runner** | Host-side GPU inference exposed as API | Only for LLM inference, not general compute |
| **Native execution** | Run MLX/Metal workloads directly on macOS | No container isolation |

#### Podman with Vulkan GPU Passthrough

Podman Desktop now defaults to libkrun, which enables Vulkan (not Metal) GPU access:

```bash
# Initialize Podman machine (libkrun is now default)
podman machine init --memory 8192
podman machine start

# Verify GPU access
podman machine ssh ls /dev/dri
# Should show: card0  renderD128

# Run container with Vulkan GPU access (requires Fedora-based image)
podman run --device /dev/dri -it fedora:40
```

#### Recommendation for ML Workloads on macOS

| Workload | Recommendation |
|----------|---------------|
| **MLX / Apple ML** | Run natively, not in containers |
| **PyTorch with MPS** | Run natively, not in containers |
| **Vulkan-compatible AI** | Podman with libkrun |
| **LLM inference** | Native llama.cpp or Docker Model Runner |
| **CPU-only workloads** | Docker or Podman (ARM64 images) |

> **Note:** Recent llama.cpp ARM optimizations (Q4_0 quantization) run 2-3x faster on Apple Silicon CPUs than in 2024, making CPU inference viable for many workloads.

### Other Hardware Considerations

| Hardware | Docker | Podman | Notes |
|----------|--------|--------|-------|
| **USB Devices** | `--device` flag | `--device` flag | Both support device passthrough |
| **Serial Ports** | Supported | Supported | Pass device path directly |
| **Audio** | PulseAudio/ALSA passthrough | PulseAudio/ALSA passthrough | Requires volume mounts |
| **Display** | X11/Wayland passthrough | X11/Wayland passthrough | Mount `/tmp/.X11-unix` |

### Recommendation Summary

| Scenario | Recommendation |
|----------|---------------|
| **General use on macOS** | Docker Desktop (more polished) |
| **macOS 26 Tahoe users** | Apple Container (native, no license fees, no GPU) |
| **Enterprise on macOS** | Podman Desktop (no license fees) |
| **Linux servers** | Podman (rootless, better security) |
| **Linux desktop** | Either (both work well) |
| **Windows development** | Docker Desktop (better GPU support) |
| **GPU workloads (Linux)** | Docker on Linux (simpler setup) |
| **GPU workloads (macOS)** | Run natively, or Podman with libkrun (Vulkan only) |
| **Security-critical** | Podman (daemonless, rootless) |
| **Kubernetes workflows** | Podman (native pod support) |

---

## Container Setup

Running AI coding assistants in containers provides isolation and reproducibility.

### Dockerfile

Create a file named `Dockerfile`:

```dockerfile
FROM node:20-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tmux \
    jq \
    git \
    curl \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install uv (fast Python package manager)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Install AI CLIs
RUN npm install -g @anthropic-ai/claude-code @google/gemini-cli @openai/codex

# Create non-root user
RUN useradd -m -s /bin/bash developer

# Setup directories for CLI configs and workspace
RUN mkdir -p /home/developer/.claude \
             /home/developer/.gemini \
             /home/developer/.codex \
             /home/developer/workspace && \
    chown -R developer:developer /home/developer

# Install uv for developer user
USER developer
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /home/developer

# Add shell aliases and PATH
RUN echo "alias c='claude'" >> ~/.bashrc && \
    echo "alias g='gemini'" >> ~/.bashrc && \
    echo "alias x='codex'" >> ~/.bashrc && \
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

WORKDIR /home/developer/workspace

CMD ["/bin/bash"]
```

> **Tip:** Use `uv pip install <package>` instead of `pip install` for faster Python package installation inside the container.

### Building the Container

```bash
# Docker
docker build -t ai-coding-cli -f Dockerfile .

# Podman
podman build -t ai-coding-cli -f Dockerfile .

# Rebuild without cache (to get latest CLI versions)
docker build --no-cache -t ai-coding-cli -f Dockerfile .
```

### Running the Container

> **Note:** The container paths like `/home/developer/workspace` are **Linux paths inside the container** (standard Linux home directory structure). Your host paths depend on your OS:
> - **macOS:** `~` = `/Users/username`
> - **Linux:** `~` = `/home/username`
> - **Windows:** `~` = `C:\Users\username`

**Basic usage:**
```bash
# Docker
docker run -it ai-coding-cli

# Podman
podman run -it ai-coding-cli
```

**Mount current directory as workspace:**
```bash
# Mounts your current working directory into the container
docker run -it -v "$(pwd)":/home/developer/workspace ai-coding-cli
```

**Persist authentication credentials (recommended):**
```bash
docker run -it \
  -v ~/.claude:/home/developer/.claude \
  -v ~/.gemini:/home/developer/.gemini \
  -v ~/.codex:/home/developer/.codex \
  -v "$(pwd)":/home/developer/workspace \
  ai-coding-cli
```

| Host Path | Container Path | Purpose |
|-----------|---------------|---------|
| `~/.claude` | `/home/developer/.claude` | Claude Code auth & settings |
| `~/.gemini` | `/home/developer/.gemini` | Gemini CLI auth & settings |
| `~/.codex` | `/home/developer/.codex` | Codex CLI auth & settings (`config.toml`, sessions) |
| `$(pwd)` | `/home/developer/workspace` | Your current project directory |

**Using environment variables for API keys:**
```bash
docker run -it \
  -e ANTHROPIC_API_KEY="your-key" \
  -e OPENAI_API_KEY="your-key" \
  -e GEMINI_API_KEY="your-key" \
  -v "$(pwd)":/home/developer/workspace \
  ai-coding-cli
```

### Docker Compose Setup

Create `docker-compose.yml`:

```yaml
services:
  ai-cli:
    build:
      context: .
      dockerfile: Dockerfile
    image: ai-coding-cli
    container_name: ai-coding-assistant
    stdin_open: true
    tty: true
    volumes:
      - .:/home/developer/workspace                # Current directory
      - claude-config:/home/developer/.claude
      - gemini-config:/home/developer/.gemini
      - codex-config:/home/developer/.codex
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-}
      - OPENAI_API_KEY=${OPENAI_API_KEY:-}
      - GEMINI_API_KEY=${GEMINI_API_KEY:-}

volumes:
  claude-config:
  gemini-config:
  codex-config:
```

Run with:
```bash
docker compose run --rm ai-cli
```

### Docker Compose with Model Runner (macOS GPU Inference)

This configuration adds Docker Model Runner for GPU-accelerated LLM inference on macOS:

```yaml
services:
  ai-cli:
    build:
      context: .
      dockerfile: Dockerfile
    image: ai-coding-cli
    container_name: ai-coding-assistant
    stdin_open: true
    tty: true
    volumes:
      - .:/home/developer/workspace
      - claude-config:/home/developer/.claude
      - gemini-config:/home/developer/.gemini
      - codex-config:/home/developer/.codex
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-}
      - OPENAI_API_KEY=${OPENAI_API_KEY:-}
      - GEMINI_API_KEY=${GEMINI_API_KEY:-}
      # OpenAI-compatible endpoint for local LLM
      - OPENAI_API_BASE=http://model-runner.docker.internal/engines/llama.cpp/v1
      - LOCAL_LLM_MODEL=ai/llama3.2:1B-Q8_0
    extra_hosts:
      - "model-runner.docker.internal:host-gateway"

volumes:
  claude-config:
  gemini-config:
  codex-config:
```

**Setup Docker Model Runner (one-time, on host):**

```bash
# Enable Model Runner in Docker Desktop
docker desktop enable model-runner

# Optional: Enable TCP access from host applications (port 12434)
docker desktop enable model-runner --tcp 12434

# Pull the model (runs on host with Metal GPU)
docker model pull ai/llama3.2:1B-Q8_0

# Verify model is available
docker model list
```

**Using Model Runner from inside the container:**

```bash
# Start container
docker compose run --rm ai-cli

# Inside container: Test the API
curl -s http://model-runner.docker.internal/engines/llama.cpp/v1/models | jq

# Chat completion request
curl -X POST http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ai/llama3.2:1B-Q8_0",
    "messages": [
      {"role": "system", "content": "You are a helpful coding assistant."},
      {"role": "user", "content": "Write a Python hello world program."}
    ],
    "temperature": 0.7,
    "max_tokens": 256
  }'
```

**Python example (inside container):**

```python
# Install: uv pip install openai
from openai import OpenAI

client = OpenAI(
    base_url="http://model-runner.docker.internal/engines/llama.cpp/v1",
    api_key="not-needed"  # No API key required for local model
)

response = client.chat.completions.create(
    model="ai/llama3.2:1B-Q8_0",
    messages=[
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "Explain Docker volumes briefly."}
    ],
    temperature=0.7,
    max_tokens=256
)

print(response.choices[0].message.content)
```

**Model Runner API Endpoints:**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/engines/llama.cpp/v1/models` | GET | List available models |
| `/engines/llama.cpp/v1/chat/completions` | POST | Chat completion (OpenAI-compatible) |
| `/engines/llama.cpp/v1/completions` | POST | Text completion |
| `/engines/llama.cpp/v1/embeddings` | POST | Generate embeddings |

> **Note:** Model Runner runs on the **macOS host** with direct Metal GPU access. Containers access it via the `model-runner.docker.internal` DNS name. This bypasses the VM's GPU limitations.

### Authentication in Containers

Each CLI requires authentication on first use:

1. **Claude Code**: Run `claude` and follow the browser authentication flow
2. **Gemini CLI**: Run `gemini` and authenticate with Google
3. **Codex CLI**: Run `codex` and sign in with ChatGPT

For headless environments, copy the authentication URL to your host machine's browser.

---

## Troubleshooting

### Common Issues

**"Permission denied" on Linux/macOS:**
```bash
# Fix npm global permissions
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

**Claude Code not found after installation:**
```bash
# Add to PATH (adjust for your shell)
export PATH="$HOME/.claude/bin:$PATH"
```

**Container authentication issues:**
- For browser-based auth, copy the URL to your host browser
- For API key auth, use environment variables

**Docker permission denied:**
```bash
# Add user to docker group
sudo usermod -aG docker $USER
# Log out and back in
```

**Podman GPU access issues:**
```bash
# Regenerate CDI specification
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml

# For rootless containers, edit /etc/nvidia-container-runtime/config.toml
# Set: no-cgroups = true
```

### Verifying Installation

```bash
# Check Claude Code
claude --version

# Check Gemini CLI
gemini --version

# Check Codex CLI
codex --version
```

---

## References

### Official CLI Documentation

- **Claude Code**
  - Documentation: https://code.claude.com/docs/en/overview
  - Repository: https://github.com/anthropics/claude-code
  - Releases: https://github.com/anthropics/claude-code/releases

- **Gemini CLI**
  - Repository: https://github.com/google-gemini/gemini-cli
  - Documentation: https://geminicli.com/docs/
  - Releases: https://github.com/google-gemini/gemini-cli/releases

- **OpenAI Codex CLI**
  - Repository: https://github.com/openai/codex
  - Releases: https://github.com/openai/codex/releases
  - [Configuration Reference](https://developers.openai.com/codex/config-reference/)

### Docker Model Runner

- [Docker Model Runner Documentation](https://docs.docker.com/ai/model-runner/)
- [DMR REST API Reference](https://docs.docker.com/ai/model-runner/api-reference/)
- [Introducing Docker Model Runner](https://www.docker.com/blog/introducing-docker-model-runner/)
- [Docker Model Runner GA Announcement](https://www.docker.com/blog/announcing-docker-model-runner-ga/)
- [Model Runner Vulkan GPU Support](https://www.docker.com/blog/docker-model-runner-vulkan-gpu-support/)
- [GitHub: docker/model-runner](https://github.com/docker/model-runner)

### Container Documentation

- **Docker**
  - What is a Container: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/
  - Install Docker: https://docs.docker.com/get-docker/
  - Docker Compose: https://docs.docker.com/compose/

- **Podman**
  - Official Site: https://podman.io/
  - Podman Desktop: https://podman-desktop.io/
  - GPU Access: https://podman-desktop.io/docs/podman/gpu

- **Container Comparison**
  - [Podman vs Docker 2026: Security, Performance & Which to Choose](https://last9.io/blog/podman-vs-docker/)
  - [Podman vs Docker: Key Differences Explained](https://www.invensislearning.com/blog/podman-vs-docker/)
  - [Docker vs Podman: Containerization Tools Comparison](https://spacelift.io/blog/podman-vs-docker)

### GPU Support

- **NVIDIA Container Toolkit**
  - Installation Guide: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
  - Podman Configuration: https://docs.nvidia.com/ai-enterprise/deployment/rhel-with-kvm/latest/podman.html

- **Apple Native Container Tool (macOS 26+)**
  - [Apple Container GitHub Repository](https://github.com/apple/container)
  - [Apple Container Releases](https://github.com/apple/container/releases)
  - [GPU Passthrough Discussion (not supported)](https://github.com/apple/container/discussions/62)
  - [Under the hood with Apple's Containerization framework](https://anil.recoil.org/notes/apple-containerisation)
  - [Apple's Container Tool Overview (WWDC 2025)](https://techxplainator.com/apple-macos-container-tool/)

- **macOS GPU in Containers**
  - [Enabling containers to access the GPU on macOS](https://sinrega.org/2024-03-06-enabling-containers-gpu-macos/)
  - [GPU-Accelerated Containers for M-series Macs](https://medium.com/@andreask_75652/gpu-accelerated-containers-for-m1-m2-m3-macs-237556e5fe0b)
  - [Podman Desktop GPU Access](https://podman-desktop.io/docs/podman/gpu)

### Windows Tools

- **PowerShell**
  - [Install PowerShell on Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
  - [PowerShell Documentation](https://learn.microsoft.com/en-us/powershell/)

- **WinGet (Windows Package Manager)**
  - [WinGet Documentation](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
  - [WinGet CLI Repository](https://github.com/microsoft/winget-cli)

- **OpenSSH on Windows**
  - [OpenSSH for Windows Overview](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-overview)
  - [Get started with OpenSSH](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)

### Package Managers

- **uv** (Python): https://docs.astral.sh/uv/
- Homebrew (macOS/Linux): https://brew.sh/
- WinGet (Windows): https://learn.microsoft.com/en-us/windows/package-manager/winget/
- npm: https://www.npmjs.com/
- Node.js: https://nodejs.org/

### Community Resources

- [Claude Code Tips (Container Setup)](https://github.com/ykdojo/claude-code-tips/tree/main/container)

---

## License and Disclaimer

**Author:** Torbjörn E. M. Nordling, PhD

Unless otherwise specified, content in this repository is licensed under:

- **Documentation:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Source Code:** [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

See individual submissions for specific license declarations.

THIS DOCUMENT AND ALL ASSOCIATED CODE ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS DOCUMENT OR THE USE OR OTHER DEALINGS IN THIS DOCUMENT.

*Last updated: 2026-01-17*
