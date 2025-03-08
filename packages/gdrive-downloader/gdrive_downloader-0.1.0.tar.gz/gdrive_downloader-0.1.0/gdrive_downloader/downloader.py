import os
import re
import gdown
import argparse
from rich import print


def parse_args():
    parser = argparse.ArgumentParser(
        description="Download files or folders from Google Drive."
    )
    parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="The Google Drive URL of the file or folder to download."
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="The local path to save the downloaded file."
    )
    parser.add_argument(
        "--force_download",
        action="store_true",
        help="Force re-download even if the file already exists."
    )
    return parser.parse_args()


def main():
    """
    Example usage:
    
    python -m gdrive_downloader.downloader \
        --url https://drive.google.com/file/d/1x65ixChKFlWHCecfm6rkZTGT6MlreAIO/view?usp=sharing \
        --output /path/to/save/file.txt
    """
    args = parse_args()
    file_url = args.url
    pattern = r'/d/([a-zA-Z0-9_-]+)'
    match = re.search(pattern, file_url)
    if not match:
        print("[red]Error:[/red] Unable to extract file id from URL.")
        return
    gid = match.group(1)
    refine_url = f'http://drive.google.com/uc?id={gid}&confirm=t'

    # Create folder if it doesn't exist
    to_path = os.path.dirname(args.output)
    if not os.path.exists(to_path):
        try:
            print(f'[green]Creating folder:[/green] {to_path}')
            os.makedirs(to_path, exist_ok=True)
        except OSError as e:
            print(f"[red]Error creating folder {to_path}:[/red] {e}")
            return

    # Download file if it doesn't exist or if force_download is enabled
    if not os.path.exists(args.output) or args.force_download:
        print(f'[green]Downloading file to:[/green] {args.output}')
        gdown.download(refine_url, args.output, quiet=False)
    else:
        print(f'[yellow]File already exists at {args.output}. Use --force_download to re-download.[/yellow]')


if __name__ == '__main__':
    main()
