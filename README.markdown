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

## Available commands:

```none
allow_passwordless_sudo  (SUDO) Enable use of sudo without password. | (string) username.
brew_upgrade             (HOMEBREW) Update formulas and upgrade installed formulas.
change_password          (PASSWORD) Change password. | (string) password_type, (string) user.
connect_cyrus            (CYRUS) Open the cyrus 'cyradm' shell.
create_mailbox           (CYRUS) Create a new mailbox for the specified user.
delete_mailbox           (CYRUS) Delete a given mailbox. | (string) username.
get_IPs                  (NETWORK) Retrieve IP, network interface & MAC address of a machine.
get_cronjobs             (CRON) Retrieve lists of custom and scheduled cronjobs.
get_fingerprints         (SSH) Retrieve a machine's fingerprints.
renew_aliases            (POSTFIX): Read in the aliases file.
restart_dhcp             (DHCP) Restart the DHCP service.
set_password_login       (SSH) Enable/Disable password login. | (bool) boolean.
```

### Available options:

* `change_password`: options for `password_type` are: `local`, `samba`.

## Notes

* **cyrus**: `default_quota` is measured in megabytes.
