from fastapi import FastAPI, HTTPException
from configs_generator import DockerfileGenerator
from models import DockerConfig

app = FastAPI()
generator = DockerfileGenerator()

@app.post("/generate_dockerfile")
async def generate_dockerfile(config: DockerConfig):
    try:
        dockerfile = generator.generate_dockerfile(config)
        return {"dockerfile": dockerfile, "requirements": config.requirements}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)