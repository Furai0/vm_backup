import subprocess

vm_names = '', ''
vm_path = ''
vm_backup_path = ''


def vm_backup():
    for vm in vm_names:
        vm_config_path = f'/etc/libvirt/qemu/{vm}.xml'
        try:
            subprocess.run(["virsh", "shutdown", vm], check=True)
            print(f'shutdowned {vm}')
        except:
            print(f'cant shutdown {vm}')
        try:
            subprocess.run(['cp', vm_path, vm_backup_path], check=True)
            print(f'copied {vm} disk')
            subprocess.run(['cp', vm_config_path, vm_backup_path], check=True)
            print(f'copied {vm} config')
        except:
            print(f'cant copy {vm}')
        try:
            subprocess.run(['virsh', 'start', vm], check=True)
            print(f'started {vm}')
        except:
            print(f'cant start {vm}')


if __name__ == '__main__':
    vm_backup()
