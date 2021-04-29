
# Parameters

    Name :                      Coconuts_teleport-2
    Main :                      teleport
    Level :                     Levels.Coconuts
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


      78759634377 function calls (78497715202 primitive calls) in 86105.05 seconds

##    Ordered by: cumulative time
   List reduced from 482 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.055 86105.055 {built-in method builtins.exec}
                      1    1.552    1.552 86105.055 86105.055 <string>:1(<module>)
                      1  289.773  289.773 86103.503 86103.503 main.py:45(teleport)
                9374630   47.962    0.000 29097.977    0.003 agent.py:29(learn)
                4687315   26.928    0.000 28119.333    0.006 game.py:41(step)
                4687315   31.381    0.000 26935.948    0.006 layers.py:718(step)
                9374630  722.935    0.000 24150.829    0.003 learner.py:42(Qlearn)
                4687315  461.648    0.000 18218.554    0.004 layers.py:17(step)
              468731500 1795.852    0.000 17715.164    0.000 layer.py:98(move)
                4687315  198.638    0.000 17532.210    0.004 agent.py:54(_learn)
        294681746/32763582 1222.436    0.000 12015.744    0.000 module.py:715(_call_impl)
                4687315  162.881    0.000 11493.248    0.002 agent.py:117(_learn)
               23388952   63.651    0.000 11134.052    0.000 network.py:27(forward)
               23388952  303.712    0.000 10912.189    0.000 container.py:115(forward)
              468731500 1740.356    0.000 10691.836    0.000 layers.py:735(check)
                9374630   74.942    0.000 9257.191    0.001 grad_mode.py:23(decorate_context)
                9374630  338.640    0.000 9047.677    0.001 adam.py:55(step)
                4687316  714.616    0.000 8632.875    0.002 layers.py:684(update)
                4687315 6147.203    0.001 8397.266    0.002 replaybuffer.py:22(sample_data)
                9327007  283.411    0.000 7564.257    0.001 agent.py:49(__call__)
                9374630 1674.836    0.000 7417.602    0.001 functional.py:53(adam)
                4687315 2803.032    0.001 6382.379    0.001 agent.py:88(interveen)
                9374630   61.387    0.000 6028.680    0.001 tensor.py:181(backward)
                9374630   44.579    0.000 5967.292    0.001 __init__.py:68(backward)
                9374630 5666.282    0.001 5666.282    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4687315 2907.551    0.001 5199.520    0.001 replaybuffer.py:28(teleporter_save_data)
                4687315 2399.010    0.001 4826.575    0.001 agent.py:67(modify)
               46777904   85.090    0.000 4140.086    0.000 conv.py:422(forward)
               46777904  110.314    0.000 4015.313    0.000 conv.py:414(_conv_forward)
              468731500  677.926    0.000 3978.278    0.000 layers.py:729(isFree)
               46777904 3884.514    0.000 3884.514    0.000 {built-in method conv2d}
               60792226  138.213    0.000 3462.599    0.000 linear.py:92(forward)
              468731500 2362.513    0.000 3308.984    0.000 layers.py:471(check)
             3052256219 2809.024    0.000 3300.352    0.000 layer.py:95(isFree)
               60792226  239.647    0.000 3249.409    0.000 functional.py:1669(linear)
               32811212 1916.103    0.000 3068.719    0.000 layer.py:151(update)
              468731500 1923.386    0.000 2665.612    0.000 layers.py:77(check)
             1314404921  706.284    0.000 2435.693    0.000 {built-in method builtins.any}
               14014322  122.148    0.000 2366.265    0.000 agent.py:59(modify_board)
               60792226 2324.799    0.000 2324.799    0.000 {built-in method addmm}
                4687315   83.896    0.000 2310.085    0.000 agent.py:112(__call__)
              590601744 1372.258    0.000 2275.713    0.000 tensor.py:933(grad)
               37450897 2224.471    0.000 2224.471    0.000 {built-in method cat}
             7950602149 1465.545    0.000 2136.755    0.000 enum.py:646(__hash__)
                9374630  186.553    0.000 1978.857    0.000 optimizer.py:167(zero_grad)
              164519665 1886.812    0.000 1886.812    0.000 {built-in method clone}
                2447609   33.390    0.000 1874.595    0.001 layers.py:740(restart)
                4687315   93.409    0.000 1847.985    0.000 replaybuffer.py:18(stacker)
               20022980 1631.035    0.000 1631.035    0.000 {built-in method tensor}
                2447609   17.091    0.000 1573.966    0.001 level.py:8(__init__)
               14014322 1533.649    0.000 1533.649    0.000 {built-in method torch._C._nn.one_hot}
              168743340 1488.233    0.000 1488.233    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               84181178   82.544    0.000 1485.800    0.000 activation.py:713(forward)
               84181178  126.234    0.000 1403.256    0.000 functional.py:1292(leaky_relu)
              468731500 1102.119    0.000 1398.941    0.000 layers.py:62(check)
                2447609  103.723    0.000 1394.707    0.001 levels.py:262(generate)
               32814645  189.936    0.000 1334.854    0.000 tensor.py:21(wrapped)
                9374630   17.238    0.000 1287.264    0.000 game.py:37(board)
               84181178 1265.570    0.000 1265.570    0.000 {built-in method torch._C._nn.leaky_relu}
             3730271928 1028.356    0.000 1257.867    0.000 layers.py:700(<genexpr>)
              768579443  404.070    0.000 1235.195    0.000 overrides.py:1070(has_torch_function)
              168743340 1219.523    0.000 1219.523    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               21831445  209.349    0.000 1200.655    0.000 level.py:41(notUsed)
              501546245  107.736    0.000 1164.682    0.000 {built-in method builtins.all}
              944832601  210.130    0.000 1095.206    0.000 layers.py:690(<genexpr>)
            10946999879 1012.992    0.000 1012.992    0.000 layer.py:91(positions)
              468731600  615.752    0.000  881.881    0.000 layers.py:113(isDone)
                4687315  505.826    0.000  875.698    0.000 collector.py:46(collect)
               84371670  860.163    0.000  860.163    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                9327007  286.852    0.000  830.165    0.000 exploration.py:53(softmaxer)
               84371670  812.990    0.000  812.990    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1308865613  742.634    0.000  742.634    0.000 layer.py:146(elements)
               84371670  710.252    0.000  710.252    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              468731500  464.754    0.000  691.423    0.000 layers.py:48(check)
             7950636244  671.216    0.000  671.216    0.000 {built-in method builtins.hash}
               84371670  627.642    0.000  627.642    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9374630   19.524    0.000  585.757    0.000 loss.py:445(forward)
                9374630   70.636    0.000  566.233    0.000 functional.py:2637(mse_loss)
              178533987  552.566    0.000  552.566    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               21831445   20.713    0.000  533.206    0.000 level.py:38(elementsIn)
              468731500  349.874    0.000  508.693    0.000 layers.py:23(check)
        4911545272/4911545270  364.396    0.000  495.667    0.000 {built-in method builtins.len}
               84371670  469.051    0.000  469.051    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               23436575  464.718    0.000  464.718    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
             1630764825  375.891    0.000  464.698    0.000 overrides.py:1083(<genexpr>)
              481244047  282.669    0.000  442.787    0.000 layer.py:126(remove)
               60792226  411.118    0.000  411.118    0.000 {method 't' of 'torch._C._TensorBase' objects}
                4689179  407.977    0.000  407.977    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                4687315  148.750    0.000  393.019    0.000 random.py:315(sample)
              622269227  289.957    0.000  388.159    0.000 layer.py:130(add)
               28123890  368.965    0.000  368.965    0.000 {built-in method sum}
             3052256219  341.741    0.000  341.741    0.000 layer.py:203(isBlocking)
               21831445  166.476    0.000  338.929    0.000 level.py:39(<listcomp>)
             3754539315  331.774    0.000  331.774    0.000 {method 'random' of '_random.Random' objects}
                9374630  320.296    0.000  320.296    0.000 {built-in method torch._C._nn.mse_loss}
                4687315   26.355    0.000  300.064    0.000 exploration.py:47(epsilonGreedy)
             1006220183  295.230    0.000  295.230    0.000 level.py:32(inverse)
                9376030  288.675    0.000  288.675    0.000 {built-in method max}
                9327007  271.067    0.000  271.067    0.000 {built-in method multinomial}
               46777904   38.179    0.000  270.054    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550922: <Coconuts_teleport_2> in cluster <dcc> Done

Job <Coconuts_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:52 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 26 07:08:54 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 26 07:08:54 2021
Terminated at Tue Apr 27 07:04:07 2021
Results reported at Tue Apr 27 07:04:07 2021

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

    CPU time :                                   85900.60 sec.
    Max Memory :                                 2675 MB
    Average Memory :                             2672.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13709.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            571335 sec.

The output (if any) is above this job summary.

