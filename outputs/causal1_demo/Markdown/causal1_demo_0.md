
# Parameters

    Name :                      causal1_demo-0
    Main :                      teleport
    Level :                     Levels.Causal1
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      46696560043 function calls (46505094156 primitive calls) in 57317.25 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57317.251 57317.251 {built-in method builtins.exec}
                      1    1.833    1.833 57317.251 57317.251 <string>:1(<module>)
                      1  150.267  150.267 57315.418 57315.418 main.py:40(teleport)
                6838510   23.441    0.000 18400.592    0.003 agent.py:29(learn)
                6838510  442.745    0.000 15476.390    0.002 learner.py:42(Qlearn)
                3419255   13.209    0.000 12525.717    0.004 game.py:41(step)
                3419255   19.679    0.000 11861.100    0.003 layers.py:710(step)
                3419255  108.851    0.000 11135.608    0.003 agent.py:54(_learn)
                3419255 5414.626    0.002 9718.493    0.003 replaybuffer.py:28(teleporter_save_data)
        215398544/23933668  777.151    0.000 7607.080    0.000 module.py:715(_call_impl)
                3419255   89.741    0.000 7228.123    0.002 agent.py:117(_learn)
               17095158   42.062    0.000 7102.287    0.000 network.py:24(forward)
               17095158  190.900    0.000 6957.705    0.000 container.py:115(forward)
                3419256  472.013    0.000 6508.831    0.002 layers.py:676(update)
                3419255 4096.660    0.001 6418.007    0.002 agent.py:88(interveen)
                6838510   39.690    0.000 6222.649    0.001 grad_mode.py:23(decorate_context)
                6838510  206.225    0.000 6109.348    0.001 adam.py:55(step)
                3419255  259.294    0.000 5307.700    0.002 layers.py:17(step)
              341925500  527.637    0.000 5019.108    0.000 layer.py:98(move)
                6838510 1120.569    0.000 5017.365    0.001 functional.py:53(adam)
                6837393  143.242    0.000 4708.881    0.001 agent.py:49(__call__)
                3419255 2930.865    0.001 4546.761    0.001 replaybuffer.py:22(sample_data)
                6838510   38.717    0.000 3652.067    0.001 tensor.py:181(backward)
                6838510   23.930    0.000 3613.350    0.001 __init__.py:68(backward)
                6838510 3439.849    0.001 3439.849    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              352580620 3408.280    0.000 3408.280    0.000 {built-in method clone}
                3419255 1672.127    0.000 3117.854    0.001 agent.py:67(modify)
                7862118   61.751    0.000 2656.581    0.000 layers.py:731(restart)
               34190316   57.177    0.000 2570.932    0.000 conv.py:422(forward)
               34190316   61.597    0.000 2491.985    0.000 conv.py:414(_conv_forward)
               34190316 2419.141    0.000 2419.141    0.000 {built-in method conv2d}
               44446964   95.309    0.000 2228.718    0.000 linear.py:92(forward)
               44446964  158.208    0.000 2090.134    0.000 functional.py:1669(linear)
              341925500  564.685    0.000 2087.611    0.000 layers.py:727(check)
                7862118   31.296    0.000 2063.396    0.000 level.py:8(__init__)
              341925500  414.437    0.000 1886.916    0.000 layers.py:721(isFree)
                7862118   92.330    0.000 1732.367    0.000 levels.py:122(generate)
               30772178 1606.154    0.000 1606.154    0.000 {built-in method cat}
              430826184  944.090    0.000 1576.389    0.000 tensor.py:933(grad)
               30660924  278.029    0.000 1558.758    0.000 level.py:41(notUsed)
               20515536  910.610    0.000 1528.881    0.000 layer.py:167(NoRock_update)
                3419255   43.882    0.000 1498.036    0.000 agent.py:112(__call__)
              952943253  457.021    0.000 1494.314    0.000 {built-in method builtins.any}
               44446964 1473.884    0.000 1473.884    0.000 {built-in method addmm}
             2012676561 1198.846    0.000 1472.479    0.000 layer.py:95(isFree)
               10256648   64.561    0.000 1419.567    0.000 agent.py:59(modify_board)
                3419255   60.725    0.000 1373.324    0.000 replaybuffer.py:18(stacker)
                6838510  124.295    0.000 1349.110    0.000 optimizer.py:167(zero_grad)
              123093180 1020.195    0.000 1020.195    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               61542122   55.731    0.000  976.127    0.000 activation.py:713(forward)
              362837268  952.183    0.000  952.183    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               61542122   76.553    0.000  920.396    0.000 functional.py:1292(leaky_relu)
               10256648  918.234    0.000  918.234    0.000 {built-in method torch._C._nn.one_hot}
               14694003  915.467    0.000  915.467    0.000 {built-in method tensor}
             3598281281  624.259    0.000  902.066    0.000 enum.py:646(__hash__)
              560755786  290.294    0.000  860.597    0.000 overrides.py:1070(has_torch_function)
              123093180  847.984    0.000  847.984    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               61542122  835.985    0.000  835.985    0.000 {built-in method torch._C._nn.leaky_relu}
               23936641  119.081    0.000  812.542    0.000 tensor.py:21(wrapped)
              365862241   80.004    0.000  795.761    0.000 {built-in method builtins.all}
              724445590  166.973    0.000  740.420    0.000 layers.py:682(<genexpr>)
             2338444374  580.374    0.000  716.827    0.000 layers.py:692(<genexpr>)
               30660924   24.337    0.000  710.699    0.000 level.py:38(elementsIn)
                6838510    6.688    0.000  697.808    0.000 game.py:37(board)
                3419255  348.382    0.000  593.357    0.000 collector.py:53(collect)
               61546590  584.497    0.000  584.497    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              341925500  358.144    0.000  568.920    0.000 layers.py:135(check)
              341925600  375.042    0.000  566.601    0.000 layers.py:107(isDone)
               61546590  535.437    0.000  535.437    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               47172708   46.079    0.000  514.659    0.000 layer.py:69(restart)
                6837393  180.724    0.000  492.275    0.000 exploration.py:53(softmaxer)
               61546590  477.257    0.000  477.257    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              341925500  297.787    0.000  458.427    0.000 layers.py:42(check)
               30660924  225.343    0.000  451.001    0.000 level.py:39(<listcomp>)
               61546590  416.050    0.000  416.050    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              341925500  266.861    0.000  414.312    0.000 layers.py:118(check)
             1294450283  391.684    0.000  391.684    0.000 layer.py:146(elements)
                7862218  192.290    0.000  382.019    0.000 layers.py:30(reset)
             1414311388  359.472    0.000  359.472    0.000 level.py:32(inverse)
             3845861942  334.775    0.000  334.775    0.000 layer.py:91(positions)
              630502743  241.719    0.000  332.238    0.000 layer.py:130(add)
                6838510    8.989    0.000  326.330    0.000 loss.py:445(forward)
                6838510   36.344    0.000  317.341    0.000 functional.py:2637(mse_loss)
             1189894494  252.371    0.000  316.006    0.000 overrides.py:1083(<genexpr>)
               61546590  310.413    0.000  310.413    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               17096275  299.194    0.000  299.194    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                7862118  161.553    0.000  282.200    0.000 level.py:16(<dictcomp>)
             3598306232  277.811    0.000  277.811    0.000 {built-in method builtins.hash}
        2601413325/2601413323  181.241    0.000  268.518    0.000 {built-in method builtins.len}
               44446964  266.971    0.000  266.971    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1386830966  241.864    0.000  241.864    0.000 enum.py:352(<genexpr>)
               20515530  237.849    0.000  237.849    0.000 {built-in method sum}
                3419255   87.929    0.000  236.893    0.000 random.py:315(sample)
               30660924  146.454    0.000  235.361    0.000 {built-in method _functools.reduce}
              335980810  160.445    0.000  235.143    0.000 layer.py:126(remove)
                3420621  224.014    0.000  224.014    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                6838510  183.648    0.000  183.648    0.000 {built-in method torch._C._nn.mse_loss}
               34190316   23.752    0.000  177.814    0.000 flatten.py:39(forward)
                3419255   13.497    0.000  176.615    0.000 exploration.py:47(epsilonGreedy)
                6839534  169.567    0.000  169.567    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9497203: <causal1_demo_0> in cluster <dcc> Done

Job <causal1_demo_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 21:09:35 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr  7 20:29:55 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 20:29:55 2021
Terminated at Thu Apr  8 12:25:22 2021
Results reported at Thu Apr  8 12:25:22 2021

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

    CPU time :                                   57170.88 sec.
    Max Memory :                                 2819 MB
    Average Memory :                             2812.17 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13565.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57341 sec.
    Turnaround time :                            227747 sec.

The output (if any) is above this job summary.

