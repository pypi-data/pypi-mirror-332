#!/usr/bin/env python3

"""Script to upload HotS replays to HeroesProfile."""

from __future__ import annotations

import argparse
import errno
import importlib.metadata
import json
import logging
import multiprocessing
import os
import pathlib
import sys
import tomllib
import typing
from concurrent.futures import ThreadPoolExecutor

if typing.TYPE_CHECKING:
    import threading

import requests
import xdg_base_dirs

NAME = "heroes-profile-replay-uploader"

VERSION = "2.4.0"
URL = "https://api.heroesprofile.com/api/upload/heroesprofile/electron"
USER_AGENT = f"HeroesProfile Electron Uploader / version {VERSION} (https://github.com/Heroes-Profile/heroesprofile-electron-uploader)"

logger = logging.getLogger(NAME)
logging.basicConfig(format="%(message)s", encoding="utf-8", level=logging.INFO)


class Uploader:
    """Uploader to HeroesProfile."""

    _m: multiprocessing.managers.SyncManager
    _db_lock: threading.Lock

    catalogue: pathlib.Path
    database: dict[str, typing.Any]
    timeout: float
    uploads_performed: int

    Files = typing.Mapping[str, str | typing.BinaryIO]

    def __init__(self, catalogue: pathlib.Path, timeout: float) -> None:
        """Create an uploader."""
        self._m = multiprocessing.Manager()
        self._db_lock = self._m.Lock()
        self.catalogue = catalogue
        self.database = json.load(catalogue.open())
        self.timeout = timeout
        self.uploads_performed = 0

    def add_file_to_catalogue(self, file_path: pathlib.Path, status: str) -> None:
        """Add a file to the catalogue so it doesn't get reuploaded."""
        with self._db_lock:
            self.uploads_performed += 1
            self.database[file_path.name] = status
            json.dump(self.database, self.catalogue.open(mode="wt"), indent=4)

    def upload(self, file_path: pathlib.Path) -> None:
        """Upload a file, terminating early if we have already uploaded it."""
        if self.database.get(file_path.name) is not None:
            logger.debug("Not uploading '%s'", file_path.name)
            return
        logger.info("Uploading '%s' ...", file_path.name)
        files: Uploader.Files = {
            "file": pathlib.Path.open(file_path, "rb"),
            "version": VERSION,
        }
        r = requests.post(
            URL,
            headers={
                "User-Agent": USER_AGENT,
            },
            files=files,
            timeout=self.timeout,
        )
        status = json.loads(r.text)["status"]
        self.add_file_to_catalogue(file_path, status)
        return


def get_cpu_count() -> int:
    """Get the amount of CPUs that this process can use."""
    # TODO: can use os.process_cpu_count in Python 3.13
    #       https://docs.python.org/3/library/os.html#os.process_cpu_count
    return len(os.sched_getaffinity(0))


DESCRIPTION = (
    "A command line uploader for Heroes of the Storm replays to heroesprofile.com"
)


CONFIG_FIELDS = {
    "accounts-directory": pathlib.Path,
    "catalogue": pathlib.Path,
    "config": pathlib.Path,
    "quiet": bool,
    "threads": str,
    "timeout": float,
    "verbose": bool,
    "version": bool,
}

Config = typing.TypedDict(
    "Config",
    {
        "accounts-directory": pathlib.Path,
        "catalogue": pathlib.Path,
        "config": pathlib.Path,
        "quiet": bool,
        "threads": str | int,
        "timeout": float,
        "verbose": bool,
        "version": bool,
    },
    total=False,
)

DEFAULT_CONFIG: Config = {
    "catalogue": xdg_base_dirs.xdg_data_home() / NAME / "catalogue.json",
    "config": xdg_base_dirs.xdg_config_home() / f"{NAME}.toml",
    "threads": 1,
    "timeout": 10.0,
}


def set_log_level(args: argparse.Namespace | Config) -> None:
    """Set the log level from the args Namespace or dict."""
    if isinstance(args, argparse.Namespace):
        quiet = args.quiet
        verbose = args.verbose
    else:
        quiet = args["quiet"]
        verbose = args["verbose"]
    if quiet:
        logger.setLevel(logging.CRITICAL + 1)
    elif verbose:
        logger.setLevel(logging.DEBUG)


def get_command_line_arguments(
    cmdline_args: list[str] = sys.argv[1:],
) -> argparse.Namespace:
    """Get the arguments provided by the user on the command line."""
    argparser = argparse.ArgumentParser(description=DESCRIPTION)
    argparser.add_argument(
        "-a",
        "--accounts-directory",
        type=pathlib.Path,
        default=None,
        help="The 'Accounts' directory for Heroes of the Storm",
    )
    argparser.add_argument(
        "-C",
        "--catalogue",
        type=pathlib.Path,
        default=None,
        help=(
            "The JSON file of already examined replays "
            f"(default: {DEFAULT_CONFIG['catalogue']})"
        ),
    )
    argparser.add_argument(
        "-c",
        "--config",
        type=pathlib.Path,
        default=None,
        help=(
            "The TOML file containing the application config "
            f"(default: {DEFAULT_CONFIG['config']})"
        ),
    )
    argparser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Run with no output (prioritised over --verbose)",
    )
    argparser.add_argument(
        "-T",
        "--threads",
        default=None,
        help=(
            "The number of uploads to attempt concurrently, a number or 'auto' "
            f"(default: {DEFAULT_CONFIG['threads']})"
        ),
    )
    argparser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=None,
        help=(
            "The timeout in seconds (float) for API interactions "
            f"(default: {DEFAULT_CONFIG['timeout']})"
        ),
    )
    argparser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable printing debug messages to stdout",
    )
    argparser.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="Print the version of the program and exit",
    )
    parsed_args, unknown_args = argparser.parse_known_args(cmdline_args)
    if len(unknown_args) != 0:
        set_log_level(parsed_args)
        logger.error("Extra arguments not recognised: %s", unknown_args)
        sys.exit(errno.EINVAL)
    return parsed_args


def get_config(args: argparse.Namespace) -> Config:
    """
    Get the complete configuration.

    Raises
    ------
    RuntimeError:
        If the accounts directory is not defined.

    """

    # Determine what was requested at the command line
    def underscore_to_hyphen(string: str) -> str:
        return string.replace("_", "-")

    command_line_config = typing.cast(
        "Config",
        {underscore_to_hyphen(k): v for k, v in vars(args).items() if v is not None},
    )

    # Load configs
    config_file = command_line_config.get("config")
    if config_file is None or not config_file.exists():
        config_file = DEFAULT_CONFIG["config"]

    file_config: Config = {}
    if config_file.exists():
        raw_load = tomllib.load(DEFAULT_CONFIG["config"].open(mode="rb")).get(
            "heroes-profile-replay-uploader",
            {},
        )
        file_config = typing.cast(
            "Config",
            {k: CONFIG_FIELDS[k](v) for k, v in raw_load.items()},
        )
    config: Config = {**DEFAULT_CONFIG, **file_config, **command_line_config}

    set_log_level(config)
    logger.debug("Configuration Pass 1: %s", command_line_config)
    logger.debug("Configuration Pass 2: %s", config)

    # Fail if no accounts
    if config.get("accounts-directory") is None or config["accounts-directory"] is None:
        message = (
            "No accounts directory has been provided. "
            "Use --accounts-directory or supply a config file."
        )
        raise RuntimeError(message)

    return config


def main(cmdline_args: list[str] = sys.argv[1:]) -> None:
    """Run the uploader."""
    # Arguments
    args = get_command_line_arguments(cmdline_args)
    set_log_level(args)
    if args.version:
        print(importlib.metadata.version(__package__.split(".")[0]))  # noqa: T201
        sys.exit(0)

    config: Config = {}
    try:
        # Get full config
        config = get_config(args)

        # Create catalogue if it doesn't exist
        config["catalogue"].parent.mkdir(exist_ok=True)
        if not config["catalogue"].exists():
            json.dump({}, config["catalogue"].open(mode="wt"), indent=4)
            logger.debug("Created '%s'", config["catalogue"])

        # Get all available replays
        logger.debug("Scanning '%s' for replays ...", config["accounts-directory"])
        files = list(config["accounts-directory"].rglob("*.StormReplay"))
        files.sort(key=lambda x: x.stat().st_mtime)
        logger.debug("Found %s files", len(files))

        if isinstance(config["threads"], str) and config["threads"] == "auto":
            threads = get_cpu_count()
        else:
            threads = int(config["threads"])
        logger.debug("Starting %s upload threads ...", threads)
        uploader = Uploader(config["catalogue"], config["timeout"])
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for file in files:
                executor.submit(uploader.upload, file)
        logger.info("%s uploads performed", uploader.uploads_performed)

    except Exception as err:
        logger.error(str(err))  # noqa: TRY400
        args_verbose = args.verbose and not args.quiet
        config_verbose = config.get("verbose", False) and not config.get("quiet", False)
        if args_verbose and (len(config) == 0 or config_verbose):
            raise
        sys.exit(1)


if __name__ == "__main__":
    main()
