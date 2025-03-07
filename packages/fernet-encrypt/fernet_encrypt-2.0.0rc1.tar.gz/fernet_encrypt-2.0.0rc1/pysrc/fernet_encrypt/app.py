import json
import sys
import time
from typing import Annotated

import typer

from fernet_encrypt import cli
from fernet_encrypt.commands import (
    create_key,
    decrypt,
    decrypt_remote,
    encrypt,
    encrypt_remote,
    get_remote_keys,
    remote_login,
)
from fernet_encrypt.utils import KEY_PATH, api, logger

if sys.argv[-1] == "-":
    sys.argv.pop()


def main():
    try:
        cli()
    except Exception as e:
        typer.echo(f"{e.__class__.__name__}: {e}")
        sys.exit(1)


@cli.command(name="login", help=f"Sign up or Login to {api.REMOTE_API}")
def login(
    refresh_token: Annotated[
        str | None, typer.Option("--refresh-token", help="A refresh token to login with. Useful for CI environments")
    ] = None,
):
    remote_login(refresh_token=refresh_token)


@cli.command(name="get-keys", help="Sync remote keys to fernet-encrypt local key storage")
def get_keys(
    stdout: Annotated[bool, typer.Option("--stdout", help="Output fetched keys as JSON to stdout")] = False,
):
    keys = get_remote_keys()

    if stdout:
        typer.echo(json.dumps(keys, indent=2))

    for key in keys:
        keyfile = KEY_PATH / f"{key['timestamp']}.key"
        with open(keyfile, "wb") as f:
            f.write(key["key"].encode("utf-8"))

        logger.debug(f"Created keyfile: {keyfile}")


@cli.command(name="create-local-key", help="Create a new local storage Fernet key")
def create_local_key():
    create_key()


@cli.command(name="encrypt", help="Encrypt stdin data using local key storage or remote API keys")
def encrypt_stdin(
    name: Annotated[
        str | None, typer.Option("--name", help="A key name for the encrypted data. Defaults to an epoch timestamp")
    ] = None,
    remote: Annotated[bool, typer.Option("--remote", help="Encrypt using the remote API")] = False,
):
    if not sys.stdin.isatty():
        data = sys.stdin.buffer.read().strip()
    else:
        data = input("Input data to encrypt: ").encode("utf-8")

    if data is None:
        typer.echo("No input data provided.")
        raise typer.Exit(code=1)

    name = name or str(int(time.time()))

    if remote:
        result = encrypt_remote(data, name)
    else:
        result = encrypt(data)

    typer.echo(result, nl=False)


@cli.command(name="decrypt", help="Decrypt stdin data using local key storage or remote API keys")
def decrypt_stdin(
    remote: Annotated[bool, typer.Option("--remote", help="Decrypt using the remote API")] = False,
):
    if not sys.stdin.isatty():
        data = sys.stdin.buffer.read().strip()
    else:
        data = input("Input data to decrypt: ").encode("utf-8")

    if data is None:
        typer.echo("No input data provided.")
        raise typer.Exit(code=1)

    if remote:
        result = decrypt_remote(data)
    else:
        result = decrypt(data)

    typer.echo(result, nl=False)
