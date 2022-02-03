import sys
from jinja2 import Template
from pathlib import Path

template_path = Path(__file__).parent / "skeleton.jinja2"

def say(text):
    template = Template(template_path.read_text())
    print(template.render(text=text))

if __name__ == "__main__":
    say(sys.argv[1])
