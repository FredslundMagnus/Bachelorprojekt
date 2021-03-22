
# Parameters

    Name :                      causal2_9x9-3
    Main :                      teleport
    Level :                     Levels.Causal2
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
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.02
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


      27250397992 function calls (27157157185 primitive calls) in 35710.70 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.704 35710.704 {built-in method builtins.exec}
                      1    0.992    0.992 35710.704 35710.704 <string>:1(<module>)
                      1   89.342   89.342 35709.712 35709.712 main.py:13(teleport)
                1665027    7.906    0.000 9345.404    0.006 game.py:27(step)
                3330054   12.846    0.000 9328.580    0.003 agent.py:26(learn)
                1665027   10.054    0.000 8951.868    0.005 layers.py:373(step)
                3330054  217.631    0.000 7970.629    0.002 learner.py:42(Qlearn)
                1665027 4531.019    0.003 7793.686    0.005 replaybuffer.py:27(teleporter_save_data)
                1665027   52.726    0.000 5575.236    0.003 agent.py:50(_learn)
                1665027  148.561    0.000 5337.428    0.003 layers.py:18(step)
              166502700  430.587    0.000 5172.471    0.000 layer.py:74(move)
                1665027 3387.531    0.002 4591.292    0.003 agent.py:77(interveen)
        104894842/11655046  446.091    0.000 3951.749    0.000 module.py:715(_call_impl)
                1665027   46.306    0.000 3733.698    0.002 agent.py:101(_learn)
                8324992   21.201    0.000 3682.991    0.000 network.py:24(forward)
                8324992  101.402    0.000 3607.254    0.000 container.py:115(forward)
                1665028  205.704    0.000 3589.665    0.002 layers.py:344(update)
                3330054   20.352    0.000 3182.653    0.001 grad_mode.py:23(decorate_context)
                3330054  121.348    0.000 3123.852    0.001 adam.py:55(step)
              166502700  542.228    0.000 2984.748    0.000 layers.py:390(check)
              260726172 2565.172    0.000 2565.172    0.000 {built-in method clone}
                3330054  572.477    0.000 2509.119    0.001 functional.py:53(adam)
                3329911   78.508    0.000 2423.742    0.001 agent.py:45(__call__)
                1665027 1049.756    0.001 1887.966    0.001 replaybuffer.py:23(sample_data)
                3330054   20.644    0.000 1836.004    0.001 tensor.py:181(backward)
                3330054   12.390    0.000 1815.360    0.001 __init__.py:68(backward)
                3330054 1728.321    0.001 1728.321    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              166502700  342.686    0.000 1435.310    0.000 layers.py:384(isFree)
                4220811   45.093    0.000 1434.560    0.000 layers.py:394(restart)
                1665027  706.797    0.000 1396.227    0.001 agent.py:59(modify)
               14985252  860.409    0.000 1365.936    0.000 layer.py:119(update)
               16649984   28.738    0.000 1310.998    0.000 conv.py:422(forward)
               16649984   36.767    0.000 1269.216    0.000 conv.py:414(_conv_forward)
               16649984 1226.101    0.000 1226.101    0.000 {built-in method conv2d}
               21644922   48.627    0.000 1144.163    0.000 linear.py:92(forward)
             1463528100  884.222    0.000 1092.624    0.000 layer.py:71(isFree)
               21644922   85.049    0.000 1071.099    0.000 functional.py:1669(linear)
                4220811   20.583    0.000 1020.521    0.000 level.py:8(__init__)
                4220811   56.596    0.000  927.773    0.000 levels.py:151(generate)
              209793456  517.418    0.000  881.147    0.000 tensor.py:933(grad)
               14985100  817.553    0.000  817.553    0.000 {built-in method cat}
               23636090  184.808    0.000  810.200    0.000 level.py:41(notUsed)
             2822640152  562.082    0.000  792.206    0.000 enum.py:646(__hash__)
                1665027   22.436    0.000  755.000    0.000 agent.py:96(__call__)
                3330054   74.705    0.000  752.060    0.000 optimizer.py:167(zero_grad)
               21644922  746.538    0.000  746.538    0.000 {built-in method addmm}
                4994938   34.631    0.000  724.159    0.000 agent.py:54(modify_board)
              265721110  703.394    0.000  703.394    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1665027   31.938    0.000  697.847    0.000 replaybuffer.py:19(stacker)
                6913289  554.179    0.000  554.179    0.000 {built-in method tensor}
              173163684   58.391    0.000  521.324    0.000 {built-in method builtins.all}
               59940972  505.147    0.000  505.147    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               29969914   25.382    0.000  499.783    0.000 activation.py:713(forward)
              166502700  307.361    0.000  499.214    0.000 layers.py:216(check)
              166502700  308.949    0.000  496.109    0.000 layers.py:244(check)
              166502700  304.570    0.000  494.848    0.000 layers.py:230(check)
              532964499  154.147    0.000  479.529    0.000 layers.py:350(<genexpr>)
              268069506  169.307    0.000  478.733    0.000 overrides.py:1070(has_torch_function)
               29969914   41.187    0.000  474.401    0.000 functional.py:1292(leaky_relu)
                4994938  466.565    0.000  466.565    0.000 {built-in method torch._C._nn.one_hot}
                3330054    4.517    0.000  449.826    0.000 game.py:23(board)
               29969914  429.031    0.000  429.031    0.000 {built-in method torch._C._nn.leaky_relu}
              166502700  295.382    0.000  415.719    0.000 layers.py:76(check)
               59940972  412.358    0.000  412.358    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             3963986025  397.294    0.000  397.294    0.000 layer.py:67(positions)
               37987299   34.421    0.000  354.971    0.000 layer.py:48(restart)
              667450444  338.020    0.000  338.020    0.000 layer.py:114(elements)
              166502800  200.902    0.000  303.423    0.000 layers.py:110(isDone)
                1665027  172.740    0.000  296.310    0.000 collector.py:54(collect)
               29970486  295.212    0.000  295.212    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              296374537  114.154    0.000  293.623    0.000 {built-in method builtins.any}
               29970486  270.570    0.000  270.570    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               23636090   18.352    0.000  268.712    0.000 level.py:38(elementsIn)
             1126682456  264.324    0.000  264.324    0.000 level.py:32(inverse)
                4220911  127.668    0.000  259.970    0.000 layers.py:33(reset)
              166502700  163.186    0.000  253.963    0.000 layers.py:203(check)
                3329911   90.060    0.000  249.899    0.000 exploration.py:53(softmaxer)
               29970486  239.739    0.000  239.739    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              166502700  151.132    0.000  231.556    0.000 layers.py:63(check)
             2822652503  230.126    0.000  230.126    0.000 {built-in method builtins.hash}
              320833417  172.766    0.000  220.999    0.000 layer.py:98(add)
               29970486  205.159    0.000  205.159    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6660884   31.906    0.000  190.553    0.000 tensor.py:21(wrapped)
              564444486  146.474    0.000  176.945    0.000 overrides.py:1083(<genexpr>)
                3330054    5.332    0.000  170.483    0.000 loss.py:445(forward)
               23636090   81.456    0.000  165.299    0.000 level.py:39(<listcomp>)
                3330054   19.988    0.000  165.151    0.000 functional.py:2637(mse_loss)
               29970486  165.023    0.000  165.023    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1463528100  161.522    0.000  161.522    0.000 layer.py:175(isBlocking)
        1438410993/1438410991  111.947    0.000  159.866    0.000 {built-in method builtins.len}
              176401842  112.830    0.000  156.439    0.000 layer.py:94(remove)
                1665027   48.987    0.000  137.432    0.000 random.py:315(sample)
               21644922  136.178    0.000  136.178    0.000 {method 't' of 'torch._C._TensorBase' objects}
                9990162  117.656    0.000  117.656    0.000 {built-in method sum}
                4995081   23.192    0.000  102.265    0.000 tensor.py:506(__rsub__)
                3330054   92.599    0.000   92.599    0.000 {built-in method torch._C._nn.mse_loss}
                4995081   91.623    0.000   91.623    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               29970576   39.174    0.000   90.636    0.000 tensor.py:596(__hash__)
               16649984   12.846    0.000   90.346    0.000 flatten.py:39(forward)
                3330552   86.520    0.000   86.520    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9447209: <causal2_9x9_3> in cluster <dcc> Done

Job <causal2_9x9_3> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Sun Mar 21 22:24:33 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Mar 21 22:24:36 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 22:24:36 2021
Terminated at Mon Mar 22 08:20:00 2021
Results reported at Mon Mar 22 08:20:00 2021

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

    CPU time :                                   35618.15 sec.
    Max Memory :                                 2445 MB
    Average Memory :                             2417.70 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5747.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35766 sec.
    Turnaround time :                            35727 sec.

The output (if any) is above this job summary.

