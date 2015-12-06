Vagrant.require_version ">= 1.6"

Vagrant.configure('2') do |config|
  config.vm.define 'akl' do |akl|
    akl.vm.box = 'ubuntu/trusty64'
    akl.vm.synced_folder '.', '/vagrant', disabled: true
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "setup.yml"
  end
end
