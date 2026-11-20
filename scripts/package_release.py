"""Build the portable skill and the offline demo with Python's standard library."""

from pathlib import Path
from shutil import copyfile
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    root = Path(__file__).resolve().parents[1]
    skill_name = "ui-dsign-agent"
    skill = root / "skills" / skill_name
    dist = root / "dist"
    dist.mkdir(exist_ok=True)

    entries = [(root / "INSTALL.txt", "安装说明.txt")]
    for relative in ("SKILL.md", "LICENSE", "agents/openai.yaml", "references/visual-prompts.md"):
        entries.append((skill / relative, f"{skill_name}/{relative}"))

    with TemporaryDirectory(dir=dist) as staging:
        archive_path = Path(staging) / f"{skill_name}.zip"
        demo_path = Path(staging) / "ui-dsign-demo.html"
        with ZipFile(archive_path, "w") as archive:
            for source, name in entries:
                info = ZipInfo(name)
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, source.read_bytes(), compress_type=ZIP_DEFLATED)
        copyfile(root / "docs" / "index.html", demo_path)
        for asset in (archive_path, demo_path):
            target = dist / asset.name
            asset.replace(target)
            print(target)


if __name__ == "__main__":
    main()
