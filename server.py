from fastmcp import FastMCP
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# 1️⃣ Create a FastAPI app
app = FastAPI()

# 2️⃣ Create your MCP logic manually
mcp = FastMCP("ci_cd_advisor")

# 3️⃣ Define endpoint functions that wrap MCP tools
@app.post("/fetch_jenkins_logs")
async def fetch_jenkins_logs(job_name: str = "build_job"):
    """Mock Jenkins log retrieval."""
    data = {
        "job_name": job_name,
        "status": "SUCCESS",
        "duration": "125s",
        "log_excerpt": "Build completed successfully after caching Docker layers."
    }
    return JSONResponse(data)

@app.post("/analyze_test_results")
async def analyze_test_results():
    """Mock test analysis."""
    data = {
        "slow_tests": ["test_integration.py::test_large_dataset"],
        "avg_runtime": "3m45s"
    }
    return JSONResponse(data)

# 4️⃣ Start the HTTP server
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting MCP server on http://localhost:8000 ...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
