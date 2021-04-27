
# Parameters

    Name :                      Rocks_teleport-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
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
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      64679112854 function calls (64446520851 primitive calls) in 86105.28 seconds

##    Ordered by: cumulative time
   List reduced from 471 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.281 86105.281 {built-in method builtins.exec}
                      1    1.441    1.441 86105.281 86105.281 <string>:1(<module>)
                      1  174.890  174.890 86103.840 86103.840 main.py:45(teleport)
                8308790   30.009    0.000 29858.845    0.004 agent.py:29(learn)
                4154395   16.160    0.000 26096.704    0.006 game.py:41(step)
                8308790  697.702    0.000 25685.044    0.003 learner.py:42(Qlearn)
                4154395   21.294    0.000 25209.774    0.006 layers.py:718(step)
                4154395  138.495    0.000 17880.785    0.004 agent.py:54(_learn)
                4154395  375.348    0.000 15298.779    0.004 layers.py:17(step)
              415439500 1131.213    0.000 14887.824    0.000 layer.py:98(move)
                4154395  118.217    0.000 11932.137    0.003 agent.py:117(_learn)
        261667163/29076171 1049.116    0.000 11489.088    0.000 module.py:715(_call_impl)
                8308790   51.207    0.000 11078.719    0.001 grad_mode.py:23(decorate_context)
                8308790  277.664    0.000 10926.634    0.001 adam.py:55(step)
              415439500 1205.538    0.000 10862.129    0.000 layers.py:735(check)
               20767381   52.513    0.000 10761.692    0.001 network.py:27(forward)
               20767381  280.491    0.000 10581.519    0.001 container.py:115(forward)
                4154396  587.004    0.000 9862.997    0.002 layers.py:684(update)
                8308790 2015.588    0.000 9464.928    0.001 functional.py:53(adam)
                4154395 4411.856    0.001 8651.356    0.002 replaybuffer.py:28(teleporter_save_data)
              415439500 6834.234    0.000 7995.278    0.000 layers.py:77(check)
                4154395 4444.624    0.001 7947.998    0.002 agent.py:88(interveen)
                8304196  183.933    0.000 7023.173    0.001 agent.py:49(__call__)
                8308790   57.306    0.000 5914.955    0.001 tensor.py:181(backward)
                8308790   28.308    0.000 5857.649    0.001 __init__.py:68(backward)
                8308790 5605.909    0.001 5605.909    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4154395 2764.629    0.001 4985.608    0.001 agent.py:67(modify)
                4154395 2849.832    0.001 4759.591    0.001 replaybuffer.py:22(sample_data)
               12007993   86.676    0.000 3998.775    0.000 layers.py:740(restart)
               41534762   73.059    0.000 3819.963    0.000 conv.py:422(forward)
               41534762   79.892    0.000 3720.310    0.000 conv.py:414(_conv_forward)
               41534762 3626.413    0.000 3626.413    0.000 {built-in method conv2d}
               53993353  123.027    0.000 3443.803    0.000 linear.py:92(forward)
              225590535 3352.854    0.000 3352.854    0.000 {built-in method clone}
               53993353  210.518    0.000 3269.084    0.000 functional.py:1669(linear)
               12007993   43.189    0.000 2820.444    0.000 level.py:8(__init__)
               20771980 1916.508    0.000 2713.815    0.000 layer.py:151(update)
               12007993  308.153    0.000 2402.747    0.000 levels.py:95(generate)
               53993353 2352.514    0.000 2352.514    0.000 {built-in method addmm}
              415439500  412.984    0.000 2225.546    0.000 layers.py:729(isFree)
              523453824 1403.220    0.000 2212.213    0.000 tensor.py:933(grad)
                4154395   53.955    0.000 2211.290    0.001 agent.py:112(__call__)
                8308790  214.930    0.000 2177.408    0.000 optimizer.py:167(zero_grad)
               12458591   92.106    0.000 2099.908    0.000 agent.py:59(modify_board)
               33230566 2023.365    0.000 2023.365    0.000 {built-in method cat}
              149558220 1963.848    0.000 1963.848    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1686826150 1513.548    0.000 1812.562    0.000 layer.py:95(isFree)
             1155350929  554.957    0.000 1739.593    0.000 {built-in method builtins.any}
              149558220 1667.143    0.000 1667.143    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4154395   69.493    0.000 1622.971    0.000 replaybuffer.py:18(stacker)
               74760734   66.382    0.000 1594.827    0.000 activation.py:713(forward)
               24015986  195.962    0.000 1548.148    0.000 level.py:41(notUsed)
               74760734  104.204    0.000 1528.445    0.000 functional.py:1292(leaky_relu)
               74760734 1414.831    0.000 1414.831    0.000 {built-in method torch._C._nn.leaky_relu}
              444522441  197.687    0.000 1385.515    0.000 {built-in method builtins.all}
               12458591 1309.223    0.000 1309.223    0.000 {built-in method torch._C._nn.one_hot}
             4575647209  855.834    0.000 1253.157    0.000 enum.py:646(__hash__)
             1678771412  441.832    0.000 1220.080    0.000 layers.py:690(<genexpr>)
               17783663 1158.887    0.000 1158.887    0.000 {built-in method tensor}
               74779110 1120.610    0.000 1120.610    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               29082841  158.689    0.000 1116.458    0.000 tensor.py:21(wrapped)
              681308388  375.679    0.000 1101.852    0.000 overrides.py:1070(has_torch_function)
               60039965  137.227    0.000 1069.505    0.000 layer.py:69(restart)
              238049126 1044.435    0.000 1044.435    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4154395  614.288    0.000 1030.399    0.000 collector.py:46(collect)
               74779110  980.348    0.000  980.348    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              415439500  619.500    0.000  965.336    0.000 layers.py:62(check)
               74779110  896.238    0.000  896.238    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8308790    9.109    0.000  830.857    0.000 game.py:37(board)
             1635234356  598.717    0.000  814.323    0.000 layer.py:130(add)
               74779110  795.507    0.000  795.507    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             2420589642  628.420    0.000  776.200    0.000 layers.py:700(<genexpr>)
                8304196  270.572    0.000  756.721    0.000 exploration.py:53(softmaxer)
              794901700  363.158    0.000  727.383    0.000 layer.py:126(remove)
              415439600  467.627    0.000  717.176    0.000 layers.py:113(isDone)
               16162388  228.058    0.000  631.951    0.000 random.py:315(sample)
               74779110  625.201    0.000  625.201    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24015986   21.605    0.000  611.979    0.000 level.py:38(elementsIn)
               12008093  303.015    0.000  604.756    0.000 layers.py:36(reset)
             3297690176  598.398    0.000  598.398    0.000 layer.py:146(elements)
              660439615  567.002    0.000  567.002    0.000 level.py:32(inverse)
             5860843243  554.480    0.000  554.480    0.000 layer.py:91(positions)
                8308790   12.085    0.000  485.237    0.000 loss.py:445(forward)
               20771975  478.811    0.000  478.811    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                8308790   44.226    0.000  473.153    0.000 functional.py:2637(mse_loss)
               53993353  457.703    0.000  457.703    0.000 {method 't' of 'torch._C._TensorBase' objects}
              415439500  311.760    0.000  457.089    0.000 layers.py:23(check)
               24926370  413.260    0.000  413.260    0.000 {built-in method sum}
             1445692140  321.618    0.000  402.900    0.000 overrides.py:1083(<genexpr>)
             4575677488  397.328    0.000  397.328    0.000 {built-in method builtins.hash}
        2752853233/2752853231  254.512    0.000  379.798    0.000 {built-in method builtins.len}
               24015986  182.552    0.000  371.613    0.000 level.py:39(<listcomp>)
             5036053771  364.843    0.000  364.843    0.000 {method 'append' of 'list' objects}
              415439500  154.766    0.000  353.047    0.000 layers.py:104(<listcomp>)
               12007993  155.653    0.000  350.355    0.000 level.py:16(<dictcomp>)
              507970767  209.983    0.000  305.327    0.000 random.py:250(_randbelow_with_getrandbits)
               41534762   30.956    0.000  300.917    0.000 flatten.py:39(forward)
                8308790  300.332    0.000  300.332    0.000 {built-in method torch._C._nn.mse_loss}
              794901700  295.023    0.000  295.023    0.000 {method 'remove' of 'list' objects}
               41534762  269.960    0.000  269.960    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550917: <Rocks_teleport_0> in cluster <dcc> Done

Job <Rocks_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:51 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 25 07:19:25 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 25 07:19:25 2021
Terminated at Mon Apr 26 07:14:34 2021
Results reported at Mon Apr 26 07:14:34 2021

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

    CPU time :                                   86009.70 sec.
    Max Memory :                                 2673 MB
    Average Memory :                             2670.48 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13711.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86110 sec.
    Turnaround time :                            485563 sec.

The output (if any) is above this job summary.

