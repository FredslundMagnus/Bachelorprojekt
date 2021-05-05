
# Parameters

    Name :                      MonsterLevel_Conver1-1
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
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


      67113367168 function calls (66810077405 primitive calls) in 86110.02 seconds

##    Ordered by: cumulative time
   List reduced from 507 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.019 86110.019 {built-in method builtins.exec}
                      1    5.018    5.018 86110.019 86110.019 <string>:1(<module>)
                      1  388.448  388.448 86105.000 86105.000 main.py:79(CFagent)
                8920431   38.221    0.000 23183.215    0.003 agent.py:29(learn)
                2973477   14.560    0.000 22786.580    0.008 game.py:41(step)
                2973477   18.842    0.000 22141.192    0.007 layers.py:718(step)
                8920431  596.358    0.000 18633.574    0.002 learner.py:42(Qlearn)
        338473668/35185596 1438.885    0.000 11722.187    0.000 module.py:866(_call_impl)
                2973477  295.748    0.000 11335.871    0.004 layers.py:17(step)
              295575936  910.175    0.000 11013.601    0.000 layer.py:98(move)
               26265165   76.151    0.000 10973.395    0.000 network.py:27(forward)
                2973478  471.310    0.000 10755.773    0.004 layers.py:684(update)
               26265165  353.906    0.000 10711.060    0.000 container.py:117(forward)
                2973477 1520.798    0.001 9367.126    0.003 agent.py:212(counterfact)
                2973477  383.812    0.000 9020.103    0.003 agent.py:54(_learn)
                2973477  380.114    0.000 8244.577    0.003 agent.py:204(_learn)
              295575936  952.553    0.000 7331.534    0.000 layers.py:735(check)
                8920431   86.401    0.000 7111.063    0.001 optimizer.py:84(wrapper)
                8920431   46.606    0.000 6734.334    0.001 grad_mode.py:24(decorate_context)
                2973477 5659.317    0.002 6702.924    0.002 replaybuffer.py:22(sample_data)
                8920431  284.418    0.000 6591.841    0.001 adam.py:55(step)
                2973477 5543.454    0.002 6545.758    0.002 replaybuffer.py:67(sample_data)
                8672296  271.698    0.000 5998.189    0.001 agent.py:49(__call__)
                8920431 1382.480    0.000 5992.560    0.001 _functional.py:53(adam)
                2973477  105.273    0.000 5858.082    0.002 agent.py:117(_learn)
                2973477 3155.735    0.001 5331.215    0.002 replaybuffer.py:28(teleporter_save_data)
                9293130   84.831    0.000 5302.919    0.001 layers.py:740(restart)
                8920431   40.228    0.000 4925.548    0.001 tensor.py:195(backward)
                8920431   39.878    0.000 4884.028    0.001 __init__.py:68(backward)
                2973477 2654.263    0.001 4679.054    0.002 agent.py:88(interveen)
                8920431 4645.208    0.001 4645.208    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9293130   41.969    0.000 4490.062    0.000 level.py:8(__init__)
              295575936 2480.919    0.000 4278.843    0.000 layers.py:538(check)
                9293130  709.118    0.000 4072.707    0.000 levels.py:413(generate)
               52530330  124.621    0.000 4019.223    0.000 conv.py:398(forward)
               52530330   82.246    0.000 3836.069    0.000 conv.py:390(_conv_forward)
               52530330 3753.824    0.000 3753.824    0.000 {built-in method conv2d}
                2725484   62.756    0.000 3682.116    0.001 agent.py:176(choose_action)
               35681730 2317.423    0.000 3564.656    0.000 layer.py:151(update)
               42684530 3244.567    0.000 3244.567    0.000 {built-in method tensor}
               35806428   25.545    0.000 3067.400    0.000 game.py:37(board)
               72848541  154.505    0.000 3017.258    0.000 linear.py:93(forward)
               72848541   61.698    0.000 2784.082    0.000 functional.py:1737(linear)
               72848541 2707.682    0.000 2707.682    0.000 {built-in method torch._C._nn.linear}
               46465650  430.621    0.000 2669.982    0.000 level.py:41(notUsed)
                2973477 1675.727    0.001 2485.396    0.001 agent.py:67(modify)
                2973477 1802.348    0.001 2407.399    0.001 replaybuffer.py:73(CF_save_data)
              235499284 2324.711    0.000 2324.711    0.000 {built-in method clone}
              295575936  397.731    0.000 2136.686    0.000 layers.py:729(isFree)
              297365393  227.394    0.000 2037.966    0.000 {built-in method builtins.any}
             2029057180  558.924    0.000 1811.377    0.000 layers.py:700(<genexpr>)
               41380543 1753.694    0.000 1753.694    0.000 {built-in method cat}
             1699652264 1484.171    0.000 1738.956    0.000 layer.py:95(isFree)
             6367131842 1144.580    0.000 1650.957    0.000 enum.py:646(__hash__)
               11645773   81.450    0.000 1634.877    0.000 agent.py:59(modify_board)
               99113706   88.230    0.000 1591.025    0.000 activation.py:713(forward)
               99113706   85.235    0.000 1502.795    0.000 functional.py:1364(leaky_relu)
                2973477   60.633    0.000 1462.015    0.000 agent.py:172(__call__)
               99113706 1401.306    0.000 1401.306    0.000 {built-in method torch._C._nn.leaky_relu}
                2973477   58.145    0.000 1344.210    0.000 agent.py:112(__call__)
              166514712 1182.473    0.000 1182.473    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               46465650   39.216    0.000 1165.610    0.000 level.py:38(elementsIn)
              294391915  722.173    0.000 1147.595    0.000 layers.py:575(isDead)
               11645773 1082.635    0.000 1082.635    0.000 {built-in method torch._C._nn.one_hot}
                8920431  183.298    0.000 1035.506    0.000 optimizer.py:189(zero_grad)
              166514712 1026.977    0.000 1026.977    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              295575936  717.641    0.000 1010.273    0.000 layers.py:77(check)
               52412604  348.608    0.000  886.916    0.000 random.py:315(sample)
             2277709246  846.216    0.000  846.216    0.000 layer.py:146(elements)
                2973477   56.279    0.000  808.058    0.000 replaybuffer.py:18(stacker)
                2973477   57.216    0.000  772.660    0.000 replaybuffer.py:63(stacker)
               46465650  374.464    0.000  747.277    0.000 level.py:39(<listcomp>)
              426726803  143.622    0.000  744.738    0.000 random.py:244(randint)
             1982396046  733.303    0.000  733.303    0.000 level.py:32(inverse)
               55758780   70.787    0.000  708.424    0.000 layer.py:69(restart)
               83257356  683.600    0.000  683.600    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              931400630  473.834    0.000  682.259    0.000 random.py:250(_randbelow_with_getrandbits)
             1115002840  454.168    0.000  614.339    0.000 layer.py:130(add)
                8672296  224.160    0.000  613.433    0.000 exploration.py:53(softmaxer)
              426726803  252.019    0.000  601.117    0.000 random.py:200(randrange)
               83257356  593.627    0.000  593.627    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              690256200  383.486    0.000  576.775    0.000 layer.py:126(remove)
               83257356  549.829    0.000  549.829    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               83257356  549.587    0.000  549.587    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             5877502275  546.713    0.000  546.713    0.000 layer.py:91(positions)
              295575936  368.728    0.000  539.800    0.000 layers.py:48(check)
              297347800   92.372    0.000  519.575    0.000 {built-in method builtins.all}
                2725484  518.822    0.000  518.822    0.000 agent.py:187(convert_values)
             6367165809  506.383    0.000  506.383    0.000 {built-in method builtins.hash}
              250118534  498.849    0.000  498.849    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9293230  247.497    0.000  489.493    0.000 layers.py:36(reset)
              582801576  392.579    0.000  487.467    0.000 tensor.py:906(grad)
              295575936  163.295    0.000  467.627    0.000 layers.py:572(<listcomp>)
              930387272  257.156    0.000  465.780    0.000 layers.py:690(<genexpr>)
                2973477  268.005    0.000  459.583    0.000 collector.py:46(collect)
                8920431   16.662    0.000  431.443    0.000 loss.py:527(forward)
        4564978036/4564978033  366.343    0.000  428.394    0.000 {built-in method builtins.len}
                8920431   42.225    0.000  414.781    0.000 functional.py:2898(mse_loss)
               83257356  410.217    0.000  410.217    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               46465650  233.064    0.000  379.117    0.000 {built-in method _functools.reduce}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579179: <MonsterLevel_Conver1_1> in cluster <dcc> Done

Job <MonsterLevel_Conver1_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:08 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat May  1 19:02:49 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  1 19:02:49 2021
Terminated at Sun May  2 18:58:04 2021
Results reported at Sun May  2 18:58:04 2021

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

    CPU time :                                   85906.43 sec.
    Max Memory :                                 9041 MB
    Average Memory :                             6193.76 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7343.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86117 sec.
    Turnaround time :                            490436 sec.

The output (if any) is above this job summary.

