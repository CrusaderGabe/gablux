import subprocess, re, sys, os, datetime, random, string, mintutils, debianutils, mainutils

USER_WHITELIST = ["root", "daemon", "bin", "sys", "sync", "games", "man", "lp", "mail", "news", "uucp", "proxy", "www-data", "backup", "list", "irc", "gnats", "nobody", "systemd-network", "systemd-resolve", "messagebus", "systemd-timesync", "syslog", "_apt", "tss", "rtkit", "systemd-coredump", "kernoops", "uuidd", "cups-pk-helper", "lightdm", "tcpdump", "speech-dispatcher", "avahi-autoipd", "usbmux", "nm-openvpn", "geoclue", "dnsmasq", "pulse", "_flatpak", "avahi", "saned", "colord", "fwupd-refresh", "hplip", "ftp", "dovecot", "dovenull", "clamav"]



def ssh_rootdisable():
        subprocess.run(["sudo sed -i \"s/^#\\?PermitRootLogin.*/PermitRootLogin no/\" /etc/ssh/sshd_config"])

flavor = input("What flavor of LINUX are you using? Only Debian && Mint are available.")

if flavor == "Mint":
    mainutils.ask("✗ INITIATE STEP 1? ✗", mintutils.update())
    mainutils.ask("✗ INITIATE STEP 2? ✗", mainutils.add_a_user)
    



if flavor == "Debian":
    mainutils.ask("✗ INITIATE STEP 1? ✗", debianutils.update())
    mainutils.ask("✗ INITIATE STEP 2? ✗", debianutils.auto_update())
    mainutils.ask("✗ INITIATE STEP 3? ✗", debianutils.remove_users())
    mainutils.ask("✗ INITIATE STEP 4? ✗", debianutils.remove_admins())
    