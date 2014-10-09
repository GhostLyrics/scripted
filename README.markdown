# Commandline tools

Most of these tools were originally written for use at the [ICG][].

[ICG]: http://icg.tugraz.at

## Installation

Check out the repository and run `make`.

    git clone https://github.com/GhostLyrics/scripted.git
    make

## Files

* `add-scripted-to-path` is used by the Makefile to add the checked out directory to the PATH environment variable.
* `deploy-unattended-upgrades` can be used to enable unattended-upgrades on Debian and Ubuntu installations. Optionally, `apt-listchanges` can be enabled.
* `show-fingerprint` is used to print the fingerprints of the machine's host keys from the default paths. It will print RSA, RSA1, DSA and ECDSA fingerprints.
