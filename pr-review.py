
import sys
import subprocess
from pathlib import Path
from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel
from MarkdownReviewerTool import markdown_specifications_documentation_tool

# Predetermined repository to diff against.
# Update this path to the repository you want to review.
TARGET_REPO_PATH = Path(r"..\blogdoc")


def run_git(*args):
    return subprocess.run(
        ["git", "-C", str(TARGET_REPO_PATH), *args],
        check=True,
        capture_output=True,
        text=True,
    )

def main():
    if len(sys.argv) != 2:
        print("Usage: pr-review.py <branch-name>")
        sys.exit(1)

    branch_name = sys.argv[1].strip()

    if not TARGET_REPO_PATH.exists():
        print(f"Error: repository path does not exist: {TARGET_REPO_PATH}")
        sys.exit(1)

    if not (TARGET_REPO_PATH / ".git").exists():
        print(f"Error: not a git repository: {TARGET_REPO_PATH}")
        sys.exit(1)

    try:
        # Fetch explicit remote-tracking refs so origin/<branch> is available locally.
        run_git(
            "fetch",
            "origin",
            f"refs/heads/main:refs/remotes/origin/main",
            f"refs/heads/{branch_name}:refs/remotes/origin/{branch_name}",
        )

        # Compare branch changes relative to main using merge-base diff.
        diff_proc = run_git("--no-pager", "diff", f"origin/main...origin/{branch_name}")
        diff_text = diff_proc.stdout
    except subprocess.CalledProcessError as exc:
        print("Git command failed:")
        if exc.stderr:
            print(exc.stderr.strip())
        else:
            print(str(exc))
        sys.exit(exc.returncode)

    if not diff_text.strip():
        print("No diff found between origin/main and the target branch.")
        return

    # Initialize the agent with the diff and a code model.
    model = LiteLLMModel(
    model_id="anthropic/claude-sonnet-4-6",
    temperature=0.2,
    api_key="YOUR_ANTHROPIC_API_KEY"
    )
    agent = CodeAgent(tools=[markdown_specifications_documentation_tool], model=model)
    response = agent.run(f"Review the following code changes and provide feedback:\n\n{diff_text}")
    print("Agent response:")
    print(response)

if __name__ == "__main__":
    main()