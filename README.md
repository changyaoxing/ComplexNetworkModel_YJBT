# ComplexNetworkModel_YJBT
这是一个对复杂网络YJBT加权模型生成过程的演示。借鉴了Networkx.barabasi_albert_graph()  BA模型的生成过程

具体过程为：每加一个点就显示一幅图。关掉图后，再加一个点，再显示一幅图。

YJBT模型是加权无标度网络的最小模型，模型中随着网络增长，拓扑和权都受择优连接规则驱动。
YJBT模型的拓扑结构与BA网络相同。开始于m0个点，每一时步，添加一个具有m<m0条边的新节点vj。点vj与已有的点vi相连的概率为 vi节点的度/全部节点的度。
每条边权为 vi节点的度/要连接的节点的度之和。可以发现新节点的边权之和为1 。

YJBT的模型的性质可看博客：https://blog.csdn.net/qq_42213329/article/details/109494379


