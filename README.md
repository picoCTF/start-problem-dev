# You've come to the right place...

Welcome to picoCTF problem-dev! This is the place to start.

I (ltj) recommend 3 steps to acclimating to picoCTF problem-dev:

1. Starting your own picoCTF server for local testing
2. Adding a problem to your picoCTF server
3. Reviewing relevant documentation

Documentation includes some more complex problems that can help bootstrap your
knowledge of the capabilities of the "hacksport" CTF problem templating
language in Python. More of that later. First, let's get our very own instance
of picoCTF on our computer!


## 1. Starting your own picoCTF server for local testing

If you're fairly confident with Vagrant and VirtualBox software, (and have them
installed on your development/testing box), then the quickest option for you
will probably be to follow the instructions found here:

https://github.com/picoCTF/picoCTF/blob/master/README.md#quick-start

If this succeeds, please go on to step 2., found here:

[TODO: insert link to step 2 section]

Otherwise, some of the most common exceptions are listed in the following 
sections.

And please be aware that you can reach out for support in the venues listed 
here:

https://www.picoctf.com/community

### a. Installing pre-requisites

#### i. VirtualBox

VirtualBox can host virtual machines on many sorts of hardware and operating
systems. This is a dependency of Vagrant as Vagrant only provides easy creation
of virtual machines, but does not provide software to run them.

Install VirtualBox natively:

https://www.virtualbox.org/wiki/Downloads

#### ii. Vagrant

Vagrant streamlines the creation of a new virtual machine.

Install Vagrant natively:

https://www.vagrantup.com/downloads.html


### b. Avoiding network collision

The default network address for the shell and web virtual machines (VM's) tend
to conflict with personal WiFi networks. To avoid, provision again using the
`SIP` (Shell IP) and `WIP` (Web IP) environment variables.

Environment Variables are something most operating systems 
(Windows/Mac/Linux/BSD/...) have, but setting them is quite different across
systems. Setting environment variables for one's system is currently an 
exercise left to reader.

The following demonstration is for Powershell users on Windows:

```
PS C:\Users\tron> $Env:SIP = "192.168.13.37"
PS C:\Users\tron> $Env:WIP = "192.168.13.38"
PS C:\Users\tron> vagrant up --provision shell web
```


### c. Provision dies at interactive prompt

Apt asks to be able to restart services, but unfortunately sometimes this kills
Vagrant's ability to provision automatically the first time.

If `vagrant` hangs with a screen like the following, you will need to Ctrl-C
and do some manual config of the `shell` and `web` VM's

![Apt Hangup](/img/death-by-prompt.png)

## 2. Adding a problem to your picoCTF server

