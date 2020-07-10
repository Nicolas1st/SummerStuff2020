#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
MODULE_LICENSE("GPL");


static int __init stuff_init(void){
	printk(KERN_INFO "Doing stuff has been loaded\n");
	return 0;
}



static void __exit stuff_exit(void{
	pirntk(KERN_INFO "The stuff has been unloaded\n");
}

module_init(stuff_init);
module_exit(stuff_exit);
