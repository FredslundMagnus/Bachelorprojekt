
# Parameters

    Name :                      causal2_demo-1
    Main :                      teleport
    Level :                     Levels.Causal2
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


      42406543830 function calls (42260852043 primitive calls) in 57310.05 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57310.045 57310.045 {built-in method builtins.exec}
                      1    1.841    1.841 57310.045 57310.045 <string>:1(<module>)
                      1  129.047  129.047 57308.204 57308.204 main.py:40(teleport)
                5203614   19.216    0.000 19339.669    0.004 agent.py:29(learn)
                5203614  458.975    0.000 16570.768    0.003 learner.py:42(Qlearn)
                2601807   12.921    0.000 11885.979    0.005 game.py:39(step)
                2601807   92.342    0.000 11631.299    0.004 agent.py:54(_learn)
                2601807   15.399    0.000 11263.856    0.004 layers.py:581(step)
                2601807 5448.591    0.002 10462.470    0.004 replaybuffer.py:28(teleporter_save_data)
                2601807   75.958    0.000 7678.674    0.003 agent.py:115(_learn)
        163902557/18211781  688.933    0.000 7497.953    0.000 module.py:715(_call_impl)
                5203614   32.359    0.000 7070.153    0.001 grad_mode.py:23(decorate_context)
               13008167   33.501    0.000 7021.741    0.001 network.py:24(forward)
                5203614  180.661    0.000 6974.323    0.001 adam.py:55(step)
               13008167  180.031    0.000 6910.604    0.001 container.py:115(forward)
                2601807 4476.915    0.002 6765.131    0.003 agent.py:86(interveen)
                2601807  211.208    0.000 6019.928    0.002 layers.py:17(step)
                5203614 1284.412    0.000 6003.739    0.001 functional.py:53(adam)
              260180700  615.049    0.000 5783.188    0.000 layer.py:92(move)
                2601808  384.450    0.000 5209.785    0.002 layers.py:552(update)
                5202746  127.198    0.000 4606.875    0.001 agent.py:49(__call__)
              260838540 3907.837    0.000 3907.837    0.000 {built-in method clone}
                5203614   34.189    0.000 3825.766    0.001 tensor.py:181(backward)
                5203614   18.519    0.000 3791.577    0.001 __init__.py:68(backward)
                5203614 3628.697    0.001 3628.697    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2601807 2197.610    0.001 3620.632    0.001 replaybuffer.py:22(sample_data)
              260180700  542.494    0.000 3073.859    0.000 layers.py:598(check)
                2601807 1332.170    0.001 2673.580    0.001 agent.py:67(modify)
               26016334   47.728    0.000 2501.974    0.000 conv.py:422(forward)
               26016334   53.023    0.000 2436.145    0.000 conv.py:414(_conv_forward)
               26016334 2372.553    0.000 2372.553    0.000 {built-in method conv2d}
               33820887   81.626    0.000 2240.427    0.000 linear.py:92(forward)
               33820887  135.787    0.000 2122.064    0.000 functional.py:1669(linear)
                4192143   37.529    0.000 1612.668    0.000 layers.py:602(restart)
              260180700  400.816    0.000 1555.618    0.000 layers.py:592(isFree)
               33820887 1518.166    0.000 1518.166    0.000 {built-in method addmm}
              327827736  953.265    0.000 1485.574    0.000 tensor.py:933(grad)
               23415395 1477.746    0.000 1477.746    0.000 {built-in method cat}
                2601807   37.522    0.000 1458.359    0.001 agent.py:110(__call__)
                5203614  131.164    0.000 1425.400    0.000 optimizer.py:167(zero_grad)
                7804553   59.160    0.000 1370.513    0.000 agent.py:59(modify_board)
              721708071  397.819    0.000 1326.374    0.000 {built-in method builtins.any}
               18212656  750.096    0.000 1293.175    0.000 layer.py:163(NoRock_update)
                4192143   19.787    0.000 1267.232    0.000 level.py:8(__init__)
               93665052 1252.899    0.000 1252.899    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2601807   53.179    0.000 1225.246    0.000 replaybuffer.py:18(stacker)
              268643093 1187.945    0.000 1187.945    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1779303760  930.620    0.000 1154.802    0.000 layer.py:89(isFree)
                4192143   50.883    0.000 1081.193    0.000 levels.py:151(generate)
             4307788330  748.923    0.000 1064.634    0.000 enum.py:646(__hash__)
               93665052 1060.023    0.000 1060.023    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               46829054   41.297    0.000 1040.369    0.000 activation.py:713(forward)
               46829054   65.336    0.000  999.072    0.000 functional.py:1292(leaky_relu)
               20122062  188.672    0.000  977.339    0.000 level.py:41(notUsed)
              273191379  160.787    0.000  943.687    0.000 {built-in method builtins.all}
               46829054  927.147    0.000  927.147    0.000 {built-in method torch._C._nn.leaky_relu}
                7804553  855.913    0.000  855.913    0.000 {built-in method torch._C._nn.one_hot}
               11258728  847.078    0.000  847.078    0.000 {built-in method tensor}
             1663325485  449.598    0.000  806.329    0.000 layers.py:558(<genexpr>)
              260180700  462.456    0.000  730.260    0.000 layers.py:201(check)
              421491298  243.764    0.000  711.092    0.000 overrides.py:1070(has_torch_function)
              260180700  442.236    0.000  707.608    0.000 layers.py:225(check)
              260180700  441.610    0.000  703.345    0.000 layers.py:213(check)
               46832526  686.527    0.000  686.527    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2601807  397.518    0.000  669.931    0.000 collector.py:53(collect)
             2047909256  547.668    0.000  666.134    0.000 layers.py:563(<genexpr>)
               46832526  625.500    0.000  625.500    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5203614    6.919    0.000  622.756    0.000 game.py:35(board)
               13010579   74.364    0.000  573.425    0.000 tensor.py:21(wrapped)
               46832526  566.360    0.000  566.360    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               46832526  512.371    0.000  512.371    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                5202746  175.434    0.000  494.024    0.000 exploration.py:53(softmaxer)
               20122062   15.570    0.000  434.219    0.000 level.py:38(elementsIn)
             4187556077  401.844    0.000  401.844    0.000 layer.py:85(positions)
               46832526  394.227    0.000  394.227    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              840197715  327.359    0.000  327.359    0.000 layer.py:142(elements)
              260180700  210.692    0.000  324.729    0.000 layers.py:190(check)
                5203614    7.984    0.000  315.784    0.000 loss.py:445(forward)
             4307807449  315.715    0.000  315.715    0.000 {built-in method builtins.hash}
                5203614   28.881    0.000  307.800    0.000 functional.py:2637(mse_loss)
               33820887  304.652    0.000  304.652    0.000 {method 't' of 'torch._C._TensorBase' objects}
               29345001   25.643    0.000  297.232    0.000 layer.py:64(restart)
               20122062  136.676    0.000  275.045    0.000 level.py:39(<listcomp>)
               15610842  269.024    0.000  269.024    0.000 {built-in method sum}
              889813542  206.887    0.000  258.952    0.000 overrides.py:1083(<genexpr>)
        2240305549/2240305547  170.572    0.000  253.174    0.000 {built-in method builtins.len}
              403964253  169.983    0.000  235.322    0.000 layer.py:126(add)
                4192243  113.675    0.000  226.846    0.000 layers.py:30(reset)
              966112015  219.533    0.000  219.533    0.000 level.py:32(inverse)
                7805421   40.895    0.000  205.928    0.000 tensor.py:506(__rsub__)
                5203614  194.879    0.000  194.879    0.000 {built-in method torch._C._nn.mse_loss}
                2601807   69.948    0.000  192.835    0.000 random.py:315(sample)
               26016334   19.996    0.000  192.065    0.000 flatten.py:39(forward)
                7805421  186.996    0.000  186.996    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              257931249  124.230    0.000  185.667    0.000 layer.py:122(remove)
                2602847  183.895    0.000  183.895    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               98346101  121.399    0.000  181.666    0.000 layers.py:107(isDone)
             1779303760  180.534    0.000  180.534    0.000 layer.py:199(isBlocking)
                5204394  175.209    0.000  175.209    0.000 {built-in method max}
               26016334  172.068    0.000  172.068    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9497198: <causal2_demo_1> in cluster <dcc> Done

Job <causal2_demo_1> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 21:09:35 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr  6 22:48:21 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr  6 22:48:21 2021
Terminated at Wed Apr  7 14:43:35 2021
Results reported at Wed Apr  7 14:43:35 2021

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

    CPU time :                                   57166.44 sec.
    Max Memory :                                 2809 MB
    Average Memory :                             2805.05 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13575.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57315 sec.
    Turnaround time :                            149640 sec.

The output (if any) is above this job summary.

