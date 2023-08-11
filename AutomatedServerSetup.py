
# Project: Automated Server Setup
"""
Description: This project automates the initial setup and configuration of a Linux server by installing necessary packages,
creating users, setting up SSH keys, and configuring system settings.
It helps streamline the server setup process and ensures consistency across different deployments.
"""
"""
Steps:

Define the required packages and dependencies for the server setup.
Write a Python script to install the packages using package managers like apt or yum.
Create users and set up SSH keys for secure remote access.
Configure system settings, such as firewall rules or network settings.
Requirements:

A Linux server or virtual machine to configure (Ubuntu, CentOS, etc.).
Python (installed on the server).
Basic knowledge of Linux commands and package managers.
Example Code (for Ubuntu Server):
"""
import subprocess

def install_packages(package_list):
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
    subprocess.run(['sudo', 'apt', 'install'] + package_list + ['-y'])

def create_user(username, password):
    subprocess.run(['sudo', 'useradd', '-m', username])
    subprocess.run(['sudo', 'usermod', '-aG', 'sudo', username])
    subprocess.run(['sudo', 'chpasswd'], input=f'{username}:{password}'.encode())

def setup_ssh_key(username, ssh_key):
    ssh_dir = f'/home/{username}/.ssh'
    subprocess.run(['sudo', 'mkdir', '-p', ssh_dir])
    subprocess.run(['sudo', 'chown', f'{username}:{username}', ssh_dir])
    with open(f'{ssh_dir}/authorized_keys', 'a') as f:
        f.write(ssh_key)

def configure_firewall():
    subprocess.run(['sudo', 'ufw', 'enable'])
    subprocess.run(['sudo', 'ufw', 'allow', 'OpenSSH'])
    subprocess.run(['sudo', 'ufw', 'enable'])

if __name__ == "__main__":
    # Configuration parameters
    packages_to_install = ['git', 'nginx', 'python3-pip']
    new_user = 'newuser'
    user_password = 'your_user_password'
    ssh_public_key = 'your_ssh_public_key'

    install_packages(packages_to_install)
    create_user(new_user, user_password)
    setup_ssh_key(new_user, ssh_public_key)
    configure_firewall()

    print("Server setup completed.")
