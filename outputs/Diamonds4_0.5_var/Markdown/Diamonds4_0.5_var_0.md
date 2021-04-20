
# Parameters

    Name :                      Diamonds4_0.5_var-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.var
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      20019429667 function calls (19331749994 primitive calls) in 35708.57 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.572 35708.572 {built-in method builtins.exec}
                      1    0.001    0.001 35708.572 35708.572 <string>:1(<module>)
                      1  171.773  171.773 35708.571 35708.571 allGraphsTrain.py:10(graphTrain)
                 774346 5538.465    0.007 13393.870    0.017 allGraphs.py:146(transformNot)
              774352592 8745.849    0.000 8745.849    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 774346   17.346    0.000 8420.810    0.011 allGraphsTrain.py:29(<listcomp>)
               78209047 1947.932    0.000 8403.506    0.000 allGraphs.py:110(states)
              696911800 6260.117    0.000 6260.117    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 774346  706.391    0.001 3772.482    0.005 allGraphsTrain.py:35(<listcomp>)
                 774346    2.346    0.000 3228.104    0.004 game.py:41(step)
                 774346    3.593    0.000 3075.451    0.004 layers.py:718(step)
               18081751   26.281    0.000 3066.091    0.000 allGraphs.py:158(getInterventions)
                 774346  137.921    0.000 2094.074    0.003 allGraphsTrain.py:37(<listcomp>)
               25239200 2025.613    0.000 2025.613    0.000 {built-in method tensor}
               21953482   11.307    0.000 1929.436    0.000 game.py:37(board)
                 774347  101.487    0.000 1780.550    0.002 layers.py:684(update)
               18081751   69.699    0.000 1643.369    0.000 allGraphs.py:153(format)
                 774346    2.553    0.000 1578.769    0.002 agent.py:29(learn)
                 774346   14.877    0.000 1574.610    0.002 agent.py:117(_learn)
                 774346   45.879    0.000 1559.733    0.002 learner.py:42(Qlearn)
               16960919   14.274    0.000 1381.931    0.000 allGraphs.py:129(rightIntervention)
        152787211/16960919   93.250    0.000 1307.719    0.000 {built-in method builtins.min}
                 774346   52.472    0.000 1287.272    0.002 layers.py:17(step)
               42861965   17.093    0.000 1284.029    0.000 allGraphs.py:130(<lambda>)
               82080676  181.127    0.000 1272.333    0.000 tensor.py:21(wrapped)
        288613503/42861965  393.582    0.000 1266.935    0.000 allGraphs.py:74(expected_moves)
               77434600  112.062    0.000 1228.015    0.000 layer.py:98(move)
                 774346   54.681    0.000 1206.805    0.002 allGraphsTrain.py:44(<listcomp>)
        381577830/90963290  104.232    0.000 1044.711    0.000 allGraphs.py:78(<genexpr>)
                2487625   18.056    0.000  897.463    0.000 layers.py:740(restart)
               81306330  871.672    0.000  871.672    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               77434600  826.416    0.000  826.416    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2487625    8.804    0.000  720.567    0.000 level.py:8(__init__)
                 774346  389.550    0.001  707.524    0.001 agent.py:67(modify)
             2873073728  468.952    0.000  681.500    0.000 enum.py:646(__hash__)
                2487625   25.188    0.000  626.544    0.000 levels.py:441(generate)
                 774346    4.174    0.000  624.629    0.001 grad_mode.py:23(decorate_context)
        17809958/2323038   63.878    0.000  613.411    0.000 module.py:715(_call_impl)
                 774346   21.046    0.000  612.433    0.001 adam.py:55(step)
               77434600  156.397    0.000  607.906    0.000 layers.py:735(check)
               11940261  105.780    0.000  573.338    0.000 level.py:41(notUsed)
                1548692    3.717    0.000  559.795    0.000 network.py:27(forward)
                1548692   14.669    0.000  547.304    0.000 container.py:115(forward)
                 774346  111.766    0.000  503.831    0.001 functional.py:53(adam)
              153908043   86.432    0.000  417.199    0.000 allGraphs.py:83(layers_not_in)
               77434600  104.781    0.000  399.691    0.000 layers.py:729(isFree)
              214329490  112.153    0.000  376.912    0.000 {built-in method builtins.any}
                 774346    3.961    0.000  362.034    0.000 tensor.py:181(backward)
                 774346    2.485    0.000  358.073    0.000 __init__.py:68(backward)
                 774346  339.232    0.000  339.232    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              153908043  161.323    0.000  330.767    0.000 allGraphs.py:84(<listcomp>)
                5420429  190.229    0.000  329.754    0.000 layer.py:167(NoRock_update)
                 774346    8.994    0.000  325.304    0.000 agent.py:112(__call__)
              529877988  222.015    0.000  294.910    0.000 layer.py:95(isFree)
               11940261    8.205    0.000  267.761    0.000 level.py:38(elementsIn)
               80531984  261.520    0.000  261.520    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2323038    8.321    0.000  253.744    0.000 tensor.py:576(__iter__)
                2323038  239.992    0.000  239.992    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              159515376   48.934    0.000  238.748    0.000 {built-in method builtins.all}
                3097384    4.970    0.000  218.430    0.000 conv.py:422(forward)
             2873076285  212.548    0.000  212.548    0.000 {built-in method builtins.hash}
                3097384    5.691    0.000  211.635    0.000 conv.py:414(_conv_forward)
              134736338   63.782    0.000  210.861    0.000 overrides.py:1070(has_torch_function)
                3097384  204.923    0.000  204.923    0.000 {built-in method conv2d}
              288613503  134.591    0.000  198.798    0.000 allGraphs.py:45(p)
              599576600  148.311    0.000  181.582    0.000 layers.py:700(<genexpr>)
               11940261   84.346    0.000  174.158    0.000 level.py:39(<listcomp>)
              230402545   54.548    0.000  169.716    0.000 layers.py:690(<genexpr>)
                3097384    6.809    0.000  162.650    0.000 linear.py:92(forward)
               43363430   93.872    0.000  156.344    0.000 tensor.py:933(grad)
               17413375   12.855    0.000  153.062    0.000 layer.py:69(restart)
                3097384   11.340    0.000  152.841    0.000 functional.py:1669(linear)
                 774346   12.823    0.000  136.099    0.000 optimizer.py:167(zero_grad)
                2487725   60.064    0.000  120.860    0.000 layers.py:36(reset)
              573281265  117.996    0.000  117.996    0.000 level.py:32(inverse)
                 774346    5.160    0.000  112.527    0.000 agent.py:59(modify_board)
                 774346   63.420    0.000  109.018    0.000 collector.py:46(collect)
                3097384  108.809    0.000  108.809    0.000 {built-in method addmm}
               38722293   64.497    0.000  106.510    0.000 layers.py:602(check)
               38722327   64.093    0.000  105.136    0.000 layers.py:632(check)
               38717504   62.491    0.000  104.423    0.000 layers.py:617(check)
               12389536  102.025    0.000  102.025    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1050517356   92.870    0.000   92.870    0.000 layer.py:91(positions)
              519405389   90.019    0.000   90.019    0.000 enum.py:352(<genexpr>)
               11940261   53.702    0.000   85.399    0.000 {built-in method _functools.reduce}
               12389536   85.072    0.000   85.072    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              334651132   82.898    0.000   82.898    0.000 layer.py:146(elements)
              354650736   69.707    0.000   82.695    0.000 overrides.py:1083(<genexpr>)
              162899955   59.005    0.000   81.287    0.000 layer.py:130(add)
                2487625   41.248    0.000   79.417    0.000 level.py:16(<dictcomp>)
               51287842   51.383    0.000   79.360    0.000 layers.py:113(isDone)
                 774346   50.725    0.000   76.911    0.000 allGraphsTrain.py:43(<listcomp>)
                 774346   74.414    0.000   74.414    0.000 {built-in method torch._C._nn.one_hot}
                4646076    3.802    0.000   72.247    0.000 activation.py:713(forward)
                4646076    6.140    0.000   68.446    0.000 functional.py:1292(leaky_relu)
                4646076   61.679    0.000   61.679    0.000 {built-in method torch._C._nn.leaky_relu}
              292057373   56.276    0.000   60.833    0.000 {built-in method builtins.max}
              529877988   60.370    0.000   60.370    0.000 layer.py:203(isBlocking)
                6194768   58.959    0.000   58.959    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 774346   15.879    0.000   58.702    0.000 allGraphs.py:137(transform)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532018: <Diamonds4_0.5_var_0> in cluster <dcc> Done

Job <Diamonds4_0.5_var_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:42 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 19:44:25 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 19:44:25 2021
Terminated at Mon Apr 19 05:39:39 2021
Results reported at Mon Apr 19 05:39:39 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 720
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35618.41 sec.
    Max Memory :                                 2067 MB
    Average Memory :                             2065.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14317.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35756 sec.
    Turnaround time :                            144657 sec.

The output (if any) is above this job summary.

