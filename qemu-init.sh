#!/bin/sh

busybox insmod rust_minimal.ko
busybox  rmmod rust_minimal.ko

busybox reboot -f
