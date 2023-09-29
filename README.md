# RepoBackups
A small "quick and dirty" script to create GitHub repository backups of a configurable amount of repositories.  

## Intention
This script was created with the intention of ensuring the life of the repositories for a couple of students I'm teaching. Use, modify, and distribute it as you see fit.  

### Setup
In the configuration file, you'll find a few options:
- `delay` : The delay in seconds for the backups to occur
- `backups_path` : The path for the storage of created backups.
- `github-login` : The GitHub PA Token to access your account. (This can be modified and be taken out if you're only going to use public repos. Search for the config declaration.
- `Groups` : The repositories to be backed up, mapped as NAME:URL
