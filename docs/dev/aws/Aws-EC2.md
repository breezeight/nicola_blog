# EC2

## [JOB] Detach volumes for mainteinance / resize

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-detaching-volume.html

Nel caso il volume sia ancora full dopo un riavvio della macchina:

- stacchi il volume
- lo attacchi ad una altra istanza e poi ci fai un po di pulizia
- WARNING BEFORE DETACHING take note of the originl volume ex: `/dev/xvda`, you will need it when you reattach it

Nel caso la macchina sia ancora accessibile sembra che si possa fare senza reboot o detach dei volumi, ma non l'ho mai provato: Resize AWS EBS without Rebooting: https://faun.pub/resize-aws-ebs-4d6e2bf00feb

- if the instance is running, you must first unmount the volume from the instance.
- if an EBS volume is the root device of an instance, you must stop the instance before you can detach the volume.

Resize:

- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html
- !!!! Before extending a file system that contains valuable data, it is best practice to create a snapshot of the volume
