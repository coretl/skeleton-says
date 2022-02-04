from pathlib import Path

from jinja2 import Template

template_path = Path(__file__).parent / "skeleton.jinja2"


def say(text: str) -> str:
    template = Template(template_path.read_text())
    return template.render(text=text)
