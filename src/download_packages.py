import os
import subprocess
from pathlib import Path

def download_package(package: str, py_version: str, base_dir: Path):
    """Download a package and its dependencies for a specific Python version."""
    print(f"📦 Downloading '{package}' for Python {py_version}")

    # Format folder name
    py_folder = f"python{py_version}"
    safe_pkg_name = package.replace("==", "_").replace(">=", "_ge_").replace("~=", "_approx_")
    download_dir = base_dir / py_folder / safe_pkg_name
    download_dir.mkdir(parents=True, exist_ok=True)

    # Download with dependencies (binary only, no cached builds)
    cmd = [
        "pip", "download", package,
        "--dest", str(download_dir),
        "--python-version", py_version,
        "--only-binary", ":all:",
        "--no-cache-dir"
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to download {package}: {e}")
    else:
        print(f"✅ Downloaded {package} into {download_dir}")

def main(requirements_file: str, python_version: str, base_output_dir: str = "downloaded_packages"):
    base_path = Path(base_output_dir)
    base_path.mkdir(exist_ok=True)

    with open(requirements_file, "r") as f:
        packages = [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]

    for pkg in packages:
        download_package(pkg, python_version, base_path)

    print(f"\n✅ All packages downloaded into: {base_path / f'python{python_version}'}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Download packages and dependencies for offline use.")
    parser.add_argument(
        "--requirements", default="raw_requirements.txt",
        help="Path to the requirements file (e.g., raw_requirements.txt)"
    )
    parser.add_argument(
        "--python-version", required=True,
        help="Target Python version to download for (e.g., 3.8)"
    )
    parser.add_argument(
        "--output-dir", default="downloaded_packages",
        help="Directory to store downloaded packages"
    )

    args = parser.parse_args()
    main(args.requirements, args.python_version, args.output_dir)

    # python download_requirements_by_version.py --requirements raw_requirements.txt --python-version 3.8
    # pip install --no-index --find-links=. package-name