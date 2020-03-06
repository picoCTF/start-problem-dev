// WIP:BOOKMARK: choose your own adventure style.
// * choose 1. Quick, or 2. Deep
//   * branch 1. Quick for prereqs needed or not... so on
// 
// NOTE: Twine might be really good for this actually
//       * could have dev choose from common setups from beginning (Win/Mac/
//         Linux.. brew/ports
//       * great way to easily generate complicated branching HTML

# Getting started real quick!

The most expeditious start to developing problems for the picoCTF framework
involves at least two steps:

1. Downloading, starting and verifying your own picoCTF servers for local
   testing
2. Creating, adding and deploying a simple problem to your picoCTF servers

## Getting your own picoCTF servers

```
#!/bin/bash
# NOTE: syntax of this script for Ubuntu, but rough equivalents for Windows & 
#       Mac as well.

# * Step 1: download latest picoCTF release and cd into base directory

cd
mkdir my-picoCTF
cd my-picoCTF
wget https://github.com/picoCTF/picoCTF/archive/v19.0.1.zip
unzip v19.0.1.zip
cd picoCTF-19.0.1


# * Step 2: create web/database and shell servers with vagrant
#   * Two pre-requisites:
#     1. VirtualBox (more guidance below)
#     2. Vagrant (more guidance below) 
##############################################################################
# if needed, vagrant install instructions included below. Windows devs, 
# I recommend installing Vagrant natively, not for WSL, or any other option.
#
# https://www.vagrantup.com/docs/installation/
##############################################################################

# (NOTE: many issues tend to occur here)

vagrant up
```

# Getting a solid foundation...
