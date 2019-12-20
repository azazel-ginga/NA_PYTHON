###线程池
	> 系统启动一个新的线程成本是比较高的，因为它涉及与操作系统的交互。在这种情况下，使用线程池
      可以很好地提升性能，尤其是当程序中需要创建大量生存期很短暂的线程，更应该考虑使用线程池。

      线程池在系统启动时，即创建大量空闲的线程，程序只要将一个函数提交给线程池，线程池就会启动
      一个空闲的线程来执行它。当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成
      空闲状态，等待下一个函数。

      此外，使用线程池可以有效地控制系统中并发线程的数量。当系统中包含有大量的并发线程时
      会导致系统性能急聚下降，甚至导致Python解释器崩溃，而线程池的最大线程数参数可以控制
      系统中并发线程数量不超过此数。

###使用线程池  
    > 线程池的基类是concurrent.futures模块中的Executor,Executor提供了两个子类，即
      ThreadPoolExecutor和ProcessPoolExecutor,其中ThreadPoolExecutor用于创建
      线程池，而ProcessPoolExecutor用于创建进程池。

      如果使用线程池/进程池来管理并发编成，那么只要将相应的task函数提交给线程池/进程池
      身下的事情就由线程池/进程池来搞定

    > Executor提供了如下常用方法:
    	> submit(fn,*args,**kwargs):将fn函数提交给线程池。*args代表传给fn函数的参数
    	  *kwargs代表以关键字参数的形式为fn函数传入参数。
    	> map(func,*iterables,timeout=None,chunksize=1):该函数类似于全局函数
    	  map(func,*iterables)，只是该函数将会启动多个线程，以异步方式立即对iterables
    	  执行map处理。
    	> shutdown(wait=True):关闭线程池
    > 程序将task函数提交(submit)给线程池后，submit方法会返回一个Future对象，Future类
      主要用于获取线程任务函数返回值。由于线程任务会在新线程中以异步方式来执行，因此，线程
      执行的函数相当于一个"将来完成"的任务，所以Python使用Future来代表。

    > Future提供如下方法:
    	> cancel():取消Future代表的线程任务。如果该任务正在执行，不可取消，则该方法
    	  返回False;否则，程序会取消该任务，并返回True。
    	> cancelled():返回Future代表的线程任务是否被成功取消。
    	> running():返回Future代表的线程任务正在执行、不可被取消，该方法返回True返回Future代表的线程任务是否被成功取消。
        > done():如果该Future代表的线程任务被成功取消或执行完成，则该方法返回True。
        > result(timeout=None):获取该Future代表的线程任务最后返回的结果。如果Future代表的
          线程任务还未完成，该方法将会阻塞当前线程，其中timeout参数指定最多阻塞多少秒
        > exception(timeout=None):获取该Future代表的线程任务所引发的异常。如果该任务成功
          完成，没有异常，则该方法返回None。
        > add_done_callback(fn):为该Future代表的线程任务注册一个"回调函数"，当该任务成功
          完成时，程序会自动触发该fn函数。
    > 在用完一个线程池后，应该调用该线程池的shutdown()方法，该方法将启动线程池的关闭序列。调用
      shutdown()方法后的线程池不再接收新任务，但会将以下所有的已提交的任务执行完成。当线程池中
      所有任务都执行完成后，该线程池中的所有线程都会死亡。

    >使用线程池来执行线程任务的步骤如下:
    	> 1.调用ThreadPoolExecutor类的构造器创建一个线程池。
    	> 2.定义一个普通函数作为线程任务。
    	> 3.调用ThreadPoolExecutor对象的submit()方法来提交线程任务。
    	> 4.当不想提交任何任务时，调用ThreadPoolExecutor对象的shutdown()方法来
    	    关闭线程池。
