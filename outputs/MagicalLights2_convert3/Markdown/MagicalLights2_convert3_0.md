
# Parameters

    Name :                      MagicalLights2_convert3-0
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      1
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67881980012 function calls (67583280181 primitive calls) in 86116.17 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.168 86116.168 {built-in method builtins.exec}
                      1    4.289    4.289 86116.168 86116.168 <string>:1(<module>)
                      1  347.399  347.399 86111.879 86111.879 main.py:79(CFagent)
                9636582   34.627    0.000 28786.968    0.003 agent.py:29(learn)
                9636582  719.510    0.000 23981.148    0.002 learner.py:42(Qlearn)
                3212194   14.361    0.000 18844.931    0.006 game.py:41(step)
                3212194   19.433    0.000 18046.773    0.006 layers.py:718(step)
        334296965/35598825 1366.992    0.000 12330.332    0.000 module.py:866(_call_impl)
                3212194  265.268    0.000 11945.815    0.004 layers.py:17(step)
              319101502  836.445    0.000 11653.945    0.000 layer.py:98(move)
               25962243   72.185    0.000 11558.858    0.000 network.py:27(forward)
               25962243  362.252    0.000 11324.447    0.000 container.py:117(forward)
                3212194  335.127    0.000 11110.784    0.003 agent.py:54(_learn)
                3212194  333.421    0.000 10290.023    0.003 agent.py:202(_learn)
                3212194 1005.296    0.000 10221.134    0.003 agent.py:210(counterfact)
                9636582   82.353    0.000 10156.546    0.001 optimizer.py:84(wrapper)
                9636582   40.131    0.000 9767.331    0.001 grad_mode.py:24(decorate_context)
                9636582  282.874    0.000 9635.548    0.001 adam.py:55(step)
                9636582 1978.156    0.000 9040.005    0.001 _functional.py:53(adam)
                3212194   96.856    0.000 7329.910    0.002 agent.py:117(_learn)
              319101502 1411.013    0.000 7135.508    0.000 layers.py:735(check)
                3212195  449.929    0.000 6055.834    0.002 layers.py:684(update)
                9636582   41.924    0.000 5958.323    0.001 tensor.py:195(backward)
                9636582   37.841    0.000 5914.981    0.001 __init__.py:68(backward)
                8159814  219.766    0.000 5896.226    0.001 agent.py:49(__call__)
                9636582 5661.090    0.001 5661.090    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3212194 4534.904    0.001 5579.524    0.002 replaybuffer.py:22(sample_data)
               51153665 5450.916    0.000 5450.916    0.000 {built-in method tensor}
                3212194 4419.186    0.001 5434.938    0.002 replaybuffer.py:67(sample_data)
               43748008   29.272    0.000 5237.142    0.000 game.py:37(board)
                3212194 2710.204    0.001 5078.467    0.002 replaybuffer.py:28(teleporter_save_data)
                3212194 2571.750    0.001 4886.628    0.002 agent.py:88(interveen)
               51924486  112.139    0.000 4075.907    0.000 conv.py:398(forward)
               64243890 2325.481    0.000 3957.689    0.000 layer.py:151(update)
               51924486   68.858    0.000 3912.721    0.000 conv.py:390(_conv_forward)
               51924486 3843.863    0.000 3843.863    0.000 {built-in method conv2d}
               71462341  140.564    0.000 3293.653    0.000 linear.py:93(forward)
              319101502  614.476    0.000 3112.662    0.000 layers.py:729(isFree)
               71462341   58.891    0.000 3085.363    0.000 functional.py:1737(linear)
               71462341 3011.549    0.000 3011.549    0.000 {built-in method torch._C._nn.linear}
                3212194 1836.865    0.001 2773.429    0.001 agent.py:67(modify)
                1741459   40.862    0.000 2607.231    0.001 agent.py:175(choose_action)
             3025059755 2054.448    0.000 2498.187    0.000 layer.py:95(isFree)
              170617463 2222.510    0.000 2222.510    0.000 {built-in method clone}
              179882864 1856.483    0.000 1856.483    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               97424584   76.986    0.000 1827.023    0.000 activation.py:713(forward)
               43493948 1807.862    0.000 1807.862    0.000 {built-in method cat}
               97424584   80.397    0.000 1750.037    0.000 functional.py:1364(leaky_relu)
               11372008   77.918    0.000 1654.808    0.000 agent.py:59(modify_board)
               97424584 1652.284    0.000 1652.284    0.000 {built-in method torch._C._nn.leaky_relu}
              179882864 1635.638    0.000 1635.638    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3212194   56.879    0.000 1619.310    0.001 agent.py:171(__call__)
             6317855213 1062.905    0.000 1533.980    0.000 enum.py:646(__hash__)
                3212194   54.651    0.000 1515.793    0.000 agent.py:112(__call__)
                9636582  226.221    0.000 1411.515    0.000 optimizer.py:189(zero_grad)
                3212194 1080.259    0.000 1406.842    0.000 replaybuffer.py:73(CF_save_data)
              320971474  307.482    0.000 1342.893    0.000 {built-in method builtins.any}
                3460221   40.986    0.000 1185.699    0.000 layers.py:740(restart)
              319101502  854.482    0.000 1130.230    0.000 layers.py:77(check)
              319101502  686.613    0.000 1057.865    0.000 layers.py:286(check)
               11372008 1054.199    0.000 1054.199    0.000 {built-in method torch._C._nn.one_hot}
             3495352069  852.229    0.000 1035.411    0.000 layers.py:700(<genexpr>)
               89941432 1011.432    0.000 1011.432    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1100168883  920.370    0.000  920.370    0.000 layer.py:146(elements)
              319101502  561.301    0.000  916.918    0.000 layers.py:246(check)
              321219500   89.250    0.000  872.816    0.000 {built-in method builtins.all}
               89941432  866.147    0.000  866.147    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89941432  839.183    0.000  839.183    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3460221   18.337    0.000  835.964    0.000 level.py:8(__init__)
               89941432  827.228    0.000  827.228    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3212194   59.364    0.000  821.873    0.000 replaybuffer.py:18(stacker)
             1050285625  254.036    0.000  821.790    0.000 layers.py:690(<genexpr>)
                3212194   61.257    0.000  799.770    0.000 replaybuffer.py:63(stacker)
             8308769836  705.379    0.000  705.379    0.000 layer.py:91(positions)
                3460221  110.038    0.000  675.066    0.000 levels.py:199(generate)
                3212194  398.489    0.000  658.789    0.000 collector.py:46(collect)
               89941432  644.939    0.000  644.939    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              319101502  496.195    0.000  633.555    0.000 layers.py:62(check)
                8159814  218.549    0.000  605.934    0.000 exploration.py:53(softmaxer)
        8462900074/8462900071  535.463    0.000  597.291    0.000 {built-in method builtins.len}
              185201665  567.230    0.000  567.230    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              321219500  358.936    0.000  533.979    0.000 layers.py:113(isDone)
              629590108  419.062    0.000  520.163    0.000 tensor.py:906(grad)
              319101502  309.741    0.000  490.213    0.000 layers.py:273(check)
               13344830  182.852    0.000  477.145    0.000 random.py:315(sample)
              319101502  301.854    0.000  476.191    0.000 layers.py:313(check)
             6317891868  471.081    0.000  471.081    0.000 {built-in method builtins.hash}
                9636582   13.806    0.000  467.413    0.000 loss.py:527(forward)
                6920442   53.802    0.000  460.445    0.000 level.py:41(notUsed)
                9636582   35.933    0.000  453.607    0.000 functional.py:2898(mse_loss)
                1741459  418.323    0.000  444.103    0.000 agent.py:186(convert_values)
              319101502  277.965    0.000  409.258    0.000 layers.py:48(check)
              319101502  218.667    0.000  323.296    0.000 layers.py:23(check)
               51924486   37.395    0.000  302.041    0.000 flatten.py:39(forward)
                9636582  299.856    0.000  299.856    0.000 {built-in method torch._C._nn.mse_loss}
               34602210   44.259    0.000  298.190    0.000 layer.py:69(restart)
              279152049  209.240    0.000  280.740    0.000 layer.py:126(remove)
               19273164  279.638    0.000  279.638    0.000 {built-in method sum}
                6424390  274.252    0.000  274.252    0.000 {built-in method nonzero}
                9637718  266.880    0.000  266.880    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9571368: <MagicalLights2_convert3_0> in cluster <dcc> Done

Job <MagicalLights2_convert3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 24 18:36:26 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 24 18:36:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 18:36:28 2021
Terminated at Sun Apr 25 18:31:56 2021
Results reported at Sun Apr 25 18:31:56 2021

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

    CPU time :                                   85901.73 sec.
    Max Memory :                                 9249 MB
    Average Memory :                             6226.92 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7135.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86183 sec.
    Turnaround time :                            86130 sec.

The output (if any) is above this job summary.

