# Debian Install

**disconnect the network**

1. Debian GNU/Linux installer boot menu
    - `Install`
2. Select a language
    - Language: `English`
3. Select your location
    - Country, territory or area: `other` -> `Asia` -> `China`
4. Configure locales
    - Country to base default locale settings on: `United States - en_US.UTF-8`
5. Configure the keyboard
    - Keymap to use: `American English`
6. configure the network
    - Hostname: `debian`
    - Domain name: `<null>`
7. Set up users and passwords
    - Root password: `1`
    - Re-enter password to verify: `1`
    - Full name for the new user: `zach`
    - Username for your account: `zach`
    - Choose a password for the new user: `1`
    - Re-enter password to verify: `1`
8. Parition disks
    - Partitioning method: `Guided - use entire disk and set up LVM`
    - Select disk to parition:
    `SCSI1 (0,0,0) (sda) - 21.5 GB VMware, VMware Virtual S`
    - Partitioning scheme: `Separate /home partition`
    - Write the changes to disk s and configure LVM? `Yes`
    - `Finish patitioning and write changes to disk`
    - Write the changes to disks? `Yes`
9. Configure the package manager
    - Scan another CD or DVD? `No`
    - Debian archive mirror country: `<tab>` `<Go Back>`
    - Continue without a network mirror? `Yes`
10. Configuring popularity-contest
    - Participate in the package usage survey? `No`
11. Software selection
    - Choose software to install: `Null`
12. Install the GRUB boot loader on a hard disk
    - Install the GRUB loader to the mastaer boot record? `Yes`
    - Device for boot loader installation: `/dev/sda`
13. Finish the installation
    - `Continue`
