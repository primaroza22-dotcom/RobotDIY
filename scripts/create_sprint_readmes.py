from pathlib import Path
root = Path('Sprint')
created = []
for sprint in sorted(root.glob('Sprint-*')):
    if not sprint.is_dir():
        continue
    for folder in sorted(sprint.iterdir()):
        if folder.is_dir():
            readme = folder / 'README.md'
            if not readme.exists():
                readme.write_text(f"# {folder.name}\n\nDokumentasi dan isi folder `{folder.name}` untuk {sprint.name}.\n")
                created.append(str(readme))
print('CREATED', len(created))
for path in created:
    print(path)
