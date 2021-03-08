
# Parameters

    Name :                      gold_medium-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      18147070575 function calls (18015261244 primitive calls) in 35680.14 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35714.745 35714.745 {built-in method builtins.exec}
                      1    0.900    0.900 35714.745 35714.745 <string>:1(<module>)
                      1  101.082  101.082 35713.844 35713.844 main.py:10(teleport)
                4705616   15.781    0.000 10209.305    0.002 agent.py:26(learn)
                4705616  277.843    0.000 8572.038    0.002 learner.py:42(Qlearn)
                2352808  221.539    0.000 8079.541    0.003 collector.py:36(collect)
               11764040 6893.693    0.001 7831.891    0.001 {built-in method builtins.sum}
                2352808   83.045    0.000 6115.190    0.003 agent.py:50(_learn)
                2352808    8.206    0.000 5287.385    0.002 game.py:21(step)
                2352808   10.321    0.000 4899.393    0.002 layers.py:212(step)
        148221080/16469208  564.059    0.000 4604.641    0.000 module.py:866(_call_impl)
                2352808 2623.757    0.001 4419.847    0.002 replaybuffer.py:27(teleporter_save_data)
               11763592   33.100    0.000 4279.720    0.000 network.py:24(forward)
               11763592  139.555    0.000 4174.299    0.000 container.py:117(forward)
                2352808   70.868    0.000 4063.780    0.002 agent.py:101(_learn)
                2352808 2157.178    0.001 3570.810    0.002 agent.py:77(interveen)
                4705616   38.305    0.000 3319.079    0.001 optimizer.py:84(wrapper)
                4705616   19.258    0.000 3151.706    0.001 grad_mode.py:24(decorate_context)
                4705616  123.507    0.000 3089.434    0.001 adam.py:55(step)
                4705168  107.197    0.000 2854.401    0.001 agent.py:45(__call__)
                4705616  639.111    0.000 2816.424    0.001 _functional.py:53(adam)
                2352809  203.237    0.000 2658.017    0.001 layers.py:192(update)
                2352808  152.116    0.000 2214.988    0.001 layers.py:17(step)
                4705616   18.191    0.000 2182.315    0.000 tensor.py:195(backward)
                4705616   17.231    0.000 2163.509    0.000 __init__.py:68(backward)
                4705616 2058.276    0.000 2058.276    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              235280800  225.458    0.000 2043.065    0.000 layer.py:66(move)
               23527184   51.173    0.000 1574.267    0.000 conv.py:398(forward)
                2352808  792.260    0.000 1533.486    0.001 replaybuffer.py:23(sample_data)
              177705381 1513.893    0.000 1513.893    0.000 {built-in method clone}
               23527184   29.557    0.000 1501.896    0.000 conv.py:390(_conv_forward)
               23527184 1472.338    0.000 1472.338    0.000 {built-in method conv2d}
                2352808  843.473    0.000 1415.100    0.001 agent.py:59(modify)
                3339543   22.875    0.000 1292.778    0.000 layers.py:233(restart)
               30585160   60.708    0.000 1157.753    0.000 linear.py:93(forward)
               30585160   24.143    0.000 1070.204    0.000 functional.py:1737(linear)
               30585160 1040.083    0.000 1040.083    0.000 {built-in method torch._C._nn.linear}
                3339543    4.881    0.000 1034.276    0.000 levels.py:8(__init__)
                3339543   12.051    0.000 1029.395    0.000 level.py:8(__init__)
                3339543  171.311    0.000  986.465    0.000 levels.py:11(generate)
               14117788   25.592    0.000  980.395    0.000 tensor.py:575(__iter__)
              235280800  186.563    0.000  962.170    0.000 layers.py:223(isFree)
               14117788  933.061    0.000  933.061    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2352808   31.478    0.000  899.626    0.000 agent.py:96(__call__)
                7057976   39.484    0.000  860.664    0.000 agent.py:54(modify_board)
              811467475  662.288    0.000  775.606    0.000 layer.py:63(isFree)
               18822016  715.846    0.000  715.846    0.000 {built-in method cat}
               42348752   33.129    0.000  623.099    0.000 activation.py:713(forward)
              235280800  234.560    0.000  622.394    0.000 layers.py:229(check)
               42348752   34.277    0.000  589.970    0.000 functional.py:1364(leaky_relu)
                2352808   39.624    0.000  583.667    0.000 replaybuffer.py:19(stacker)
              235280900   63.683    0.000  574.620    0.000 {built-in method builtins.all}
                7057976  571.008    0.000  571.008    0.000 {built-in method torch._C._nn.one_hot}
               42348752  548.756    0.000  548.756    0.000 {built-in method torch._C._nn.leaky_relu}
               84701088  544.120    0.000  544.120    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              714470243  159.231    0.000  536.338    0.000 layers.py:197(<genexpr>)
                9411236  262.304    0.000  527.205    0.000 layer.py:90(update)
                9954165  513.458    0.000  513.458    0.000 {built-in method tensor}
                4705616   92.498    0.000  503.696    0.000 optimizer.py:189(zero_grad)
               84701088  490.671    0.000  490.671    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3339543  215.858    0.000  410.850    0.000 levels.py:76(RFS)
                4705616    4.726    0.000  387.268    0.000 game.py:17(board)
              235280900  234.017    0.000  356.102    0.000 layers.py:65(isDone)
              235280800  219.812    0.000  335.521    0.000 layers.py:50(check)
              184763357  326.118    0.000  326.118    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               42350544  323.844    0.000  323.844    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4705168  107.173    0.000  282.838    0.000 exploration.py:53(softmaxer)
               42350544  281.058    0.000  281.058    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               42350544  267.071    0.000  267.071    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               42350544  260.172    0.000  260.172    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              296453862  192.269    0.000  236.147    0.000 tensor.py:906(grad)
               13358172   22.841    0.000  230.611    0.000 layer.py:40(restart)
              767041929  203.044    0.000  203.044    0.000 layer.py:85(elements)
                9031894   79.092    0.000  202.466    0.000 random.py:315(sample)
               42350544  197.291    0.000  197.291    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              375740290  142.537    0.000  190.458    0.000 layer.py:76(add)
                4705616    6.652    0.000  189.264    0.000 loss.py:527(forward)
                4705616   16.995    0.000  182.612    0.000 functional.py:2898(mse_loss)
              660915655  127.183    0.000  180.903    0.000 enum.py:646(__hash__)
                3339643   80.704    0.000  159.826    0.000 layers.py:37(reset)
             1842367568  153.569    0.000  153.569    0.000 layer.py:59(positions)
              201509037   92.649    0.000  134.541    0.000 layer.py:72(remove)
                3339543   20.596    0.000  130.840    0.000 level.py:34(notUsed)
        731751486/731751484   83.090    0.000  116.680    0.000 {built-in method builtins.len}
              188195246   79.393    0.000  115.174    0.000 random.py:250(_randbelow_with_getrandbits)
                4705616  113.219    0.000  113.219    0.000 {built-in method torch._C._nn.mse_loss}
               23527184   17.053    0.000  105.233    0.000 flatten.py:39(forward)
                4706321  104.056    0.000  104.056    0.000 {built-in method max}
              163637607  101.584    0.000  101.584    0.000 level.py:25(inverse)
                7058424   10.814    0.000   98.957    0.000 tensor.py:525(__rsub__)
              200372580   64.831    0.000   97.499    0.000 levels.py:33(<genexpr>)
                2352808    8.639    0.000   94.613    0.000 exploration.py:47(epsilonGreedy)
              162338868   93.160    0.000   93.160    0.000 {built-in method torch._C._get_tracing_state}
             1299739514   90.896    0.000   90.896    0.000 {method 'append' of 'list' objects}
                4705168   89.006    0.000   89.006    0.000 {built-in method multinomial}
               23527184   88.180    0.000   88.180    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7058424   86.465    0.000   86.465    0.000 {built-in method rsub}
                4705616   18.074    0.000   84.307    0.000 __init__.py:28(_make_grads)
                4705616   80.900    0.000   80.900    0.000 {built-in method gather}
                9411232   18.220    0.000   80.189    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9393239: <gold_medium_0> in cluster <dcc> Done

Job <gold_medium_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 01:58:30 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 01:58:35 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 01:58:35 2021
Terminated at Mon Mar  8 11:54:10 2021
Results reported at Mon Mar  8 11:54:10 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   35622.51 sec.
    Max Memory :                                 5659 MB
    Average Memory :                             4138.92 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2533.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35739 sec.
    Turnaround time :                            35740 sec.

The output (if any) is above this job summary.

