
# Parameters

    Name :                      Diamonds2_convert1-0
    Main :                      CFagent
    Level :                     Levels.Causal5
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Topn :                      2
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      65795962610 function calls (65504557631 primitive calls) in 86115.10 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.096 86115.096 {built-in method builtins.exec}
                      1    4.210    4.210 86115.096 86115.096 <string>:1(<module>)
                      1  346.567  346.567 86110.886 86110.886 main.py:80(CFagent)
                8954169   34.259    0.000 27105.447    0.003 agent.py:29(learn)
                8954159  679.048    0.000 22557.474    0.003 learner.py:42(Qlearn)
                2984723   14.263    0.000 16284.081    0.005 game.py:42(step)
                2984723   17.975    0.000 15560.016    0.005 layers.py:827(step)
        325635962/34232674 1312.379    0.000 12099.565    0.000 module.py:866(_call_impl)
               25278515   71.441    0.000 11375.482    0.000 network.py:28(forward)
               25278515  357.548    0.000 11142.809    0.000 container.py:117(forward)
                2984723  328.137    0.000 10467.067    0.004 agent.py:54(_learn)
                2984723 1185.814    0.000 9982.912    0.003 agent.py:212(counterfact)
                2984723  325.129    0.000 9687.734    0.003 agent.py:204(_learn)
                8954159   76.508    0.000 9514.959    0.001 optimizer.py:84(wrapper)
                8954159   36.472    0.000 9145.693    0.001 grad_mode.py:24(decorate_context)
                8954159  261.011    0.000 9023.620    0.001 adam.py:55(step)
                2984723  245.548    0.000 8953.077    0.003 layers.py:17(step)
              298401708  467.697    0.000 8680.436    0.000 layer.py:106(move)
                2984723 4611.520    0.002 8485.886    0.003 replaybuffer.py:28(teleporter_save_data)
                8954159 1860.316    0.000 8479.363    0.001 _functional.py:53(adam)
                2984723   93.427    0.000 6896.993    0.002 agent.py:117(_learn)
                2984724  415.964    0.000 6563.929    0.002 layers.py:793(update)
                2984723 4175.407    0.001 6351.681    0.002 agent.py:88(interveen)
                8161155  226.197    0.000 5957.482    0.001 agent.py:49(__call__)
                8954159   37.464    0.000 5657.172    0.001 tensor.py:195(backward)
                8954159   34.641    0.000 5618.320    0.001 __init__.py:68(backward)
              298401708 1133.883    0.000 5572.656    0.000 layers.py:844(check)
                8954159 5381.807    0.001 5381.807    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2984723 4276.052    0.001 5283.893    0.002 replaybuffer.py:67(sample_data)
                2984723 4211.989    0.001 5252.961    0.002 replaybuffer.py:22(sample_data)
               46926845 4680.822    0.000 4680.822    0.000 {built-in method tensor}
               40024262   27.508    0.000 4479.276    0.000 game.py:38(board)
               50557030  108.499    0.000 4016.318    0.000 conv.py:398(forward)
               50557030   63.542    0.000 3858.432    0.000 conv.py:390(_conv_forward)
               50557030 3794.889    0.000 3794.889    0.000 {built-in method conv2d}
              276705551 3517.639    0.000 3517.639    0.000 {built-in method clone}
               69866099  138.218    0.000 3257.839    0.000 linear.py:93(forward)
                2193765   48.932    0.000 3223.704    0.001 agent.py:176(choose_action)
               53725023 1761.471    0.000 3155.717    0.000 layer.py:175(NoRock_update)
               69866099   58.494    0.000 3052.092    0.000 functional.py:1737(linear)
               69866099 2979.269    0.000 2979.269    0.000 {built-in method torch._C._nn.linear}
                2984723 1812.725    0.001 2687.394    0.001 agent.py:67(modify)
                4998547   54.785    0.000 2575.170    0.001 layers.py:849(restart)
              298401708  509.188    0.000 2184.194    0.000 layers.py:838(isFree)
                4998547   24.558    0.000 2166.697    0.000 level.py:8(__init__)
                4998547   74.609    0.000 1917.344    0.000 levels.py:249(generate)
               40993058 1809.316    0.000 1809.316    0.000 {built-in method cat}
               95144614   72.939    0.000 1799.521    0.000 activation.py:713(forward)
                2984723 1320.431    0.000 1768.785    0.001 replaybuffer.py:73(CF_save_data)
               32489462  302.779    0.000 1768.367    0.000 level.py:41(notUsed)
              167144288 1739.368    0.000 1739.368    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               95144614   75.952    0.000 1726.582    0.000 functional.py:1364(leaky_relu)
             2633881917 1367.436    0.000 1675.007    0.000 layer.py:103(isFree)
               11145878   77.152    0.000 1639.972    0.000 agent.py:59(modify_board)
               95144614 1633.887    0.000 1633.887    0.000 {built-in method torch._C._nn.leaky_relu}
              167144288 1525.587    0.000 1525.587    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2984713   56.045    0.000 1517.035    0.001 agent.py:172(__call__)
             6362604871 1032.132    0.000 1485.398    0.000 enum.py:646(__hash__)
                2984723   51.821    0.000 1426.138    0.000 agent.py:112(__call__)
                8954159  209.297    0.000 1309.727    0.000 optimizer.py:189(zero_grad)
              296458577  264.489    0.000 1131.541    0.000 {built-in method builtins.any}
               11145878 1048.740    0.000 1048.740    0.000 {built-in method torch._C._nn.one_hot}
               83572144  949.870    0.000  949.870    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              290836142  875.824    0.000  875.824    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             2934738530  714.167    0.000  867.052    0.000 layers.py:809(<genexpr>)
               32489462   23.578    0.000  858.962    0.000 level.py:38(elementsIn)
                2984723   60.851    0.000  823.342    0.000 replaybuffer.py:18(stacker)
               83572144  817.616    0.000  817.616    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              298401708  516.894    0.000  814.754    0.000 layers.py:387(check)
                2984713   62.811    0.000  801.502    0.000 replaybuffer.py:63(stacker)
             1063484159  791.285    0.000  791.285    0.000 layer.py:154(elements)
               83572144  781.902    0.000  781.902    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               83572144  780.106    0.000  780.106    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              298401708  489.333    0.000  775.576    0.000 layers.py:337(check)
              298401708  473.539    0.000  773.130    0.000 layers.py:375(check)
              298401708  486.988    0.000  768.194    0.000 layers.py:349(check)
              298472400   93.177    0.000  699.802    0.000 {built-in method builtins.all}
             1067874648  266.145    0.000  640.795    0.000 layers.py:799(<genexpr>)
                2984723  373.831    0.000  620.547    0.000 collector.py:46(collect)
             6963956916  619.383    0.000  619.383    0.000 layer.py:99(positions)
                8161155  223.560    0.000  614.830    0.000 exploration.py:53(softmaxer)
               83572144  605.430    0.000  605.430    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               32489462  279.974    0.000  563.548    0.000 level.py:39(<listcomp>)
        7414294927/7414294924  481.540    0.000  539.586    0.000 {built-in method builtins.len}
                2193765  481.081    0.000  481.081    0.000 agent.py:187(convert_values)
              585005092  377.206    0.000  470.146    0.000 tensor.py:906(grad)
             6362638950  453.272    0.000  453.272    0.000 {built-in method builtins.hash}
                8954159   12.207    0.000  439.188    0.000 loss.py:527(forward)
                8954159   32.794    0.000  426.980    0.000 functional.py:2898(mse_loss)
                5969446  152.566    0.000  412.545    0.000 random.py:315(sample)
              298401708  257.557    0.000  387.096    0.000 layers.py:364(check)
              298401708  248.978    0.000  377.853    0.000 layers.py:326(check)
             1532318956  347.453    0.000  347.453    0.000 level.py:32(inverse)
               44986923   35.917    0.000  339.798    0.000 layer.py:77(restart)
              298401708  197.120    0.000  297.438    0.000 layers.py:23(check)
               50557030   33.715    0.000  294.981    0.000 flatten.py:39(forward)
                8954159  281.215    0.000  281.215    0.000 {built-in method torch._C._nn.mse_loss}
             1611986552  279.510    0.000  279.510    0.000 enum.py:352(<genexpr>)
               32489462  169.753    0.000  271.836    0.000 {built-in method _functools.reduce}
               17908338  264.318    0.000  264.318    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9678082: <Diamonds2_convert1_0> in cluster <dcc> Done

Job <Diamonds2_convert1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May 21 19:42:38 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri May 21 19:42:40 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri May 21 19:42:40 2021
Terminated at Sat May 22 19:38:02 2021
Results reported at Sat May 22 19:38:02 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85895.77 sec.
    Max Memory :                                 8640 MB
    Average Memory :                             5869.98 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7744.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86136 sec.
    Turnaround time :                            86124 sec.

The output (if any) is above this job summary.

