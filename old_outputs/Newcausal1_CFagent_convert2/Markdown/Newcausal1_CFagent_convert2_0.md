
# Parameters

    Name :                      Newcausal1_CFagent_convert2-0
    Main :                      CFagent
    Level :                     Levels.Causal1
    Hours :                     3.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        500000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                1
    Minutes used :              175 minutes.
    Hours used :                2 hours.

# Profiling


      6316311148 function calls (6269019277 primitive calls) in 10523.78 seconds

##    Ordered by: cumulative time
   List reduced from 484 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 10523.783 10523.783 {built-in method builtins.exec}
                      1    4.898    4.898 10523.783 10523.783 <string>:1(<module>)
                      1   35.522   35.522 10518.885 10518.885 main.py:96(CFagent)
                1441959    5.402    0.000 3499.880    0.002 agent.py:28(learn)
                1441951   88.861    0.000 2843.748    0.002 learner.py:42(Qlearn)
                 480653    2.328    0.000 1703.392    0.004 game.py:36(step)
        52833197/5543017  210.675    0.000 1689.706    0.000 module.py:866(_call_impl)
                 480653    2.930    0.000 1609.498    0.003 layers.py:594(step)
                4101066   10.362    0.000 1581.997    0.000 network.py:24(forward)
                4101066   51.227    0.000 1545.074    0.000 container.py:117(forward)
                 480653   52.765    0.000 1362.880    0.003 agent.py:53(_learn)
                 480653   52.154    0.000 1246.540    0.003 agent.py:189(_learn)
                 480653  193.786    0.000 1215.080    0.003 agent.py:197(counterfact)
                1441951   12.654    0.000 1101.963    0.001 optimizer.py:84(wrapper)
                 480653  642.438    0.001 1082.576    0.002 replaybuffer.py:28(teleporter_save_data)
                1441951    6.199    0.000 1048.688    0.001 grad_mode.py:24(decorate_context)
                1441951   44.299    0.000 1028.441    0.001 adam.py:55(step)
                1441951  216.405    0.000  934.934    0.001 _functional.py:53(adam)
                 480653   14.417    0.000  881.729    0.002 agent.py:114(_learn)
                1329422   35.089    0.000  841.604    0.001 agent.py:48(__call__)
                 480653   44.229    0.000  807.700    0.002 layers.py:18(step)
                 480654   53.552    0.000  794.233    0.002 layers.py:565(update)
                 480653  593.610    0.001  768.061    0.002 replaybuffer.py:22(sample_data)
                 480653  460.022    0.001  760.586    0.002 agent.py:85(interveen)
               48011879   61.252    0.000  759.275    0.000 layer.py:82(move)
                1441951    5.791    0.000  752.228    0.001 tensor.py:195(backward)
                1441951    5.784    0.000  746.218    0.001 __init__.py:68(backward)
                1441951  712.749    0.000  712.749    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 480653  438.781    0.001  592.466    0.001 replaybuffer.py:49(sample_data)
                8202132   18.487    0.000  570.140    0.000 conv.py:398(forward)
                8202132   10.903    0.000  542.905    0.000 conv.py:390(_conv_forward)
                8202132  532.001    0.000  532.001    0.000 {built-in method conv2d}
                6488536  471.978    0.000  471.978    0.000 {built-in method tensor}
                5396605    4.020    0.000  445.858    0.000 game.py:32(board)
               11341892   22.694    0.000  434.232    0.000 linear.py:93(forward)
               46011359  429.802    0.000  429.802    0.000 {built-in method clone}
                5767842  241.292    0.000  416.282    0.000 layer.py:143(NoRock_update)
               11341892    9.274    0.000  400.029    0.000 functional.py:1737(linear)
               11341892  388.356    0.000  388.356    0.000 {built-in method torch._C._nn.linear}
                 368395    3.398    0.000  383.101    0.001 agent.py:167(choose_action)
                1182987    9.800    0.000  362.364    0.000 layers.py:615(restart)
                 480653  204.176    0.000  330.566    0.001 agent.py:66(modify)
               48011879   59.228    0.000  327.038    0.000 layers.py:605(isFree)
               48011879   79.036    0.000  312.778    0.000 layers.py:611(check)
              264081984  224.665    0.000  267.809    0.000 layer.py:79(isFree)
                1182987    5.237    0.000  267.608    0.000 level.py:8(__init__)
                7097218  265.871    0.000  265.871    0.000 {built-in method cat}
                1810075   10.710    0.000  232.874    0.000 agent.py:58(modify_board)
               15442958   12.634    0.000  231.022    0.000 activation.py:713(forward)
                1182987   14.071    0.000  228.737    0.000 levels.py:122(generate)
               15442958   12.939    0.000  218.388    0.000 functional.py:1364(leaky_relu)
                 480645    8.572    0.000  212.225    0.000 agent.py:163(__call__)
               15442958  202.812    0.000  202.812    0.000 {built-in method torch._C._nn.leaky_relu}
                4613303   39.345    0.000  202.071    0.000 level.py:41(notUsed)
                 480653  101.767    0.000  201.034    0.000 replaybuffer.py:55(CF_save_data)
                 480653    8.225    0.000  200.634    0.000 agent.py:109(__call__)
               26916408  181.319    0.000  181.319    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               26916408  162.396    0.000  162.396    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1441951   29.232    0.000  161.461    0.000 optimizer.py:189(zero_grad)
                1810075  155.098    0.000  155.098    0.000 {built-in method torch._C._nn.one_hot}
                 480653   16.747    0.000  137.678    0.000 replaybuffer.py:18(stacker)
               48065400   14.554    0.000  135.105    0.000 {built-in method builtins.all}
              151296646   38.481    0.000  126.364    0.000 layers.py:571(<genexpr>)
                 480645   14.456    0.000  119.006    0.000 replaybuffer.py:45(stacker)
               13458204  106.659    0.000  106.659    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              406195441   72.624    0.000  103.503    0.000 enum.py:646(__hash__)
              186962348  101.513    0.000  101.513    0.000 layer.py:122(elements)
               13458204   94.599    0.000   94.599    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               48302079   93.821    0.000   93.821    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               48011879   58.015    0.000   89.090    0.000 layers.py:143(check)
                1329422   31.421    0.000   85.533    0.000 exploration.py:53(softmaxer)
               13458204   85.141    0.000   85.141    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13458204   84.500    0.000   84.500    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48065400   56.569    0.000   82.438    0.000 layers.py:111(isDone)
                7097922    8.124    0.000   82.419    0.000 layer.py:56(restart)
                4613303    3.534    0.000   79.381    0.000 level.py:38(elementsIn)
               94207512   61.886    0.000   76.884    0.000 tensor.py:906(grad)
                 480653   43.345    0.000   73.135    0.000 collector.py:54(collect)
                 961306   26.196    0.000   69.711    0.000 random.py:315(sample)
               48011879   45.495    0.000   67.319    0.000 layers.py:47(check)
        816821553/816821550   57.913    0.000   67.019    0.000 {built-in method builtins.len}
               48011879   42.318    0.000   65.093    0.000 layers.py:124(check)
               13458204   63.301    0.000   63.301    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1441951    2.127    0.000   62.831    0.000 loss.py:527(forward)
                1183087   30.933    0.000   61.794    0.000 layers.py:33(reset)
                1441951    5.623    0.000   60.705    0.000 functional.py:2898(mse_loss)
              212801231   58.628    0.000   58.628    0.000 level.py:32(inverse)
                1441960   58.351    0.000   58.351    0.000 {built-in method nonzero}
              541779285   49.565    0.000   49.565    0.000 layer.py:75(positions)
               88216209   35.672    0.000   49.322    0.000 layer.py:106(add)
                4613303   24.472    0.000   49.174    0.000 level.py:39(<listcomp>)
               43974904   31.857    0.000   44.076    0.000 layer.py:102(remove)
                8202132    5.685    0.000   37.832    0.000 flatten.py:39(forward)
                1441951   37.472    0.000   37.472    0.000 {built-in method torch._C._nn.mse_loss}
               52701446   22.824    0.000   33.750    0.000 random.py:250(_randbelow_with_getrandbits)
                1442131   33.426    0.000   33.426    0.000 {built-in method max}
                8202132   32.147    0.000   32.147    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2883918   31.300    0.000   31.300    0.000 {built-in method sum}
                1182987   17.345    0.000   30.976    0.000 level.py:16(<dictcomp>)
              406201520   30.880    0.000   30.880    0.000 {built-in method builtins.hash}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9493845: <Newcausal1_CFagent_convert2_0> in cluster <dcc> Done

Job <Newcausal1_CFagent_convert2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr  3 15:09:50 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr  3 15:09:51 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr  3 15:09:51 2021
Terminated at Sat Apr  3 18:05:23 2021
Results reported at Sat Apr  3 18:05:23 2021

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

    CPU time :                                   10479.67 sec.
    Max Memory :                                 4188 MB
    Average Memory :                             3727.57 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12196.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   10637 sec.
    Turnaround time :                            10533 sec.

The output (if any) is above this job summary.

