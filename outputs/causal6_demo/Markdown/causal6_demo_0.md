
# Parameters

    Name :                      causal6_demo-0
    Main :                      teleport
    Level :                     Levels.Causal6
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
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      50881859626 function calls (50728339023 primitive calls) in 57311.60 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57311.598 57311.598 {built-in method builtins.exec}
                      1    1.855    1.855 57311.598 57311.598 <string>:1(<module>)
                      1  128.742  128.742 57309.743 57309.743 main.py:40(teleport)
                5483206   18.206    0.000 18634.644    0.003 agent.py:29(learn)
                5483206  447.683    0.000 15936.717    0.003 learner.py:42(Qlearn)
                2741603   12.128    0.000 13318.809    0.005 game.py:39(step)
                2741603   16.286    0.000 12662.723    0.005 layers.py:581(step)
                2741603   90.940    0.000 11219.580    0.004 agent.py:54(_learn)
                2741603 5331.862    0.002 10095.456    0.004 replaybuffer.py:28(teleporter_save_data)
                2741603   74.370    0.000 7386.152    0.003 agent.py:115(_learn)
        172709965/19190373  658.864    0.000 7236.306    0.000 module.py:715(_call_impl)
               13707167   33.485    0.000 6772.562    0.000 network.py:24(forward)
                5483206   32.835    0.000 6755.202    0.001 grad_mode.py:23(decorate_context)
                2741603  202.884    0.000 6706.152    0.002 layers.py:17(step)
                5483206  170.637    0.000 6662.927    0.001 adam.py:55(step)
               13707167  183.138    0.000 6661.729    0.000 container.py:115(forward)
              274160300  576.016    0.000 6478.815    0.000 layer.py:92(move)
                2741603 4259.106    0.002 6473.105    0.002 agent.py:86(interveen)
                2741604  368.965    0.000 5921.051    0.002 layers.py:552(update)
                5483206 1229.972    0.000 5739.111    0.001 functional.py:53(adam)
                5482358  128.392    0.000 4467.659    0.001 agent.py:49(__call__)
              274160300  580.777    0.000 3744.290    0.000 layers.py:598(check)
              274163086 3712.089    0.000 3712.089    0.000 {built-in method clone}
                5483206   32.008    0.000 3703.347    0.001 tensor.py:181(backward)
                2741603 2273.106    0.001 3677.062    0.001 replaybuffer.py:22(sample_data)
                5483206   18.597    0.000 3671.339    0.001 __init__.py:68(backward)
                5483206 3512.318    0.001 3512.318    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2741603 1291.570    0.000 2585.000    0.001 agent.py:67(modify)
               27414334   45.316    0.000 2426.491    0.000 conv.py:422(forward)
               27414334   49.631    0.000 2362.955    0.000 conv.py:414(_conv_forward)
               27414334 2302.976    0.000 2302.976    0.000 {built-in method conv2d}
               35638295   77.027    0.000 2153.188    0.000 linear.py:92(forward)
               35638295  132.260    0.000 2038.004    0.000 functional.py:1669(linear)
                4553539   42.322    0.000 1861.149    0.000 layers.py:602(restart)
              274160300  416.247    0.000 1647.648    0.000 layers.py:592(isFree)
                4553539   20.596    0.000 1506.313    0.000 level.py:8(__init__)
               35638295 1460.170    0.000 1460.170    0.000 {built-in method addmm}
               24673579 1449.641    0.000 1449.641    0.000 {built-in method cat}
                2741603   37.957    0.000 1414.881    0.001 agent.py:110(__call__)
              345442032  906.878    0.000 1414.562    0.000 tensor.py:933(grad)
               21932832  805.774    0.000 1402.255    0.000 layer.py:163(NoRock_update)
              760349895  400.074    0.000 1400.924    0.000 {built-in method builtins.any}
                5483206  128.378    0.000 1363.073    0.000 optimizer.py:167(zero_grad)
             6059651084  943.528    0.000 1361.062    0.000 enum.py:646(__hash__)
                8223961   60.084    0.000 1340.316    0.000 agent.py:59(modify_board)
                4553539   59.656    0.000 1320.591    0.000 levels.py:293(generate)
             2146942660  999.991    0.000 1231.401    0.000 layer.py:89(isFree)
              287870003  141.228    0.000 1220.311    0.000 {built-in method builtins.all}
                2741603   52.768    0.000 1208.760    0.000 replaybuffer.py:18(stacker)
               98697708 1200.386    0.000 1200.386    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               27319704  227.724    0.000 1196.403    0.000 level.py:41(notUsed)
              282387047 1130.430    0.000 1130.430    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1519926256  381.924    0.000 1102.743    0.000 layers.py:558(<genexpr>)
              274160300  663.313    0.000 1068.986    0.000 layers.py:418(check)
               98697708 1012.774    0.000 1012.774    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               49345462   39.979    0.000  992.763    0.000 activation.py:713(forward)
               49345462   65.783    0.000  952.784    0.000 functional.py:1292(leaky_relu)
               11843272  919.572    0.000  919.572    0.000 {built-in method tensor}
               49345462  880.505    0.000  880.505    0.000 {built-in method torch._C._nn.leaky_relu}
                8223961  841.622    0.000  841.622    0.000 {built-in method torch._C._nn.one_hot}
             2426461749  615.738    0.000  748.903    0.000 layers.py:563(<genexpr>)
                5483206    6.886    0.000  699.166    0.000 game.py:35(board)
              274160300  439.881    0.000  693.086    0.000 layers.py:431(check)
              274160300  436.088    0.000  691.280    0.000 layers.py:446(check)
              444138326  236.082    0.000  680.407    0.000 overrides.py:1070(has_torch_function)
               49348854  656.534    0.000  656.534    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2741603  380.784    0.000  639.573    0.000 collector.py:53(collect)
               49348854  596.766    0.000  596.766    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               13709603   71.637    0.000  555.464    0.000 tensor.py:21(wrapped)
               49348854  539.090    0.000  539.090    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               27319704   18.661    0.000  526.271    0.000 level.py:38(elementsIn)
             5586234409  497.347    0.000  497.347    0.000 layer.py:85(positions)
               49348854  488.495    0.000  488.495    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                5482358  172.696    0.000  486.271    0.000 exploration.py:53(softmaxer)
             6059671211  417.537    0.000  417.537    0.000 {built-in method builtins.hash}
              274160400  256.405    0.000  407.691    0.000 layers.py:436(isDone)
               49348854  378.757    0.000  378.757    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              910582449  362.580    0.000  362.580    0.000 layer.py:142(elements)
               27319704  166.500    0.000  334.203    0.000 level.py:39(<listcomp>)
              274160300  219.411    0.000  330.204    0.000 layers.py:407(check)
              274160300  204.074    0.000  315.052    0.000 layers.py:396(check)
                5483206    7.021    0.000  310.996    0.000 loss.py:445(forward)
                5483206   29.466    0.000  303.975    0.000 functional.py:2637(mse_loss)
               36428312   28.508    0.000  300.585    0.000 layer.py:64(restart)
               35638295  290.429    0.000  290.429    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1295868582  281.846    0.000  281.846    0.000 level.py:32(inverse)
               16449618  258.069    0.000  258.069    0.000 {built-in method sum}
        2628860250/2628860248  176.494    0.000  255.039    0.000 {built-in method builtins.len}
              937624002  197.435    0.000  248.193    0.000 overrides.py:1083(<genexpr>)
              435611517  163.962    0.000  228.474    0.000 layer.py:126(add)
                4553639  111.380    0.000  220.330    0.000 layers.py:30(reset)
                8224809   39.254    0.000  200.044    0.000 tensor.py:506(__rsub__)
                5483206  190.099    0.000  190.099    0.000 {built-in method torch._C._nn.mse_loss}
                2741603   70.538    0.000  190.057    0.000 random.py:315(sample)
             2146942660  188.296    0.000  188.296    0.000 layer.py:199(isBlocking)
               27414334   18.499    0.000  184.950    0.000 flatten.py:39(forward)
                2742699  182.888    0.000  182.888    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
              273251385  121.404    0.000  181.914    0.000 layer.py:122(remove)
                8224809  176.828    0.000  176.828    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               27319704  107.936    0.000  173.406    0.000 {built-in method _functools.reduce}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9497201: <causal6_demo_0> in cluster <dcc> Done

Job <causal6_demo_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 21:09:35 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr  6 23:38:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr  6 23:38:35 2021
Terminated at Wed Apr  7 15:33:52 2021
Results reported at Wed Apr  7 15:33:52 2021

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

    CPU time :                                   57167.28 sec.
    Max Memory :                                 2813 MB
    Average Memory :                             2808.40 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13571.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57318 sec.
    Turnaround time :                            152657 sec.

The output (if any) is above this job summary.

