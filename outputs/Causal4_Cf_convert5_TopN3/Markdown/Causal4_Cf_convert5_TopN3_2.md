
# Parameters

    Name :                      Causal4_Cf_convert5_TopN3-2
    Main :                      CFagent
    Level :                     Levels.Causal4
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
    Cf convert :                5
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      81542721987 function calls (81181057188 primitive calls) in 86114.45 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.446 86114.446 {built-in method builtins.exec}
                      1    4.297    4.297 86114.446 86114.446 <string>:1(<module>)
                      1  393.154  393.154 86110.149 86110.149 main.py:79(CFagent)
               11802417   38.400    0.000 26715.289    0.002 agent.py:29(learn)
                3934139   17.591    0.000 22255.258    0.006 game.py:41(step)
               11802415  672.616    0.000 21723.497    0.002 learner.py:42(Qlearn)
                3934139   20.043    0.000 21383.016    0.005 layers.py:718(step)
                3934139  328.233    0.000 14459.052    0.004 layers.py:17(step)
              392888091 1035.082    0.000 14098.598    0.000 layer.py:98(move)
        404915495/43252387 1496.730    0.000 12273.433    0.000 module.py:866(_call_impl)
               31449972   83.589    0.000 11470.762    0.000 network.py:27(forward)
               31449972  369.216    0.000 11196.897    0.000 container.py:117(forward)
                3934139  867.581    0.000 10790.002    0.003 agent.py:210(counterfact)
                3934139  391.702    0.000 10390.592    0.003 agent.py:54(_learn)
                3934139  388.793    0.000 9528.891    0.002 agent.py:202(_learn)
              392888091 1688.618    0.000 8673.247    0.000 layers.py:735(check)
               11802415   92.686    0.000 8499.132    0.001 optimizer.py:84(wrapper)
               11802415   48.761    0.000 8086.022    0.001 grad_mode.py:24(decorate_context)
               11802415  324.083    0.000 7938.770    0.001 adam.py:55(step)
               11802415 1638.539    0.000 7241.300    0.001 _functional.py:53(adam)
                3934140  534.353    0.000 6873.347    0.002 layers.py:684(update)
                3934139  114.576    0.000 6734.866    0.002 agent.py:117(_learn)
                3934139 5209.560    0.001 6337.916    0.002 replaybuffer.py:22(sample_data)
               61792332 6159.676    0.000 6159.676    0.000 {built-in method tensor}
                3934139 4990.539    0.001 6080.016    0.002 replaybuffer.py:67(sample_data)
               52795937   31.653    0.000 5957.424    0.000 game.py:37(board)
                9808451  232.532    0.000 5858.242    0.001 agent.py:49(__call__)
               11802415   42.419    0.000 5597.170    0.000 tensor.py:195(backward)
               11802415   41.359    0.000 5553.153    0.000 __init__.py:68(backward)
               11802415 5297.907    0.000 5297.907    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               78682790 2726.625    0.000 4698.111    0.000 layer.py:151(update)
               62899944  127.901    0.000 4156.702    0.000 conv.py:398(forward)
               62899944   78.801    0.000 3967.845    0.000 conv.py:390(_conv_forward)
               62899944 3889.044    0.000 3889.044    0.000 {built-in method conv2d}
                3934139 1561.883    0.000 3880.853    0.001 agent.py:88(interveen)
              392888091  687.071    0.000 3688.314    0.000 layers.py:729(isFree)
               86481638  160.634    0.000 3160.930    0.000 linear.py:93(forward)
                3934139 1715.669    0.000 3027.526    0.001 replaybuffer.py:28(teleporter_save_data)
             3713884411 2465.422    0.000 3001.243    0.000 layer.py:95(isFree)
               86481638   65.620    0.000 2916.968    0.000 functional.py:1737(linear)
               86481638 2835.585    0.000 2835.585    0.000 {built-in method torch._C._nn.linear}
                3934139 1754.482    0.000 2670.098    0.001 agent.py:67(modify)
                1970830   38.080    0.000 2398.566    0.001 agent.py:175(choose_action)
             7667288919 1315.966    0.000 1888.115    0.000 enum.py:646(__hash__)
               53083970 1840.676    0.000 1840.676    0.000 {built-in method cat}
              117931610   89.313    0.000 1680.427    0.000 activation.py:713(forward)
               13742590   83.811    0.000 1671.309    0.000 agent.py:59(modify_board)
                3934137   62.808    0.000 1630.840    0.000 agent.py:171(__call__)
              393732701  376.486    0.000 1617.018    0.000 {built-in method builtins.any}
              117931610   89.875    0.000 1591.113    0.000 functional.py:1364(leaky_relu)
                3934139   58.112    0.000 1547.014    0.000 agent.py:112(__call__)
              117931610 1483.549    0.000 1483.549    0.000 {built-in method torch._C._nn.leaky_relu}
              220311744 1427.400    0.000 1427.400    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              392888091 1049.384    0.000 1393.327    0.000 layers.py:77(check)
              142356808 1334.727    0.000 1334.727    0.000 {built-in method clone}
              220311744 1272.711    0.000 1272.711    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11802415  220.109    0.000 1257.043    0.000 optimizer.py:189(zero_grad)
             4287784171 1012.553    0.000 1240.531    0.000 layers.py:700(<genexpr>)
                3615439   40.168    0.000 1239.907    0.000 layers.py:740(restart)
                3934139  966.911    0.000 1215.649    0.000 replaybuffer.py:73(CF_save_data)
              392888091  774.901    0.000 1211.169    0.000 layers.py:246(check)
              392888091  674.919    0.000 1111.176    0.000 layers.py:286(check)
               13742590 1098.891    0.000 1098.891    0.000 {built-in method torch._C._nn.one_hot}
             1266160635 1098.507    0.000 1098.507    0.000 layer.py:146(elements)
                3615439   19.932    0.000  876.176    0.000 level.py:8(__init__)
                3934139   66.927    0.000  857.891    0.000 replaybuffer.py:18(stacker)
            10235313863  857.869    0.000  857.869    0.000 layer.py:91(positions)
              393414000   70.273    0.000  837.424    0.000 {built-in method builtins.all}
              110155872  833.600    0.000  833.600    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3934137   67.670    0.000  826.437    0.000 replaybuffer.py:63(stacker)
              798269861  160.308    0.000  814.391    0.000 layers.py:690(<genexpr>)
              392888091  598.852    0.000  775.993    0.000 layers.py:62(check)
              110155872  713.550    0.000  713.550    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        10447401917/10447401914  636.789    0.000  705.746    0.000 {built-in method builtins.len}
                3615439  115.519    0.000  702.696    0.000 levels.py:199(generate)
              110155872  666.102    0.000  666.102    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              110155872  662.303    0.000  662.303    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              393414000  437.506    0.000  650.558    0.000 layers.py:113(isDone)
              392888091  408.137    0.000  633.036    0.000 layers.py:273(check)
              771091188  478.541    0.000  592.748    0.000 tensor.py:906(grad)
              392888091  364.392    0.000  587.729    0.000 layers.py:313(check)
                9808451  215.822    0.000  577.434    0.000 exploration.py:53(softmaxer)
               15099156  219.405    0.000  573.514    0.000 random.py:315(sample)
             7667333638  572.157    0.000  572.157    0.000 {built-in method builtins.hash}
                3934139  329.506    0.000  559.248    0.000 collector.py:46(collect)
              392888091  349.096    0.000  517.589    0.000 layers.py:48(check)
              110155872  502.180    0.000  502.180    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7230878   55.738    0.000  477.185    0.000 level.py:41(notUsed)
               11802415   15.434    0.000  472.264    0.000 loss.py:527(forward)
               11802415   43.064    0.000  456.829    0.000 functional.py:2898(mse_loss)
              392888091  272.907    0.000  397.700    0.000 layers.py:23(check)
                1970830  362.205    0.000  384.625    0.000 agent.py:186(convert_values)
             4337075266  323.255    0.000  323.255    0.000 {method 'random' of '_random.Random' objects}
               36154390   46.529    0.000  312.631    0.000 layer.py:69(restart)
              160033535  305.667    0.000  305.667    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              337667481  215.421    0.000  299.443    0.000 layer.py:126(remove)
              555102647  212.267    0.000  289.871    0.000 layer.py:130(add)
             2933026811  287.835    0.000  287.835    0.000 layer.py:203(isBlocking)
                7868280  282.382    0.000  282.382    0.000 {built-in method nonzero}
               11802415  280.836    0.000  280.836    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551823: <Causal4_Cf_convert5_TopN3_2> in cluster <dcc> Done

Job <Causal4_Cf_convert5_TopN3_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:32 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 23 07:02:23 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 07:02:23 2021
Terminated at Sat Apr 24 06:57:45 2021
Results reported at Sat Apr 24 06:57:45 2021

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

    CPU time :                                   85907.35 sec.
    Max Memory :                                 10808 MB
    Average Memory :                             7060.06 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5576.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86122 sec.
    Turnaround time :                            272233 sec.

The output (if any) is above this job summary.

