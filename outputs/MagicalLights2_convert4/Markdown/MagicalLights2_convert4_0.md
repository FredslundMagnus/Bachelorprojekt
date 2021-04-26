
# Parameters

    Name :                      MagicalLights2_convert4-0
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      1
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69863221554 function calls (69553686899 primitive calls) in 86113.49 seconds

##    Ordered by: cumulative time
   List reduced from 515 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.485 86113.485 {built-in method builtins.exec}
                      1    4.187    4.187 86113.485 86113.485 <string>:1(<module>)
                      1  327.052  327.052 86109.298 86109.298 main.py:79(CFagent)
               10027740   34.816    0.000 29548.652    0.003 agent.py:29(learn)
               10027739  721.722    0.000 24759.074    0.002 learner.py:42(Qlearn)
                3342580   14.056    0.000 19332.108    0.006 game.py:41(step)
                3342580   18.367    0.000 18517.546    0.006 layers.py:718(step)
        346469310/36936346 1359.537    0.000 12385.816    0.000 module.py:866(_call_impl)
                3342580  290.352    0.000 12262.379    0.004 layers.py:17(step)
              333165328  868.524    0.000 11945.495    0.000 layer.py:98(move)
               26908607   73.204    0.000 11610.455    0.000 network.py:27(forward)
               26908607  362.087    0.000 11374.178    0.000 container.py:117(forward)
                3342580  315.872    0.000 11373.200    0.003 agent.py:54(_learn)
                3342580  313.413    0.000 10542.172    0.003 agent.py:202(_learn)
               10027739   83.329    0.000 10522.030    0.001 optimizer.py:84(wrapper)
                3342580 1020.638    0.000 10402.393    0.003 agent.py:210(counterfact)
               10027739   42.423    0.000 10109.507    0.001 grad_mode.py:24(decorate_context)
               10027739  288.561    0.000 9975.427    0.001 adam.py:55(step)
               10027739 2028.560    0.000 9368.897    0.001 _functional.py:53(adam)
                3342580   89.262    0.000 7575.125    0.002 agent.py:117(_learn)
              333165328 1476.812    0.000 7402.266    0.000 layers.py:735(check)
               10027739   50.843    0.000 6279.720    0.001 tensor.py:195(backward)
               10027739   38.424    0.000 6227.456    0.001 __init__.py:68(backward)
                3342581  463.986    0.000 6210.594    0.002 layers.py:684(update)
               10027739 5969.128    0.001 5969.128    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8432201  192.588    0.000 5921.747    0.001 agent.py:49(__call__)
                3342580 4754.316    0.001 5779.091    0.002 replaybuffer.py:22(sample_data)
                3342580 4709.053    0.001 5720.756    0.002 replaybuffer.py:67(sample_data)
               53124248 5581.483    0.000 5581.483    0.000 {built-in method tensor}
               45431216   28.464    0.000 5360.862    0.000 game.py:37(board)
                3342580 1905.814    0.001 4236.532    0.001 agent.py:88(interveen)
               53817214  114.361    0.000 4106.048    0.000 conv.py:398(forward)
               66851610 2317.652    0.000 4013.672    0.000 layer.py:151(update)
               53817214   71.687    0.000 3939.524    0.000 conv.py:390(_conv_forward)
               53817214 3867.837    0.000 3867.837    0.000 {built-in method conv2d}
                3342580 1945.469    0.001 3659.980    0.001 replaybuffer.py:28(teleporter_save_data)
               74040661  147.614    0.000 3320.875    0.000 linear.py:93(forward)
               74040661   59.443    0.000 3101.655    0.000 functional.py:1737(linear)
              333165328  579.331    0.000 3085.496    0.000 layers.py:729(isFree)
               74040661 3026.805    0.000 3026.805    0.000 {built-in method torch._C._nn.linear}
                3342580 1900.287    0.001 2865.252    0.001 agent.py:67(modify)
                1763508   39.639    0.000 2666.590    0.002 agent.py:175(choose_action)
             2878920993 2051.764    0.000 2506.165    0.000 layer.py:95(isFree)
              187184460 1926.625    0.000 1926.625    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              100949268   74.546    0.000 1812.041    0.000 activation.py:713(forward)
               45200576 1773.913    0.000 1773.913    0.000 {built-in method cat}
              100949268   83.192    0.000 1737.494    0.000 functional.py:1364(leaky_relu)
              130266330 1710.041    0.000 1710.041    0.000 {built-in method clone}
               11774781   82.680    0.000 1699.564    0.000 agent.py:59(modify_board)
              187184460 1682.141    0.000 1682.141    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              100949268 1636.373    0.000 1636.373    0.000 {built-in method torch._C._nn.leaky_relu}
                3342579   52.237    0.000 1624.619    0.000 agent.py:171(__call__)
             6583101625 1099.489    0.000 1564.135    0.000 enum.py:646(__hash__)
                3342580   52.038    0.000 1532.066    0.000 agent.py:112(__call__)
               10027739  232.489    0.000 1456.533    0.000 optimizer.py:189(zero_grad)
                3342580 1106.874    0.000 1439.104    0.000 replaybuffer.py:73(CF_save_data)
              334043933  319.431    0.000 1380.207    0.000 {built-in method builtins.any}
                3556748   41.724    0.000 1224.363    0.000 layers.py:740(restart)
              333165328  891.173    0.000 1177.529    0.000 layers.py:77(check)
              333165328  717.027    0.000 1096.260    0.000 layers.py:246(check)
               11774781 1084.254    0.000 1084.254    0.000 {built-in method torch._C._nn.one_hot}
               93592230 1081.206    0.000 1081.206    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             3637714872  867.747    0.000 1060.776    0.000 layers.py:700(<genexpr>)
             1126482273  947.065    0.000  947.065    0.000 layer.py:146(elements)
              333165328  570.656    0.000  927.383    0.000 layers.py:286(check)
               93592230  895.424    0.000  895.424    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               93592230  870.349    0.000  870.349    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              334258100   86.962    0.000  868.084    0.000 {built-in method builtins.all}
                3556748   18.853    0.000  866.284    0.000 level.py:8(__init__)
               93592230  857.149    0.000  857.149    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1031023536  239.436    0.000  820.153    0.000 layers.py:690(<genexpr>)
                3342580   59.132    0.000  795.619    0.000 replaybuffer.py:18(stacker)
                3342579   59.279    0.000  785.415    0.000 replaybuffer.py:63(stacker)
             8613040801  723.818    0.000  723.818    0.000 layer.py:91(positions)
                3556748  112.821    0.000  688.408    0.000 levels.py:199(generate)
                3342580  408.104    0.000  677.266    0.000 collector.py:46(collect)
               93592230  669.894    0.000  669.894    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              333165328  515.085    0.000  656.725    0.000 layers.py:62(check)
        8893551951/8893551948  560.114    0.000  623.813    0.000 {built-in method builtins.len}
                8432201  220.974    0.000  617.011    0.000 exploration.py:53(softmaxer)
              334258100  373.961    0.000  553.670    0.000 layers.py:113(isDone)
                1763508  446.180    0.000  532.407    0.000 agent.py:186(convert_values)
              655145694  425.880    0.000  529.862    0.000 tensor.py:906(grad)
              333165328  342.034    0.000  525.679    0.000 layers.py:313(check)
               13798656  187.666    0.000  494.876    0.000 random.py:315(sample)
              333165328  313.257    0.000  494.031    0.000 layers.py:273(check)
               10027739   14.230    0.000  478.925    0.000 loss.py:527(forward)
                7113496   54.615    0.000  468.413    0.000 level.py:41(notUsed)
               10027739   35.063    0.000  464.695    0.000 functional.py:2898(mse_loss)
             6583139736  464.652    0.000  464.652    0.000 {built-in method builtins.hash}
              145383690  439.974    0.000  439.974    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              333165328  281.753    0.000  416.953    0.000 layers.py:48(check)
              333165328  227.290    0.000  331.677    0.000 layers.py:23(check)
               10027739  308.384    0.000  308.384    0.000 {built-in method torch._C._nn.mse_loss}
               35567480   44.786    0.000  305.454    0.000 layer.py:69(restart)
               53817214   36.214    0.000  302.858    0.000 flatten.py:39(forward)
               20055480  287.704    0.000  287.704    0.000 {built-in method sum}
                6685162  285.863    0.000  285.863    0.000 {built-in method nonzero}
              281415131  208.193    0.000  281.463    0.000 layer.py:126(remove)
             2353329850  273.041    0.000  273.041    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9571371: <MagicalLights2_convert4_0> in cluster <dcc> Done

Job <MagicalLights2_convert4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 24 18:36:26 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 24 18:45:31 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 18:45:31 2021
Terminated at Sun Apr 25 18:40:50 2021
Results reported at Sun Apr 25 18:40:50 2021

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

    CPU time :                                   86096.20 sec.
    Max Memory :                                 3456 MB
    Average Memory :                             3447.92 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12928.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            86664 sec.

The output (if any) is above this job summary.

