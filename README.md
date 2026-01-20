# Agentic AI Course - Student Submissions Repository

This repository contains all student submissions for the **Agentic AI** course (代理式人工智慧) at National Cheng Kung University.

---

## IMPORTANT NOTICES

### License Requirements

All submitted material **must** be licensed under one of the following:

- **Apache License 2.0** (for code)
- **CC-BY-4.0** (Creative Commons Attribution 4.0, for documentation and data)

You may **only** submit material that you have the right to make public under these licenses. Each submission folder and file **must** clearly indicate its license.

### Privacy and Data Protection

**NO PERSONALLY IDENTIFIABLE INFORMATION (PII) MAY BE INCLUDED.**

This includes but is not limited to:

- Names linked to data (other than author attribution, which naturally must be included)
- Student IDs, national IDs, or any identification numbers
- Photos of identifiable individuals
- Health data linked to identifiable persons
- Contact information of subjects
- Any information that could link collected data to a specific person

**Violation of this policy may result in immediate removal of your submission and disciplinary action.**

---

## Submission Format Requirements

| Submission Type | Format | Location |
|-----------------|--------|----------|
| SSH Public Key (Individual) | OpenSSH `.pub` | `ssh-keys-individual/` |
| Case Brief (Individual) | Markdown `.md` | `case-brief-individual/` |
| Data (Group) | Folder with data files incl. `README.md` | `data-group/` |
| Project Code (Group) | Folder with code incl. `README.md` | `project-code-group/` |
| Test Cases (Group) | Markdown `.md` with reference to `tests/` in project code | `tests-group/` |
| System Design (Group) | draw.io `.drawio` XML (UML standard) | `system-design-group/` |
| Presentation Slides (Group) | Beamer `.tex` (NordlingLab 16:9 template) | `slides-demonstration-group/` |
| Video Demonstration (Group) | YouTube link `.txt` | `video-demonstration-group/` |
| Reflection (Group) | Markdown `.md` | `reflection-group/` |
| Technical Report (Individual) | Markdown `.md` | `report-individual/` |

See the `README.md` in each folder for detailed requirements, grading criteria, and examples.

### Deadline Summary

| Date | Time | Submissions Due |
|------|------|-----------------|
| Fri 2026-01-16 | 10:00 | SSH Public Key, Case Brief |
| Tue 2026-01-20 | 13:00 | Data, Project Code, Test Cases, System Design |
| Wed 2026-01-21 | 13:00 | Presentation Slides, Video, Reflection |
| Fri 2026-01-23 | 13:00 | Technical Report |

**All times are Taiwan Standard Time (UTC+8).**

---

## Naming Standards

### File Naming Convention

#### IMPORTANT: ASCII Characters Only

**Use only ASCII characters in file and folder names. No Chinese characters, spaces, or special characters.**

#### Individual Submissions

Format: `YYYY-FamilyName-FirstName.md`

Examples:

- `2026-Chen-Wei.md`
- `2026-Lin-MeiLing.md`
- `2026-Wang-XiaoMing.md`

#### Group Submissions

Format: `YYYY-FamilyName1-FamilyName2-FamilyName3/` (folder) or `YYYY-FamilyName1-FamilyName2-FamilyName3.ext` (file)

List all group members' family names in alphabetical order.

Examples:

- `2026-Chen-Lin-Wang-code` (folder for group code submissions)
- `2026-Chen-Lin-Wang.tex` (Beamer slides)
- `2026-Chen-Lin-Wang.drawio` (system design)

### Branch/Submission Naming

**Format:** `submission/YYYY-FamilyName-type` or `submission/YYYY-FamilyName1-FamilyName2-FamilyName3-type`

| Type | Example Branch Name |
|------|---------------------|
| SSH key | `submission/2026-Chen-ssh-key` |
| Case brief | `submission/2026-Lin-case-brief` |
| Group data | `submission/2026-Chen-Lin-Wang-data` |
| Group code | `submission/2026-Chen-Lin-Wang-code` |
| Group tests | `submission/2026-Chen-Lin-Wang-tests` |
| Group system design | `submission/2026-Chen-Lin-Wang-system-design` |
| Group slides | `submission/2026-Chen-Lin-Wang-slides` |
| Group video | `submission/2026-Chen-Lin-Wang-video` |
| Group reflection | `submission/2026-Chen-Lin-Wang-reflection` |
| Report | `submission/2026-Lin-report` |

### Remote Naming

| Remote Name | Used By | Points To |
|-------------|---------|-----------|
| `origin` | Everyone | Your own fork |
| `upstream-nordlinglab` | Everyone | `nordlinglab/course-agenticai-ecg-hrv` |
| `upstream-group` | Members only | Group leader's fork |

### Commit Message Format

```
<type>: <short description>

<optional longer description>

Co-Authored-By: Name <email>  (if pair programming)
```

Types: `Add`, `Update`, `Fix`, `Remove`, `Refactor`

Examples:

- `Add: Case brief for Chen-Wei`
- `Update: Fix formatting in group slides`
- `Add: ECG analysis code for group Chen-Lin-Wang`

---

## Repository Structure

```
student-material-ecg-hrv/
│
├── README.md                      # This file
├── INSTALL_CLAUDE_CODE_GEMINI_CODEX_CLI.md  # AI CLI installation guide
├── Syllabus_....md                # Course syllabus (reference)
│
├── ssh-keys-individual/           # Individual SSH public keys (for server access)
├── case-brief-individual/         # Individual case briefs (Markdown)
├── report-individual/             # Individual technical reports (Markdown)
├── reflection-group/              # Group reflection documents (Markdown)
│
├── data-group/                    # Group data submissions (folder per group)
│   └── 2026-Chen-Lin-Wang-data/   # Example: git submodule
│
├── project-code-group/            # Group project code (folder per group)
│   └── 2026-Chen-Lin-Wang-code/   # Example: git submodule
│
├── tests-group/                   # Group test cases and results document (Markdown)
│
├── slides-demonstration-group/    # Group presentation slides (Beamer .tex)
├── video-demonstration-group/    # Group video link to YouTube (.txt)
└── system-design-group/           # Group system design diagrams (draw.io .drawio)
```

### Example Submodules

The example data and code repositories are included as git submodules:

| Submodule | HTTPS URL | SSH URL |
|-----------|-----------|---------|
| `data-group/2026-Chen-Lin-Wang-data` | `https://github.com/nordlinglab/course-agenticai-ecg-hrv-example-data.git` | `git@github.com:nordlinglab/course-agenticai-ecg-hrv-example-data.git` |
| `project-code-group/2026-Chen-Lin-Wang-code` | `https://github.com/nordlinglab/course-agenticai-ecg-hrv-example-code.git` | `git@github.com:nordlinglab/course-agenticai-ecg-hrv-example-code.git` |

**Clone the repository with submodules**:
   ```bash
   git clone --recursive https://github.com/nordlinglab/nordlinglab-course-agenticai-ecg-hrv.git
   cd nordlinglab-course-agenticai-ecg-hrv
   ```

---

## Fork Hierarchy and Workflow Overview

This course uses a **hierarchical fork structure**, which is standard practice in industry for team-based software development.

### Why Hierarchical Forks?

In professional software development, teams rarely submit work directly to the main company repository. Instead:

1. **Individual developers** work in their own forks/branches
2. **Team leads** integrate and review team members' work
3. **Only reviewed, integrated work** gets submitted to the main repository

This pattern provides:

- **Quality gates**: Code is reviewed before reaching the main repo
- **Team autonomy**: Groups can iterate quickly without affecting others
- **Reduced noise**: Maintainers review fewer, higher-quality submissions
- **Clear accountability**: Team leads are responsible for their group's contributions

### The Fork Structure

```
nordlinglab/course-agenticai-ecg-hrv     ← Course repository (TA/Teacher maintains)
        │
        └── group-leader/course-agenticai-ecg-hrv     ← Group repository (Leader's fork)
                │
                ├── member-A/course-agenticai-ecg-hrv     ← Member's fork (of leader)
                └── member-B/course-agenticai-ecg-hrv     ← Member's fork (of leader)
```

### Remote Naming Convention

Each person has different remotes depending on their role:

**Group Leader:**
| Remote | Points To | Purpose |
|--------|-----------|---------|
| `origin` | Your fork | Push your work |
| `upstream-nordlinglab` | nordlinglab repo | Sync course updates, submit group PRs |

**Group Member:**
| Remote | Points To | Purpose |
|--------|-----------|---------|
| `origin` | Your fork | Push your work |
| `upstream-group` | Leader's fork | Submit PRs to group, sync group updates |
| `upstream-nordlinglab` | nordlinglab repo | Sync course updates directly (optional) |

### Complete Workflow Cycle

The diagram below shows the complete submission cycle:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: SETUP (One-time)                                                  │
│  ─────────────────────────                                                  │
│  1.  [All] Install Git                                                      │
│  2.  [All] Configure Git                                                    │
│  3.  [All] Create GitHub Account and Install GitHub CLI                     │
│  4.  [All] Get AI Assistance for Git Commands                               │
│  5.  Fork the Repository                                                    │
│      • [Leader] Fork nordlinglab → creates group repository                 │
│      • [Member] Fork leader's fork → creates personal repository            │
│  6.  [All] Clone Your Fork and Set Up Remotes                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: INDIVIDUAL WORK                                                   │
│  ────────────────────────                                                   │
│  7.  [All] Sync Your Fork Before Starting Work                              │
│  8.  [All] Create a Submission Branch                                       │
│  9.  [All] Make Changes and Commit                                          │
│  10. [All] Push Your Branch to Your Fork                                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 3: GROUP INTEGRATION                                                 │
│  ─────────────────────────                                                  │
│  11. [Member] Create a Pull Request to Group (PR to leader's fork)          │
│  12. Group Code Review Process                                              │
│      • [Leader] Review member PRs, request changes if needed                │
│      • [Member] Update PR based on feedback                                 │
│      • [Leader] Approve and merge member PRs                                │
│  13. [All] After Your PR is Merged (cleanup branches, sync)                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 4: GROUP SUBMISSION                                                  │
│  ────────────────────────                                                   │
│  14. [Leader] Create a Pull Request to Submit Group's Work                  │
│      • Create submission branch from main                                   │
│      • Push branch and create PR to upstream-nordlinglab                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 5: TA REVIEW                                                         │
│  ──────────────────                                                         │
│  15. TA Review and Final Merge                                              │
│      • [TA] Review group PR, request changes if needed                      │
│      • [Leader] Implement changes, update PR                                │
│      • [TA] Approve and merge (squash commits for clean history)            │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  PHASE 6: SYNC UPDATES                                                      │
│  ─────────────────────                                                      │
│  16. Updating Your Fork                                                     │
│      • [Leader] Fetch from upstream-nordlinglab, merge to main, push        │
│      • [Member] Fetch from upstream-group, merge to main, push              │
│      • [All] Ready for next submission cycle                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Pull Request Branch Requirements

**DO NOT submit pull requests from your `main` branch!**

Always create a feature/submission branch for your submissions:

```bash
# WRONG - Do not do this:
# (making changes directly on main and creating PR from main)

# CORRECT - Always do this:
git checkout -b submission/YYYY-YourName-type
# Example: git checkout -b submission/2026-Chen-Wei-ssh-key
```

**Why this matters:**

- PRs from `main` cause merge conflicts when other students' PRs are merged first
- Feature branches can be safely deleted after merge (main cannot)
- This is standard industry practice for collaborative Git workflows

**Branch naming convention:** `submission/YYYY-FamilyName-type` or `submission/YYYY-FamilyName1-FamilyName2-FamilyName3-type`

---

## Git Guide for Beginners

If you have never used Git before, follow these steps carefully.

### Step 1: Install Git **[All students]**

**macOS:**
```bash
# Open Terminal and run:
xcode-select --install
```

**Windows:**
```bash
# Using winget (recommended)
winget install --id Git.Git -e --source winget
# Or download and install from: https://git-scm.com/download/win
```

**Linux (Ubuntu/Debian):**
Normally preinstalled otherwise:
```bash
sudo apt update
sudo apt install git
```

### Step 2: Configure Git **[All students]**

Open your terminal and set your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Create a GitHub Account and Install the GitHub CLI **[All students]**

#### If you don't have a GitHub account:

1. Go to https://github.com/signup
2. Enter your email (you can use your university email)
3. Create a password and username
4. Complete the verification and sign up

#### Install the GitHub CLI (`gh`)

The GitHub CLI makes forking, cloning, and creating pull requests much easier from the terminal.

**macOS:**
```bash
brew install gh
```

**Windows:**
```bash
# Using winget (recommended)
winget install --id GitHub.cli

# Or using scoop
scoop install gh

# Or using choco
choco install gh
```

**Linux (Ubuntu/Debian):**
```bash
# Add GitHub CLI repository
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

#### Authenticate the GitHub CLI

```bash
gh auth login
```

Follow the prompts:

1. Select **GitHub.com**
2. Select **HTTPS** (recommended for beginners) or **SSH**
3. Authenticate with your browser when prompted

Verify authentication:
```bash
gh auth status
```

### Step 4: Get AI Assistance for Git Commands **[All students]**

AI coding assistants (Claude Code, Gemini CLI, GitHub Copilot, Codex CLI) can help you with Git commands. To ensure they understand this course's workflow:

**Recommended prompt:**
```
Read the README.md file in this repository and follow its fork hierarchy
and naming conventions when helping me with git and gh commands.
```

Or more specifically:
```
I'm in a course that uses hierarchical forks: nordlinglab → group-leader → member.
I am a [group leader / group member]. My group leader's GitHub username is [USERNAME].
Help me with git commands following this structure.
```

The AI will then provide commands that match the course's workflow and naming standards.

### Step 5: Fork the Repository

The forking process differs based on your role. See [Fork Hierarchy](#fork-hierarchy-and-workflow-overview) for why.

#### For Group Leaders **[Group Leader only]**

Fork the **course repository** (nordlinglab). Your fork becomes the group's shared repository.

**Using gh CLI:**
```bash
# Fork nordlinglab's repository
gh repo fork nordlinglab/course-agenticai-ecg-hrv --clone=false

# Verify the fork was created
gh repo list --fork
```

**Using Web Interface:**

1. Go to https://github.com/nordlinglab/course-agenticai-ecg-hrv
2. Click **"Fork"** button (upper right)
3. Select your account as destination
4. Click **"Create fork"**

Your fork is now at: `https://github.com/YOUR_USERNAME/course-agenticai-ecg-hrv`

**Tell your group members your GitHub username** so they can fork your repository.

#### For Group Members **[Group Member only]**

Fork your **group leader's repository** (not nordlinglab directly).

**Using gh CLI:**
```bash
# Fork your group leader's repository (replace LEADER_USERNAME)
gh repo fork LEADER_USERNAME/course-agenticai-ecg-hrv --clone=false

# Verify the fork was created
gh repo list --fork
```

**Using Web Interface:**

1. Go to `https://github.com/LEADER_USERNAME/course-agenticai-ecg-hrv`
2. Click **"Fork"** button (upper right)
3. Select your account as destination
4. Click **"Create fork"**

Your fork is now at: `https://github.com/YOUR_USERNAME/course-agenticai-ecg-hrv`

### Step 6: Clone Your Fork and Set Up Remotes **[All students]**

Clone your fork to your local machine and configure the remotes based on your role.

#### Cloning (Same for Everyone)

**Using gh CLI:**
```bash
# Navigate to where you want to store the project
cd ~/Documents

# Clone YOUR fork with submodules
gh repo clone YOUR_USERNAME/course-agenticai-ecg-hrv -- --recursive

# Enter the project directory
cd course-agenticai-ecg-hrv
```

**Using git clone:**
```bash
cd ~/Documents

# HTTPS (recommended for beginners)
git clone --recursive https://github.com/YOUR_USERNAME/course-agenticai-ecg-hrv.git

# Or SSH (if you have SSH keys set up already)
git clone --recursive git@github.com:YOUR_USERNAME/course-agenticai-ecg-hrv.git

cd course-agenticai-ecg-hrv
```

**Note:** See [Setting up SSH Keys for GitHub](#setting-up-ssh-keys-for-github).
The `--recursive` flag initializes git submodules. If you forgot it:
```bash
git submodule update --init --recursive
```

#### Setting Up Remotes - Group Leader **[Group Leader only]**

```bash
# Add nordlinglab as upstream (for syncing course updates and submitting group PRs)
# Using HTTPS:
git remote add upstream-nordlinglab https://github.com/nordlinglab/course-agenticai-ecg-hrv.git
# Or using SSH:
git remote add upstream-nordlinglab git@github.com:nordlinglab/course-agenticai-ecg-hrv.git

# Verify your remotes
git remote -v
# Expected output:
# origin                https://github.com/YOUR_USERNAME/course-agenticai-ecg-hrv.git (fetch)
# origin                https://github.com/YOUR_USERNAME/course-agenticai-ecg-hrv.git (push)
# upstream-nordlinglab  https://github.com/nordlinglab/course-agenticai-ecg-hrv.git (fetch)
# upstream-nordlinglab  https://github.com/nordlinglab/course-agenticai-ecg-hrv.git (push)
```

#### Setting Up Remotes - Group Member **[Group Member only]**

```bash
# Add group leader's fork as upstream-group (for submitting PRs and syncing)
# Using HTTPS:
git remote add upstream-group https://github.com/LEADER_USERNAME/course-agenticai-ecg-hrv.git
# Or using SSH:
git remote add upstream-group git@github.com:LEADER_USERNAME/course-agenticai-ecg-hrv.git

# Add nordlinglab as upstream-nordlinglab (optional, for direct course updates)
# Using HTTPS:
git remote add upstream-nordlinglab https://github.com/nordlinglab/course-agenticai-ecg-hrv.git
# Or using SSH:
git remote add upstream-nordlinglab git@github.com:nordlinglab/course-agenticai-ecg-hrv.git

# Verify your remotes
git remote -v
# Expected output:
# origin                https://github.com/YOUR_USERNAME/course-agenticai-ecg-hrv.git (fetch)
# origin                https://github.com/YOUR_USERNAME/course-agenticai-ecg-hrv.git (push)
# upstream-group        https://github.com/LEADER_USERNAME/course-agenticai-ecg-hrv.git (fetch)
# upstream-group        https://github.com/LEADER_USERNAME/course-agenticai-ecg-hrv.git (push)
# upstream-nordlinglab  https://github.com/nordlinglab/course-agenticai-ecg-hrv.git (fetch)
# upstream-nordlinglab  https://github.com/nordlinglab/course-agenticai-ecg-hrv.git (push)
```

### Step 7: Sync Your Fork Before Starting Work **[All students]**

Before creating a new submission, always sync your fork with the latest changes.

#### For Group Leaders **[Group Leaders, but Group Members can also do it]**

```bash
# Fetch updates from nordlinglab
git fetch upstream-nordlinglab

# Switch to main branch
git checkout main

# Merge updates
git merge upstream-nordlinglab/main

# Push to your fork (which is also the group repo)
git push origin main

# Update submodules
git submodule update --init --recursive
```

**Using gh CLI (alternative):**
```bash
gh repo sync YOUR_USERNAME/course-agenticai-ecg-hrv --source nordlinglab/course-agenticai-ecg-hrv
git pull origin main
git submodule update --init --recursive
```

#### For Group Members **[Group Member only]**

```bash
# Fetch updates from group leader's fork
git fetch upstream-group

# Switch to main branch
git checkout main

# Merge updates
git merge upstream-group/main

# Push to your fork
git push origin main

# Update submodules
git submodule update --init --recursive
```

### Step 8: Create a Submission Branch **[All students]**

**IMPORTANT: Never commit directly to `main`. Always create a feature branch.**

```bash
# Make sure you're on main and it's up to date
git checkout main
git pull origin main

# Create a submission branch (see Naming Standards for format)
git checkout -b submission/YYYY-YourFamilyName-type

# Examples:
# Individual: git checkout -b submission/2026-Chen-case-brief
# Group:      git checkout -b submission/2026-Chen-Lin-Wang-slides
```

### Step 9: Make Changes and Commit **[All students]**

```bash
# Navigate to the appropriate folder
cd case-brief-individual/  # or slides-demonstration-group/, etc.

# Create or edit your file(s) using your text editor
# Follow the naming convention: YYYY-FamilyName-FirstName

# Check what files have changed
git status

# Stage your files
git add YYYY-FamilyName-FirstName.md
# Or stage all changes in current folder:
git add .

# Commit with a descriptive message (see Naming Standards for format)
git commit -m "Add: Case brief for Chen-Wei"
```

### Step 10: Push Your Branch to Your Fork **[All students]**

```bash
# Push your submission branch to your fork
git push origin submission/YYYY-YourFamilyName-type

# Example:
git push origin submission/2026-Chen-case-brief
```

### Step 11: Create a Pull Request to Group **[Group Member only]**

Group members submit PRs to their group leader's fork (`upstream-group`).

#### PR to Group Leader

**Using gh CLI:**
```bash
# Create PR to your group leader's repository
gh pr create --repo LEADER_USERNAME/course-agenticai-ecg-hrv \
  --title "Submission: YYYY-YourFamilyName - [type]" \
  --body "Description of what you're submitting"

# Or interactively:
gh pr create --repo LEADER_USERNAME/course-agenticai-ecg-hrv
```

**Using Web Interface:**

1. Go to your fork: `github.com/YOUR_USERNAME/course-agenticai-ecg-hrv`
2. You'll see a banner: "submission/... had recent pushes" → Click **"Compare & pull request"**
3. Or: Click **"Pull requests"** tab → **"New pull request"**
4. Set:
   - **base repository:** `LEADER_USERNAME/course-agenticai-ecg-hrv`
   - **base:** `main`
   - **head repository:** `YOUR_USERNAME/course-agenticai-ecg-hrv`
   - **compare:** `submission/YYYY-YourFamilyName-type`
5. Fill in title and description
6. Click **"Create pull request"**

### Step 12: Group Code Review Process

#### For Group Leaders - Reviewing Member PRs **[Group Leader only]**

When group members submit PRs to your repository:

**Using gh CLI:**
```bash
# List pending PRs in your repository
gh pr list

# View a specific PR
gh pr view PR_NUMBER

# View the changes
gh pr diff PR_NUMBER

# Check out the PR locally for testing
gh pr checkout PR_NUMBER

# Add a comment
gh pr comment PR_NUMBER --body "Your feedback here"

# Request changes
gh pr review PR_NUMBER --request-changes --body "Please fix..."

# Approve the PR
gh pr review PR_NUMBER --approve --body "Looks good!"

# Merge the PR (squash recommended for clean history)
gh pr merge PR_NUMBER --squash --delete-branch
```

**Using Web Interface:**

1. Go to **"Pull requests"** tab in your repository
2. Click on the PR to review
3. Go to **"Files changed"** tab to see the diff
4. Click the **+** button on any line to add comments
5. Click **"Review changes"** → Select **Approve** or **Request changes**
6. When ready, click **"Merge pull request"** → **"Squash and merge"**

#### For Group Members - Responding to Feedback **[Group Member only]**

If the leader requests changes:

```bash
# Make sure you're on your submission branch
git checkout submission/YYYY-YourFamilyName-type

# Make the requested changes to your files

# Stage and commit the fixes
git add .
git commit -m "Fix: Address review feedback"

# Push the updates (the PR will automatically update)
git push origin submission/YYYY-YourFamilyName-type
```

### Step 13: After Your PR is Merged **[All students]**

Once your PR is merged, clean up your local branches:

```bash
# Switch back to main
git checkout main

# Delete your local submission branch
git branch -d submission/YYYY-YourFamilyName-type

# Delete the remote branch (may already be deleted by merge then this command does nothing but is safe to execute)
git push origin --delete submission/YYYY-YourFamilyName-type
```

#### For Group Leaders - Sync with Changes **[Group Leader only]**

```bash
# Sync your main with the merged changes from nordlinglab
git fetch upstream-nordlinglab
git merge upstream-nordlinglab/main

git push origin main
```

#### For Group Members - Sync with Changes **[Group Member only]**

```bash
# Sync your main with the merged changes from group
git fetch upstream-group
git merge upstream-group/main
# Sync your main with the merged changes from nordlinglab (optional)
git fetch upstream-nordlinglab
git merge upstream-nordlinglab/main

git push origin main
```

### Step 14: Create a Pull Request to Submit Group's Work **[Group Leader only]**


First, ensure all member PRs are merged into your main branch. Then create a submission branch and PR:

```bash
# 1. Make sure main has all merged member work
git checkout main
git pull origin main

# 2. Create submission branch from main
git checkout -b submission/YYYY-GroupNames-type
# Example: git checkout -b submission/2026-Chen-Lin-Wang-code

# 3. Push the branch to origin
git push origin submission/YYYY-GroupNames-type
```

**Using gh CLI:**
```bash
# 4. Create PR to the course repository (run from your submission branch)
gh pr create --repo nordlinglab/course-agenticai-ecg-hrv \
  --title "Submission: YYYY-FamilyName1-FamilyName2-FamilyName3 - [type]" \
  --body "Group submission containing work from: [list members]"

# Or interactively:
gh pr create --repo nordlinglab/course-agenticai-ecg-hrv
```

**Using Web Interface:**

1. Go to your fork: `github.com/YOUR_USERNAME/course-agenticai-ecg-hrv`
2. Click **"Contribute"** → **"Open pull request"**
3. Set:
   - **base repository:** `nordlinglab/course-agenticai-ecg-hrv`
   - **base:** `main`
   - **head repository:** `YOUR_USERNAME/course-agenticai-ecg-hrv`
   - **compare:** `submission/YYYY-GroupNames-type`
4. Fill in title and description
5. Click **"Create pull request"**

### Step 15: TA Review and Final Merge **[TA/Teacher]**

When reviewing group submissions to nordlinglab:

```bash
# List pending PRs
gh pr list --repo nordlinglab/course-agenticai-ecg-hrv

# Review a PR
gh pr view PR_NUMBER --repo nordlinglab/course-agenticai-ecg-hrv
gh pr diff PR_NUMBER --repo nordlinglab/course-agenticai-ecg-hrv

# Check out locally for testing
gh pr checkout PR_NUMBER --repo nordlinglab/course-agenticai-ecg-hrv

# Request changes if needed
gh pr review PR_NUMBER --repo nordlinglab/course-agenticai-ecg-hrv \
  --request-changes --body "Please fix the following issues: ..."

# Approve and merge with squashed commits (clean history)
gh pr review PR_NUMBER --repo nordlinglab/course-agenticai-ecg-hrv --approve
gh pr merge PR_NUMBER --repo nordlinglab/course-agenticai-ecg-hrv \
  --squash --delete-branch
```

#### For Group Leaders - Responding to Feedback **[Group Leader only]**

If TA requests changes:

```bash
# Make sure you're on your submission branch
git checkout submission/YYYY-GroupNames-type

# Make the requested changes

# Commit and push
git add .
git commit -m "Fix: Address TA feedback"
git push origin submission/YYYY-GroupNames-type
# The PR will automatically update
```

### Step 16: Updating Your Fork **[All students]**

Sync your fork when the upstream repository has new changes.

#### For Group Leaders **[Group Leader only]**

Sync from nordlinglab (course repository):

**Using git commands:**
```bash
# Fetch from nordlinglab
git fetch upstream-nordlinglab

# Merge into your main branch
git checkout main
git merge upstream-nordlinglab/main

# Update submodules
git submodule update --init --recursive

# Push to your fork (group repo)
git push origin main
```

**Using gh CLI:**
```bash
gh repo sync YOUR_USERNAME/course-agenticai-ecg-hrv --source nordlinglab/course-agenticai-ecg-hrv
git pull origin main
git submodule update --init --recursive
```

#### For Group Members **[Group Member only]**

Sync from your group leader's fork:

**Using git commands:**
```bash
# Fetch from group leader's fork
git fetch upstream-group

# Merge into your main branch
git checkout main
git merge upstream-group/main

# Update submodules
git submodule update --init --recursive

# Push to your fork
git push origin main
```

**Optional: Sync directly from nordlinglab** (if leader hasn't synced yet):
```bash
git fetch upstream-nordlinglab
git merge upstream-nordlinglab/main
git push origin main
```

---

## Common Git Commands Reference

| Command | Description |
|---------|-------------|
| `git status` | Show changed files |
| `git add <file>` | Stage a file for commit |
| `git add .` | Stage all changed files |
| `git commit -m "message"` | Commit staged changes |
| `git push` | Upload commits to remote |
| `git pull` | Download updates from remote |
| `git log` | View commit history |
| `git diff` | Show unstaged changes |

---

## Reviewing Pull Requests

This section provides additional detail on reviewing pull requests. See also [Step 12: Code Review Process](#step-12-code-review-process).

### Using the GitHub CLI (Recommended)

The `gh` CLI provides powerful commands for managing pull requests.

#### Listing Pull Requests

**[Group Leader]** - List PRs in your repository (from group members):
```bash
gh pr list
```

**[TA/Teacher]** - List PRs in nordlinglab:
```bash
gh pr list --repo nordlinglab/course-agenticai-ecg-hrv
```

**[All]** - List PRs assigned to you for review:
```bash
gh pr list --repo nordlinglab/course-agenticai-ecg-hrv --search "review-requested:@me"
```

#### Viewing a Pull Request

```bash
# View PR details in terminal
gh pr view 123 --repo nordlinglab/course-agenticai-ecg-hrv

# View PR in web browser
gh pr view 123 --repo nordlinglab/course-agenticai-ecg-hrv --web

# View the diff (changes)
gh pr diff 123 --repo nordlinglab/course-agenticai-ecg-hrv
```

#### Checking Out a PR Locally for Review

```bash
# Check out the PR branch locally to test/review the code
gh pr checkout 123 --repo nordlinglab/course-agenticai-ecg-hrv

# Run tests, review code, etc.
# ...

# Return to your main branch when done
git checkout main
```

#### Adding Comments

```bash
# Add a general comment to a PR
gh pr comment 123 --repo nordlinglab/course-agenticai-ecg-hrv --body "Your comment here"

# Add a comment interactively (opens editor)
gh pr comment 123 --repo nordlinglab/course-agenticai-ecg-hrv
```

#### Approving or Requesting Changes

```bash
# Approve the pull request
gh pr review 123 --repo nordlinglab/course-agenticai-ecg-hrv --approve

# Approve with a comment
gh pr review 123 --repo nordlinglab/course-agenticai-ecg-hrv --approve --body "Looks good!"

# Request changes
gh pr review 123 --repo nordlinglab/course-agenticai-ecg-hrv --request-changes --body "Please fix the formatting in line 42"

# Add a comment without approving or requesting changes
gh pr review 123 --repo nordlinglab/course-agenticai-ecg-hrv --comment --body "Question about line 15..."
```

#### Merging a Pull Request

```bash
# Merge with default strategy (merge commit)
gh pr merge 123 --repo nordlinglab/course-agenticai-ecg-hrv

# Squash merge (combines all commits into one)
gh pr merge 123 --repo nordlinglab/course-agenticai-ecg-hrv --squash

# Rebase merge (replay commits on top of main)
gh pr merge 123 --repo nordlinglab/course-agenticai-ecg-hrv --rebase

# Merge and delete the branch (recommended)
gh pr merge 123 --repo nordlinglab/course-agenticai-ecg-hrv --squash --delete-branch
```

#### Merging a PR into Your Local Branch

After a PR is merged on GitHub, update your local repository:

```bash
# Fetch all updates from remotes
git fetch --all

# Merge the changes into your local branch
git merge origin/main

# Or pull directly
git pull origin main

# Update submodules if any changed
git submodule update --init --recursive
```

---

### In GitHub Web Interface

#### Viewing a Pull Request

1. Go to the repository on GitHub
2. Click **"Pull requests"** tab
3. Click on the pull request you want to review
4. You'll see:

   - **"Conversation"** tab: Description, comments, and status
   - **"Commits"** tab: Individual commits in the PR
   - **"Files changed"** tab: All changed files with line-by-line diff

#### Reviewing Changes

1. Click on the **"Files changed"** tab
2. Changes are shown with:

   - **Green background:** Added lines
   - **Red background:** Removed lines

3. Hover over a line number and click the **blue +** button to add a comment

#### Adding Comments and Requesting Changes

1. Click the **blue +** button next to any line in the **"Files changed"** tab
2. Type your comment (you can use Markdown)
3. Click **"Add single comment"** for immediate comment, or **"Start a review"** to batch multiple comments
4. When done reviewing, click **"Finish your review"** and select:

   - **Comment:** General feedback without approval
   - **Approve:** Approve the changes
   - **Request changes:** Block merging until issues are fixed

#### Resolving "This branch is X commits behind"

**Problem:** You see a warning like:
> "This branch is 3 commits behind nordlinglab:main"

**What this means:** The target branch has new commits that aren't in your PR branch. You need to update your branch.

**Solution (for Group Members - PR to group leader):**

```bash
cd course-agenticai-ecg-hrv

# Fetch the latest from group leader
git fetch upstream-group

# Check out your submission branch
git checkout submission/YYYY-YourFamilyName-type

# Merge changes
git merge upstream-group/main

# If there are conflicts, resolve them, then:
git add .
git commit -m "Merge upstream-group changes"

# Push the updated branch
git push origin submission/YYYY-YourFamilyName-type
```

**Solution (for Group Leaders - PR to nordlinglab):**

```bash
# Fetch the latest from nordlinglab
git fetch upstream-nordlinglab

# Check out your submission branch
git checkout submission/YYYY-GroupNames-type

# Merge changes
git merge upstream-nordlinglab/main

# If there are conflicts, resolve them, then:
git add .
git commit -m "Merge upstream-nordlinglab changes"

# Push the updated branch
git push origin submission/YYYY-GroupNames-type
```

After pushing, the pull request will automatically update and the warning should disappear.

#### Merging a Pull Request

1. Once approved and all checks pass, click the green **"Merge pull request"** button
2. Choose merge strategy from the dropdown:

   - **Create a merge commit:** Preserves all commits
   - **Squash and merge:** Combines all commits into one (recommended for clean history)
   - **Rebase and merge:** Replays commits on top of main

3. Click **"Confirm merge"**
4. Optionally click **"Delete branch"** to clean up

---

### In the Terminal

#### Setting Up Better Diff Tools

The default `git diff` output can be hard to read. Here are better alternatives:

**Option 1: Colored diff with `colordiff`**

```bash
# Install colordiff
# macOS
brew install colordiff

# Ubuntu/Debian
sudo apt install colordiff

# Usage: pipe git diff through colordiff
git diff | colordiff

# Or set it as default pager
git config --global core.pager "colordiff | less -R"
```

**Option 2: `git-delta` (Modern, feature-rich)**

```bash
# Install delta
# macOS
brew install git-delta

# Ubuntu/Debian (download from GitHub releases)
# https://github.com/dandavison/delta/releases

# Windows (with scoop)
scoop install delta

# Configure git to use delta
git config --global core.pager delta
git config --global interactive.diffFilter "delta --color-only"
git config --global delta.navigate true
git config --global delta.side-by-side true
```

Delta features:

- Syntax highlighting
- Side-by-side view
- Line numbers
- Word-level diff highlighting

#### Reviewing a Pull Request Locally (Alternative to `gh pr checkout`)

**[Group Leader only]** - If you prefer using git commands directly to review member submissions:

```bash
# If you need to add a specific member's fork as remote (usually not needed)
# Your upstream-group is your own repo, members submit PRs to you
# To review a specific member's work before they submit:
git remote add member-name git@github.com:MEMBER_USERNAME/course-agenticai-ecg-hrv.git
git fetch member-name

# View the diff between your main and their branch
git diff main..member-name/main
# With delta for better visualization:
git diff main..member-name/main | delta

# View only file names that changed
git diff --name-only main..member-name/main

# View diff statistics (lines added/removed per file)
git diff --stat main..member-name/main
```

**Note:** For most reviews, use `gh pr checkout` which is simpler.

#### Checking Out a Pull Request Branch for Testing

```bash
# Using gh CLI (recommended)
gh pr checkout PR_NUMBER

# Manual checkout from member's remote
git checkout -b review-member member-name/submission-branch

# Run tests, check the code, etc.
# ...

# When done, switch back to your branch
git checkout main

# Delete the review branch
git branch -d review-member
```

#### Viewing Commit History

```bash
# See commits in the PR (using gh CLI)
gh pr view PR_NUMBER --json commits

# Or using git with a specific remote
git log main..member-name/main --oneline
git log main..member-name/main
git log main..member-name/main --oneline --graph
```

#### Adding Comments via Command Line

Use the GitHub CLI for all PR interactions:

```bash
# Add a comment to a PR
gh pr comment 123 --repo nordlinglab/course-agenticai-ecg-hrv --body "Your comment here"

# Add a review comment
gh pr review 123 --repo nordlinglab/course-agenticai-ecg-hrv --comment --body "Please check line 42"

# Approve the PR
gh pr review 123 --repo nordlinglab/course-agenticai-ecg-hrv --approve --body "LGTM!"

# Request changes
gh pr review 123 --repo nordlinglab/course-agenticai-ecg-hrv --request-changes --body "Please fix the bug in function X"
```

**Alternative: Using the GitHub REST API directly:**

```bash
# Add a comment to a PR (requires personal access token)
curl -X POST \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -d '{"body": "Your comment here"}' \
  "https://api.github.com/repos/nordlinglab/course-agenticai-ecg-hrv/issues/123/comments"
```

For most users, the `gh` CLI is the easiest way to manage pull request comments from the terminal.

---

### In VS Code

#### Built-in Git Diff

1. Open VS Code in your repository folder
2. Click the **Source Control** icon (branch icon) in the left sidebar, or press `Ctrl+Shift+G` / `Cmd+Shift+G`
3. Changed files appear in the sidebar
4. Click any file to see a side-by-side diff view

#### Comparing Branches

1. Open the Command Palette: `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Type **"Git: Checkout to..."** and select the branch to compare
3. Or use the **GitLens** extension for more powerful comparisons

#### Using GitLens Extension (Recommended)

**Install GitLens:**

1. Go to Extensions (`Ctrl+Shift+X` / `Cmd+Shift+X`)
2. Search for **"GitLens"**
3. Click **Install**

**Compare branches with GitLens:**

1. Click the **GitLens** icon in the sidebar
2. Expand **"Compare"** section
3. Click **"Compare References..."**
4. Select your branch (e.g., `main`)
5. Select the branch to compare against (e.g., `upstream-group/main` or `upstream-nordlinglab/main`)
6. GitLens shows:

   - List of changed files
   - Number of commits difference
   - Click any file to see the diff

**Review inline blame:**

- GitLens shows who changed each line and when
- Hover over any line to see the commit details

#### Fetching and Reviewing Remote Branches in VS Code

1. Open the Command Palette: `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Type **"Git: Fetch From..."**
3. Select the remote (e.g., `upstream-group` or `upstream-nordlinglab`)
4. Now you can compare against that remote's branches

#### VS Code Pull Request Extension (Recommended for GitHub)

GitHub has excellent native VS Code support:

1. Install **"GitHub Pull Requests and Issues"** extension from Extensions (or use the built-in support)
2. Click the GitHub icon in the sidebar
3. Sign in to your GitHub account when prompted
4. You can now:

   - View all pull requests in the repository
   - Create new pull requests directly from VS Code
   - Review code with inline comments
   - Approve, request changes, or merge PRs
   - Check out PR branches with one click

---

## Troubleshooting

### "Permission denied" when pushing

**Problem:** You see "Permission denied" or "403 Forbidden" when trying to push.

**Cause:** You're either not authenticated or trying to push to a repository you don't have write access to.

**Solutions:**

1. **Check you're pushing to your fork, not the original:**

```bash
git remote -v
```

If it shows `nordlinglab` in the origin URL, you cloned the original instead of your fork. Fix it:

```bash
# Option 1: HTTPS
git remote set-url origin https://github.com/YOUR_USERNAME/course-agenticai-ecg-hrv.git

# Option 2: SSH
git remote set-url origin git@github.com:YOUR_USERNAME/course-agenticai-ecg-hrv.git
```

2. **Re-authenticate with the GitHub CLI:**

```bash
gh auth login
gh auth status  # Verify you're logged in
```

3. **Check your SSH key is added (if using SSH):**

```bash
ssh -T git@github.com
# Should say: "Hi USERNAME! You've successfully authenticated..."
```

### "Repository not found" error

**Problem:** Git says the repository doesn't exist when you try to clone or push.

**Solutions:**

1. Check the URL is correct (no typos)
2. Ensure the repository exists and is not private (or you have access)
3. Verify you're authenticated: `gh auth status`

### Fork not showing in your account

**Problem:** You clicked "Fork" but can't find the repository in your account.

**Solution:** Check your repositories:

```bash
gh repo list --fork
```

Or visit: `https://github.com/YOUR_USERNAME?tab=repositories`

### Merge conflicts

If your pull request shows conflicts:

**For Group Members:**
```bash
git fetch upstream-group
git checkout submission/YYYY-YourFamilyName-type
git merge upstream-group/main
# Resolve conflicts in your editor
git add .
git commit -m "Resolve merge conflicts"
git push origin submission/YYYY-YourFamilyName-type
```

**For Group Leaders:**
```bash
git fetch upstream-nordlinglab
git checkout submission/YYYY-GroupNames-type
git merge upstream-nordlinglab/main
# Resolve conflicts in your editor
git add .
git commit -m "Resolve merge conflicts"
git push origin submission/YYYY-GroupNames-type
```

### Wrong file name

If you named your file incorrectly:
```bash
# Rename the file
git mv old-name.md YYYY-CorrectName-Format.md
git commit -m "Fix file naming"
git push
```

### Authentication issues with HTTPS

**Problem:** Git keeps asking for username/password when pushing/pulling.

**Solution: Use the GitHub CLI for authentication (Recommended)**

```bash
# Authenticate with GitHub
gh auth login

# Choose HTTPS when prompted
# This stores credentials securely

# Verify authentication
gh auth status
```

**Alternative: Use a Personal Access Token**

1. Go to https://github.com/settings/tokens
2. Click **"Generate new token (classic)"**
3. Give it a name, set expiration, and select `repo` scope
4. Copy the token
5. Use the token as your password when git prompts

**Best solution: Set up SSH keys (More convenient long-term)**

SSH keys let you authenticate without entering credentials each time. Follow the instructions below for your operating system.

---

### Setting up SSH Keys for GitHub

#### macOS

**Step 1: Check for existing SSH keys**

```bash
ls -la ~/.ssh
```
If you see `id_ed25519` and `id_ed25519.pub` (or `id_rsa` and `id_rsa.pub`), you already have keys. Skip to Step 3.

**Step 2: Generate a new SSH key**

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

- Press Enter to accept the default file location
- Enter a passphrase (optional but recommended) or press Enter for no passphrase

**Step 3: Start the SSH agent and add your key**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**Step 4: Copy your public key**

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```
This copies the key to your clipboard.

**Step 5: Add the key to GitHub**

1. Go to https://github.com/settings/keys
2. Click **"Add key"**
3. Give it a label (e.g., "My MacBook")
4. Paste the key (Cmd+V)
5. Click **"Add key"**

**Step 6: Test the connection**

```bash
ssh -T git@github.com
```
You should see: "Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access."

**Step 7: Update your repository to use SSH**

```bash
cd course-agenticai-ecg-hrv
git remote set-url origin git@github.com:YOUR_USERNAME/course-agenticai-ecg-hrv.git
```

---

#### Windows

**Step 1: Open Git Bash**

If you installed Git for Windows, you have Git Bash. Search for "Git Bash" in the Start menu.

**Step 2: Check for existing SSH keys**

```bash
ls -la ~/.ssh
```
If you see `id_ed25519` and `id_ed25519.pub`, you already have keys. Skip to Step 4.

**Step 3: Generate a new SSH key**

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

- Press Enter to accept the default file location
- Enter a passphrase (optional) or press Enter for no passphrase

**Step 4: Start the SSH agent and add your key**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**Step 5: Copy your public key**

```bash
clip < ~/.ssh/id_ed25519.pub
```
This copies the key to your clipboard.

**Step 6: Add the key to GitHub**

1. Go to https://github.com/settings/keys
2. Click **"Add key"**
3. Give it a label (e.g., "My Windows PC")
4. Paste the key (Ctrl+V)
5. Click **"Add key"**

**Step 7: Test the connection**

```bash
ssh -T git@github.com
```
You should see: "Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access."

**Step 8: Update your repository to use SSH**

```bash
cd course-agenticai-ecg-hrv
git remote set-url origin git@github.com:YOUR_USERNAME/course-agenticai-ecg-hrv.git
```

---

#### Linux (Ubuntu/Debian)

**Step 1: Check for existing SSH keys**

```bash
ls -la ~/.ssh
```
If you see `id_ed25519` and `id_ed25519.pub`, you already have keys. Skip to Step 3.

**Step 2: Generate a new SSH key**

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```
- Press Enter to accept the default file location
- Enter a passphrase (optional but recommended) or press Enter for no passphrase

**Step 3: Start the SSH agent and add your key**

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**Step 4: Copy your public key**

```bash
# Install xclip if not installed
sudo apt install xclip

# Copy to clipboard
xclip -selection clipboard < ~/.ssh/id_ed25519.pub
```

Or manually display and copy:
```bash
cat ~/.ssh/id_ed25519.pub
```
Then select and copy the output.

**Step 5: Add the key to GitHub**

1. Go to https://github.com/settings/keys
2. Click **"Add key"**
3. Give it a label (e.g., "My Linux PC")
4. Paste the key (Ctrl+Shift+V in terminal, or Ctrl+V in browser)
5. Click **"Add key"**

**Step 6: Test the connection**

```bash
ssh -T git@github.com
```
You should see: "Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access."

**Step 7: Update your repository to use SSH**

```bash
cd course-agenticai-ecg-hrv
git remote set-url origin git@github.com:YOUR_USERNAME/course-agenticai-ecg-hrv.git
```

---

## Getting Help

- **Git documentation:** https://git-scm.com/doc
- **GitHub documentation:** https://docs.github.com/
- **GitHub CLI manual:** https://cli.github.com/manual/
- **TA contact:** See course syllabus for TA information

---

## License and Disclaimer

**Author:** Torbjörn E. M. Nordling, PhD

Unless otherwise specified, content in this repository is licensed under:

- **Documentation:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Source Code:** [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

See individual submissions for specific license declarations.

THIS DOCUMENT AND ALL ASSOCIATED CODE ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS DOCUMENT OR THE USE OR OTHER DEALINGS IN THIS DOCUMENT.
