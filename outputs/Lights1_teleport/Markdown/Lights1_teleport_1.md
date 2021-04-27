
# Parameters

    Name :                      Lights1_teleport-1
    Main :                      teleport
    Level :                     Levels.Causal3
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


      87673212606 function calls (87376999943 primitive calls) in 86104.44 seconds

##    Ordered by: cumulative time
   List reduced from 478 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86104.439 86104.439 {built-in method builtins.exec}
                      1    1.481    1.481 86104.439 86104.439 <string>:1(<module>)
                      1  217.563  217.563 86102.958 86102.958 main.py:45(teleport)
               10583434   37.954    0.000 29620.983    0.003 agent.py:29(learn)
                5291717   19.752    0.000 25828.011    0.005 game.py:41(step)
               10583434  711.261    0.000 24999.189    0.002 learner.py:42(Qlearn)
                5291717   25.938    0.000 24680.375    0.005 layers.py:718(step)
                5291717  168.778    0.000 17886.470    0.003 agent.py:54(_learn)
                5291717  446.669    0.000 15353.440    0.003 layers.py:17(step)
              529171700  887.343    0.000 14859.801    0.000 layer.py:98(move)
        333243296/37031644 1276.644    0.000 12247.470    0.000 module.py:715(_call_impl)
                5291717  140.197    0.000 11676.685    0.002 agent.py:117(_learn)
               26448210   68.001    0.000 11430.125    0.000 network.py:27(forward)
               26448210  309.391    0.000 11194.420    0.000 container.py:115(forward)
               10583434   65.234    0.000 10140.116    0.001 grad_mode.py:23(decorate_context)
               10583434  344.388    0.000 9957.741    0.001 adam.py:55(step)
                5291718  761.089    0.000 9265.765    0.002 layers.py:684(update)
              529171700 1922.616    0.000 9058.583    0.000 layers.py:735(check)
               10583434 1863.683    0.000 8205.225    0.001 functional.py:53(adam)
                5291717 4202.424    0.001 7762.160    0.001 replaybuffer.py:28(teleporter_save_data)
                5291717 3982.869    0.001 7718.821    0.001 agent.py:88(interveen)
               10573059  224.025    0.000 7537.559    0.001 agent.py:49(__call__)
                5291717 3842.056    0.001 6126.189    0.001 replaybuffer.py:22(sample_data)
               10583434   61.051    0.000 5761.617    0.001 tensor.py:181(backward)
               10583434   36.273    0.000 5700.566    0.001 __init__.py:68(backward)
               10583434 5424.535    0.001 5424.535    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5291717 2565.752    0.000 4897.886    0.001 agent.py:67(modify)
              529171700  888.567    0.000 4124.565    0.000 layers.py:729(isFree)
               52896420   85.948    0.000 4095.131    0.000 conv.py:422(forward)
               52896420   99.355    0.000 3975.147    0.000 conv.py:414(_conv_forward)
               52896420 3857.929    0.000 3857.929    0.000 {built-in method conv2d}
               68761196  148.118    0.000 3611.592    0.000 linear.py:92(forward)
               68761196  261.371    0.000 3396.404    0.000 functional.py:1669(linear)
             4008226436 2571.033    0.000 3235.998    0.000 layer.py:95(isFree)
             1479794834  836.432    0.000 2929.760    0.000 {built-in method builtins.any}
              266070274 2857.456    0.000 2857.456    0.000 {built-in method clone}
               42333744 1548.443    0.000 2721.330    0.000 layer.py:167(NoRock_update)
              666756396 1502.466    0.000 2514.752    0.000 tensor.py:933(grad)
               68761196 2401.141    0.000 2401.141    0.000 {built-in method addmm}
                5291717   64.136    0.000 2375.148    0.000 agent.py:112(__call__)
               42323361 2300.918    0.000 2300.918    0.000 {built-in method cat}
                7117413   72.079    0.000 2286.585    0.000 layers.py:740(restart)
               15864776  109.199    0.000 2279.143    0.000 agent.py:59(modify_board)
               10583434  229.125    0.000 2236.989    0.000 optimizer.py:167(zero_grad)
             8143245713 1512.701    0.000 2176.965    0.000 enum.py:646(__hash__)
                5291717   83.663    0.000 1904.677    0.000 replaybuffer.py:18(stacker)
              529171700 1104.471    0.000 1801.080    0.000 layers.py:246(check)
              529171700 1045.726    0.000 1757.967    0.000 layers.py:286(check)
              190501812 1638.200    0.000 1638.200    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                7117413   34.499    0.000 1626.876    0.000 level.py:8(__init__)
               22564468 1610.527    0.000 1610.527    0.000 {built-in method tensor}
             4698489483 1311.588    0.000 1578.154    0.000 layers.py:700(<genexpr>)
               95209406   82.289    0.000 1575.869    0.000 activation.py:713(forward)
               95209406  130.526    0.000 1493.580    0.000 functional.py:1292(leaky_relu)
               15864776 1460.986    0.000 1460.986    0.000 {built-in method torch._C._nn.one_hot}
              867812382  453.098    0.000 1381.770    0.000 overrides.py:1070(has_torch_function)
              190501812 1373.188    0.000 1373.188    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               95209406 1351.233    0.000 1351.233    0.000 {built-in method torch._C._nn.leaky_relu}
              566216651  154.101    0.000 1279.570    0.000 {built-in method builtins.all}
               37044851  189.398    0.000 1271.344    0.000 tensor.py:21(wrapped)
               10583434   12.582    0.000 1270.299    0.000 game.py:37(board)
                7117413  147.732    0.000 1266.050    0.000 levels.py:164(generate)
             1092356099  250.102    0.000 1168.668    0.000 layers.py:690(<genexpr>)
               95250906  964.995    0.000  964.995    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5291717  555.036    0.000  953.715    0.000 collector.py:46(collect)
            10286363233  950.085    0.000  950.085    0.000 layer.py:91(positions)
               14234826  130.805    0.000  916.911    0.000 level.py:41(notUsed)
              529171800  600.782    0.000  913.530    0.000 layers.py:113(isDone)
              529171700  576.985    0.000  909.758    0.000 layers.py:313(check)
               95250906  875.715    0.000  875.715    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              529171700  548.740    0.000  865.230    0.000 layers.py:273(check)
              281935050  846.610    0.000  846.610    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               10573059  292.265    0.000  783.277    0.000 exploration.py:53(softmaxer)
               95250906  782.497    0.000  782.497    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              529171700  492.904    0.000  756.884    0.000 layers.py:48(check)
             1810744699  700.716    0.000  700.716    0.000 layer.py:146(elements)
               95250906  681.292    0.000  681.292    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             8143284200  664.271    0.000  664.271    0.000 {built-in method builtins.hash}
              529171700  401.633    0.000  590.516    0.000 layers.py:23(check)
        6125464762/6125464760  441.477    0.000  586.230    0.000 {built-in method builtins.len}
               56939304   68.859    0.000  567.653    0.000 layer.py:69(restart)
               95250906  539.719    0.000  539.719    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10583434   15.114    0.000  525.361    0.000 loss.py:445(forward)
               19526543  195.002    0.000  512.001    0.000 random.py:315(sample)
               10583434   57.911    0.000  510.248    0.000 functional.py:2637(mse_loss)
             1841429754  409.321    0.000  507.692    0.000 overrides.py:1083(<genexpr>)
              866045710  354.480    0.000  483.494    0.000 layer.py:130(add)
               26458585  479.772    0.000  479.772    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               68761196  428.203    0.000  428.203    0.000 {method 't' of 'torch._C._TensorBase' objects}
             4800578813  408.943    0.000  408.943    0.000 {method 'random' of '_random.Random' objects}
               31750302  384.292    0.000  384.292    0.000 {built-in method sum}
              503864272  252.562    0.000  379.024    0.000 layer.py:126(remove)
               14234826   13.980    0.000  369.047    0.000 level.py:38(elementsIn)
                7117513  183.456    0.000  363.528    0.000 layers.py:36(reset)
             3019665164  347.785    0.000  347.785    0.000 layer.py:203(isBlocking)
                5293831  330.086    0.000  330.086    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
              466934188  311.156    0.000  311.156    0.000 level.py:32(inverse)
                7117413  184.954    0.000  305.148    0.000 level.py:16(<dictcomp>)
              437238175  207.093    0.000  301.553    0.000 random.py:250(_randbelow_with_getrandbits)
               10583434  300.139    0.000  300.139    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550890: <Lights1_teleport_1> in cluster <dcc> Done

Job <Lights1_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:47 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 21 06:38:32 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 06:38:32 2021
Terminated at Thu Apr 22 06:33:40 2021
Results reported at Thu Apr 22 06:33:40 2021

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

    CPU time :                                   85899.01 sec.
    Max Memory :                                 2689 MB
    Average Memory :                             2686.24 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13695.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86108 sec.
    Turnaround time :                            137513 sec.

The output (if any) is above this job summary.

