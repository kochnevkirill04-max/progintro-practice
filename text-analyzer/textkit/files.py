from pathlib import Path

def read_text(path: Path) -> str:
    """Načte textový soubor v UTF-8."""
    with path.open(encoding="utf-8") as file:
        return file.read()

def write_text(path: Path, content: str) -> None:
    """Zapíše textový soubor v UTF-8."""
    path.write_text(content, encoding="utf-8")