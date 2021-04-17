
# Parameters

    Name :                      causal2_online_var_0.5_full_UCB1-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Failed actions chance :     0.5
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      26742509704 function calls (25646446111 primitive calls) in 42908.09 seconds

##    Ordered by: cumulative time
   List reduced from 462 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42908.087 42908.087 {built-in method builtins.exec}
                      1    0.001    0.001 42908.087 42908.087 <string>:1(<module>)
                      1  202.544  202.544 42908.086 42908.086 allGraphsTrain.py:10(graphTrain)
                 873730 6536.103    0.007 15420.122    0.018 allGraphs.py:146(transformNot)
              873737384 9811.173    0.000 9811.173    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 873730   25.243    0.000 9618.442    0.011 allGraphsTrain.py:29(<listcomp>)
               88246831 2309.562    0.000 9593.233    0.000 allGraphs.py:110(states)
              786357400 7146.167    0.000 7146.167    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 873730  824.143    0.001 5481.588    0.006 allGraphsTrain.py:35(<listcomp>)
               20672607   33.297    0.000 4657.445    0.000 allGraphs.py:158(getInterventions)
                 873730    2.961    0.000 4269.774    0.005 game.py:41(step)
                 873730    4.319    0.000 4095.149    0.005 layers.py:718(step)
               20672607   19.566    0.000 2716.932    0.000 allGraphs.py:133(UCB1)
        236370490/20672607  173.963    0.000 2615.990    0.000 {built-in method builtins.min}
               59028176   28.402    0.000 2577.933    0.000 allGraphs.py:134(<lambda>)
        452068373/59028176  704.218    0.000 2549.531    0.000 allGraphs.py:68(expected_moves_UCB1)
                 873731  123.048    0.000 2524.739    0.003 layers.py:684(update)
                 873730  168.723    0.000 2396.669    0.003 allGraphsTrain.py:37(<listcomp>)
               28744037 2331.346    0.000 2331.346    0.000 {built-in method tensor}
               25041258   14.188    0.000 2220.266    0.000 game.py:37(board)
        608738080/138887550  199.932    0.000 2143.632    0.000 allGraphs.py:72(<genexpr>)
               20672607   85.707    0.000 1907.216    0.000 allGraphs.py:153(format)
                 873730    2.811    0.000 1894.487    0.002 agent.py:29(learn)
                 873730   17.818    0.000 1889.824    0.002 agent.py:117(_learn)
                 873730   53.947    0.000 1872.006    0.002 learner.py:42(Qlearn)
                 873730   66.635    0.000 1561.150    0.002 layers.py:17(step)
               92615380  224.748    0.000 1528.507    0.000 tensor.py:21(wrapped)
               87373000  142.119    0.000 1486.737    0.000 layer.py:98(move)
                 873730   72.666    0.000 1461.822    0.002 allGraphsTrain.py:44(<listcomp>)
                3775633   30.558    0.000 1429.542    0.000 layers.py:740(restart)
                3775633   14.385    0.000 1143.490    0.000 level.py:8(__init__)
               91741650 1045.579    0.000 1045.579    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3775633   43.153    0.000 1001.015    0.000 levels.py:151(generate)
             4099183223  687.389    0.000  999.505    0.000 enum.py:646(__hash__)
               87373000  939.174    0.000  939.174    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               18126809  165.329    0.000  912.666    0.000 level.py:41(notUsed)
                 873730  469.825    0.001  840.414    0.001 agent.py:67(modify)
                 873730    4.967    0.000  745.707    0.001 grad_mode.py:23(decorate_context)
               87373000  191.806    0.000  733.786    0.000 layers.py:735(check)
        20095790/2621190   77.331    0.000  732.248    0.000 module.py:715(_call_impl)
                 873730   26.011    0.000  731.427    0.001 adam.py:55(step)
              236370490  148.041    0.000  689.627    0.000 allGraphs.py:83(layers_not_in)
                1747460    4.840    0.000  670.081    0.000 network.py:24(forward)
              452068373  423.004    0.000  660.175    0.000 allGraphs.py:60(UCB1)
                1747460   18.430    0.000  654.800    0.000 container.py:115(forward)
                 873730  132.859    0.000  597.929    0.001 functional.py:53(adam)
              236370490  271.069    0.000  541.587    0.000 allGraphs.py:84(<listcomp>)
               87373000  123.144    0.000  480.759    0.000 layers.py:729(isFree)
              240869002  131.712    0.000  449.839    0.000 {built-in method builtins.any}
                 873730    5.603    0.000  439.332    0.001 tensor.py:181(backward)
                 873730    3.050    0.000  433.729    0.000 __init__.py:68(backward)
               18126809   13.420    0.000  427.881    0.000 level.py:38(elementsIn)
                6116117  248.847    0.000  424.333    0.000 layer.py:167(NoRock_update)
                 873730  411.604    0.000  411.604    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 873730   10.184    0.000  387.667    0.000 agent.py:112(__call__)
              598004724  281.601    0.000  357.615    0.000 layer.py:95(isFree)
             4099186100  312.116    0.000  312.116    0.000 {built-in method builtins.hash}
               90867920  301.397    0.000  301.397    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2621190   10.349    0.000  296.187    0.000 tensor.py:576(__iter__)
              179988480   55.284    0.000  290.200    0.000 {built-in method builtins.all}
                2621190  279.229    0.000  279.229    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               18126809  135.303    0.000  274.265    0.000 level.py:39(<listcomp>)
                3494920    5.940    0.000  262.734    0.000 conv.py:422(forward)
              152029154   78.411    0.000  254.322    0.000 overrides.py:1070(has_torch_function)
                3494920    7.337    0.000  253.685    0.000 conv.py:414(_conv_forward)
               26429431   20.926    0.000  246.305    0.000 layer.py:69(restart)
                3494920  245.008    0.000  245.008    0.000 {built-in method conv2d}
              668779736  176.206    0.000  217.648    0.000 layers.py:700(<genexpr>)
              222034849   58.234    0.000  211.424    0.000 layers.py:690(<genexpr>)
                3775733   97.130    0.000  193.649    0.000 layers.py:36(reset)
               48928934  117.145    0.000  193.426    0.000 tensor.py:933(grad)
                3494920    8.030    0.000  191.487    0.000 linear.py:92(forward)
              870305779  186.831    0.000  186.831    0.000 level.py:32(inverse)
                3494920   14.670    0.000  179.793    0.000 functional.py:1669(linear)
                 873730   17.111    0.000  169.401    0.000 optimizer.py:167(zero_grad)
               87373100   95.148    0.000  146.073    0.000 layers.py:113(isDone)
              788489405  143.340    0.000  143.340    0.000 enum.py:352(<genexpr>)
               18126809   87.616    0.000  140.197    0.000 {built-in method _functools.reduce}
                 873730    6.747    0.000  131.618    0.000 agent.py:59(modify_board)
               43679684   79.335    0.000  129.849    0.000 layers.py:207(check)
               43683391   77.638    0.000  127.540    0.000 layers.py:219(check)
                 873730   74.724    0.000  127.324    0.000 collector.py:46(collect)
               43683865   77.305    0.000  127.054    0.000 layers.py:231(check)
                3494920  126.284    0.000  126.284    0.000 {built-in method addmm}
               13979680  119.573    0.000  119.573    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3775633   60.705    0.000  119.267    0.000 level.py:16(<dictcomp>)
              219520127   84.894    0.000  115.158    0.000 layer.py:130(add)
             1176471211  112.712    0.000  112.712    0.000 layer.py:91(positions)
              448277337  108.512    0.000  108.512    0.000 layer.py:146(elements)
              400168608   83.366    0.000   99.918    0.000 overrides.py:1083(<genexpr>)
               13979680   99.083    0.000   99.083    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 873730   62.301    0.000   93.114    0.000 allGraphsTrain.py:43(<listcomp>)
              454689563   86.397    0.000   86.397    0.000 {built-in method builtins.max}
                5242380    4.717    0.000   85.681    0.000 activation.py:713(forward)
              452061468   85.516    0.000   85.516    0.000 {built-in method math.log}
                 873730   85.486    0.000   85.486    0.000 {built-in method torch._C._nn.one_hot}
                5242380    8.114    0.000   80.963    0.000 functional.py:1292(leaky_relu)
                6989840   75.155    0.000   75.155    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5242380   72.120    0.000   72.120    0.000 {built-in method torch._C._nn.leaky_relu}
                 873730   19.369    0.000   69.213    0.000 allGraphs.py:137(transform)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 9512221: <causal2_online_var_0.5_full_UCB1_0> in cluster <dcc> Done

Job <causal2_online_var_0.5_full_UCB1_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Tue Apr 13 11:09:10 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 13 13:39:49 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 13:39:49 2021
Terminated at Wed Apr 14 01:35:03 2021
Results reported at Wed Apr 14 01:35:03 2021

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
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   42824.66 sec.
    Max Memory :                                 2082 MB
    Average Memory :                             2081.34 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14302.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42913 sec.
    Turnaround time :                            51953 sec.

The output (if any) is above this job summary.

