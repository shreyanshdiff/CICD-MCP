from langchain_agent.cicd_agent import analyze_ci_cd, interactive_chat

if __name__ == "__main__":
    logs = """
    [INFO] Starting build...
    [WARNING] Tests failed in stage 'Test'.
    [INFO] Build took 12 minutes.
    """
    pipeline = """
    stages:
      - Build
      - Test
      - Deploy
    """

    print("🔍 Running initial CI/CD analysis...\n")
    report = analyze_ci_cd(logs, pipeline)
    print("🧾 AI Analysis:\n", report)

    # Start interactive mode
    interactive_chat(logs, pipeline)
