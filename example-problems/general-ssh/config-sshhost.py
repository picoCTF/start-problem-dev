################################################################################
# Configure a box for the general ssh example challenge.
################################################################################

import sys
import subprocess

def main():

    try:
        # Grab password from file =========================================
        password = ""
        with open("/tmp/password.txt", "r") as f:
          password = f.read()
          password = password.strip()

        subprocess.run(
            ["/bin/sh", "-c", "rm /tmp/password.txt"], check=True
        )

        # =====================================================================

        # Create ctf-player user
        subprocess.run(
            [
                "/usr/sbin/useradd",
                "-U",
                "ctf-player",
                "-d",
                "/home/ctf-player",
                "-s",
                "/bin/bash",
            ],
            check=True,
        )

        # Pipe the output of echo into chpasswd to change password of
        # ctf-user
        pEcho = subprocess.Popen(
            (
                'echo', 
                f'ctf-player:{password}'
            ),
            stdout=subprocess.PIPE
        )

        output = subprocess.check_output(('chpasswd'), stdin=pEcho.stdout)

        pEcho.wait()

        # Make sure ownership is changed to ctf-player
        subprocess.run(
            [
                "/usr/bin/chown",
                "-R",
                "ctf-player:ctf-player",
                "/home/ctf-player/",
            ],
            check=True,
        )

    except subprocess.CalledProcessError:
        print("A subprocess has returned an error code")
        sys.exit(1)

# =============================================================================

if __name__ == "__main__":
    main()
