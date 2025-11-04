from jinja2 import Environment, FileSystemLoader, select_autoescape
from models import DockerConfig

class DockerfileGenerator:
    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader("../templates"),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def generate_dockerfile(self, config: DockerConfig) -> str:
        template = self.env.get_template("Dockerfile.j2")
        return template.render(
            config=config
        )