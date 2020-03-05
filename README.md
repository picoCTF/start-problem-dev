# Getting started real quick!

The most expeditious start to developing problems for the picoCTF framework involves at least two steps:

1. Downloading, starting and verifying your own picoCTF servers for local testing
2. Creating, adding and deploying a simple problem to your picoCTF servers

## Getting your own picoCTF servers

```
# download latest picoCTF release and cd into base directory

$ cd
$ mkdir my-picoCTF
$ cd my-picoCTF
$ wget https://github.com/picoCTF/picoCTF/archive/v19.0.1.zip
$ unzip v19.0.1.zip
$ cd picoCTF-19.0.1


# if needed, vagrant install instructions included below. Windows devs, 
# I recommend installing Vagrant natively, not for WSL, or any other option.
# https://www.vagrantup.com/docs/installation/
#
# create web/database and shell servers with vagrant
# (NOTE: many issues tend to occur here)

$ vagrant up
```

# Getting a solid foundation...
