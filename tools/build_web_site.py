"""Build the static website and Ren'Py Web edition using the installed SDK."""
from pathlib import Path
import argparse
import json
import shutil
import subprocess
from zipfile import ZipFile, ZIP_DEFLATED


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sdk', type=Path, required=True, help='RenPy SDK with matching Web component installed')
    parser.add_argument('--output', type=Path, required=True, help='Dedicated build output directory')
    args = parser.parse_args()
    project = Path(__file__).resolve().parents[1]
    output = args.output.resolve()
    source = project / 'website'
    if output == project or output.is_relative_to(source):
        parser.error('Use a dedicated output directory outside website/ and the project root itself.')
    site = output / 'sflsgal-site'
    site.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, site, dirs_exist_ok=True)
    destination = (site / 'play/game').resolve()
    assert destination.is_relative_to(site.resolve()) and destination.name == 'game'
    sdk = args.sdk.resolve()
    python = sdk / 'lib/py3-windows-x86_64/python.exe'
    if not python.exists():
        parser.error('This helper currently expects the Windows RenPy SDK.')
    subprocess.run([str(python), str(sdk / 'renpy.py'), str(sdk / 'launcher'), 'web_build', str(project), '--destination', str(destination)], check=True)
    index = destination / 'index.html'
    html = index.read_text(encoding='utf-8').replace('lang="en-us"', 'lang="zh-CN"')
    html = html.replace('>Import Saves</a>', '>导入存档 / Import Saves</a>')
    html = html.replace('>Export Saves</a>', '>导出存档 / Export Saves</a>')
    html = html.replace('>Download Log</a>', '>下载运行日志</a>')
    index.write_text(html, encoding='utf-8')
    shutil.copy2(project / 'game/gui/main_menu.jpg', destination / 'web-presplash.jpg')
    # RenPy also creates a complete game ZIP outside its runtime directory.
    # Keep that download outside the deployed website (it is over 25 MiB).
    full_game_zip = destination.with_suffix('.zip')
    full_game_zip.unlink()
    with ZipFile(output / 'SFLS_Dear_Moments-web.zip', 'w', ZIP_DEFLATED) as archive:
        for p in sorted(destination.rglob('*')):
            if p.is_file():
                archive.write(p, p.relative_to(destination).as_posix())
    files = [p for p in site.rglob('*') if p.is_file()]
    oversized = [str(p.relative_to(site)) for p in files if p.stat().st_size > 25 * 1024 * 1024]
    if oversized or len(files) > 20000:
        raise RuntimeError(f'Cloudflare static asset limits exceeded: {oversized}; files={len(files)}')
    with ZipFile(output / 'sflsgal-site.zip', 'w', ZIP_DEFLATED) as archive:
        for p in sorted(files):
            archive.write(p, p.relative_to(site).as_posix())
    print(json.dumps({'website': str(site), 'files': len(files), 'largest_file_bytes': max(p.stat().st_size for p in files)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
