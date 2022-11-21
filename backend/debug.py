import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "app.main:api",
        port=3000,
        log_level="debug",
        reload=True,
        headers=[],
        reload_dirs=["app"],
        reload_delay=2,
        debug=True,
        factory=True,
    )
