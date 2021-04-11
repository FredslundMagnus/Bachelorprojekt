
# Parameters

    Name :                      MONTEST_CF_5c3-1
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Hours :                     22.0
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
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                5
    Counterfacts :              3
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      48700102787 function calls (48406373628 primitive calls) in 78908.91 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78908.908 78908.908 {built-in method builtins.exec}
                      1    4.732    4.732 78908.908 78908.908 <string>:1(<module>)
                      1  154.425  154.425 78904.176 78904.176 main.py:95(CFagent)
                1978296 4586.741    0.002 23304.576    0.012 agent.py:217(counterfact)
                5934888   25.757    0.000 19362.893    0.003 agent.py:29(learn)
                5934888  477.469    0.000 16167.632    0.003 learner.py:42(Qlearn)
                1978296   10.980    0.000 14877.639    0.008 game.py:41(step)
                1978296   12.319    0.000 14442.698    0.007 layers.py:710(step)
        324799077/31071609 1399.296    0.000 12673.834    0.000 module.py:866(_call_impl)
               25136721   71.621    0.000 12083.422    0.000 network.py:24(forward)
               25136721  370.298    0.000 11847.646    0.000 container.py:117(forward)
                5644359  131.557    0.000 9266.669    0.002 agent.py:172(choose_action)
                1978297  317.974    0.000 8366.695    0.004 layers.py:676(update)
                1978296  223.399    0.000 7456.317    0.004 agent.py:54(_learn)
                9600882  272.906    0.000 7375.308    0.001 agent.py:49(__call__)
                1978296  223.078    0.000 6932.392    0.004 agent.py:209(_learn)
                5934888   52.911    0.000 6868.228    0.001 optimizer.py:84(wrapper)
                5934888   28.195    0.000 6613.538    0.001 grad_mode.py:24(decorate_context)
                5934888  191.004    0.000 6527.036    0.001 adam.py:55(step)
                5934888 1346.370    0.000 6124.133    0.001 _functional.py:53(adam)
                1978296  178.200    0.000 6046.604    0.003 layers.py:17(step)
               74755901 5978.730    0.000 5978.730    0.000 {built-in method tensor}
               70072419   50.446    0.000 5867.675    0.000 game.py:37(board)
              174227865  538.841    0.000 5847.367    0.000 layer.py:98(move)
                1978296 3111.565    0.002 5805.277    0.003 replaybuffer.py:28(teleporter_save_data)
                1978296   65.574    0.000 4935.335    0.002 agent.py:117(_learn)
                8287383   68.251    0.000 4776.277    0.001 layers.py:731(restart)
               50273442  119.427    0.000 4170.152    0.000 conv.py:398(forward)
                8287383   33.875    0.000 4055.806    0.000 level.py:8(__init__)
                5934888   25.877    0.000 4047.656    0.001 tensor.py:195(backward)
               47479110 2629.863    0.000 4032.615    0.000 layer.py:151(update)
                5934888   24.390    0.000 4020.637    0.001 __init__.py:68(backward)
               50273442   72.425    0.000 3999.612    0.000 conv.py:390(_conv_forward)
               50273442 3927.187    0.000 3927.187    0.000 {built-in method conv2d}
                1978296 2405.463    0.001 3924.017    0.002 agent.py:88(interveen)
                5934888 3854.720    0.001 3854.720    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              174227865  381.420    0.000 3733.818    0.000 layers.py:727(check)
                8287383  653.690    0.000 3720.634    0.000 levels.py:418(generate)
               71453571  157.605    0.000 3476.576    0.000 linear.py:93(forward)
               71453571   64.412    0.000 3249.224    0.000 functional.py:1737(linear)
               71453571 3168.483    0.000 3168.483    0.000 {built-in method torch._C._nn.linear}
                1978296 2398.841    0.001 3160.615    0.002 replaybuffer.py:22(sample_data)
                1978296 2240.601    0.001 2919.367    0.001 replaybuffer.py:49(sample_data)
              201078727 2817.965    0.000 2817.965    0.000 {built-in method clone}
               41436915  392.960    0.000 2436.389    0.000 level.py:41(notUsed)
              174227865 1366.826    0.000 2380.094    0.000 layers.py:531(check)
                1978296 1400.120    0.001 2021.590    0.001 agent.py:67(modify)
               96590292   79.734    0.000 1959.314    0.000 activation.py:713(forward)
               96590292   85.538    0.000 1879.580    0.000 functional.py:1364(leaky_relu)
                5644359 1549.863    0.000 1834.058    0.000 agent.py:183(convert_values)
               11579178   81.669    0.000 1777.453    0.000 agent.py:59(modify_board)
               96590292 1775.545    0.000 1775.545    0.000 {built-in method torch._C._nn.leaky_relu}
                1978296  857.409    0.000 1736.871    0.001 replaybuffer.py:55(CF_save_data)
               33340434 1447.052    0.000 1447.052    0.000 {built-in method cat}
              199504864  156.636    0.000 1369.731    0.000 {built-in method builtins.any}
              110784576 1247.992    0.000 1247.992    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             4734863641  850.362    0.000 1228.780    0.000 enum.py:646(__hash__)
              174061607  225.245    0.000 1214.312    0.000 layers.py:721(isFree)
             1342906851  382.362    0.000 1213.617    0.000 layers.py:692(<genexpr>)
               11579178 1125.793    0.000 1125.793    0.000 {built-in method torch._C._nn.one_hot}
              110784576 1098.041    0.000 1098.041    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1978296   38.066    0.000 1074.445    0.001 agent.py:168(__call__)
               41436915   33.576    0.000 1056.515    0.000 level.py:38(elementsIn)
                1978296   36.363    0.000 1025.916    0.001 agent.py:112(__call__)
              950293286  830.207    0.000  989.067    0.000 layer.py:95(isFree)
                5934888  152.498    0.000  950.723    0.000 optimizer.py:189(zero_grad)
             1635568967  813.103    0.000  813.103    0.000 layer.py:146(elements)
                9600882  279.364    0.000  764.666    0.000 exploration.py:53(softmaxer)
              193569975  472.637    0.000  754.704    0.000 layers.py:568(isDead)
              214636201  711.063    0.000  711.063    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              405306620  564.707    0.000  685.680    0.000 layer.py:126(remove)
               55392288  680.976    0.000  680.976    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               41436915  333.921    0.000  674.344    0.000 level.py:39(<listcomp>)
               45393507  261.650    0.000  672.029    0.000 random.py:315(sample)
             1767872256  671.733    0.000  671.733    0.000 level.py:32(inverse)
               49825776  667.541    0.000  667.541    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               49724298   63.437    0.000  634.196    0.000 layer.py:69(restart)
              174227865  438.029    0.000  620.043    0.000 layers.py:71(check)
                1978296   42.261    0.000  612.861    0.000 replaybuffer.py:18(stacker)
               55392288  600.172    0.000  600.172    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               55392288  568.150    0.000  568.150    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               55392288  564.653    0.000  564.653    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                1978296   41.308    0.000  533.861    0.000 replaybuffer.py:45(stacker)
        5816557164/5816557161  429.981    0.000  493.660    0.000 {built-in method builtins.len}
              615242217  317.948    0.000  459.126    0.000 random.py:250(_randbelow_with_getrandbits)
                8287483  224.966    0.000  445.125    0.000 layers.py:30(reset)
                1978296  268.392    0.000  443.945    0.000 collector.py:53(collect)
              232543647   88.220    0.000  433.163    0.000 random.py:244(randint)
               55392288  432.925    0.000  432.925    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              778088901  317.748    0.000  427.558    0.000 layer.py:130(add)
             4734886408  378.423    0.000  378.423    0.000 {built-in method builtins.hash}
              387746100  285.335    0.000  353.403    0.000 tensor.py:906(grad)
               41436915  214.325    0.000  348.595    0.000 {built-in method _functools.reduce}
              232543647  146.257    0.000  344.944    0.000 random.py:200(randrange)
             1790076182  343.705    0.000  343.705    0.000 enum.py:352(<genexpr>)
               50273442   37.862    0.000  321.295    0.000 flatten.py:39(forward)
                5934888    9.455    0.000  311.096    0.000 loss.py:527(forward)
             3204751776  310.202    0.000  310.202    0.000 layer.py:91(positions)
              174227865  208.815    0.000  303.337    0.000 layers.py:42(check)
                5934888   23.843    0.000  301.640    0.000 functional.py:2898(mse_loss)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9507478: <MONTEST_CF_5c3_1> in cluster <dcc> Done

Job <MONTEST_CF_5c3_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:50 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 10 03:48:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 10 03:48:59 2021
Terminated at Sun Apr 11 01:44:11 2021
Results reported at Sun Apr 11 01:44:11 2021

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

    CPU time :                                   78717.98 sec.
    Max Memory :                                 7281 MB
    Average Memory :                             5431.21 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9103.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78913 sec.
    Turnaround time :                            83241 sec.

The output (if any) is above this job summary.

