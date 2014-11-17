# Fabric tools

**Please note that this repository is currently being rewritten to be based on Fabric. The rewrite is not yet complete.**

Most of these tools were originally written for use at the [ICG][].

[ICG]: http://icg.tugraz.at

## Installation

    git clone https://github.com/GhostLyrics/scripted.git

## Requirements

* [Fabric](http://www.fabfile.org)

## Usage

After having checked out the repository, you can get a list of everything that is available in the current version with `fab --list` (You need to be in the checked out directory for that command).
Keep in mind that some modules require configuration. You can find the corresponding JSON templates in `templates/`. Copy the ones you need to `configuration/` and edit them to suit your environment.

## Notes: configuration

### cyrus

`default_quota` is measured in megabytes.
