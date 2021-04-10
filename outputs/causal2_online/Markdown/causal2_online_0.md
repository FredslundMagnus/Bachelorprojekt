
# Parameters

    Name :                      causal2_online-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      22627040460 function calls (22613284737 primitive calls) in 42907.77 seconds

##    Ordered by: cumulative time
   List reduced from 458 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42907.768 42907.768 {built-in method builtins.exec}
                      1    0.001    0.001 42907.767 42907.767 <string>:1(<module>)
                      1  173.871  173.871 42907.767 42907.767 allGraphsTrain.py:5(graphTrain)
                 687767 7621.860    0.011 16931.745    0.025 allGraphs.py:220(transformNot)
                 687767   19.471    0.000 10228.703    0.015 allGraphsTrain.py:27(<listcomp>)
               69464568 2702.241    0.000 10209.248    0.000 allGraphs.py:141(states)
              687772896 9253.762    0.000 9253.762    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              618990700 8328.015    0.000 8328.015    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 687767    2.734    0.000 3883.948    0.006 game.py:41(step)
                 687767    3.426    0.000 3729.598    0.005 layers.py:710(step)
                 687767  767.737    0.001 3658.751    0.005 allGraphsTrain.py:33(<listcomp>)
               10400041   61.233    0.000 2891.014    0.000 allGraphs.py:228(getInterventions)
                 687767  190.259    0.000 2502.355    0.004 allGraphsTrain.py:35(<listcomp>)
                 687768   99.134    0.000 2257.506    0.003 layers.py:676(update)
                 687767    2.565    0.000 1918.723    0.003 agent.py:29(learn)
                 687767   14.939    0.000 1914.517    0.003 agent.py:117(_learn)
                 687767   55.345    0.000 1899.578    0.003 learner.py:42(Qlearn)
                9756117   56.051    0.000 1785.009    0.000 allGraphs.py:188(rightIntervention)
               72903302  197.459    0.000 1562.757    0.000 tensor.py:21(wrapped)
                 687767   70.806    0.000 1503.894    0.002 allGraphsTrain.py:42(<listcomp>)
                 687767   56.230    0.000 1464.851    0.002 layers.py:17(step)
               16760546 1429.179    0.000 1429.179    0.000 {built-in method tensor}
               68776700  117.058    0.000 1402.818    0.000 layer.py:98(move)
               12815289  102.946    0.000 1395.511    0.000 allGraphs.py:192(<dictcomp>)
              176520449  426.671    0.000 1384.170    0.000 allGraphs.py:163(flip_chance)
                3703688   28.368    0.000 1382.341    0.000 layers.py:731(restart)
               13838877    9.540    0.000 1325.204    0.000 game.py:37(board)
               72215535 1151.766    0.000 1151.766    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3703688   13.253    0.000 1105.710    0.000 level.py:8(__init__)
               68776700 1041.705    0.000 1041.705    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                3703688   41.350    0.000  972.309    0.000 levels.py:151(generate)
             4066490597  638.453    0.000  937.143    0.000 enum.py:646(__hash__)
               17781049  162.330    0.000  887.798    0.000 level.py:41(notUsed)
                 687767  500.767    0.001  845.514    0.001 agent.py:67(modify)
              964827647  581.858    0.000  811.612    0.000 allGraphs.py:157(compress)
                 687767    4.169    0.000  799.791    0.001 grad_mode.py:23(decorate_context)
               68776700  142.283    0.000  797.576    0.000 layers.py:727(check)
                 687767   21.956    0.000  787.776    0.001 adam.py:55(step)
        15818641/2063301   68.375    0.000  688.206    0.000 module.py:715(_call_impl)
                 687767  142.331    0.000  675.726    0.001 functional.py:53(adam)
                1375534    3.816    0.000  631.350    0.000 network.py:24(forward)
                1375534   16.465    0.000  619.042    0.000 container.py:115(forward)
              341235707  161.553    0.000  541.734    0.000 {built-in method builtins.any}
                 687767    4.517    0.000  438.631    0.001 tensor.py:181(backward)
                 687767    2.436    0.000  434.114    0.001 __init__.py:68(backward)
               17781049   12.740    0.000  415.440    0.000 level.py:38(elementsIn)
                 687767  413.852    0.001  413.852    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               68776700  100.186    0.000  382.333    0.000 layers.py:721(isFree)
                 687767    8.755    0.000  363.140    0.001 agent.py:112(__call__)
               71527768  356.793    0.000  356.793    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                4814376  208.262    0.000  349.751    0.000 layer.py:167(NoRock_update)
             4066492866  298.690    0.000  298.690    0.000 {built-in method builtins.hash}
              466189046  221.666    0.000  282.148    0.000 layer.py:95(isFree)
               17781049  133.048    0.000  267.040    0.000 level.py:39(<listcomp>)
                2751068    5.144    0.000  242.218    0.000 conv.py:422(forward)
                2063301    8.442    0.000  241.690    0.000 tensor.py:576(__iter__)
               25925816   18.836    0.000  239.294    0.000 layer.py:69(restart)
                2751068    5.396    0.000  235.190    0.000 conv.py:414(_conv_forward)
                2751068  228.784    0.000  228.784    0.000 {built-in method conv2d}
              141680102   54.161    0.000  228.769    0.000 {built-in method builtins.all}
                2063301  227.530    0.000  227.530    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              119671592   64.838    0.000  204.502    0.000 overrides.py:1070(has_torch_function)
               68776700  120.936    0.000  192.513    0.000 layers.py:225(check)
                3703788   96.272    0.000  191.472    0.000 layers.py:30(reset)
              853706913  183.050    0.000  183.050    0.000 level.py:32(inverse)
                2751068    6.515    0.000  182.282    0.000 linear.py:92(forward)
               68776700  112.009    0.000  181.228    0.000 layers.py:201(check)
               68776700  111.797    0.000  179.995    0.000 layers.py:213(check)
                2751068   11.712    0.000  172.702    0.000 functional.py:1669(linear)
               38515006  107.136    0.000  168.997    0.000 tensor.py:933(grad)
              520584896  138.562    0.000  168.600    0.000 layers.py:692(<genexpr>)
                 687767   16.340    0.000  163.089    0.000 optimizer.py:167(zero_grad)
              271260141   71.970    0.000  155.576    0.000 layers.py:682(<genexpr>)
               11004272  140.745    0.000  140.745    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 687767   32.658    0.000  139.630    0.000 allGraphs.py:209(transform)
                 687767   82.298    0.000  138.266    0.000 collector.py:53(collect)
              773452022  137.741    0.000  137.741    0.000 enum.py:352(<genexpr>)
               17781049   84.802    0.000  135.661    0.000 {built-in method _functools.reduce}
              380200520   84.149    0.000  135.260    0.000 allGraphs.py:192(<genexpr>)
                2751068  123.255    0.000  123.255    0.000 {built-in method addmm}
               11004272  119.495    0.000  119.495    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 687767    5.430    0.000  117.715    0.000 agent.py:59(modify_board)
                3703688   54.418    0.000  111.743    0.000 level.py:16(<dictcomp>)
             1179068630  110.816    0.000  110.816    0.000 layer.py:91(positions)
              202537656   78.198    0.000  106.248    0.000 layer.py:130(add)
               12815289   15.412    0.000   94.759    0.000 allGraphs.py:198(<dictcomp>)
              411009784   89.852    0.000   89.852    0.000 layer.py:146(elements)
                4126602    4.011    0.000   87.433    0.000 activation.py:713(forward)
               68776700   54.162    0.000   83.689    0.000 layers.py:190(check)
                4126602    6.322    0.000   83.422    0.000 functional.py:1292(leaky_relu)
               38165631   43.561    0.000   82.462    0.000 allGraphs.py:150(expand)
                5502136   80.526    0.000   80.526    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              314997554   65.514    0.000   78.093    0.000 overrides.py:1083(<genexpr>)
                4126602   76.529    0.000   76.529    0.000 {built-in method torch._C._nn.leaky_relu}
                 687767   52.497    0.000   76.399    0.000 allGraphsTrain.py:41(<listcomp>)
                 687767   73.714    0.000   73.714    0.000 {built-in method torch._C._nn.one_hot}
                5502136   69.935    0.000   69.935    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5502136   63.264    0.000   63.264    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        712073842/712073840   50.686    0.000   63.175    0.000 {built-in method builtins.len}
                 643924   12.718    0.000   57.661    0.000 allGraphs.py:170(bestIntervention)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 9505743: <causal2_online_0> in cluster <dcc> Done

Job <causal2_online_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Thu Apr  8 23:40:13 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr  8 23:40:14 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr  8 23:40:14 2021
Terminated at Fri Apr  9 11:35:24 2021
Results reported at Fri Apr  9 11:35:24 2021

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

    CPU time :                                   42827.72 sec.
    Max Memory :                                 2080 MB
    Average Memory :                             2079.99 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14304.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   43011 sec.
    Turnaround time :                            42911 sec.

The output (if any) is above this job summary.

