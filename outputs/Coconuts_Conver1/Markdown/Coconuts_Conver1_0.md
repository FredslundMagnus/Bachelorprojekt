
# Parameters

    Name :                      Coconuts_Conver1-0
    Main :                      CFagent
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66823296120 function calls (66488749809 primitive calls) in 86123.69 seconds

##    Ordered by: cumulative time
   List reduced from 510 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86123.693 86123.693 {built-in method builtins.exec}
                      1    4.612    4.612 86123.693 86123.693 <string>:1(<module>)
                      1  424.599  424.599 86119.081 86119.081 main.py:79(CFagent)
               11250564   46.242    0.000 27761.071    0.002 agent.py:29(learn)
               11250558  704.393    0.000 22515.102    0.002 learner.py:42(Qlearn)
                3750188   17.385    0.000 20839.671    0.006 game.py:41(step)
                3750188   22.741    0.000 20054.818    0.005 layers.py:718(step)
                3750188  356.349    0.000 14079.460    0.004 layers.py:17(step)
              374830049 1368.364    0.000 13689.033    0.000 layer.py:98(move)
        374923959/40379339 1522.041    0.000 12292.876    0.000 module.py:866(_call_impl)
               29128781   78.880    0.000 11461.580    0.000 network.py:27(forward)
               29128781  369.538    0.000 11187.843    0.000 container.py:117(forward)
                3750188  421.137    0.000 10805.221    0.003 agent.py:54(_learn)
                3750188  415.020    0.000 9891.569    0.003 agent.py:204(_learn)
               11250558   95.800    0.000 8763.238    0.001 optimizer.py:84(wrapper)
               11250558   50.294    0.000 8335.236    0.001 grad_mode.py:24(decorate_context)
              374830049 1342.809    0.000 8309.198    0.000 layers.py:735(check)
               11250558  348.092    0.000 8176.203    0.001 adam.py:55(step)
                3750188 6399.582    0.002 7592.519    0.002 replaybuffer.py:22(sample_data)
               11250558 1696.359    0.000 7443.108    0.001 _functional.py:53(adam)
                3750188 6094.139    0.002 7233.191    0.002 replaybuffer.py:67(sample_data)
                3750188  548.493    0.000 7034.551    0.002 agent.py:212(counterfact)
                3750188  115.291    0.000 6990.574    0.002 agent.py:117(_learn)
                3750189  537.964    0.000 5917.658    0.002 layers.py:684(update)
               11250558   45.328    0.000 5887.942    0.001 tensor.py:195(backward)
               11250558   47.338    0.000 5841.090    0.001 __init__.py:68(backward)
                8931942  241.733    0.000 5825.219    0.001 agent.py:49(__call__)
               11250558 5569.106    0.000 5569.106    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3750188 2148.560    0.001 4557.142    0.001 agent.py:88(interveen)
                3750188 2434.422    0.001 4171.012    0.001 replaybuffer.py:28(teleporter_save_data)
               58257562  129.554    0.000 4143.217    0.000 conv.py:398(forward)
               58257562   83.957    0.000 3948.193    0.000 conv.py:390(_conv_forward)
               58257562 3864.237    0.000 3864.237    0.000 {built-in method conv2d}
               52502639 2220.610    0.000 3741.652    0.000 layer.py:151(update)
               45921790 3667.541    0.000 3667.541    0.000 {built-in method tensor}
               37330508   24.625    0.000 3446.726    0.000 game.py:37(board)
               79885967  166.141    0.000 3171.631    0.000 linear.py:93(forward)
              374830049  542.873    0.000 3075.102    0.000 layers.py:729(isFree)
               79885967   68.405    0.000 2917.226    0.000 functional.py:1737(linear)
               79885967 2832.237    0.000 2832.237    0.000 {built-in method torch._C._nn.linear}
                3750188 1814.817    0.000 2772.635    0.001 agent.py:67(modify)
              374830049 1836.658    0.000 2568.130    0.000 layers.py:471(check)
             2516697830 2158.373    0.000 2532.230    0.000 layer.py:95(isFree)
              374830049 1517.264    0.000 2112.176    0.000 layers.py:77(check)
               50183980 1908.043    0.000 1908.043    0.000 {built-in method cat}
                1445911   29.717    0.000 1875.419    0.001 agent.py:176(choose_action)
                3750182   68.699    0.000 1699.700    0.000 agent.py:172(__call__)
               12682130   85.031    0.000 1695.247    0.000 agent.py:59(modify_board)
              109014748   88.696    0.000 1657.248    0.000 activation.py:713(forward)
              162466611 1619.828    0.000 1619.828    0.000 {built-in method clone}
                3750188   63.923    0.000 1594.893    0.000 agent.py:112(__call__)
             6031791552 1091.155    0.000 1591.653    0.000 enum.py:646(__hash__)
                2132905   26.430    0.000 1572.823    0.001 layers.py:740(restart)
              109014748   87.210    0.000 1568.553    0.000 functional.py:1364(leaky_relu)
              109014748 1463.597    0.000 1463.597    0.000 {built-in method torch._C._nn.leaky_relu}
              210010408 1448.274    0.000 1448.274    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2132905   12.753    0.000 1324.534    0.001 level.py:8(__init__)
              210010408 1297.742    0.000 1297.742    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11250558  228.554    0.000 1290.739    0.000 optimizer.py:189(zero_grad)
              376636184  295.140    0.000 1221.358    0.000 {built-in method builtins.any}
                2132905   87.584    0.000 1203.585    0.001 levels.py:262(generate)
               12682130 1120.094    0.000 1120.094    0.000 {built-in method torch._C._nn.one_hot}
              374830049  827.584    0.000 1055.787    0.000 layers.py:62(check)
               19023891  179.314    0.000 1040.463    0.000 level.py:41(notUsed)
                3750188  839.234    0.000 1015.483    0.000 replaybuffer.py:73(CF_save_data)
             2983087960  759.304    0.000  926.218    0.000 layers.py:700(<genexpr>)
                3750188   74.072    0.000  906.390    0.000 replaybuffer.py:18(stacker)
             1127820197  881.720    0.000  881.720    0.000 layer.py:146(elements)
                3750182   75.590    0.000  863.611    0.000 replaybuffer.py:63(stacker)
              105005204  854.954    0.000  854.954    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              105005204  740.728    0.000  740.728    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             8047915730  740.417    0.000  740.417    0.000 layer.py:91(positions)
              105005204  691.406    0.000  691.406    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              105005204  685.149    0.000  685.149    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              735036512  488.060    0.000  605.548    0.000 tensor.py:906(grad)
        7570174149/7570174146  526.454    0.000  594.946    0.000 {built-in method builtins.len}
                8931942  214.385    0.000  591.042    0.000 exploration.py:53(softmaxer)
                3750188  335.656    0.000  570.161    0.000 collector.py:46(collect)
                7500376  210.749    0.000  548.130    0.000 random.py:315(sample)
              374830049  357.249    0.000  531.053    0.000 layers.py:48(check)
              105005204  518.614    0.000  518.614    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6031834255  500.506    0.000  500.506    0.000 {built-in method builtins.hash}
               11250558   19.135    0.000  495.197    0.000 loss.py:527(forward)
               11250558   46.107    0.000  476.062    0.000 functional.py:2898(mse_loss)
               19023891   19.099    0.000  461.626    0.000 level.py:38(elementsIn)
              374830049  289.352    0.000  422.641    0.000 layers.py:23(check)
              375018900   69.057    0.000  377.767    0.000 {built-in method builtins.all}
              178898923  369.346    0.000  369.346    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              388452435  231.582    0.000  355.808    0.000 layer.py:126(remove)
              782605634  172.986    0.000  355.533    0.000 layers.py:690(<genexpr>)
                7500378  299.880    0.000  299.880    0.000 {built-in method nonzero}
               19023891  144.531    0.000  293.418    0.000 level.py:39(<listcomp>)
               11250558  291.995    0.000  291.995    0.000 {built-in method torch._C._nn.mse_loss}
              512013111  214.569    0.000  290.026    0.000 layer.py:130(add)
                1445911  281.566    0.000  281.566    0.000 agent.py:187(convert_values)
               58257562   39.608    0.000  276.146    0.000 flatten.py:39(forward)
               11251826  268.741    0.000  268.741    0.000 {built-in method max}
              876818575  259.906    0.000  259.906    0.000 level.py:32(inverse)
             2516697830  252.450    0.000  252.450    0.000 layer.py:203(isBlocking)
               22501128  247.496    0.000  247.496    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579166: <Coconuts_Conver1_0> in cluster <dcc> Done

Job <Coconuts_Conver1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:06 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 29 10:27:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 10:27:05 2021
Terminated at Fri Apr 30 10:22:53 2021
Results reported at Fri Apr 30 10:22:53 2021

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

    CPU time :                                   85837.30 sec.
    Max Memory :                                 10248 MB
    Average Memory :                             6686.65 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6136.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86183 sec.
    Turnaround time :                            286727 sec.

The output (if any) is above this job summary.

