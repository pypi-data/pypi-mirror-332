# slidge-whatsapp

A
[feature-rich](https://slidge.im/slidge-whatsapp/features.html)
[WhatsApp](https://whatsapp.com) to
[XMPP](https://xmpp.org/) puppeteering
[gateway](https://xmpp.org/extensions/xep-0100.html), based on
[slidge](https://slidge.im) and
[whatsmeow](https://github.com/tulir/whatsmeow).

[![PyPI package version](https://badge.fury.io/py/slidge-whatsapp.svg)](https://pypi.org/project/slidge-whatsapp/)
[![CI pipeline status](https://ci.codeberg.org/api/badges/14066/status.svg)](https://ci.codeberg.org/repos/14066)
[![Chat](https://conference.nicoco.fr:5281/muc_badge/slidge@conference.nicoco.fr)](https://conference.nicoco.fr:5281/muc_log/slidge/)

## Installation

Refer to the [slidge admin documentation](https://slidge.im/docs/slidge/main/admin/)
for general info on how to set up an XMPP server component.

### Containers

From [the codeberg package registry](https://codeberg.org/slidge/-/packages?q=&type=container)

```sh
# use docker.io/ravermeister/slidge-whatsapp for arm64 (thanks raver! <3)
docker run codeberg.org/slidge/slidge-whatsapp
```

### Python package

With [pipx](https://pypa.github.io/pipx/):

```sh

# for the latest stable release (if any)
pipx install slidge-whatsapp

# for the bleeding edge
pipx install slidge-whatsapp==0.0.0.dev0 \
    --pip-args='--extra-index-url https://codeberg.org/api/packages/slidge/pypi/simple/'

# to update bleeding edge installs
pipx install slidge-whatsapp==0.0.0.dev0 \
    --pip-args='--extra-index-url https://codeberg.org/api/packages/slidge/pypi/simple/' --force

slidge-whatsapp --help
```

Make sure to install `ffmpeg` for full outgoing media compatibility; for
example, in Debian/Ubuntu:

```sh
sudo apt install ffmpeg
```

## Dev

```sh
git clone https://codeberg.org/slidge/slidge
git clone https://codeberg.org/slidge/slidge-whatsapp
cd slidge-whatsapp
docker-compose up
```
