variable "resource_group_name" {
  description = "Name of the resource group"
  default     = "terraform-rg"
}

variable "location" {
  description = "Azure region to deploy resources"
  default     = "eastus"
}

variable "container_name" {
  description = "Name of the blob container"
  default     = "tfstate"
}

variable "vnet_name" {
  description = "Name of the virtual network"
  default     = "terraform-vnet"
}

variable "subnet_name" {
  description = "Name of the subnet"
  default     = "terraform-subnet"
}

variable "nic_name" {
  description = "Name of the network interface"
  default     = "terraform-nic"
}

variable "vm_name" {
  description = "Name of the virtual machine"
  default     = "terraform-vm"
}

variable "admin_username" {
  description = "Admin username for the virtual machine"
  default     = "azureuser"
}

variable "admin_password" {
  description = "Admin password for the virtual machine"
  default     = "P@ssw0rd1234"  # Você deve mudar para uma senha segura
}
