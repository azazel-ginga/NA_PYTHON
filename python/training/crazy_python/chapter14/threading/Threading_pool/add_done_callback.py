#coding = utf - 8


'''
前面程序调用了Future的result()方法来获取线程任务返回值，但该方法会阻塞当前主线程
只有等到线程任务完成后，result()方法的阻塞在会被解除。

如果程序不希望直接调用result()方法阻塞线程，则可以通过Future的add_done_callback()方法来
添加回调函数，该回调函数形式如fn(future)。当线程任务完成后，程序会自动触发该回调函数，并将
对应的Future对象作为参数传给该回调函数。
'''


#下面程序使用add_done_callback()方法来获取线程任务的返回值


