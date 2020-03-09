# You've come to the right place...

Welcome to picoCTF problem-dev! This is the place to start.

We recommend 3 steps to acclimating to picoCTF problem-dev:

1. Starting your own picoCTF server for local testing.
2. Adding a problem to your picoCTF server.
3. Reviewing relevant documentation.

Documentation includes some more complex problems that can help bootstrap your
knowledge of the capabilities of the "hacksport" CTF problem templating
language in Python. More of that later. First, let's get your very own instance
of picoCTF on your computer!


## 1. Starting your own picoCTF server for local testing

If you're fairly confident with Vagrant and VirtualBox software, (and have them
installed on your development/testing box), then the quickest option for you
will probably be to follow the instructions found here:

https://github.com/picoCTF/picoCTF/blob/master/README.md#quick-start

If this succeeds, please go on to step 2., linked here:

[2. Adding a problem to your picoCTF server](https://github.com/picoCTF/start-problem-dev#2-adding-a-problem-to-your-picoctf-server)

Otherwise, some of the most common exceptions are listed in the following 
few subsections.

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
and do some manual config of the `shell` and `web` VM's:

![Apt Hangup](/img/death-by-prompt.png)

Once you've Ctrl-C'd out of being stuck in the apt prompt via vagrant, you will
need to manually update each VM, by doing something like the following for both
the shell and web VM's:

```
vagrant ssh shell
sudo killall dpkg
sudo apt update
sudo apt install
sudo apt upgrade
exit
vagrant up --provision shell
```




## 2. Adding a problem to your picoCTF server

Adding a problem to your picoCTF server happens on both the shell VM and the
web VM.

### Creating web platform superuser

1. Browse to your web VM's IP address (192.168.2.2 or the WIP environment var)
2. Register the first user.
  * This first user is the superuser for the web platform and has a lot of 
    configuration options for the CTF.
3. Enable default problems. Navigate to `Management > Manage Problems`
  * This step can be skipped.
  * There typically 3 default problems loaded but disabled, although if 
    provisioning was problematic, then they might not have auto-loaded
    correctly.
  * Hit the "Enable All Problems" button.
4. Turn competition live. Navigate to `Management > Configuration`.
  * By default, "Competition Start/End Time" are set to same time.
  * Move "Competition End Time" to some time in the distant future.
5. Refresh browser.
  * "Problems" tab should be visible now.
  * If default problems loaded successfully, those should be visible as well,
    under the "Problems" tab.

### Create and deploy fresh problem on shell VM

1. `vagrant ssh shell`
  * On the host machine, Vagrant uses keys to log in, but for sudo use 
    vagrant/vagrant
  * NOTE: change vagrant's password before going live with CTF!
2. `git clone https://github.com/picoCTF/picoCTF-2019-example-problems.git`
3. `cd picoCTF-2019-example-problems`
4. `sudo shell_manager install grep-1/`
5. `sudo shell_manager status`
6. `sudo shell_manager deploy grep-1-dc5ec3a`

### Load and enable grep-1 on web platform

1. Log in as superuser.
2. Load new deployment. Navigate to `Management > Shell Server` and hit "Load Deployment" button.
3. Enable grep-1 problem. Navigate to `Management > Manage Problems` and hit "Enable All Problems" button.
4. Verify visibility. Navigate to `Challenge Problems` and make sure "grep 1" is visible.




## 3. Review relevant documentation

* Exceedingly relevant: [Problem directory structure overview](https://docs.picoctf.com/adding-your-own-content.html).
* Exceedingly relevant: [Buffer overflow problem-dev tutorial](https://docs.picoctf.com/tutorials/buffer-overflow-challenge-beginner.html).
* Exceedingly relevant: [Hacksport documentation of challenge.py](https://docs.picoctf.com/specs/challenge.py.html).
* Relevant: [Top level docs](https://docs.picoctf.com/).
* Relevant: [Overview of picoCTF servers architecture](https://github.com/picoCTF/picoCTF#project-overview).




# Conclusion

At the moment, problem developers not only create problems, but also deploy 
their own picoCTF servers to be able to test and debug their problems. From my
own experience with the picoCTF platform, I think there are 3 main skills for
problem-devs to master:

1. Deployment and operations on local picoCTF servers
2. Understanding "hacksport" (problem directory structure and abilities within challenge.py)
3. Creativity to make security issues interesting!

Again, feel free to [email me](https://github.com/syreal17/) or join a [picoCTF
community](https://www.picoctf.com/community) to get help outside of what is
covered here!
